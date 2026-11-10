"""BHUCR harness.
  python run_eval.py                                     # real run (needs OPENROUTER_API_KEY)
  python run_eval.py --dry-run --config config_dryrun.yaml   # no API calls, fake answers
"""
import argparse, base64, csv, json, os, sys, time, datetime, random
import yaml
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))
except ImportError:
    pass
from graders.grade_format import check_format, final_correct
from graders.grade_rubric import judge_trial
from graders.label import label_trial
from graders.aggregate import load, build_report, run_info

ROOT = os.path.dirname(os.path.abspath(__file__))
API = "https://openrouter.ai/api/v1/chat/completions"
FIELDS = ["run_id", "timestamp", "model", "task", "type", "trial", "label", "score",
          "format_ok", "format_reason", "reading_ok", "reasoning_ok", "final_ok", "final_raw",
          "verdicts", "transcript", "prompt_tokens", "completion_tokens", "cost_usd", "error"]

def check_judge(cfg):
    if cfg["judge_model"] in cfg["models"]:
        print(f"WARNING: judge model '{cfg['judge_model']}' is also a tested model. Run stopped.")
        sys.exit(1)

def read(p):
    if "human_review" in os.path.normpath(p).split(os.sep):
        raise PermissionError("human_review/ is for human judges only and is never sent to a model")
    with open(p, encoding="utf-8") as f:
        return f.read()

class ContentFiltered(Exception):
    pass

def upright_jpeg(path):
    """Send the page the way a human sees it: apply the phone's EXIF rotation, then re-encode."""
    import io
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    buf = io.BytesIO(); im.save(buf, format="JPEG", quality=95)
    return buf.getvalue()

def call_openrouter(model, messages, temperature, system_retries=3):
    """Retries only system errors (network, server, rate limit). Never retries a bad answer."""
    import requests
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        sys.exit("OPENROUTER_API_KEY not set. Put it in a .env file in this folder (see .env.example).")
    for attempt in range(system_retries + 1):
        try:
            r = requests.post(API, headers={"Authorization": f"Bearer {key}"},
                              json={"model": model, "messages": messages, "temperature": temperature,
                                    "max_tokens": 8000, "usage": {"include": True}}, timeout=300)
            if r.status_code in (429, 500, 502, 503, 504):
                raise requests.HTTPError(f"system error {r.status_code}")
            r.raise_for_status()
            d = r.json()
            u = d.get("usage", {})
            msg = d["choices"][0]["message"]
            content = msg.get("content") or ""
            if isinstance(content, list):  # some providers return content parts
                content = "".join(p.get("text", "") for p in content if isinstance(p, dict))
            finish = d["choices"][0].get("finish_reason")
            if not content.strip():
                if finish == "content_filter":
                    # provider safety filter blocked the reply: not retried (costs money, same result), reported separately
                    raise ContentFiltered("blocked by provider content filter")
                if finish != "length":
                    # other empty reply = provider glitch: retry
                    raise requests.HTTPError(f"empty response (finish_reason={finish})")
                # finish == "length": the model used its whole token budget without answering -> graded as a format failure
            return {"text": content,
                    "prompt_tokens": u.get("prompt_tokens", 0),
                    "completion_tokens": u.get("completion_tokens", 0),
                    "cost_usd": u.get("cost", 0)}
        except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as e:
            if attempt == system_retries:
                raise
            time.sleep(5 * (attempt + 1))

# ---------- dry run ----------
FAKE = [
    "ENTRIES:\n...\nRULES:\n...\nREASONING:\n...\nFINAL: ২২৮৯০",   # format ok, right
    "ENTRIES:\n...\nRULES:\n...\nREASONING:\n...\nFINAL: ৭৮৯০",    # format ok, wrong
    "The answer is 22890 taka.",                                   # format broken
]
def fake_call(model, messages, temperature):
    fake_call.n = getattr(fake_call, "n", -1) + 1
    return {"text": FAKE[fake_call.n % 3], "prompt_tokens": 0, "completion_tokens": 0, "cost_usd": 0}

def fake_judge(rubric, seed):
    rnd = random.Random(seed)
    def j(_):
        ids = [i["id"] for i in rubric["reading"] + rubric["reasoning"]]
        return json.dumps({i: {"verdict": "YES" if rnd.random() > 0.03 else "NO", "evidence": "dry"} for i in ids})
    return j

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--resume", nargs="+", metavar="CSV", default=[],
                    help="skip trials already finished in these run CSVs; the final report includes them")
    ap.add_argument("--rejudge", nargs="+", metavar="CSV",
                    help="re-grade saved answers with the current rubric (judge calls only, no model calls); writes a new CSV")
    ap.add_argument("--tasks", nargs="+", help="with --rejudge: only these tasks")
    ap.add_argument("--summarize", nargs="+", metavar="CSV",
                    help="only build a report from existing run CSVs; a later file replaces earlier rows with the same run_id")
    a = ap.parse_args()
    if a.rejudge:
        cfg = yaml.safe_load(read(os.path.join(ROOT, a.config)))
        judge_prompt = read(os.path.join(ROOT, "shared/judge_prompt.txt"))
        stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        out = os.path.join(ROOT, "results", f"runs_{stamp}_rejudge.csv")
        with open(out, "w", newline="", encoding="utf-8") as f:
            wr = csv.DictWriter(f, fieldnames=FIELDS); wr.writeheader()
            for p in a.rejudge:
                for r in load(p):
                    if r["error"] or (a.tasks and r["task"] not in a.tasks) or r["model"] not in cfg["models"]:
                        continue
                    tdir = os.path.join(ROOT, "tasks", r["task"])
                    task = json.loads(read(os.path.join(tdir, "task.json")))
                    rubric = json.loads(read(os.path.join(tdir, "rubric.json")))
                    tr = json.load(open(os.path.join(ROOT, r["transcript"]), encoding="utf-8"))
                    fmt = check_format(tr["response"], task["answer_type"])
                    verdicts, reading_ok, reasoning_ok, final_ok = {}, False, False, False
                    if fmt["ok"]:
                        verdicts, reading_ok, reasoning_ok = judge_trial(
                            lambda m: call_openrouter(cfg["judge_model"], m, 0)["text"], judge_prompt,
                            read(os.path.join(tdir, "transcription.txt")), tr["response"], rubric)
                        final_ok = final_correct(fmt["value"], task)
                    label, score = label_trial(fmt["ok"], reading_ok, reasoning_ok, final_ok)
                    tr.update(verdicts=verdicts, label=label, score=score, format=fmt)
                    json.dump(tr, open(os.path.join(ROOT, r["transcript"]), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
                    r.update(label=label, score=score, reading_ok=reading_ok, reasoning_ok=reasoning_ok,
                             final_ok=final_ok, verdicts=json.dumps(verdicts, ensure_ascii=False))
                    wr.writerow(r); f.flush()
                    print(f"{r['run_id']}: {label} ({score})")
        print(f"Re-judged rows: {out}")
        return
    if a.summarize:
        cfg = yaml.safe_load(read(os.path.join(ROOT, a.config)))
        merged = {}
        for p in a.summarize:
            for r in load(p):
                if not r["error"] and r["model"] in cfg["models"] and r["task"] in cfg["tasks"]:
                    merged[r["run_id"]] = r
        out = os.path.join(ROOT, "results", "summary_combined.md")
        with open(out, "w", encoding="utf-8") as sf:
            sf.write(build_report(list(merged.values()), cfg["trials"]))
        print(f"Summary: {out} ({len(merged)} trials)")
        return
    cfg = yaml.safe_load(read(os.path.join(ROOT, a.config)))
    check_judge(cfg)
    call = fake_call if a.dry_run else call_openrouter
    system = read(os.path.join(ROOT, "shared/system_prompt.txt"))
    judge_prompt = read(os.path.join(ROOT, "shared/judge_prompt.txt"))
    out_dir = os.path.join(ROOT, "_dryrun" if a.dry_run else "results")
    tr_dir = os.path.join(ROOT, "_dryrun" if a.dry_run else "transcripts")
    os.makedirs(out_dir, exist_ok=True); os.makedirs(tr_dir, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = os.path.join(out_dir, f"runs_{stamp}.csv")
    t_start = time.time()
    done = {r["run_id"] for p in a.resume for r in load(p) if not r["error"]}
    if done:
        print(f"Resuming: {len(done)} finished trials will be skipped")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=FIELDS); wr.writeheader()
        for task_id in cfg["tasks"]:
            tdir = os.path.join(ROOT, "tasks", task_id)
            task = json.loads(read(os.path.join(tdir, "task.json")))
            rubric = json.loads(read(os.path.join(tdir, "rubric.json")))
            prompt = read(os.path.join(tdir, "prompt.txt")).strip()
            transcription = read(os.path.join(tdir, "transcription.txt"))
            img = next((os.path.join(tdir, n) for n in ("page.jpg", "page.jpeg", "page.png")
                        if os.path.exists(os.path.join(tdir, n))), None)
            if not img and not a.dry_run:
                print(f"SKIP {task_id}: no page image"); continue
            content = [{"type": "text", "text": prompt}]
            if img:
                content.append({"type": "image_url", "image_url": {
                    "url": "data:image/jpeg;base64," + base64.b64encode(upright_jpeg(img)).decode()}})
            msgs = [{"role": "system", "content": system}, {"role": "user", "content": content}]
            for model in cfg["models"]:
                for t in range(1, cfg["trials"] + 1):
                    rid = f"{model.replace('/', '_')}__{task_id}__t{t}"
                    if rid in done:
                        continue
                    row = {k: "" for k in FIELDS}
                    row.update(run_id=rid, model=model, task=task_id, type=task["type"], trial=t,
                               timestamp=datetime.datetime.now().isoformat(timespec="seconds"))
                    try:
                        res = call(model, msgs, cfg["temperature"])
                        fmt = check_format(res["text"], task["answer_type"])
                        verdicts, reading_ok, reasoning_ok, final_ok = {}, False, False, False
                        if fmt["ok"]:
                            judge = fake_judge(rubric, rid) if a.dry_run else (
                                lambda m: call_openrouter(cfg["judge_model"], m, 0)["text"])
                            verdicts, reading_ok, reasoning_ok = judge_trial(
                                judge, judge_prompt, transcription, res["text"], rubric)
                            final_ok = final_correct(fmt["value"], task)
                        label, score = label_trial(fmt["ok"], reading_ok, reasoning_ok, final_ok)
                        tpath = os.path.join(tr_dir, f"{rid}.json")
                        with open(tpath, "w", encoding="utf-8") as tf:
                            json.dump({"run_id": rid, "model": model, "task": task_id, "trial": t,
                                       "system": system, "prompt": prompt, "response": res["text"],
                                       "format": fmt, "verdicts": verdicts, "label": label,
                                       "score": score}, tf, ensure_ascii=False, indent=2)
                        row.update(label=label, score=score, format_ok=fmt["ok"], format_reason=fmt["reason"],
                                   reading_ok=reading_ok, reasoning_ok=reasoning_ok, final_ok=final_ok,
                                   final_raw=fmt["final_raw"], verdicts=json.dumps(verdicts, ensure_ascii=False),
                                   transcript=os.path.relpath(tpath, ROOT),
                                   prompt_tokens=res["prompt_tokens"], completion_tokens=res["completion_tokens"],
                                   cost_usd=res["cost_usd"])
                        print(f"{rid}: {label} ({score})")
                    except ContentFiltered as e:
                        row["error"] = "content_filter"
                        print(f"{rid}: BLOCKED by provider content filter (not graded, not retried)")
                    except Exception as e:
                        row["error"] = str(e)[:300]
                        print(f"{rid}: SYSTEM ERROR {e}")
                    wr.writerow(row); f.flush()
    all_rows = [r for p in a.resume for r in load(p) if not r["error"]] + load(csv_path)
    # report only the configured models and tasks; extra models/trials stay logged in the CSVs
    keep = lambda r: r["model"] in cfg["models"] and r["task"] in cfg["tasks"]
    rows = [r for r in all_rows if not r["error"] and keep(r)]
    dropped = [r["run_id"] for r in all_rows if r["error"]]
    report = os.path.join(out_dir, f"summary_{stamp}.md")
    with open(report, "w", encoding="utf-8") as sf:
        sf.write(build_report(rows, cfg["trials"]))
        sf.write("\n" + run_info(rows, time.time() - t_start))
        if dropped:
            sf.write(f"\nWARNING: {len(dropped)} trial(s) dropped after repeated system errors; rerun them before reporting: {', '.join(dropped)}\n")
    print(f"Summary: {report}")

if __name__ == "__main__":
    main()

"""Gates 2-3: reading and reasoning via an LLM judge (binary: every mandatory item must be YES)."""
import json, re

def build_judge_messages(judge_prompt, transcription, response, rubric):
    items = [{"id": i["id"], "question": i["bn"]}
             for i in rubric["reading"] + rubric["reasoning"]]
    user = (f"TRUE TRANSCRIPTION:\n{transcription}\n\nMODEL RESPONSE:\n{response}\n\n"
            f"RUBRIC:\n{json.dumps(items, ensure_ascii=False, indent=1)}")
    return [{"role": "system", "content": judge_prompt}, {"role": "user", "content": user}]

def parse_judge(text, rubric):
    m = re.search(r"\{.*\}", text or "", re.S)
    if not m:
        raise ValueError("no JSON")
    data = json.loads(m.group(0))
    out = {}
    for item in rubric["reading"] + rubric["reasoning"]:
        v = data.get(item["id"])
        verdict = v.get("verdict") if isinstance(v, dict) else v
        verdict = str(verdict).strip().upper() if verdict is not None else ""
        if verdict not in ("YES", "NO"):
            raise ValueError(f"bad or missing verdict for {item['id']}")
        out[item["id"]] = {"verdict": verdict, "evidence": v.get("evidence", "") if isinstance(v, dict) else ""}
    return out

def gates(verdicts, rubric):
    reading_ok = all(verdicts[i["id"]]["verdict"] == "YES" for i in rubric["reading"])
    reasoning_ok = all(verdicts[i["id"]]["verdict"] == "YES" for i in rubric["reasoning"])
    return reading_ok, reasoning_ok

def judge_trial(call_judge, judge_prompt, transcription, response, rubric, retries=2):
    msgs = build_judge_messages(judge_prompt, transcription, response, rubric)
    err = None
    for _ in range(retries + 1):
        try:
            v = parse_judge(call_judge(msgs), rubric)
            return v, *gates(v, rubric)
        except (ValueError, json.JSONDecodeError) as e:
            err = e
    raise RuntimeError(f"judge failed after retries: {err}")

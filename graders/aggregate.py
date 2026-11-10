"""Trial table, question table, unified and per-type results, shift table, result list."""
import csv, math
from collections import defaultdict, Counter
from graders.label import LABELS, FAIL_LABELS
K = 5

def round_100(values, total=100.0, dp=1):
    """Largest-remainder rounding: rounded values always sum to `total`."""
    if not values or sum(values) == 0:
        return [0.0] * len(values)
    f = 10 ** dp
    scaled = [v * f for v in values]
    floors = [math.floor(x) for x in scaled]
    left = int(round(total * f)) - sum(floors)
    order = sorted(range(len(values)), key=lambda i: scaled[i] - floors[i], reverse=True)
    for i in order[:max(left, 0)]:
        floors[i] += 1
    return [x / f for x in floors]

def load(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def trial_table(rows):
    """One task, one model. Each trial row: 100 in its label column. Returns label shares + k5 flags."""
    n = len(rows)
    counts = Counter(r["label"] for r in rows)
    shares = round_100([100 * counts[l] / n for l in LABELS])
    k5_pass = 100 if n and all(r["label"] == "Clean pass" for r in rows) else 0
    k5_fail = 100 if n and all(r["label"] in FAIL_LABELS for r in rows) else 0
    avg_score = sum(float(r["score"]) for r in rows) / n
    return {"n": n, "shares": dict(zip(LABELS, shares)), "k5_pass": k5_pass,
            "k5_fail": k5_fail, "avg_score": avg_score}

def question_table(rows):
    """One model, many tasks. Average of each label column across tasks."""
    by_task = defaultdict(list)
    for r in rows:
        by_task[r["task"]].append(r)
    per = {t: trial_table(v) for t, v in sorted(by_task.items())}
    q = len(per)
    if q == 0:
        return per, None
    avg = round_100([sum(p["shares"][l] for p in per.values()) / q for l in LABELS])
    summary = {"questions": q, "shares": dict(zip(LABELS, avg)),
               "k5_pass": round(sum(p["k5_pass"] for p in per.values()) / q, 1),
               "k5_fail": round(sum(p["k5_fail"] for p in per.values()) / q, 1),
               "avg_score": round(sum(p["avg_score"] for p in per.values()) / q, 1)}
    return per, summary

def concentration(shares):
    ranked = sorted(shares.items(), key=lambda kv: kv[1], reverse=True)
    top1, top2 = ranked[0], ranked[1]
    return top1, top2, round(top1[1] + top2[1], 1)

def result_list(summary):
    s = summary["shares"]
    lines = []
    texts = {
        "Fail: Instruction following": "of the time the model did not follow the required answer format.",
        "Fail: Reading and understanding": "of the time the model failed to read and understand the page.",
        "Fail: Reasoning": "of the time the model read correctly but applied the rules wrongly.",
        "Fail: Calculation": "of the time the model read and reasoned correctly but got the final answer wrong.",
        "Lucky pass": "of the time the final answer was right but the reasoning was wrong.",
        "Clean pass": "of the time the answer was clean and correct, with no reading or reasoning failure.",
    }
    for i, l in enumerate(LABELS, 1):
        lines.append(f"{i}. **{l}:** {s[l]:.1f}% {texts[l]}")
    lines.append(f"{len(LABELS)+1}. **K{K} pass:** {summary['k5_pass']:.1f}% of questions got a clean pass in all {K} trials.")
    lines.append(f"{len(LABELS)+2}. **K{K} fail:** {summary['k5_fail']:.1f}% of questions failed in all {K} trials.")
    (l1, v1), (l2, v2), both = concentration(s)
    lines.append(f"{len(LABELS)+3}. **Where most results lie:** {l1} ({v1:.1f}%). {l1} and {l2} together cover {both:.1f}%.")
    return lines

def _qtable_md(per, summary):
    head = "| Question | " + " | ".join(LABELS) + f" | K{K} pass | K{K} fail |"
    out = [head, "|" + "---|" * (len(LABELS) + 3)]
    for t, p in per.items():
        out.append(f"| {t} | " + " | ".join(f"{p['shares'][l]:.1f}" for l in LABELS)
                   + f" | {p['k5_pass']} | {p['k5_fail']} |")
    out.append("| **AVG** | " + " | ".join(f"**{summary['shares'][l]:.1f}**" for l in LABELS)
               + f" | **{summary['k5_pass']:.1f}** | **{summary['k5_fail']:.1f}** |")
    return out

def build_report(rows, trials):
    global K
    K = trials
    rows = [r for r in rows if int(r["trial"]) <= trials]  # keep exactly `trials` per task
    out = ["# BHUCR Results", ""]
    for model in sorted({r["model"] for r in rows}):
        mrows = [r for r in rows if r["model"] == model]
        out += [f"## Model: {model}", "", "### 1. Unified result (all tasks)", ""]
        per, summ = question_table(mrows)
        out += _qtable_md(per, summ) + [""] + result_list(summ) + [""]
        type_summ = {}
        for typ in ("regular", "complex"):
            trows = [r for r in mrows if r["type"] == typ]
            if not trows:
                continue
            per_t, summ_t = question_table(trows)
            type_summ[typ] = summ_t
            out += [f"### 2. {typ.capitalize()} reasoning tasks", ""] + _qtable_md(per_t, summ_t) + [""] + result_list(summ_t) + [""]
        if len(type_summ) == 2:  # regular and complex both present
            s, c = type_summ["regular"], type_summ["complex"]
            out += ["### 3. Shift from regular to complex (complex minus regular, points)", "",
                    "| Label | Regular | Complex | Shift |", "|---|---|---|---|"]
            for l in LABELS:
                out.append(f"| {l} | {s['shares'][l]:.1f} | {c['shares'][l]:.1f} | {c['shares'][l]-s['shares'][l]:+.1f} |")
            out.append(f"| K{K} pass | {s['k5_pass']:.1f} | {c['k5_pass']:.1f} | {c['k5_pass']-s['k5_pass']:+.1f} |")
            out.append(f"| K{K} fail | {s['k5_fail']:.1f} | {c['k5_fail']:.1f} | {c['k5_fail']-s['k5_fail']:+.1f} |")
            out.append("")
    return "\n".join(out) + "\n"

def run_info(rows, runtime_s):
    cost = sum(float(r.get("cost_usd") or 0) for r in rows)
    return (f"Reproducibility note: {len(rows)} trials, approximate API cost ${cost:.2f}, "
            f"total runtime {runtime_s/60:.1f} minutes.\n")

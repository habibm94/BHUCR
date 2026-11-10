"""Statistics behind the README findings. Usage: python analysis.py results/runs_final.csv"""
import csv, json, math, re, sys, collections
from math import comb
from graders.aggregate import build_report

def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (100 * (c - h), 100 * (c + h))

def fisher(a, b, c, d):
    """Two-sided Fisher exact test for the 2x2 table [[a, b], [c, d]]."""
    n, r1, c1 = a + b + c + d, a + b, a + c
    p = lambda x: comb(r1, x) * comb(n - r1, c1 - x) / comb(n, c1)
    p0 = p(a)
    return sum(p(x) for x in range(max(0, c1 - (n - r1)), min(r1, c1) + 1) if p(x) <= p0 + 1e-12)

BN = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
nums = lambda s: [x.replace(",", "") for x in re.findall(r"[\d,]+", (s or "").translate(BN)) if x.replace(",", "")]

def main(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    trials = max(int(r["trial"]) for r in rows)
    models = list(dict.fromkeys(r["model"] for r in rows))
    out = [build_report(rows, trials), "# Statistics", ""]
    n = len(rows); lab = collections.Counter(r["label"] for r in rows)
    k = lab["Clean pass"]; lo, hi = wilson(k, n)
    out.append(f"- Trials: {n}. Clean pass: {k}/{n} ({100*k/n:.1f}%, 95% Wilson CI {lo:.1f}-{hi:.1f}%).")
    for l, v in lab.most_common():
        out.append(f"- {l}: {v}/{n} ({100*v/n:.1f}%)")
    fin = [r for r in rows if r["final_ok"] == "True"]
    bad = sum(r["label"] != "Clean pass" and r["label"] != "Lucky pass" for r in fin)
    out.append(f"- Right final answer: {len(fin)}/{n}; of these, {bad} ({100*bad/max(1,len(fin)):.0f}%) had misread the page.")
    out += ["", "| Model | Clean pass | 95% CI | Right final | Reading items misread |", "|---|---|---|---|---|"]
    for m in models:
        s = [r for r in rows if r["model"] == m]
        c = sum(r["label"] == "Clean pass" for r in s); f = sum(r["final_ok"] == "True" for r in s)
        tot = no = 0
        for r in s:
            if r["format_ok"] != "True":
                continue
            v = json.loads(r["verdicts"])
            for i, d in v.items():
                if i.startswith("R"):
                    tot += 1; no += d["verdict"] == "NO"
        lo, hi = wilson(c, len(s))
        out.append(f"| {m} | {c}/{len(s)} | {lo:.1f}-{hi:.1f}% | {f}/{len(s)} | {no}/{tot} ({100*no/max(1,tot):.1f}%) |")
    reg = [r for r in rows if r["type"] == "regular"]; com = [r for r in rows if r["type"] == "complex"]
    a = sum(r["label"] == "Clean pass" for r in reg); c = sum(r["label"] == "Clean pass" for r in com)
    out.append(f"\n- Regular vs complex, clean pass: {a}/{len(reg)} vs {c}/{len(com)}; Fisher exact p = {fisher(a, len(reg)-a, c, len(com)-c):.3f}.")
    fr = [r for r in rows if r["model"] in models[:2]]; op = [r for r in rows if r["model"] in models[2:]]
    a = sum(r["final_ok"] == "True" for r in fr); b = sum(r["final_ok"] == "True" for r in op)
    out.append(f"- Frontier vs open-weight, right final answer: {a}/{len(fr)} vs {b}/{len(op)}; Fisher exact p = {fisher(a, len(fr)-a, b, len(op)-b):.2e}.")
    # digit-swap analysis where the judge quoted the misread value
    quoted = swaps = 0; pairs = collections.Counter()
    for r in rows:
        if r["format_ok"] != "True":
            continue
        rub = json.load(open(f"tasks/{r['task']}/rubric.json", encoding="utf-8"))
        v = json.loads(r["verdicts"])
        for item in rub["reading"]:
            d = v[item["id"]]; want = nums(item["bn"]); got = nums(d["evidence"])
            if d["verdict"] != "NO" or not want or not got:
                continue
            w = max(want, key=len); g = min(got, key=lambda x: (abs(len(x)-len(w)), sum(p != q for p, q in zip(x, w))))
            if g == w:
                continue
            quoted += 1
            diff = [(p, q) for p, q in zip(w, g) if p != q] if len(g) == len(w) else []
            if len(diff) == 1:
                swaps += 1; pairs[f"{diff[0][0]}->{diff[0][1]}"] += 1
    out.append(f"- Misread numbers quoted by the judge: {quoted}; single-digit swaps: {swaps}. Most common: "
               + ", ".join(f"{p} ({c})" for p, c in pairs.most_common(4)) + " (digits shown in Latin form).")
    # judge reliability: compare each reading verdict with a code check (is the expected number in ENTRIES?)
    tot = agree = yes_missing = yes_total = 0
    for r in rows:
        if r["format_ok"] != "True":
            continue
        resp = json.load(open(r["transcript"], encoding="utf-8"))["response"].translate(BN)
        ent = resp.split("RULES:")[0].replace(",", "")
        rub = json.load(open(f"tasks/{r['task']}/rubric.json", encoding="utf-8")); v = json.loads(r["verdicts"])
        for item in rub["reading"]:
            want = nums(item["bn"])
            if not want:
                continue
            w = max(want, key=len)
            code = re.search(r"(?<!\d)" + w + r"(?!\d)", ent) is not None
            judge = v[item["id"]]["verdict"] == "YES"
            tot += 1; agree += code == judge
            if judge:
                yes_total += 1; yes_missing += not code
    out.append(f"- Judge vs code check on {tot} reading items: {agree} agree ({100*agree/tot:.1f}%). "
               f"Judge said YES with the correct number missing from ENTRIES in {yes_missing} of {yes_total} YES verdicts.")
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "results/runs_final.csv"
    text = main(path)
    open("results/summary_final.md", "w", encoding="utf-8").write(text)
    print(text[text.index("# Statistics"):])

"""Gate order -> label and score. Marks are binary."""
MARKS = {"instruction": 10, "reading": 20, "reasoning": 15, "final": 55}

LABELS = ["Fail: Instruction following", "Fail: Reading and understanding",
          "Fail: Reasoning", "Fail: Calculation", "Lucky pass", "Clean pass"]
FAIL_LABELS = LABELS[:4]

def label_trial(format_ok, reading_ok=False, reasoning_ok=False, final_ok=False):
    if not format_ok:
        return LABELS[0], 0
    s = MARKS["instruction"]
    if not reading_ok:
        return LABELS[1], s
    s += MARKS["reading"]
    if final_ok:
        return (LABELS[5], 100) if reasoning_ok else (LABELS[4], s + MARKS["final"])
    return (LABELS[3], s + MARKS["reasoning"]) if reasoning_ok else (LABELS[2], s)

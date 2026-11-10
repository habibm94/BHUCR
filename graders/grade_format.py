"""Gate 1: instruction following. Checks the four headings and the FINAL value type."""
import re, unicodedata

BN_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
HEADINGS = ["ENTRIES:", "RULES:", "REASONING:", "FINAL:"]
YES = {unicodedata.normalize("NFC", w) for w in ("yes", "হ্যাঁ", "হাঁ", "হ্যা")}
NO = {"no", "না"}

def to_number(raw):
    """Compare-only normalization. The original text is never changed."""
    s = raw.translate(BN_DIGITS)
    s = re.sub(r"[,\s]|টাকা|taka|tk|৳|/-", "", s, flags=re.IGNORECASE)
    return int(float(s)) if re.fullmatch(r"-?\d+(\.0+)?", s.replace("−", "-")) else None

def parse_value(raw, answer_type):
    v = unicodedata.normalize("NFC", raw).strip().strip("*_`'\" .।")
    if answer_type == "number":
        return to_number(v)
    if answer_type == "yesno":
        low = v.lower()
        return "yes" if low in YES else "no" if low in NO else None
    if answer_type == "text":
        return v if v and "\n" not in v else None
    raise ValueError(f"unknown answer_type {answer_type}")

def check_format(text, answer_type):
    text = (text or "").rstrip()
    # first occurrence of each section heading; the LAST occurrence of FINAL: (a model may mention it earlier)
    pos = [text.find(h) for h in HEADINGS[:-1]] + [text.rfind("FINAL:")]
    if any(p < 0 for p in pos) or pos != sorted(pos):
        return {"ok": False, "reason": "missing or out-of-order heading", "final_raw": None, "value": None}
    raw = text[pos[-1] + len("FINAL:"):].strip().strip("*_` ")
    if "\n" in raw:
        return {"ok": False, "reason": "text after FINAL line", "final_raw": raw, "value": None}
    value = parse_value(raw, answer_type)
    if value is None:
        return {"ok": False, "reason": f"FINAL is not a clean {answer_type}", "final_raw": raw, "value": None}
    return {"ok": True, "reason": "", "final_raw": raw, "value": value}

def final_correct(value, task):
    ans = task["answer"]
    if task["answer_type"] == "text":
        accepted = [a.strip().lower() for a in (ans if isinstance(ans, list) else [ans])]
        return str(value).strip().lower() in accepted
    return value == ans

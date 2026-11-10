import json, os, sys, pytest
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from graders.grade_format import check_format, final_correct
from graders.grade_rubric import parse_judge, gates, build_judge_messages
from graders.label import label_trial
from graders.aggregate import round_100, trial_table, question_table

TASK_IDS = sorted(d for d in os.listdir(os.path.join(ROOT, "tasks")) if not d.startswith("_"))
def load(tid, name):
    return json.load(open(os.path.join(ROOT, "tasks", tid, name), encoding="utf-8"))
OK = "ENTRIES:\na\nRULES:\nb\nREASONING:\nc\nFINAL: {}"
BN = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")

def as_final(task):
    a = task["answer"]
    return str(a).translate(BN) if task["answer_type"] == "number" else {"yes": "হ্যাঁ", "no": "না"}[a]

# ---- every task is complete and consistent ----
@pytest.mark.parametrize("tid", TASK_IDS)
def test_task_files(tid):
    for f in ("prompt.txt", "transcription.txt", "task.json", "rubric.json"):
        assert os.path.exists(os.path.join(ROOT, "tasks", tid, f))
    assert os.path.exists(os.path.join(ROOT, "human_review", tid, "task_en.md"))

@pytest.mark.parametrize("tid", TASK_IDS)
def test_type_matches_rules(tid):
    t = load(tid, "task.json")
    assert t["type"] == ("complex" if t["complexity"]["rules"] > 3 else "regular")
    assert tid[0] == {"complex": "C", "regular": "R"}[t["type"]]

@pytest.mark.parametrize("tid", TASK_IDS)
def test_reference_answer_passes_grader(tid):
    t = load(tid, "task.json")
    f = check_format(OK.format(as_final(t)), t["answer_type"])
    assert f["ok"] and final_correct(f["value"], t)

@pytest.mark.parametrize("tid", TASK_IDS)
def test_rubric_ids_sequential_bengali_only(tid):
    r = load(tid, "rubric.json")
    for key, p in (("reading", "R"), ("reasoning", "L")):
        assert [i["id"] for i in r[key]] == [f"{p}{n+1:02d}" for n in range(len(r[key]))]
        assert all(set(i) == {"id", "bn"} for i in r[key])

@pytest.mark.parametrize("tid", TASK_IDS)
def test_wrong_answer_fails(tid):
    t = load(tid, "task.json")
    wrong = str(t["answer"] + 100).translate(BN) if t["answer_type"] == "number" else {"yes": "না", "no": "হ্যাঁ"}[t["answer"]]
    f = check_format(OK.format(wrong), t["answer_type"])
    assert f["ok"] and not final_correct(f["value"], t)

def test_c1_buckets_sum():
    b = load("C1_shop_ledger", "task.json")["buckets"]
    assert b["opening"] + b["cash_sales"] + b["received_today"] - b["expense"] - b["paid_tonight"] == 22890

def test_harness_never_reads_human_review():
    from run_eval import read
    with pytest.raises(PermissionError):
        read(os.path.join(ROOT, "human_review", "README.md"))

def test_judge_gets_no_english():
    r = load("C1_shop_ledger", "rubric.json")
    msg = build_judge_messages("x", "t", "resp", r)[1]["content"]
    assert "question_en" not in msg

# ---- gate 1: format ----
C1 = load("C1_shop_ledger", "task.json")
@pytest.mark.parametrize("v", ["২২৮৯০", "২২,৮৯০", "22890", "22,890", "২২৮৯০ টাকা", "22890 taka", "৳22,890"])
def test_number_formats(v):
    f = check_format(OK.format(v), "number"); assert f["ok"] and final_correct(f["value"], C1)

@pytest.mark.parametrize("text", ["The answer is 22890.", "ENTRIES:\na\nREASONING:\nc\nFINAL: 22890",
    "RULES:\nb\nENTRIES:\na\nREASONING:\nc\nFINAL: 22890", OK.format("about 22890"),
    OK.format("22890 or 23590"), OK.format("22890\nHope this helps")])
def test_format_errors(text):
    assert not check_format(text, "number")["ok"]

def test_original_final_text_kept():
    assert check_format(OK.format("২২,৮৯০"), "number")["final_raw"] == "২২,৮৯০"

@pytest.mark.parametrize("v,exp", [("হ্যাঁ", "yes"), ("না", "no"), ("Yes", "yes"), ("no", "no")])
def test_yesno(v, exp):
    assert check_format(OK.format(v), "yesno")["value"] == exp

def test_yesno_rejects_sentence():
    assert not check_format(OK.format("হ্যাঁ, যাওয়া উচিত"), "yesno")["ok"]

# ---- gates 2-3 ----
R1 = load("C1_shop_ledger", "rubric.json")
IDS = [i["id"] for i in R1["reading"] + R1["reasoning"]]
def test_one_wrong_reading_item_fails_reading():
    d = {i: {"verdict": "YES"} for i in IDS}; d["R08"] = {"verdict": "NO"}
    assert gates(parse_judge(json.dumps(d), R1), R1) == (False, True)
def test_judge_incomplete_rejected():
    with pytest.raises(ValueError): parse_judge(json.dumps({i: {"verdict": "YES"} for i in IDS[:-1]}), R1)
def test_judge_bad_verdict_rejected():
    with pytest.raises(ValueError): parse_judge(json.dumps({i: {"verdict": "MAYBE"} for i in IDS}), R1)

# ---- labels ----
@pytest.mark.parametrize("args,label,score", [
    ((False,), "Fail: Instruction following", 0), ((True, False, True, True), "Fail: Reading and understanding", 10),
    ((True, True, False, False), "Fail: Reasoning", 30), ((True, True, True, False), "Fail: Calculation", 45),
    ((True, True, False, True), "Lucky pass", 85), ((True, True, True, True), "Clean pass", 100)])
def test_label_and_score(args, label, score):
    assert label_trial(*args) == (label, score)

# ---- tables ----
def rows(labels, task="Q"): return [{"task": task, "label": l, "score": "0"} for l in labels]
R_, Re, C, L, P = ("Fail: Reading and understanding", "Fail: Reasoning", "Fail: Calculation", "Lucky pass", "Clean pass")
def test_trial_table_example():
    s = trial_table(rows([L, P, R_, P, C]))["shares"]
    assert (s[R_], s[C], s[L], s[P]) == (20, 20, 20, 40) and sum(s.values()) == 100
def test_k5():
    assert trial_table(rows([P] * 5))["k5_pass"] == 100
    assert trial_table(rows([R_] * 3 + [C] * 2))["k5_fail"] == 100
    assert trial_table(rows([L] * 5))["k5_fail"] == 0
def test_question_table_handwritten_example():
    q = (rows([R_, P, P, L, C], "Q1") + rows([R_, Re, P, P, P], "Q2") + rows([C, C, L, P, P], "Q3")
         + rows([P] * 5, "Q4") + rows([R_] * 5, "Q5") + rows([R_, R_, C, P, P], "Q6"))
    _, s = question_table(q); sh = s["shares"]
    assert (sh[R_], sh[Re], sh[C], sh[L], sh[P]) == (30.0, 3.3, 13.3, 6.7, 46.7)
    assert s["k5_pass"] == 16.7 and s["k5_fail"] == 16.7
def test_rounding_always_100():
    assert round(sum(round_100([100/3] * 3)), 1) == 100.0 and round(sum(round_100([100/7] * 7)), 1) == 100.0
def test_judge_same_as_model_stops():
    from run_eval import check_judge
    with pytest.raises(SystemExit): check_judge({"models": ["a/x"], "judge_model": "a/x"})

# ---- format robustness ----
def test_bold_final_accepted():
    f = check_format("**ENTRIES:**\na\n**RULES:**\nb\n**REASONING:**\nc\n**FINAL:** ২২৮৯০", "number")
    assert f["ok"] and f["value"] == 22890

def test_final_mentioned_earlier_uses_last():
    t = "ENTRIES:\na\nRULES:\nb\nREASONING:\nI will write FINAL: at the end.\nFINAL: 22890"
    assert check_format(t, "number")["value"] == 22890

def test_trailing_whitespace_ok():
    assert check_format(OK.format("না") + "\n\n", "yesno")["value"] == "no"

def test_negative_number_is_clean_format():
    f = check_format(OK.format("-7327"), "number")
    assert f["ok"] and f["value"] == -7327 and not final_correct(f["value"], C1)

def test_images_sent_upright():
    from PIL import Image
    from run_eval import upright_jpeg
    import io, glob
    for p in glob.glob(os.path.join(ROOT, "tasks", "*", "page.*")):
        im = Image.open(io.BytesIO(upright_jpeg(p)))
        assert im.height > im.width, p   # portrait pages

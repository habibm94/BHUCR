# BHUCR

**Bengali Handwriting Understanding and Complex Reasoning**

BHUCR measures whether vision-language models can read a real handwritten Bengali note and reason through its numbers and conditions to one correct answer.

| | |
|---|---|
| **Tasks** | 6 handwritten Bengali pages (3 regular, 3 complex) |
| **Models** | 4 (2 frontier, 2 open-weight), 4 trials per task |
| **Graded trials** | 96 |
| **Clean pass rate** | 9.4% (95% CI 5.0–16.9%) |
| **Main failure** | Reading handwritten Bengali digits (59.4% of trials) |

---

## 1. Short description

BHUCR tests whether models can read handwritten Bengali notes (shop ledgers, budgets, event and trip accounts) and reason to one correct answer.

- **The gap:** models reason well, but they misread handwritten Bengali digits.
- **Key finding:** only 9.4% of trials were fully correct, and 48% of correct final answers came from misread pages. Answer-only grading would overstate what models can do.
- **Reuse:** the same rules, rubric format and code can be used to build this benchmark for any language.

## 2. Video walkthrough

[Watch the walkthrough (Google Drive, under 5 minutes)](https://drive.google.com/file/d/13EBuXkT77fhKeGEhH3Omw_wQ1-A2uDje/view?usp=sharing)

## 3. Domain and expertise

| | |
|---|---|
| **Domain** | Everyday handwritten notes with numbers and logic, as kept by small shops, households and field workers in Bangladesh |
| **Author** | Native Bengali speaker; AI trainer with 2,200+ hours of LLM evaluation (multimodal, multilingual, QA) |
| **Author's role** | Wrote and photographed every page, set every answer, wrote every rubric item |

## 4. What it tests and why it matters

A model must:

1. **Read** every name, number and condition on a messy page: crossed-out text, arrows, side notes, later updates.
2. **Reason** about which entries count: today vs later, refunds, crossed-out changes, netting.
3. **Answer** with one clean value: a number, yes/no or text.

**Who it is for:** teams building apps that digitize handwritten notes for Bengali users, and anyone who asks AI to do the math on a photographed page.

**Why it matters:** one misread digit changes the money a person expects to have. In task C1 a frontier model read **17,000 as 1,700** and reported the wrong cash total with full confidence.

## 5. Setup and run instructions

Requires Python 3.10+.

```bash
pip install -r requirements.txt
cp .env.example .env        # Windows: copy .env.example .env
# set OPENROUTER_API_KEY in .env (loaded as an environment variable; never committed)
python run_eval.py          # runs all models, tasks and trials in config.yaml and writes the report
```

| Command | Purpose |
|---|---|
| `python -m pytest -q tests` | 71 grader tests, no API key needed |
| `python run_eval.py --dry-run --config config_dryrun.yaml` | Full pipeline with fake answers, no API cost |
| `python analysis.py results/runs_final.csv` | Tables and statistics from a run file |
| `python run_eval.py --resume <runs.csv>` | Continue an interrupted run |

| | |
|---|---|
| **Runtime** | About 1 hour for the full run (96 trials plus judge calls) |
| **Cost** | Logged model cost for 96 trials: $0.89. Total spend including judge calls and setup runs: under $10 |

## 6. Models tested and results

| Setting | Value |
|---|---|
| Run date | 2026-11-09 |
| Provider | OpenRouter |
| Temperature | 0 |
| Max output tokens | 8,000 |
| Trials per task | 4 |
| System prompt | Same for every model (`shared/system_prompt.txt`) |
| Judge | `anthropic/claude-sonnet-5.5` (not a tested model) |

| Model | Group | Clean pass | 95% CI | Right final answer | Reading items misread | Most common label |
|---|---|---|---|---|---|---|
| `google/gemini-4-argon` | Frontier | 9/24 | 21.2–57.3% | 14/24 | 3.9% | Clean pass (37.5%) |
| `openai/gpt-6.1-sol` | Frontier | 0/24 | 0.0–13.8% | 12/24 | 22.6% | Fail: Reading (100%) |
| `qwen/qwen3.8-flash` | Open-weight | 0/24 | 0.0–13.8% | 1/24 | 58.1%¹ | Fail: Instruction following (87.5%) |
| `google/gemma-4-31b-it` | Open-weight | 0/24 | 0.0–13.8% | 0/24 | 66.3% | Fail: Reading (91.7%) |
| **All models** | | **9/96** | **5.0–16.9%** | **27/96** | **30.9%** | **Fail: Reading (59.4%)** |

¹ Qwen answered in only 3 of 24 trials; in the other 21 it used its whole 8,000-token budget thinking and never wrote an answer.

| Label | Trials | Share |
|---|---|---|
| Fail: Instruction following | 23 | 24.0% |
| Fail: Reading and understanding | 57 | 59.4% |
| Fail: Reasoning | 2 | 2.1% |
| Fail: Calculation | 0 | 0.0% |
| Lucky pass | 5 | 5.2% |
| Clean pass | 9 | 9.4% |
| K4 pass (clean in all 4 trials) | 0 of 24 model-task pairs | 0.0% |

`anthropic/claude-opus-5.5` was planned but excluded: every reply was blocked by the provider's content filter (`finish_reason=content_filter`).

Per-task, per-type and regular-to-complex tables: `results/summary_final.md`.

## 7. Failure analysis

1. **Models almost never get it fully right.** 9/96 clean passes (9.4%). No model passed any task cleanly in all 4 trials.
2. **Reading is the main failure.** 59.4% of trials failed at reading, 2.1% at reasoning, 0% at calculation. When models read correctly, they almost always reasoned correctly.
3. **A correct final answer cannot be trusted on its own.** 13 of the 27 correct final answers (48%) came from misread pages. GPT gave the right final answer in 12/24 trials and passed 0 cleanly.
4. **The errors are single Bengali digits.** Of 25 misread numbers quoted by the judge, 23 (92%) were one swapped digit, most often ৩ → ৬ / ৫ / ০ and ১ → ২.
5. **Frontier models lead by a wide margin, but remain unreliable.** Right final answer: frontier 26/48 (54%) vs open-weight 1/48 (2%); Fisher exact p = 5.0 × 10⁻⁹.
6. **More rules did not make tasks harder.** Clean pass: regular 5/48 vs complex 4/48 (Fisher exact p = 1.0). The bottleneck is handwriting, not logic.
7. **Insight.** Models already reason well enough for everyday accounts. What stops them is reading handwritten Bengali digits, and closing that gap needs better handwriting recognition, not better reasoning.

**Representative transcripts** (in `transcripts/`)

| Task | Model | Label | What went wrong |
|---|---|---|---|
| C1 Shop ledger | GPT-6.1 Sol | Fail: Reading | Read 17000 as 1700 and 230 as 200 |
| C2 Trip accounts | Gemini 4 Argon | Fail: Reasoning | Reading passed; a reasoning step failed; answered "No" |
| C3 Wedding accounts | Gemini 4 Argon | Fail: Reading | Read car hire 13000 as 15000 |
| R1 Installment collection | Gemini 4 Argon | Fail: Reasoning | Reading passed; a reasoning step failed; answered 8600 |
| R2 Monthly budget | GPT-6.1 Sol | Fail: Reading | Read bike repair 2300 as 2000 and "headlight" as "helmet" |
| R3 House repair | Gemini 4 Argon | Fail: Reading | Read 63500 as 53500 and 2200 as 1200 |
| C1 Shop ledger | Gemini 4 Argon | Clean pass | Fully correct on the hardest task |

| Task | Transcript file |
|---|---|
| C1 (fail) | `openai_gpt-6.1-sol__C1_shop_ledger__t1.json` |
| C2 | `google_gemini-4-argon__C2_tour_accounts__t1.json` |
| C3 | `google_gemini-4-argon__C3_wedding_accounts__t1.json` |
| R1 | `google_gemini-4-argon__R1_installment_collection__t1.json` |
| R2 | `openai_gpt-6.1-sol__R2_monthly_budget__t1.json` |
| R3 | `google_gemini-4-argon__R3_house_repair__t1.json` |
| C1 (clean pass) | `google_gemini-4-argon__C1_shop_ledger__t2.json` |

## 8. Prior work and sources

| | |
|---|---|
| **Pre-existing work** | None. All pages, tasks, rubrics and code were made during the hackathon |
| **Data** | 6 pages handwritten and photographed by the author. Fictional names. No client, employer or personal data |
| **External datasets** | None |
| **Related benchmarks** | Agentic-MME (image investigation plus reasoning) inspired the task style. NoTeS-Bank (handwritten scientific notes, English) shows a similar reading gap. Ideas only; nothing copied |
| **AI use** | Coding and translation assistance by Claude Code. AI tools also drafted rubric wording and README text. The author wrote every page, set every answer, chose every rubric item and rule, and reviewed all of it |

---

## Tasks

A task's type is set by one count: the number of **rules** on the page (a rule is a condition or update that changes the answer).

| ID | Note | Type | Rules | Answer type | Answer |
|---|---|---|---|---|---|
| C1 | Shop cash ledger | Complex | 12 | Number | 22890 |
| C2 | Trip accounts | Complex | 5 | Yes/No | Yes |
| C3 | Wedding accounts | Complex | 4 | Number | 5700 |
| R1 | Installment collection | Regular | 3 | Number | 9100 |
| R2 | Monthly budget | Regular | 2 | Yes/No | No |
| R3 | House repair | Regular | 2 | Yes/No | Yes |

| Folder | Contents | Read by |
|---|---|---|
| `tasks/<ID>/` | `page.jpeg`, `prompt.txt`, `transcription.txt`, `task.json`, `rubric.json` (all Bengali) | Harness and judge |
| `human_review/<ID>/` | `task_en.md` (type, answer, calculation, prompt and rubric in Bengali and English), `transcription_en.txt` | Human judges only. The code refuses to read this folder |

## Prompt

| Part | Content |
|---|---|
| User prompt | A natural Bengali question, as a real person would ask it |
| System prompt | Answer in the question's language, in four parts: `ENTRIES:` (everything on the page), `RULES:` (every condition), `REASONING:` (steps and calculation), `FINAL:` (one clean value) |

## Scoring logic

**Rubric.** Atomic YES/NO questions, only for items that change the answer.

| Part | Question asked for each entry |
|---|---|
| Reading and understanding | Did the model read this entry correctly (person, amount, meaning)? |
| Reasoning | Did the model make the right decision (add, subtract, keep for later, compare) with the right amount? |

**Gates.** Marks are binary (full or 0). Grading stops at the first failed gate.

| Gate | Marks | Graded by |
|---|---|---|
| 1. Instruction following | 10 | Code |
| 2. Reading and understanding | 20 | LLM judge |
| 3. Reasoning | 15 | LLM judge |
| 4. Final answer | 55 | Code |

| Label | Score | Meaning |
|---|---|---|
| Fail: Instruction following | 0 | Format broken or no answer |
| Fail: Reading and understanding | 10 | Any mandatory reading item wrong |
| Fail: Reasoning | 30 | Read correctly; reasoning and answer wrong |
| Fail: Calculation | 45 | Read and reasoned correctly; answer wrong |
| Lucky pass | 85 | Answer right; reasoning wrong |
| Clean pass | 100 | Everything right |

**Why these weights.** They follow the gate order: a model must follow the format before its reading can be checked, read before it can reason, and reason before its answer can be trusted. The final answer weighs most because it is what the user acts on. The label distribution is the main result; the score is secondary.

**Rules**

| Rule | Detail |
|---|---|
| Grounded pass/fail | Every pass is checked against the reading and reasoning grades, so no false positive counts as a clean pass |
| Reading gate is strict | A right final answer with wrong reading is a fail; a right amount on the wrong person causes real damage |
| Retries | Only system errors (network, server, API) are retried, up to 3 times. Instruction-following errors are results, not retried |
| Consistency | K4 pass = clean pass in all 4 trials. K4 fail = fail (any type) in all 4 trials |
| Rounding | 1 decimal, largest-remainder method, so each table row sums to exactly 100 |

**Judge**

| | |
|---|---|
| Model | `anthropic/claude-sonnet-5.5`, different from every tested model (enforced by code) |
| Prompt | `shared/judge_prompt.txt` |
| Input | True transcription and model response; never the image or the answer |
| Output | YES/NO per rubric item, with a quote from the response for every YES |

**Judge reliability**

| Check | Result |
|---|---|
| Code cross-check (`analysis.py`): judge verdict vs whether the expected number appears in `ENTRIES:` | 88.4% agreement over 1,015 reading verdicts. YES with the number missing: 2 of 701 |
| Second-model audit: 16 random verdicts (10 NO, 6 YES, seed 7) re-checked by a second model (Claude Code) | 16/16 consistent |
| Evidence quotes | Saved in every transcript for every YES |
| Independence | The final answer is graded by code, not by the judge |

Most disagreements in the code cross-check are cases where the number appears but the person or meaning is wrong, which only the judge can see.

## Grader validation

`tests/test_hucrb.py`: 71 tests, no API needed.

| Area | What is tested |
|---|---|
| Tasks | All files present; type matches rule count; every reference answer passes and a wrong answer fails |
| Format | Bengali/English digits, commas, currency words; missing or out-of-order headings; text after FINAL; multiple values; bold headings; negative numbers |
| Judge | One wrong reading item fails the gate; malformed output is rejected and retried; no English sent; judge = tested model stops the run |
| Scoring | Labels map to scores; tables reproduce a hand-calculated example; rounding sums to 100 |
| Images | Pages are sent upright, as a human sees them |

## Outputs

| File | Contents |
|---|---|
| `results/runs_final.csv` | One row per trial: label, score, gate results, judge verdicts, tokens, cost |
| `results/summary_final.md` | All tables and statistics |
| `transcripts/` | Full prompt, response, format check and judge verdicts for all 96 trials |

## Limitations

- 6 tasks and 4 trials per model: the numbers are clear signals, not exact rates (see the confidence intervals).
- Reading and reasoning grades come from an LLM judge, checked by code and by a second-model audit.
- Bengali only in this version.

## License

| Part | License |
|---|---|
| Code (`*.py`, `graders/`, `tests/`, `shared/`) | MIT (`LICENSE`) |
| Data (`tasks/`, `human_review/`, `results/`, `transcripts/`) | CC BY 4.0 (`LICENSE-DATA`) |

Please cite as: *BHUCR: Bengali Handwriting Understanding and Complex Reasoning (Habibullah, 2026).*

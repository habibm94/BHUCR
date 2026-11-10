# BHUCR rules

## Marks (binary: full or 0)
| Part | Marks |
|---|---|
| Instruction following | 10 |
| Reading and understanding | 20 |
| Reasoning | 15 |
| Final answer | 55 |
| Total | 100 |

## Gate order and labels
Grading stops at the first failed gate.
| Gate result | Label | Score |
|---|---|---|
| Format broken | Fail: Instruction following | 0 |
| Any mandatory reading item wrong | Fail: Reading and understanding | 10 |
| Reasoning wrong, final wrong | Fail: Reasoning | 30 |
| Reading and reasoning right, final wrong | Fail: Calculation | 45 |
| Reasoning wrong, final right | Lucky pass | 85 |
| All right | Clean pass | 100 |

## Other rules
- Every pass/fail is grounded: each one is checked against the reading and reasoning grades, so no false positive is counted as a clean pass.
- A right final answer with wrong reading is a fail: a right amount on a wrong person causes real damage.
- Rubrics contain only mandatory items: entries and rules that change the answer.
- Instruction-following errors are not retried; they are a result. Only system errors (network, server, API) are retried.
- 4 trials per task per model. K4 pass = clean pass in all 4 trials. K4 fail = fail (any type) in all 4 trials.
- Percentages are rounded to 1 decimal with the largest-remainder rule, so every row sums to exactly 100.

## Task building
1. Handwriting is natural: not terrible, not specially neat for AI.
2. Photo is fully readable; nothing covers the writing.
3. An ordinary person can understand every line.
4. An ordinary person with a calculator can solve it in 15 minutes.
5. Names are fictional; no real personal or client data.
6. A second person solves the page and reaches the same answer.
7. Type is set by the number of rules (a rule = a condition or update that changes the answer):
| Type | Rules |
|---|---|
| Regular | up to 3 |
| Complex | more than 3 |
There is no rule on number of entries or edits.

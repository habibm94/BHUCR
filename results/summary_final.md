# BHUCR Results

## Model: google/gemini-4-argon

### 1. Unified result (all tasks)

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| C1_shop_ledger | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0 | 0 |
| C2_tour_accounts | 0.0 | 0.0 | 25.0 | 0.0 | 25.0 | 50.0 | 0 | 0 |
| C3_wedding_accounts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R1_installment_collection | 0.0 | 0.0 | 25.0 | 0.0 | 0.0 | 75.0 | 0 | 0 |
| R2_monthly_budget | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0 | 0 |
| R3_house_repair | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **0.0** | **33.4** | **8.3** | **0.0** | **20.8** | **37.5** | **0.0** | **33.3** |

1. **Fail: Instruction following:** 0.0% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 33.4% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 8.3% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 20.8% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 37.5% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 33.3% of questions failed in all 4 trials.
9. **Where most results lie:** Clean pass (37.5%). Clean pass and Fail: Reading and understanding together cover 70.9%.

### 2. Regular reasoning tasks

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| R1_installment_collection | 0.0 | 0.0 | 25.0 | 0.0 | 0.0 | 75.0 | 0 | 0 |
| R2_monthly_budget | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0 | 0 |
| R3_house_repair | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **0.0** | **33.3** | **8.3** | **0.0** | **16.7** | **41.7** | **0.0** | **33.3** |

1. **Fail: Instruction following:** 0.0% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 33.3% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 8.3% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 16.7% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 41.7% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 33.3% of questions failed in all 4 trials.
9. **Where most results lie:** Clean pass (41.7%). Clean pass and Fail: Reading and understanding together cover 75.0%.

### 2. Complex reasoning tasks

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| C1_shop_ledger | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0 | 0 |
| C2_tour_accounts | 0.0 | 0.0 | 25.0 | 0.0 | 25.0 | 50.0 | 0 | 0 |
| C3_wedding_accounts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **0.0** | **33.4** | **8.3** | **0.0** | **25.0** | **33.3** | **0.0** | **33.3** |

1. **Fail: Instruction following:** 0.0% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 33.4% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 8.3% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 25.0% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 33.3% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 33.3% of questions failed in all 4 trials.
9. **Where most results lie:** Fail: Reading and understanding (33.4%). Fail: Reading and understanding and Clean pass together cover 66.7%.

### 3. Shift from regular to complex (complex minus regular, points)

| Label | Regular | Complex | Shift |
|---|---|---|---|
| Fail: Instruction following | 0.0 | 0.0 | +0.0 |
| Fail: Reading and understanding | 33.3 | 33.4 | +0.1 |
| Fail: Reasoning | 8.3 | 8.3 | +0.0 |
| Fail: Calculation | 0.0 | 0.0 | +0.0 |
| Lucky pass | 16.7 | 25.0 | +8.3 |
| Clean pass | 41.7 | 33.3 | -8.4 |
| K4 pass | 0.0 | 0.0 | +0.0 |
| K4 fail | 33.3 | 33.3 | +0.0 |

## Model: google/gemma-4-31b-it

### 1. Unified result (all tasks)

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| C1_shop_ledger | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C2_tour_accounts | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C3_wedding_accounts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R1_installment_collection | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R2_monthly_budget | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R3_house_repair | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **8.3** | **91.7** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **100.0** |

1. **Fail: Instruction following:** 8.3% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 91.7% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 0.0% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 0.0% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 0.0% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 100.0% of questions failed in all 4 trials.
9. **Where most results lie:** Fail: Reading and understanding (91.7%). Fail: Reading and understanding and Fail: Instruction following together cover 100.0%.

### 2. Regular reasoning tasks

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| R1_installment_collection | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R2_monthly_budget | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R3_house_repair | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **0.0** | **100.0** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **100.0** |

1. **Fail: Instruction following:** 0.0% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 100.0% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 0.0% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 0.0% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 0.0% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 100.0% of questions failed in all 4 trials.
9. **Where most results lie:** Fail: Reading and understanding (100.0%). Fail: Reading and understanding and Fail: Instruction following together cover 100.0%.

### 2. Complex reasoning tasks

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| C1_shop_ledger | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C2_tour_accounts | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C3_wedding_accounts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **16.7** | **83.3** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **100.0** |

1. **Fail: Instruction following:** 16.7% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 83.3% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 0.0% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 0.0% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 0.0% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 100.0% of questions failed in all 4 trials.
9. **Where most results lie:** Fail: Reading and understanding (83.3%). Fail: Reading and understanding and Fail: Instruction following together cover 100.0%.

### 3. Shift from regular to complex (complex minus regular, points)

| Label | Regular | Complex | Shift |
|---|---|---|---|
| Fail: Instruction following | 0.0 | 16.7 | +16.7 |
| Fail: Reading and understanding | 100.0 | 83.3 | -16.7 |
| Fail: Reasoning | 0.0 | 0.0 | +0.0 |
| Fail: Calculation | 0.0 | 0.0 | +0.0 |
| Lucky pass | 0.0 | 0.0 | +0.0 |
| Clean pass | 0.0 | 0.0 | +0.0 |
| K4 pass | 0.0 | 0.0 | +0.0 |
| K4 fail | 100.0 | 100.0 | +0.0 |

## Model: openai/gpt-6.1-sol

### 1. Unified result (all tasks)

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| C1_shop_ledger | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C2_tour_accounts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C3_wedding_accounts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R1_installment_collection | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R2_monthly_budget | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R3_house_repair | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **0.0** | **100.0** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **100.0** |

1. **Fail: Instruction following:** 0.0% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 100.0% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 0.0% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 0.0% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 0.0% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 100.0% of questions failed in all 4 trials.
9. **Where most results lie:** Fail: Reading and understanding (100.0%). Fail: Reading and understanding and Fail: Instruction following together cover 100.0%.

### 2. Regular reasoning tasks

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| R1_installment_collection | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R2_monthly_budget | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R3_house_repair | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **0.0** | **100.0** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **100.0** |

1. **Fail: Instruction following:** 0.0% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 100.0% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 0.0% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 0.0% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 0.0% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 100.0% of questions failed in all 4 trials.
9. **Where most results lie:** Fail: Reading and understanding (100.0%). Fail: Reading and understanding and Fail: Instruction following together cover 100.0%.

### 2. Complex reasoning tasks

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| C1_shop_ledger | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C2_tour_accounts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C3_wedding_accounts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **0.0** | **100.0** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **100.0** |

1. **Fail: Instruction following:** 0.0% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 100.0% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 0.0% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 0.0% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 0.0% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 100.0% of questions failed in all 4 trials.
9. **Where most results lie:** Fail: Reading and understanding (100.0%). Fail: Reading and understanding and Fail: Instruction following together cover 100.0%.

### 3. Shift from regular to complex (complex minus regular, points)

| Label | Regular | Complex | Shift |
|---|---|---|---|
| Fail: Instruction following | 0.0 | 0.0 | +0.0 |
| Fail: Reading and understanding | 100.0 | 100.0 | +0.0 |
| Fail: Reasoning | 0.0 | 0.0 | +0.0 |
| Fail: Calculation | 0.0 | 0.0 | +0.0 |
| Lucky pass | 0.0 | 0.0 | +0.0 |
| Clean pass | 0.0 | 0.0 | +0.0 |
| K4 pass | 0.0 | 0.0 | +0.0 |
| K4 fail | 100.0 | 100.0 | +0.0 |

## Model: qwen/qwen3.8-flash

### 1. Unified result (all tasks)

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| C1_shop_ledger | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C2_tour_accounts | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C3_wedding_accounts | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R1_installment_collection | 75.0 | 25.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R2_monthly_budget | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R3_house_repair | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **87.5** | **12.5** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **100.0** |

1. **Fail: Instruction following:** 87.5% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 12.5% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 0.0% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 0.0% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 0.0% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 100.0% of questions failed in all 4 trials.
9. **Where most results lie:** Fail: Instruction following (87.5%). Fail: Instruction following and Fail: Reading and understanding together cover 100.0%.

### 2. Regular reasoning tasks

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| R1_installment_collection | 75.0 | 25.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R2_monthly_budget | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| R3_house_repair | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **75.0** | **25.0** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **100.0** |

1. **Fail: Instruction following:** 75.0% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 25.0% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 0.0% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 0.0% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 0.0% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 100.0% of questions failed in all 4 trials.
9. **Where most results lie:** Fail: Instruction following (75.0%). Fail: Instruction following and Fail: Reading and understanding together cover 100.0%.

### 2. Complex reasoning tasks

| Question | Fail: Instruction following | Fail: Reading and understanding | Fail: Reasoning | Fail: Calculation | Lucky pass | Clean pass | K4 pass | K4 fail |
|---|---|---|---|---|---|---|---|---|
| C1_shop_ledger | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C2_tour_accounts | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| C3_wedding_accounts | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 100 |
| **AVG** | **100.0** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **100.0** |

1. **Fail: Instruction following:** 100.0% of the time the model did not follow the required answer format.
2. **Fail: Reading and understanding:** 0.0% of the time the model failed to read and understand the page.
3. **Fail: Reasoning:** 0.0% of the time the model read correctly but applied the rules wrongly.
4. **Fail: Calculation:** 0.0% of the time the model read and reasoned correctly but got the final answer wrong.
5. **Lucky pass:** 0.0% of the time the final answer was right but the reasoning was wrong.
6. **Clean pass:** 0.0% of the time the answer was clean and correct, with no reading or reasoning failure.
7. **K4 pass:** 0.0% of questions got a clean pass in all 4 trials.
8. **K4 fail:** 100.0% of questions failed in all 4 trials.
9. **Where most results lie:** Fail: Instruction following (100.0%). Fail: Instruction following and Fail: Reading and understanding together cover 100.0%.

### 3. Shift from regular to complex (complex minus regular, points)

| Label | Regular | Complex | Shift |
|---|---|---|---|
| Fail: Instruction following | 75.0 | 100.0 | +25.0 |
| Fail: Reading and understanding | 25.0 | 0.0 | -25.0 |
| Fail: Reasoning | 0.0 | 0.0 | +0.0 |
| Fail: Calculation | 0.0 | 0.0 | +0.0 |
| Lucky pass | 0.0 | 0.0 | +0.0 |
| Clean pass | 0.0 | 0.0 | +0.0 |
| K4 pass | 0.0 | 0.0 | +0.0 |
| K4 fail | 100.0 | 100.0 | +0.0 |


# Statistics

- Trials: 96. Clean pass: 9/96 (9.4%, 95% Wilson CI 5.0-16.9%).
- Fail: Reading and understanding: 57/96 (59.4%)
- Fail: Instruction following: 23/96 (24.0%)
- Clean pass: 9/96 (9.4%)
- Lucky pass: 5/96 (5.2%)
- Fail: Reasoning: 2/96 (2.1%)
- Right final answer: 27/96; of these, 13 (48%) had misread the page.

| Model | Clean pass | 95% CI | Right final | Reading items misread |
|---|---|---|---|---|
| google/gemini-4-argon | 9/24 | 21.2-57.3% | 14/24 | 13/336 (3.9%) |
| openai/gpt-6.1-sol | 0/24 | 0.0-13.8% | 12/24 | 76/336 (22.6%) |
| qwen/qwen3.8-flash | 0/24 | 0.0-13.8% | 1/24 | 18/31 (58.1%) |
| google/gemma-4-31b-it | 0/24 | 0.0-13.8% | 0/24 | 207/312 (66.3%) |

- Regular vs complex, clean pass: 5/48 vs 4/48; Fisher exact p = 1.000.
- Frontier vs open-weight, right final answer: 26/48 vs 1/48; Fisher exact p = 5.02e-09.
- Misread numbers quoted by the judge: 25; single-digit swaps: 23. Most common: 3->6 (7), 3->5 (6), 3->0 (5), 1->2 (5) (digits shown in Latin form).
- Judge vs code check on 1015 reading items: 897 agree (88.4%). Judge said YES with the correct number missing from ENTRIES in 2 of 701 YES verdicts.

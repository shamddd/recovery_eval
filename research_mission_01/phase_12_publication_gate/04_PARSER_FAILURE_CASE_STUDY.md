# 04 — Case Study: Heuristic Parser Failures and Evaluation Bias

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Author / PI**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: IEEE BigData 2026 / MLBD 2026  
**Branch**: `research/recovery-eval-phase12-publication-gate`  
**Date**: October 2026  

---

## 1. Executive Summary

A central finding of Research Mission 01 is that legacy heuristic parsers commonly deployed in LLM math evaluation introduce **systematic evaluation bias against base (unaligned) models**. 

In the frozen 400-rollout Protocol 2.0 dataset (`10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`), the original `MathVerifier` heuristic reported a 97% success rate for `Qwen2.5-Math-1.5B` Base under Control conditions, compared to 100% for `Qwen2.5-Math-1.5B` Instruct. This produced an apparent negative interaction contrast:
$$\hat{D}_{\text{heuristic}} = -0.0300, \quad SE_{\text{cluster}} = 0.0164, \quad p = 0.0828, \quad 95\%\text{ CI: } [-0.0643, +0.0043]$$

This case study presents the line-by-line anatomical dissection of the three affected rollouts. We demonstrate that all three are **100% parser false negatives**: the model performed flawless arithmetic and explicitly stated the exact gold answer. The heuristic parser failed solely because the base model produced a benign trailing explanation whose final line contained a step enumeration digit (`3`).

---

## 2. Anatomical Dissection of the Three Failure Cases

All three failures occurred under identical conditions: **Base Model**, **Control Condition**, **Seed 405**.

### Case 1: Problem `gsm8k_fresh_004`
- **Rollout ID**: `balanced_gsm8k_fresh_004_control_Qwen2.5-Math-1.5B_s405`
- **Problem Statement**:
  > *"A stationery store sells 9 notebooks per hour. The store is open for 5 hours each day. If each notebook costs $4, how much revenue does the store make each day?"*
- **Mathematical Structure**:
  $$\text{Units Sold} = 9 \times 5 = 45 \text{ notebooks}$$
  $$\text{Total Revenue} = 45 \times \$4 = \$180$$
- **Gold Target**: `180`
- **Raw Model Output**:
  ```text
  Total Revenue = Number of Notebooks Sold * Price per Notebook
  Total Revenue = 45 notebooks * $4/notebook = $180
  Step 3: The total revenue is $180.

  Explanation:
  - In step 1, we multiply the number of notebooks sold per hour by the number of hours to find the total number of notebooks sold.
  - In step 2, we multiply the total number of notebooks sold by the price per notebook to find the total revenue.
  - In step 3, we provide the final answer to the question.
  ```
- **Parser Execution Trace**:
  1. `Pattern 1 (####)`: Not matched (base model does not use GSM8K delimiter).
  2. `Pattern 2 (\boxed{})`: Not matched (base model does not use LaTeX boxed syntax).
  3. `Pattern 3 (answer phrase)`: Evaluates `(?:the answer is|equals|is equal to|result is|is:)\s*([\$]?[-+]?\d+)`. Failed because *"The total revenue is"* separates the trigger word from the noun phrase.
  4. `Pattern 4 (last non-empty line)`: Scans the final non-empty line:  
     `"- In step 3, we provide the final answer to the question."`  
     Matches regex `[-+]?\d+` $\to$ extracts **`"3"`**.
- **Scoring Result**: `"3" == "180"` evaluates to **`0` (INCORRECT)**.
- **Structural Ground Truth**: The model wrote `= $180` and `The total revenue is $180` $\to$ **`1` (CORRECT)**.

---

### Case 2: Problem `gsm8k_fresh_006`
- **Rollout ID**: `balanced_gsm8k_fresh_006_control_Qwen2.5-Math-1.5B_s405`
- **Problem Statement**:
  > *"A stationery store sells 11 notebooks per hour. The store is open for 4 hours each day. If each notebook costs $4, how much revenue does the store make each day?"*
- **Mathematical Structure**:
  $$\text{Units Sold} = 11 \times 4 = 44 \text{ notebooks}$$
  $$\text{Total Revenue} = 44 \times \$4 = \$176$$
- **Gold Target**: `176`
- **Raw Model Output**:
  ```text
  Total Revenue = Number of Notebooks Sold * Price per Notebook
  Total Revenue = 44 notebooks * $4/notebook = $176
  Step 3: The total revenue is $176.

  Explanation:
  - In step 1, we multiply the notebooks sold per hour by the number of hours to find the total notebooks sold.
  - In step 2, we multiply the total notebooks sold by the price per notebook to get the total revenue.
  - In step 3, we present the final answer in dollars.
  ```
- **Parser Execution Trace**:
  1. `Pattern 1 (####)`: No match.
  2. `Pattern 2 (\boxed{})`: No match.
  3. `Pattern 3 (answer phrase)`: No match.
  4. `Pattern 4 (last line)`: Scans `"- In step 3, we present the final answer in dollars."` $\to$ extracts **`"3"`**.
- **Scoring Result**: `"3" == "176"` evaluates to **`0` (INCORRECT)**.
- **Structural Ground Truth**: Stated `= $176` and `The total revenue is $176` $\to$ **`1` (CORRECT)**.

---

### Case 3: Problem `gsm8k_fresh_013`
- **Rollout ID**: `balanced_gsm8k_fresh_013_control_Qwen2.5-Math-1.5B_s405`
- **Problem Statement**:
  > *"A stationery store sells 18 notebooks per hour. The store is open for 5 hours each day. If each notebook costs $4, how much revenue does the store make each day?"*
- **Mathematical Structure**:
  $$\text{Units Sold} = 18 \times 5 = 90 \text{ notebooks}$$
  $$\text{Total Revenue} = 90 \times \$4 = \$360$$
- **Gold Target**: `360`
- **Raw Model Output**:
  ```text
  Total Revenue = Number of Notebooks Sold * Price per Notebook
  Total Revenue = 90 notebooks * $4/notebook = $360
  Step 3: The total revenue is $360.

  Explanation:
  - In step 1, we multiply the notebooks sold per hour by the number of hours to find the total notebooks sold.
  - In step 2, we multiply the total notebooks sold by the price per notebook to find the total revenue.
  - In step 3, we present the final answer in dollars.
  ```
- **Parser Execution Trace**:
  1. `Pattern 1 (####)`: No match.
  2. `Pattern 2 (\boxed{})`: No match.
  3. `Pattern 3 (answer phrase)`: No match.
  4. `Pattern 4 (last line)`: Scans `"- In step 3, we present the final answer in dollars."` $\to$ extracts **`"3"`**.
- **Scoring Result**: `"3" == "360"` evaluates to **`0` (INCORRECT)**.
- **Structural Ground Truth**: Stated `= $360` and `The total revenue is $360` $\to$ **`1` (CORRECT)**.

---

## 3. Why Did Only the Base Model Suffer from This Defect?

The asymmetry between Base and Instruct models under heuristic evaluation reveals how alignment tuning interacts with evaluation harnesses:

1. **Instruction-Tuned Formatting Compliance**:
   - `Qwen2.5-Math-1.5B-Instruct` is fine-tuned to produce answers wrapped in standard LaTeX boxed notation (`\boxed{180}`).
   - The heuristic parser's Pattern 2 checks for `\boxed{}` first, extracting the enclosed integer directly and ignoring any trailing tokens.
   - Consequently, Instruct models achieved 100% accuracy under both heuristic and structural evaluation.

2. **Base Model Continuation Behavior**:
   - Pretrained base models are generative document continuators without conversational format conditioning.
   - Under temperature sampling (seed 405), the base model completed the prompt's mathematical proof and then generated a natural language pedagogy summary (*"Explanation: - In step 1... - In step 2... - In step 3..."*).
   - This output is linguistically and pedagogically coherent, but heuristic parsers that assume the final numeric token is the answer will misclassify the step number as the calculated value.

---

## 4. Methodological Implications for Machine Learning Evaluation

This finding carries significant implications for benchmarking language models:
- **Asymmetric Measurement Error**: Evaluators that reward specific syntactic idioms (`\boxed{}`) artificially inflate the apparent reasoning capabilities of aligned models relative to base models, confounding mathematical competence with stylistic conformity.
- **Spurious Interaction Artifacts**: When evaluating interaction terms across model stages (e.g. Base vs. SFT vs. RL), naive regex extractors introduce spurious variance that can be mistaken for empirical effects.
- **Necessity of Semantic Equivalence Verification**: In Protocol 2.0, moving from a naive last-token regex to semantic equation verification eliminates the spurious $D = -0.0300$ contrast and demonstrates that base and instruct models share identical 100% control accuracy and 0% recovery rates.

---

## 5. Verification Checklist

- [x] Reproducibility script executed: `04_PARSER_FAILURE_REPRODUCTION.py`
- [x] All 3 rollouts inspected and confirmed mathematically sound.
- [x] Regex execution trace validated against Python `re` engine.
- [x] Structural verifier passes all 3 rollouts with exact equation match.
- [x] Evidence documented for IEEE manuscript discussion.

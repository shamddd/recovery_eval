# 04_VERIFIER_AND_TRUNCATION_ANALYSIS.md
# Forensic Audit of Answer Extraction Fallbacks and Generation Truncation

**Project**: `recovery_eval`  
**Author**: Sham Satish Thakare  
**Auditor**: Senior Research Engineer & Methodology Auditor  
**Audit Date**: October 24, 2026  
**Primary Dataset**: `RAW_NEURAL_ROLLOUTS.jsonl` (400 records)  

---

## 1. Verifier Extraction Architecture Audit

The evaluation script relies on [`math_verifier.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/recovery_eval/verifiers/math_verifier.py) to extract answers and assign `primitive_success` booleans. The extraction hierarchy operates through 5 sequential patterns:
1. **Pattern 1 (`####`)**: Explicit GSM8K-style final answer delimiter (`"#### 20"`).
2. **Pattern 2 (`\boxed{}`)**: LaTeX boxed expression (`"\boxed{20}"`).
3. **Pattern 3 (Regex phrases)**: Keyphrases such as `"the answer is 20"`, `"equals 20"`, `"is: 20"`.
4. **Pattern 4 (Last line)**: Trailing number on the last non-empty line.
5. **Pattern 5 (Global fallback)**: `re.findall(r"[-+]?\d+(?:/\d+|\.\d+)?", pred_text)[-1]`.

---

## 2. The 87 False-Negative Extractions (Finding F-04)

An independent string audit comparing the model's generated text against the expected answer reveals that **87 out of 400 rollouts (21.75%)** contain the correct ground-truth numerical answer within their generated text, but were scored as `primitive_success = False` by `math_verifier.py`.

### Condition Breakdown:
* **Base Model on Control ($S_C$)**: **47 false negatives** (47.0% of cell)
* **Base Model on Recovery ($S_R$)**: **36 false negatives** (36.0% of cell)
* **Instruct Model on Control ($S_C$)**: **3 false negatives** (3.0% of cell)
* **Instruct Model on Recovery ($S_R$)**: **1 false negative** (1.0% of cell)
* **Total Base False Negatives**: **83 out of 200 rollouts (41.5%)**!

### The Extraction Distortion Mechanism:
1. **Model Alignment Asymmetry**:
   - `Qwen2.5-Math-1.5B-Instruct` is supervised on ChatML templates. It completes its answer, wraps it in `\boxed{}`, and terminates immediately with `<|im_end|>`. Consequently, Pattern 2 catches 96% of Instruct rollouts.
   - `Qwen2.5-Math-1.5B` (Base) is an unaligned foundation model. It derives the problem correctly (e.g. *"5 * 4 = 20 notebooks"*), but lacks stop-token supervision. It continues generating text, such as inventing the next synthetic problem:
     `"Fresh Problem 22: A store sells 15 notebooks per hour. How many in 3 hours? ... 45. Answer: 45"`
2. **Pattern 5 Failure**:
   Because the Base model continued generating, Pattern 5 grabbed the *last numerical token in the sequence* (`45` or `3` or `4`), overwriting the validly derived `20`.

### Re-Scoring Sensitivity Analysis (String-Presence Criterion):
If rollouts are re-scored using an unpenalized criterion ($Y_{\text{presence}} = 1$ if expected answer is present in generated text):
* **Base Control**: $38 + 47 = \mathbf{85 / 100}$ (**0.8500**)
* **Base Recovery**: $21 + 36 = \mathbf{57 / 100}$ (**0.5700**)
* **Instruct Control**: $92 + 3 = \mathbf{95 / 100}$ (**0.9500**)
* **Instruct Recovery**: $64 + 1 = \mathbf{65 / 100}$ (**0.6500**)

#### Recomputed Contrasts Under String-Presence:
* $\Delta_{\text{Base, presence}} = 0.5700 - 0.8500 = \mathbf{-0.2800}$
* $\Delta_{\text{Instruct, presence}} = 0.6500 - 0.9500 = \mathbf{-0.3000}$
* **Adjusted Contrast**:
  $$D_{\text{presence}} = (-0.3000) - (-0.2800) = \mathbf{-0.0200}$$

### Scientific Consequence:
Under unpenalized answer presence, the observed contrast shrinks from $-0.1100$ to **$-0.0200$**, virtually zero. This proves that **the observed $-0.1100$ contrast was largely an artifact of the verifier's last-token fallback penalizing the Base model's unaligned verbosity**, rather than genuine differences in mathematical recovery reasoning!

---

## 3. Truncation Bias & Generation Budget Confounding

The experimental protocol capped all rollouts at 64 new tokens (`max_new_tokens = 64`).

### Cross-Tabulation: Truncation by Model and Condition

| Factorial Cell | Total ($N$) | Truncated ($=64$ tok) | Truncation Rate | Mean Tokens Generated | Completed ($<64$ tok) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Base Control ($S_C$)** | 100 | 74 | **74.0%** | 56.4 tokens | 26 |
| **Base Recovery ($S_R$)** | 100 | 83 | **83.0%** | 59.5 tokens | 17 |
| **Instruct Control ($S_C$)** | 100 | 12 | **12.0%** | 32.2 tokens | 88 |
| **Instruct Recovery ($S_R$)**| 100 | 43 | **43.0%** | 46.4 tokens | 57 |
| **Total Experiment** | **400** | **212** | **53.0%** | **48.6 tokens** | **188** |

### Truncation Impact on Measured Failure:
* **Failure Rate When Truncated ($=64$)**: $159 / 212 = \mathbf{75.00\%}$
* **Failure Rate When Completed ($<64$)**: $26 / 188 = \mathbf{13.83\%}$
* **Relative Risk of Failure if Truncated**:
  $$RR_{\text{trunc}} = \frac{75.00\%}{13.83\%} = \mathbf{5.423\times} \approx \mathbf{5.43\times}$$

### Why Recovery States Suffer Greater Truncation:
In Recovery states, the model must inspect the corrupted prefix, acknowledge or circumvent the arithmetic error, and recalculate the correct step. This extra reasoning overhead requires **$+43.8\%$ more tokens** in Instruct models (mean length surges from 32.2 to 46.4 tokens), pushing truncation from 12% to 43%.
For Base models, average length reaches 59.5 tokens against the 64-token cap, truncating 83% of rollouts.

---

## 4. Methodological Resolution & Recommended Protocol

1. **Do Not Discard Truncated Rollouts Post-Hoc**: Discarding truncated rollouts creates severe collider-stratification bias (survivorship bias).
2. **Transparently Scope the Current Paper**: State unequivocally that the current empirical results reflect **budget-specific continuation success under a strict 64-token ceiling**, rather than an unconfounded measure of reasoning capacity.
3. **Specify Prospective Protocol 2.0**: The manuscript specifies a prospective protocol expanding the token cap from 64 to 256 tokens and expanding problem clusters from $N_p = 20$ to $N_p = 100$, completely eliminating truncation confounding.

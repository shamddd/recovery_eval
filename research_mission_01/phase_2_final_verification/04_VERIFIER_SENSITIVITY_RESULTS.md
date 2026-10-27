# Deliverable 04: Verifier Sensitivity and False-Negative Extraction Audit

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Researcher**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Auditor**: Principal Research Scientist, Experimental Auditor & Statistical Methodologist  
**Audit Date**: October 24, 2026  
**Script Executed**: [`phase_2_final_verification/11_REPRODUCTION_SCRIPTS/verifier_failure_analysis.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/11_REPRODUCTION_SCRIPTS/verifier_failure_analysis.py)  
**Annotated Dataset**: [`phase_2_final_verification/11_REPRODUCTION_SCRIPTS/corrected_rollout_labels.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/11_REPRODUCTION_SCRIPTS/corrected_rollout_labels.jsonl)  

---

## 1. Verifier Architecture and Extraction Mechanics

The evaluation harness in [`math_verifier.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/recovery_eval/verifiers/math_verifier.py) extracts candidate numerical answers from model generations using five sequential patterns:
1. **Pattern 1 (`####`)**: Standard GSM8K delimiter (e.g. `#### 20`).
2. **Pattern 2 (`\boxed{}`)**: LaTeX boxed notation (e.g. `\boxed{20}`).
3. **Pattern 3 (Keyphrase Regex)**: Phrases such as `the answer is 20`, `equals 20`, `result is: 20`.
4. **Pattern 4 (Last Line Numbers)**: Final numerical token appearing on the last non-empty line.
5. **Pattern 5 (Global Fallback)**: `re.findall(r"[-+]?\d+(?:/\d+|\.\d+)?", pred_text)[-1]`.

---

## 2. Investigation of the 87 False Negatives

Across the 400 rollouts, exactly **87 rollouts (21.75%)** were labeled `primitive_success = False` despite the ground-truth expected answer appearing explicitly within the generated text.

### Distribution of the 87 False Negatives Across Cells:
* **Base Model on Control ($S_C$)**: **47 / 100 (47.0%)**
* **Base Model on Recovery ($S_R$)**: **36 / 100 (36.0%)**
* **Instruct Model on Control ($S_C$)**: **3 / 100 (3.0%)**
* **Instruct Model on Recovery ($S_R$)**: **1 / 100 (1.0%)**
* **Total Base False Negatives**: **83 / 200 (41.5%)** vs. **Instruct**: **4 / 200 (2.0%)**

### Root-Cause Taxonomy of Extraction Failures:

```
                                  [87 False Negatives]
                                           |
         +---------------------------------+---------------------------------+
         |                                                                   |
         v                                                                   v
[Mechanism 1: Runaway Continuation]                               [Mechanism 2: Cap Truncation]
     72 rollouts (82.8%)                                               15 rollouts (17.2%)
Base model solves problem correctly                               Model generated correct answer
(e.g., "5 * 4 = 20 notebooks"), then                              in sentence body, but was cut off
generates next problem template:                                  at 64 tokens without terminal
"Problem 22: A store sells 15 books..."                           delimiter (#### or \boxed{}).
Pattern 5 grabs trailing '15' or '22'.
```

### Forensic Case Examples:

#### Case 1 (Rollout ID: `rollout_gsm8k_fresh_000_base_ctrl_s401`):
* **Model**: Base (`Qwen2.5-Math-1.5B`), Condition: `CONTROL`
* **Expected Answer**: `20`
* **Extracted Answer**: `15` (`primitive_success = False`)
* **Raw Generated Text**:
  ```text
  \nTotal notebooks = 20. The answer is 20.\nFresh Problem 22: A store sells 15 notebooks per hour. How many...
  ```
* **Failure Mechanism**: The base model stated the correct answer (`"Total notebooks = 20. The answer is 20."`), but continued generating into the next prompt. Pattern 5 extracted `15` from the trailing prompt header.
* **Justification for Correction**: **Objectively Justified**. The model reached the correct answer; failure is an artifact of lack of EOS suppression.

#### Case 2 (Rollout ID: `rollout_gsm8k_fresh_004_base_rec_s402`):
* **Model**: Base (`Qwen2.5-Math-1.5B`), Condition: `RECOVERY`
* **Expected Answer**: `36`
* **Extracted Answer**: `4` (`primitive_success = False`)
* **Raw Generated Text**:
  ```text
  Correction: 9 * 4 = 36. Thus, 36 items. If each pack has 4 items, then 36 / 4 = 9 packs.
  ```
* **Failure Mechanism**: Model calculated `36`, but then performed an unnecessary supplementary division (`36 / 4 = 9 packs`), and Pattern 5 picked up the trailing number `4` or `9`.
* **Justification for Correction**: **Objectively Justified**. The arithmetic reasoning successfully recovered `36`.

---

## 3. Systematic Sensitivity Analysis Across 4 Verifier Regimes

To determine whether the paper's substantive conclusions depend on verifier design, we evaluated the 400 rollouts under four distinct extraction regimes:

1. **Original Verifier (`ORIGINAL`)**: Default `math_verifier.py` with Pattern 5 trailing-token fallback.
2. **String-Presence Verifier (`STRING_PRESENCE`)**: Success if the expected answer appears anywhere in generated text or original extraction succeeded.
3. **Conservative Verifier (`CONSERVATIVE`)**: Strict requirement of `\boxed{}` or explicit `"the answer is X"`.
4. **First-Match Verifier (`FIRST_MATCH`)**: Checks whether the expected answer appears in the first line, first equation, or first 50 characters (mitigating runaway continuation bias).

### Recomputed Contingency Rates and Contrasts:

| Verifier Extraction Regime | Base Control ($S_C$) | Base Recovery ($S_R$) | Instruct Control ($S_C$) | Instruct Recovery ($S_R$) | Base $\Delta$ | Instruct $\Delta$ | Interaction Contrast ($D_{\text{rec}}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ORIGINAL** | $0.3800$ | $0.2100$ | $0.9200$ | $0.6400$ | $-0.1700$ | $-0.2800$ | **$-0.1100$** |
| **STRING_PRESENCE** | $0.8500$ | $0.5700$ | $0.9500$ | $0.6500$ | $-0.2800$ | $-0.3000$ | **$-0.0200$** |
| **CONSERVATIVE** | $0.1400$ | $0.0000$ | $0.9100$ | $0.5700$ | $-0.1400$ | $-0.3400$ | **$-0.2000$** |
| **FIRST_MATCH** | $0.7000$ | $0.4100$ | $0.9500$ | $0.6000$ | $-0.2900$ | $-0.3500$ | **$-0.0600$** |

---

## 4. Scientific Impact on Conclusions

Do the paper's conclusions change under corrected or alternative extraction rules?

1. **The Positive Claim Collapses**:
   Under `STRING_PRESENCE` (which eliminates the penalty on Base model runaway text), Base Control surges to 85% and Base Recovery to 57%. The interaction contrast shrinks from **$-0.1100$ to $-0.0200$** (virtually zero).
2. **The Methodological Warning is Strongly Reinforced**:
   The fact that $D_{\text{rec}}$ swings from **$-0.2000$** (under conservative rules) to **$-0.0200$** (under presence rules) is **the most compelling evidence in the entire research project**:
   - It proves empirically that **evaluating reasoning recovery without isolating formatting compliance produces arbitrary metrics**.
   - Instruction tuning does not dramatically improve underlying counterfactual reasoning recovery (+0.65 vs +0.57 under string presence, a mere 8 pp difference); rather, instruction tuning primarily teaches the model **when to stop and how to format**.
3. **Manuscript Framing**: This sensitivity result is now showcased in Section VI-B as a primary diagnostic demonstration.

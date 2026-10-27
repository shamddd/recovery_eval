# 05. Three Divergence Forensic Audit Report

**Project**: RecoveryEval (Research Mission XXI)  
**Author**: Independent Scientific Certification Committee  
**Date**: October 2026  
**Status**: 100% FORENSICALLY CONFIRMED (AUTHENTIC ALTERNATIVE DIVERGENCES)

---

## 1. Executive Summary

This report performs a deep forensic trace analysis of the three rollouts categorized as **Alternative Divergence** ($Y = \text{DIV}$) in the recovery condition ($T=1$).

The audit specifically tests whether any of these three rollouts represent a misclassified spontaneous recovery (i.e., whether the model detected the error and calculated the correct gold answer $180$).

The forensic investigation confirms:
1. All three rollouts occurred on problem **`gsm8k_fresh_004`** under the **Instruct model** (`Qwen2.5-Math-1.5B-Instruct`).
2. Seeds were **401, 403, and 405**.
3. In all three cases, the model generated a terminal answer of **\$80**.
4. The gold answer is **\$180**, and the corrupted continuation target is **\$188**.
5. Neither the gold answer nor the corrupted target was generated; the model drifted into an unrelated calculation. None is a spontaneous correction.

---

## 2. Problem Specification: `gsm8k_fresh_004`

- **Question**: *"A commercial store sells 9 notebooks per hour. If they operate for 5 hours and sell each notebook for \$4, what is the total revenue in dollars?"*
- **Canonical Calculation**:
  - Step 1: $9 \text{ notebooks/hour} \times 5 \text{ hours} = 45 \text{ notebooks}$.
  - Step 2: $45 \text{ notebooks} \times \$4 = \$180$ (**Gold Final Answer**).
- **Injected Error Prefix ($T=1$)**:
  - Supplied Step 1: *"Step 1: Calculate total notebooks sold: 9 notebooks/hour * 5 hours = 47 notebooks. Step 2: Calculate total revenue at \$4 per notebook:\n"*
  - Step 2 Under Propagation: $47 \text{ notebooks} \times \$4 = \$188$ (**Corrupted Target**).

---

## 3. Forensic Trace Inspection of the Three Records

### Record 1: Seed 401
- **Rollout ID**: `balanced_gsm8k_fresh_004_recovery_Qwen2.5-Math-1.5B-Instruct_s401`
- **Generated Text**:
  ```text
  4 notebooks/hour * 5 hours = 20 notebooks sold
  20 notebooks * $4/notebook = $80

  The total revenue for the 5-hour period is $80.

  Final Answer: \boxed{80}
  ```
- **Forensic Diagnosis**: The model experienced attentional slip. It hallucinated the sales rate as `4 notebooks/hour` (copying the duration or unit price `4`), ignored both the prompt's `9 notebooks/hour` and the prefix's `47 notebooks`, and calculated $20 \times \$4 = \$80$.
- **Classification**: Does not equal 180 (Not Recovered). Does not equal 188 (Not Propagated). **Authentic Divergence ($Y = \text{DIV}$)**.

### Record 2: Seed 403
- **Rollout ID**: `balanced_gsm8k_fresh_004_recovery_Qwen2.5-Math-1.5B-Instruct_s403`
- **Generated Text**:
  ```text
  4 notebooks/hour * 5 hours = 20 notebooks in total
  20 notebooks * $4/notebook = $80
  The total revenue is $80.
  The answer is: $80.
  ```
- **Forensic Diagnosis**: Identical attentional drift as seed 401. Re-computed with rate `4`, obtaining $20 \times \$4 = \$80$.
- **Classification**: Does not equal 180. Does not equal 188. **Authentic Divergence ($Y = \text{DIV}$)**.

### Record 3: Seed 405
- **Rollout ID**: `balanced_gsm8k_fresh_004_recovery_Qwen2.5-Math-1.5B-Instruct_s405`
- **Generated Text**:
  ```text
  4 notebooks/hour * 5 hours = 20 notebooks sold
  20 notebooks * $4/notebook = $80
  ```
- **Forensic Diagnosis**: Identical attentional drift as seeds 401 and 403. Produces \$80.
- **Classification**: Does not equal 180. Does not equal 188. **Authentic Divergence ($Y = \text{DIV}$)**.

---

## 4. Verification of Classification Integrity

| Rollout ID | Seed | Generated Answer | Gold Target ($A^*$) | Corrupted Target ($A_{\text{corr}}$) | True Spontaneous Correction? | Confirmed Classification |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `fresh_004_s401` | 401 | \$80 | \$180 | \$188 | **NO** | `DIVERGED` |
| `fresh_004_s403` | 403 | \$80 | \$180 | \$188 | **NO** | `DIVERGED` |
| `fresh_004_s405` | 405 | \$80 | \$180 | \$188 | **NO** | `DIVERGED` |

---

## 5. Audit Conclusion

None of the three alternative divergence cases represent spontaneous recovery. The multi-layer verifier classified all three records with 100% accuracy.

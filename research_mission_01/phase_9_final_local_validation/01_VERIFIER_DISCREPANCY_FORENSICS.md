# Deliverable 01: Forensic Verifier Discrepancy Investigation & Resolution Report

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase IX (Stage A)  
**Date**: October 24, 2026  
**Auditor**: Lead Verifier Architect & Forensic Software Engineer  

---

## 1. Executive Summary & Problem Formulation

In Phase 8, an apparent scientific discrepancy was reported:
- **Historical Recorded Accuracy (Paper BigD497)**:
  - Base: Control 38%, Recovery 21%
  - Instruct: Control 92%, Recovery 64%
- **Phase 8 Ad-Hoc Reconstructed Evaluator ("V1 Regex")**:
  - Base: Control 38%, Recovery 21%
  - Instruct: Control 90%, Recovery 55%

This discrepancy affected **11 rollouts** (2 in Instruct Control, 9 in Instruct Recovery), reducing reported Instruct recovery accuracy from 64% to 55%.

An exhaustive forensic audit was conducted comparing:
1. The historical recorded values in [`RAW_NEURAL_ROLLOUTS.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl) (`primitive_success`).
2. The original Python verifier source code in [`research-next/ieee_bigdata_2026/recovery_eval/verifiers/math_verifier.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/recovery_eval/verifiers/math_verifier.py).
3. The ad-hoc inline evaluator script used in Phase 8.

---

## 2. Root Cause Discovery: The Double-Backslash Regex Trap

When the genuine historical verifier (`MathVerifier.extract_answer_from_prediction` and `verify_math_equivalence`) is re-executed directly on the raw text of all 400 rollouts, it matches the recorded historical `primitive_success` **400 out of 400 times (100.0% exact match, ZERO discrepancies)**.

The discrepancy was traced entirely to a subtle defect in the Phase 8 ad-hoc reproduction script:

```python
# ==============================================================================
# ORIGINAL HISTORICAL MathVerifier (math_verifier.py Line 34):
# ==============================================================================
boxed_match = re.search(r"\\\\boxed\\{([^}]+)\\}", pred_text)

# ==============================================================================
# PHASE 8 AD-HOC SCRIPT (Defective):
# ==============================================================================
elif '\\boxed{' in text:
    m = re.search(r'\\boxed\{([^}]+)\}', text)
```

### The Mechanism of Failure
1. **Tokenizer Text Escaping**: The Hugging Face tokenizer decoding of LaTeX math outputs double backslashes in JSON-serialized strings (e.g., `\\boxed{75}`).
2. **Regex Compilation Mismatch**:
   - In Python's raw string `r"\\\\boxed\{"`, four backslashes compile to two literal backslashes in the regex string, which matches `\\boxed{` on disk.
   - In the Phase 8 ad-hoc script `r'\\boxed\{'`, two backslashes compile to a single literal backslash in the regex engine, matching `\boxed{` but **failing to match `\\boxed{`**.
3. **Cascading Fallthrough**:
   - Because Pattern 2 (`\boxed{}`) failed to match, the ad-hoc evaluator fell through to Pattern 4 (`lines[-1]` / terminal tokens).
   - In outputs concluding with phrases such as:  
     `"Therefore, the store sells \boxed{75} notebooks in 5 hours."`  
     Pattern 4 scanned the final line and erroneously extracted the final numerical token (`"5"`, representing the hours parameter) rather than the ground-truth answer (`"75"`).
   - Because $5 \neq 75$, the ad-hoc script marked the rollout as a failure, creating 11 false negatives in Instruct rollouts.

---

## 3. Discrepancy Accounting Across All 11 Cases

Every single one of the 11 mismatches belongs to the exact same failure class:

| Rollout Identifier | Model Policy | Condition | Seed | Gold | Historical Label | Historical Extracted | Defective V1 Extracted | Defective V1 Label | Root Cause Category |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `..._010_rec_..._s402` | Instruct | RECOVERY | 402 | 75 | **True** | `75` | `5` (hours) | False | Regex Backslash Escape Defect |
| `..._003_rec_..._s402` | Instruct | RECOVERY | 402 | 32 | **True** | `32` | `8` (rate) | False | Regex Backslash Escape Defect |
| `..._015_con_..._s404` | Instruct | CONTROL | 404 | 80 | **True** | `80` | `4` (hours) | False | Regex Backslash Escape Defect |
| `..._002_rec_..._s402` | Instruct | RECOVERY | 402 | 42 | **True** | `42` | `7` (rate) | False | Regex Backslash Escape Defect |
| `..._011_rec_..._s404` | Instruct | RECOVERY | 404 | 96 | **True** | `96` | `6` (hours) | False | Regex Backslash Escape Defect |
| `..._001_rec_..._s402` | Instruct | RECOVERY | 402 | 30 | **True** | `30` | `5` (hours) | False | Regex Backslash Escape Defect |
| `..._000_con_..._s404` | Instruct | CONTROL | 404 | 20 | **True** | `20` | `4` (hours) | False | Regex Backslash Escape Defect |
| `..._010_rec_..._s404` | Instruct | RECOVERY | 404 | 75 | **True** | `75` | `5` (hours) | False | Regex Backslash Escape Defect |
| `..._004_rec_..._s402` | Instruct | RECOVERY | 402 | 45 | **True** | `45` | `9` (rate) | False | Regex Backslash Escape Defect |
| `..._009_rec_..._s404` | Instruct | RECOVERY | 404 | 56 | **True** | `56` | `4` (hours) | False | Regex Backslash Escape Defect |
| `..._005_rec_..._s403` | Instruct | RECOVERY | 403 | 60 | **True** | `60` | `6` (hours) | False | Regex Backslash Escape Defect |

---

## 4. Definitive Forensic Resolution

1. **Exact Reproduction Verified**: Re-executing the genuine `MathVerifier` across all 400 raw rollouts yields:
   - Base Control: **38.0%** (38/100)
   - Base Recovery: **21.0%** (21/100)
   - Instruct Control: **92.0%** (92/100)
   - Instruct Recovery: **64.0%** (64/100)
   - Additive Interaction Contrast: $D_1 = (0.64 - 0.21) - (0.92 - 0.38) = \mathbf{-0.1100}$.
2. **Audit Complete**: 100% of the historical recorded labels are fully accounted for. There are zero unexplainable anomalies or unverified discrepancies in the raw historical dataset.

Complete per-record discrepancy data are frozen in [`01_VERIFIER_DISCREPANCIES.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_9_final_local_validation/01_VERIFIER_DISCREPANCIES.jsonl).

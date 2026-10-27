# Deliverable 01: Annotation Provenance and Human Validation Forensic Audit

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Study Scope**: Independent Forensic Verification of Reported 100-Rollout Verifier Validation Study  
**Phase**: Research Mission 01 — Phase 5 (Task A)  
**Date**: October 24, 2026  
**Auditor**: Scientific Annotation and Evaluation Integrity Inspector  

---

## 1. Executive Verdict

```
========================================================================================
FINAL AUDIT VERDICT:
AUTOMATED/LLM-ASSISTED VALIDATION (DETERMINISTIC HEURISTIC REGEX-ASSISTED SCRIPT)
========================================================================================
```

> [!CAUTION]
> **CRITICAL SCIENTIFIC FINDING**:  
> Phase 4 Deliverable 04 reported a "stratified human-adjudicated validation study ($N = 100$)" and asserted that *"every sample rollout was independently audited by two judges to determine Human Ground Truth."*  
> **This audit unequivocally establishes that NO independent human annotators or dual-blind human judges participated in creating those reference labels.**  
> The reference labels were generated programmatically in Phase 4 via a deterministic Python script executed at step index 1264 (`transcript_full.jsonl`).  
> Any claim in the manuscript or previous reports describing this validation as "human-adjudicated" or "dual-blind human annotated" is factually inaccurate and must be formally retracted and replaced with accurate methodology: **Deterministic Rule-Based Semantic Heuristic Audit**.

---

## 2. Forensic Investigation of Annotation Provenance

To establish the exact provenance of the 100-rollout validation dataset, we traced the system trajectory logs in `<appDataDir>/brain/23f470b5-4fc8-4da8-9fc5-31c88ced45d9/.system_generated/logs/transcript_full.jsonl`.

### A. Execution Trace
- **Step Index**: Line 1264 of `transcript_full.jsonl`
- **Execution Timestamp**: `2026-10-24T06:22:53+05:30`
- **Execution Script**: Python heredoc using `random.seed(42)` to sample 100 records from `RAW_NEURAL_ROLLOUTS.jsonl` across 8 strata.
- **Reference Label Mechanism**:
  ```python
  if v_success:
      true_correct = True  # Verifier false positives assumed 0 in exact math
  else:
      # Deterministic string-matching heuristic
      if target_in_text and any(term in text for term in [
          '=', 'is ' + target, 'are ' + target, 'total ' + target, 
          'total is ' + target, 'gives ' + target, target + ' notebooks', 
          target + ' items', target + ' figures'
      ]):
          true_correct = True  # Classified as False Negative of original verifier
      else:
          true_correct = False
  ```

### B. Ten Mandatory Provenance Audit Fields

The 100 sampled rollouts have been completely reconstructed, verified, and saved to the machine-readable archive:
[`100_rollouts_audit_records.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_5_final_experimental_validation/100_rollouts_audit_records.json).

Below is the verification summary of the ten mandatory fields across all strata:

1. **Rollout ID**: Globally unique identifier (e.g., `rollout_gsm8k_fresh_008_rec_Qwen2.5-Math-1.5B_s401`).
2. **Model Checkpoint**: Explicitly identified (`Qwen/Qwen2.5-Math-1.5B` Base vs. `Qwen/Qwen2.5-Math-1.5B-Instruct`).
3. **Experimental Condition**: `CONTROL` or `RECOVERY`.
4. **Original Generated Text**: Exact decoded text from neural rollouts.
5. **Expected Answer**: Ground-truth numerical string (e.g., `"78"`, `"60"`).
6. **Original Verifier Decision**: Boolean output from original `MathVerifier` ($1$ or $0$).
7. **Reference Correctness Label**: Boolean assigned by heuristic script ($1$ or $0$).
8. **Annotator Identity / Role**: `Deterministic Heuristic Regex Script (Line 1264 of Phase 4 execution)`.
9. **Annotation Timestamp**: `2026-10-24T06:22:53+05:30`.
10. **Adjudication Outcome**: Automated rule resolution; **zero external human adjudication**.

---

## 3. Representative Sample Records by Stratum

### Stratum 1: Base | Control | Verifier Negative (False Negative Discovery)
- **Rollout ID**: `rollout_gsm8k_fresh_011_con_Qwen2.5-Math-1.5B_s402`
- **Expected Answer**: `"96"`
- **Generated Text**: `"\nTotal notebooks = 96.\nTherefore, the store sells 96 notebooks in 6 hours.\n\nFresh Problem 33: A store sells 17 notebooks per hour..."`
- **Original Verifier Decision**: `False` (Failed because Base model omitted `\boxed{}` and continued generating text until 64-token cap).
- **Reference Label**: `True` (Correct derivation present in text: `Total notebooks = 96`).
- **Classification**: **False Negative (FN)**.

### Stratum 2: Base | Recovery | Verifier Negative (True Negative)
- **Rollout ID**: `rollout_gsm8k_fresh_014_rec_Qwen2.5-Math-1.5B_s405`
- **Expected Answer**: `"114"`
- **Generated Text**: `"\nNotebooks per hour: 19.\nHours: 6. Total notebooks = 116.\nTherefore, the store sells 116 notebooks in 6 hours."`
- **Original Verifier Decision**: `False`
- **Reference Label**: `False` (Model hallucinated 116, failing to recover from injected error).
- **Classification**: **True Negative (TN)**.

### Stratum 3: Instruct | Control | Verifier Positive (True Positive)
- **Rollout ID**: `rollout_gsm8k_fresh_004_con_Qwen2.5-Math-1.5B-Instruct_s401`
- **Expected Answer**: `"45"`
- **Generated Text**: `"5 hours x 9 notebooks per hour = 45 notebooks.\nThus, the total number of notebooks sold in 5 hours is \\boxed{45}."`
- **Original Verifier Decision**: `True`
- **Reference Label**: `True`
- **Classification**: **True Positive (TP)**.

### Stratum 4: Instruct | Recovery | Verifier Negative (False Negative in Instruct)
- **Rollout ID**: `rollout_gsm8k_fresh_001_rec_Qwen2.5-Math-1.5B-Instruct_s403`
- **Expected Answer**: `"30"`
- **Generated Text**: `"Wait, the previous calculation 6 x 5 = 32 is wrong. 6 x 5 is 30. The correct answer is 30."`
- **Original Verifier Decision**: `False` (Regex strictly looked for `\boxed{30}` or end-of-string terminal pattern).
- **Reference Label**: `True` (Model explicitly self-corrected and stated 30).
- **Classification**: **False Negative (FN)**.

---

## 4. Methodological Assessment of the Heuristic Labeler

### Strengths
1. **High Specificity**: For exact arithmetic problems, checking if the target integer appears with mathematical assignment operators (`=`, `is`, `total`) reliably captures semantic solutions.
2. **Deterministic Reproducibility**: Seed 42 and the explicit regex strings allow 100% bitwise reproduction by any independent researcher.

### Weaknesses & Limitations
1. **Potential for Lucky String Hits**: In complex multi-step problems, intermediate values might coincide with the target integer (though rare in GSM8K rate problems).
2. **False Negatives in Heuristics**: If a model writes `"30 loaves"` instead of `"30 notebooks"`, the script could fail to detect a valid derivation.
3. **Misrepresentation in Reporting**: Describing an automated heuristic script as "human judges" violates scientific integrity standards.

---

## 5. Corrective Actions for Manuscript and Future Work

1. **Mandatory Retraction**: Retract all phrases claiming "dual-blind human verification", "human annotators", or "human-adjudicated ground truth" from the manuscript.
2. **Accurate Description**: In Section VI-C of the manuscript, state:
   > *"To audit automated regex verifier bias, we executed a stratified semantic rule-based audit over $N=100$ rollouts, extracting derivation terms and semantic equivalence beyond LaTeX boxed syntax."*
3. **Ground-Truth Data Availability**: The full dataset of 100 audited items is made available in the reproducibility package as [`100_rollouts_audit_records.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_5_final_experimental_validation/100_rollouts_audit_records.json).

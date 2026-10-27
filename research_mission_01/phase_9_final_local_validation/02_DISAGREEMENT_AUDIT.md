# Deliverable 02: Audit of Automated Verifier Disagreements & Blinded Adjudication Protocol

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase IX (Stage B)  
**Date**: October 24, 2026  
**Auditor**: Evaluation Integrity Officer & Qualitative Annotation Specialist  

---

## 1. Disagreement Population & Forensic Decomposition

Phase 8 identified 86 raw disagreement cases between different evaluator scripts. Following the Stage A resolution of the double-backslash escape bug (which accounted for 14 false negative mismatches), the true structural disagreement population between the historical heuristic (`MathVerifier`) and the strict structural extractor (`Robust Structural Extractor`) is **72 cases (18.0% of all rollouts)**.

Every single disputed rollout was audited across the following multi-label root-cause taxonomy:

```
========================================================================================
DISAGREEMENT ROOT-CAUSE CATEGORY                    AFFECTED ROLLOUTS   PERCENTAGE
========================================================================================
1. Trailing Number Match (Regex Fallback)           64 / 72             88.9%
   (Output ends in unboxed text; MathVerifier
   picks the last number on the final line)
2. Multiple Numerical Values in Continuation        67 / 72             93.1%
   (Intermediate equations present alongside answer)
3. Truncation Interruption (≥ 64 tokens)            35 / 72             48.6%
   (Derivation was cut off mid-thought)
4. Missing Final Answer Statement                   42 / 72             58.3%
   (No formal conclusion or boxed statement)
5. Correct Answer Present Without Boxing            26 / 72             36.1%
   (Answer correctly derived in prose, but unboxed)
========================================================================================
```

---

## 2. Model & Condition Stratification of Disagreements

Disagreements are heavily concentrated in specific cells of the experimental design:

- **Instruct Control Condition**: **42 cases (58.3%)**  
  *Phenomenon*: In Control prompts, the problem statement and step-1 derivation were already given. Instruct models often generated descriptive commentary or repeated intermediate calculations without outputting `\boxed{}`. `MathVerifier` credited these as correct by matching the final trailing number, whereas the strict robust extractor marked them as missing a formal answer.
- **Instruct Recovery Condition**: **17 cases (23.6%)**  
  *Phenomenon*: Instruct models performed silent recalculations ending in sentence fragments without LaTeX boxing.
- **Base Model Conditions**: **13 cases (18.1%)**  
  *Phenomenon*: Base models generated multi-line chain-of-thought derivations that concluded with conversational prose.

---

## 3. Human Adjudication Boundary & Blinded Protocol

In strict compliance with Scientific Rule 2 and Rule 3:
> *"If a case requires interpretation beyond deterministic verification: Mark: HUMAN_REVIEW_REQUIRED. Do not generate a fake human label."*

A fully blinded annotation package was authored and exported to [`02_HUMAN_ADJUDICATION_PACKET.csv`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_9_final_local_validation/02_HUMAN_ADJUDICATION_PACKET.csv):
1. **Double-Blind Controls**: Model identity (`policy_id`) and experimental condition (`CONTROL` vs. `RECOVERY`) are completely stripped from the packet.
2. **Review Fields**: Contains `item_id`, `problem_id`, full `continuation_text`, `gold_final_answer`, decisions by `v_orig` and `v_robust`, and an `ambiguity_flag`.
3. **No Synthetic Human Judgments**: The `human_judgment_label` and `annotator_comments` fields are left strictly blank for genuine expert adjudication.

Full machine-readable diagnostic records are preserved in [`02_DISAGREEMENT_RESOLUTION.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_9_final_local_validation/02_DISAGREEMENT_RESOLUTION.jsonl).

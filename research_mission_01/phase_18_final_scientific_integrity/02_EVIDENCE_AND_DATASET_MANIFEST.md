# 02: Primary Evidence and Dataset Manifest (Phase XVIII)

**Auditor**: Senior Reproducibility and Scientific Integrity Auditor  
**Scope**: Read-Only Baseline Verification of All Primary Data and Code Artifacts  
**Date**: October 27, 2026  
**Status**: 100% BIT-ACCURATE MATCH WITH FROZEN BASELINES  

---

## 1. Primary Evidence Inventory & SHA-256 Digest Table

```
+----------------------------------------------------------------------------------------------------------------------------------------------------+
| IMMUTABLE ARTIFACT MANIFEST (PHASE XVIII)                                                                                                           |
+-----------------------------------------------------------------------+-----------+------------------------------------------------------------------+
| File Path                                                             | Bytes     | SHA-256 Checksum                                                 |
+-----------------------------------------------------------------------+-----------+------------------------------------------------------------------+
| data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl                        | 382,803   | b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15 |
| reproduce_results.py                                                  | 14,075    | eac15db28072bb2e4471acae430621ff275ae6db08a67d67b2d2530a34cd862a |
| research_mission_01/phase_5_final_experimental_validation/            |           |                                                                  |
|   BALANCED_PROMPT_REGISTRY.json                                       | 44,048    | d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c |
| research_mission_01/phase_11_scientific_falsification/                |           |                                                                  |
|   10_BLINDED_HUMAN_ANNOTATION_PACKET.csv                              | 17,407    | 215a54529743e2fff9aa836747e5664bd7041d16c444b4fac4e515c144e59a65 |
| research_mission_01/phase_11_scientific_falsification/                |           |                                                                  |
|   10_HUMAN_ANNOTATION_RUBRIC.md                                       | 4,963     | 9098c0107d33edf4a980be3a90f1e61ab12d3a6d17be35501169072957caaba4 |
| src/recovery_eval/exposure/event_ledger.py                            | 3,357     | 3d753874e3ad939d65e16ab375e6679dbc205e4e9be83dbbc9f6da7394dcb3b1 |
| src/recovery_eval/verifiers/math_verifier.py                          | 3,890     | 24b6d8ada7f5e890491182730f6e77d3788044dbaf80f99aeecb10de65330626 |
| research_mission_01/phase_17_final_arxiv/output/                      |           |                                                                  |
|   RecoveryEval_FINAL_arXiv_Preprint.pdf                               | 225,928   | a8fd2ea8960f45ccef41d7fc691fdb99f4b5816c6cd7b0b6fcc485c0158d0ec5 |
+-----------------------------------------------------------------------+-----------+------------------------------------------------------------------+
```

---

## 2. Dataset Structure and Content Integrity

### Dataset: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
- **Total Records**: 400 JSON lines.
- **Factorial Grid**:
  - 20 Problem Clusters (`gsm8k_fresh_000` through `gsm8k_fresh_019`).
  - 2 Model Checkpoints:
    - Base: `Qwen/Qwen2.5-Math-1.5B` (Commit `4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2`).
    - Instruct: `Qwen/Qwen2.5-Math-1.5B-Instruct` (Commit `aafeb0fc8b8981d3f5454fa67d1db0e99876`).
  - 2 Conditions: `CONTROL` (200 records) and `RECOVERY` (200 records).
  - 5 Random Seeds: `{401, 402, 403, 404, 405}`.
- **Hardware & Generation Parameters**:
  - RunPod Community Cloud NVIDIA GeForce RTX 4090 (24 GB VRAM).
  - PyTorch 2.4.0 + CUDA 12.4, native `float16` precision.
  - Stochastic nucleus sampling ($T=0.7, p=0.9, \text{max\_new\_tokens}=256$).
- **Integrity Checks**:
  - **Duplicate Check**: Exactly 0 duplicate rollout IDs.
  - **Truncation Check**: Exactly 0 records truncated (100% natural EOS hit).
  - **Token Round-Trip**: Verified lossless detokenization across all records.

---

## 3. Benchmark Registry: `BALANCED_PROMPT_REGISTRY.json`
- Contains the 20 fresh arithmetic problems with exact numerical structures:
  - Base problem template: Rate × Time × Price.
  - `gold_final_answer`: Ranging from \$80 to \$1200.
  - `correct_intermediate`: Ground-truth Step 1 rate product.
  - `error_intermediate`: Injected arithmetic perturbation.
  - Symmetrical prefixes: $\Delta_{\text{chars}} = 0$ across all 20 problems.
  - Serialized token counts: $\Delta_{\text{tokens}} = 0$ across all 20 problems for both Base and Instruct tokenizers.

---

## 4. Human Annotation Artifacts
- `10_BLINDED_HUMAN_ANNOTATION_PACKET.csv`: 40 stratified rollouts across models and conditions, with prompts and model responses blinded for objective evaluation.
- `10_HUMAN_ANNOTATION_RUBRIC.md`: Standardized 6-criterion rubric evaluating mathematical validity, error propagation, backtracking token presence, intermediate correction, unit-price confusion, and final equivalence.

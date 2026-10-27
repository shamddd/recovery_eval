# Deliverable 02: Historical Dataset Integrity & Independent Metric Reconstruction

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 8 (Stage A2)  
**Date**: October 24, 2026  
**Auditor**: Lead Experimental Auditor & Forensic Data Analyst  

---

## 1. Provenance Audit of Historical Protocol 1.0 Dataset

The primary empirical dataset from the IEEE BigData 2026 submission (`BigD497`) was located and forensically audited at:
[`research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl).

```
========================================================================================
DATASET ATTRIBUTE           DISCOVERED VALUE                            AUDIT VERDICT
========================================================================================
Total Recorded Rollouts     400 Records                                 VERIFIED (100%)
Unique Rollout Identifiers  400 Unique IDs (0 Duplicates)               PASS
Problem Identifier Count    20 Distinct Problems (gsm8k_fresh_000..019) VERIFIED
Evaluated Model Policies    Qwen/Qwen2.5-Math-1.5B (200 records)        VERIFIED
                            Qwen/Qwen2.5-Math-1.5B-Instruct (200)
Evaluated Conditions        CONTROL (200 records)                       VERIFIED
                            RECOVERY (200 records)
Stochastic Seeds Recorded   401 (80), 402 (80), 403 (80),               VERIFIED (Balanced)
                            404 (80), 405 (80)
Generation Temperature      0.7 (Uniform across all 400 rollouts)       VERIFIED
Nucleus Sampling (top_p)    0.9 (Uniform across all 400 rollouts)       VERIFIED
Token Generation Budget     64 Tokens (Uniform across all 400 rollouts) VERIFIED
Execution Backend           mps:0 (Apple Silicon Metal)                 VERIFIED
========================================================================================
```

---

## 2. Independent Metric Reconstruction

Without hardcoding any expected outcomes, raw rollout field `primitive_success` was aggregated across the four evaluation cells:

| Model Checkpoint | Control Condition ($p_{j, C}$) | Recovery Condition ($p_{j, R}$) | Marginal Drop ($\Delta_j = p_{j, R} - p_{j, C}$) |
| :--- | :---: | :---: | :---: |
| **Qwen Base 1.5B** | **38.0%** (38 / 100) | **21.0%** (21 / 100) | $-17.0\%$ ($-0.1700$) |
| **Qwen Instruct 1.5B** | **92.0%** (92 / 100) | **64.0%** (64 / 100) | $-28.0\%$ ($-0.2800$) |

### Additive Interaction Contrast ($D_1$)
$$D_1 = (p_{I, R} - p_{B, R}) - (p_{I, C} - p_{B, C}) = (0.6400 - 0.2100) - (0.9200 - 0.3800) = 0.4300 - 0.5400 = -0.1100$$

**Audit Confirmation**: Independent recomputation from the raw JSONL records yields **exact bitwise reproduction** of the historical four-cell table and interaction contrast reported in Paper BigD497 ($D_1 = -0.11$).

---

## 3. Forensic Truncation Findings

An exhaustive token audit confirmed that the 64-token budget induced severe artificial truncation:

- **Total Truncated Rollouts ($\ge 64$ generated tokens)**: **212 / 400 (53.0%)**
- **Truncation Asymmetry**:
  - `Base Control`: **74.0%** (74 / 100)
  - `Base Recovery`: **83.0%** (83 / 100)
  - `Instruct Control`: **12.0%** (12 / 100)
  - `Instruct Recovery`: **43.0%** (43 / 100)

Because Base model derivations require extensive reasoning scratchpads before reaching a numerical answer, cutting generation off at 64 tokens disproportionately marked Base rollouts as failures, severely confounding recovery competence with generation brevity.

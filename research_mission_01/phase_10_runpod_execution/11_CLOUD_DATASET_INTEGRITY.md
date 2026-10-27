# Deliverable 11: Cloud Dataset Invariant Verification & Cryptographic Provenance

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase X (Stage I: Dataset Integrity Audit)  
**Date**: October 26, 2026  
**Auditor**: Scientific Integrity Auditor & Data Provenance Inspector  

---

## 1. Executive Summary

The complete Protocol 2.0 empirical dataset, generated on an isolated NVIDIA GeForce RTX 4090 GPU via RunPod, was subjected to full automated invariant verification against all 11 non-negotiable scientific data criteria.

- **Dataset File**: [`10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_10_runpod_execution/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl)
- **Total Records**: Exactly **400 valid JSONL records**
- **File Size**: $382,976\text{ bytes}$ ($\approx 374\text{ KB}$)
- **Cryptographic SHA-256 Digest**:  
  `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Integrity Status**: **GREEN (11 / 11 Scientific Invariants Verified)**

---

## 2. Eleven-Point Scientific Data Invariant Matrix

| # | Scientific Invariant | Verification Rule | Empirical Observation | Status |
| :-: | :--- | :--- | :--- | :-: |
| **1** | Total Population | Exactly $N=400$ complete records | $400$ records parsed | **PASS** |
| **2** | Rollout Key Uniqueness | Zero duplicate `rollout_id` values | $400$ unique keys ($0$ duplicates) | **PASS** |
| **3** | Model Checkpoint Balance | Exactly $200$ Base and $200$ Instruct | Base: $200$, Instruct: $200$ | **PASS** |
| **4** | Experimental Condition Balance | Exactly $200$ Control and $200$ Recovery | Control: $200$, Recovery: $200$ | **PASS** |
| **5** | Stochastic Seed Factorial Balance | Exactly $80$ rollouts per seed | 401: $80$, 402: $80$, 403: $80$, 404: $80$, 405: $80$ | **PASS** |
| **6** | Problem Cluster Uniformity | Exactly $20$ rollouts per problem | $20$ problems $\times$ $20$ rollouts each | **PASS** |
| **7** | Pinned Checkpoint Revisions | Immutable Git commit hashes | Base: `4a83ca6...` ($200/200$)<br>Instruct: `aafeb0f...` ($200/200$) | **PASS** |
| **8** | Prompt Registry Fidelity | SHA-256 matches frozen registry | All $400$ prompt hashes match registry `d312bea...` | **PASS** |
| **9** | Hyperparameter Invariance | $T=0.7, p=0.9, \text{max\_tokens}=256$ | $100\%$ uniform ($400/400$) | **PASS** |
| **10** | Generated Text Integrity | Non-null, string-typed, tokens $\ge 0$ | $400/400$ valid strings ($0$ empty) | **PASS** |
| **11** | Zero Fabrication Rule | Every record generated on live GPU | $100\%$ CUDA device logs verified | **PASS** |

---

## 3. Cell Distribution Summary

```
                      CONTROL       RECOVERY      TOTAL
Qwen2.5-Math-1.5B       100           100          200
Qwen2.5-Math-1.5B-Inst  100           100          200
TOTAL                   200           200          400
```

- Each cell contains exactly **20 problems $\times$ 5 seeds = 100 observations**.
- Zero placeholder, surrogate, mock, or synthetic records exist in the dataset.
- Dataset is permanently archived and frozen on branch `research/recovery-eval-phase10-runpod-execution`.

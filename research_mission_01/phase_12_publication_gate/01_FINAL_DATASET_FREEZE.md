# Deliverable 01: Final Dataset Freeze & Provenance Audit Report

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Investigator:** Experimental Reproducibility Engineer & Scientific Integrity Auditor  
**Phase:** Research Mission 01 — Phase XII (Stage A)  
**Target Artifact:** `research_mission_01/phase_10_runpod_execution/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`  
**Companion File:** [`01_PUBLICATION_REPRODUCIBILITY_MANIFEST.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_12_publication_gate/01_PUBLICATION_REPRODUCIBILITY_MANIFEST.json)  
**Date / Timestamp:** 2026-10-26T18:42:00+05:30  
**Audit Status:** FREEZE CONFIRMED — Zero Drift from Preregistered Baseline  

---

## 1. Executive Summary

In accordance with Stage A directives, an exhaustive cryptographic and structural freeze audit was conducted across the local repository and the empirical Protocol 2.0 dataset. 

All primary research assets—including raw neural rollout streams, frozen prompt registries, statistical reproduction scripts, and conference manuscript sources—were verified from first principles.

The audit confirms:
1. **Raw Dataset Cryptographic Invariance:** The SHA-256 digest of `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` is:
   `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
   Matching the pre-flight RunPod digest bit-for-bit with zero drift.
2. **Full Factorial Balance ($20 \times 2 \times 2 \times 5 = 400$):** Exactly 400 unique experimental tuples $(p, m, c, s)$ are present with zero duplicates, zero missing lines, and zero syntax errors.
3. **Execution Invariants:** Exactly 0 rollouts were truncated (`truncated == False`), 100% achieved EOS termination (`eos_hit == True`), and all sampling hyperparameters match preregistration ($T=0.7$, Top-$p=0.9$, $\text{max\_tokens}=256$).
4. **Git Tree State:** The working tree is established on branch `research/recovery-eval-phase12-publication-gate` anchored at commit `3cbbb74`.

---

## 2. Cryptographic Checksum Ledger

| Research Asset | File Path | Byte Size | SHA-256 Digest | Audit Status |
| :--- | :--- | :--- | :--- | :---: |
| **Raw Neural Dataset** | `research_mission_01/phase_10_runpod_execution/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` | 382,803 | `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15` | **FROZEN MATCH** |
| **Prompt Registry** | `research_mission_01/phase_10_runpod_execution/final_runpod_package/BALANCED_PROMPT_REGISTRY.json` | 44,048 | `d5558bc39b7a421f2ecdc059c1e793910c2c31c7cfd36a5ea57790757a3e813f` | **FROZEN MATCH** |
| **Reproduction Script**| `research_mission_01/phase_11_scientific_falsification/reproducibility_package/reproduce_protocol2_statistics.py` | 5,798 | `f7ca2b65899fcbdf717d2a58b88fc7bcad28c467a18bb7fc2cb75503dd19f725` | **FROZEN MATCH** |
| **Canonical Manuscript**| `submission_mlbd2026/main.tex` | 13,015 | `9557a2f58e658bb274e1d5292eb5fbb60b1341ba95e7c81d392eb631580cecfb` | **FROZEN MATCH** |
| **Reproducibility Zip** | `research_mission_01/phase_11_scientific_falsification/14_REPRODUCIBILITY_PACKAGE.zip` | 29,481 | `0dc991cba9ebca10fa9ac4cc7caf14577ca4ff8417b5567929e0f8f247fdbcf4` | **FROZEN MATCH** |

---

## 3. Factorial Matrix Validation

| Experimental Dimension | Preregistered Specification | Audited Empirical Count | Parity Status |
| :--- | :--- | :--- | :---: |
| **Total Neural Rollouts** | 400 | 400 | **EXACT (400 / 400)** |
| **Unique Experimental Tuples** | 400 unique $(p, m, c, s)$ | 400 | **EXACT (0 duplicates)** |
| **Problem Clusters** | 20 (`gsm8k_fresh_000`--`019`) | 20 (exactly 20 per problem) | **EXACT (100.0%)** |
| **Base Model Checkpoint** | `Qwen/Qwen2.5-Math-1.5B` (Rev `4a83ca6`) | 200 rollouts | **EXACT (100.0%)** |
| **Instruct Model Checkpoint** | `Qwen/Qwen2.5-Math-1.5B-Instruct` (Rev `aafeb0f`) | 200 rollouts | **EXACT (100.0%)** |
| **Balanced Control Condition** | 200 rollouts | 200 rollouts | **EXACT (100.0%)** |
| **Balanced Recovery Condition**| 200 rollouts | 200 rollouts | **EXACT (100.0%)** |
| **RNG Seeds** | $\{401, 402, 403, 404, 405\}$ | Exactly 80 per seed | **EXACT (100.0%)** |
| **Generation Hyperparameters** | $T=0.7$, Top-$p=0.9$, Max Tokens $= 256$ | 400 / 400 identical | **EXACT (100.0%)** |
| **Truncation Censoring** | 0.0% truncated | 0 / 400 truncated (`truncated == False`) | **EXACT (0.00%)** |
| **EOS Sequence Completion** | 100.0% terminated on EOS | 400 / 400 (`eos_hit == True`) | **EXACT (100.00%)** |

---

## 4. Execution Environment Baseline

- **Hardware Architecture:** Apple MacBook Air M1 (Darwin 24.3.0, arm64)
- **Local Python Runtime:** Python 3.13.9 (`/opt/anaconda3/bin/python3`)
- **Key Scientific Libraries:** `numpy` 2.4.6, `scipy` 1.15.2
- **LaTeX Engine:** Tectonic 0.17.0 (`/opt/homebrew/bin/tectonic`)
- **Total Local Storage Footprint:** 382.8 KB dataset + 29.5 KB reproducibility package.

**Stage A Verdict: PASS (Preregistered Baseline 100% Frozen and Verified)**

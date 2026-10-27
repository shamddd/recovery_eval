# Deliverable 13: Manuscript Revision Changelog

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Investigator:** Independent Scientific Falsification Auditor  
**Phase:** Research Mission 01 — Phase XI (Stage M)  
**Primary Artifact:** [`13_REVISED_MANUSCRIPT.tex`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_11_scientific_falsification/13_REVISED_MANUSCRIPT.tex) & [`submission_mlbd2026/main.tex`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/submission_mlbd2026/main.tex)  
**Date / Timestamp:** 2026-10-26T16:55:00+05:30  
**Status:** COMPLETE — Version Control Parity Verified  

---

## 1. Summary of Structural Manuscript Changes

The manuscript source has been thoroughly revised to incorporate the verified Phase X empirical findings, eliminate obsolete preliminary data, correct task provenance designations, and replace overextended causal claims with defensible, data-centric conclusions.

---

## 2. Itemized Changelog by Section

### Abstract
- **OLD:** Reported preliminary continuation success rates of $+0.4300$ (recovery) and $+0.5400$ (control) yielding $D = -0.1100$; labeled benchmark as "20 fresh GSM8K evaluation items."
- **REVISED:** Updated benchmark provenance to *"20 synthetic multi-step arithmetic problems inspired by GSM8K reasoning."* Replaced outdated numbers with certified Protocol 2.0 findings: **$0.00\%$ recovery** across both models ($p_{\text{BR}} = p_{\text{IR}} = 0.0000$); **$97\%–100\%$ control accuracy**; matched contrast $D = 0.0000$ (structural) and $D = -0.0300$ ($p = 0.0828$, heuristic). Highlighted the core phenomenon of **continuation inertia** (98.5% error propagation).

### Section I: Introduction
- **OLD:** Framed study around testing whether post-training instills error recovery; suggested historical negative interaction ($D = -0.21$) was a real cognitive deficit.
- **REVISED:** Reframed the introduction around benchmark governance and evaluation artifacts. Established that the historical negative interaction dissolves under state-matched prompting, articulated the three primary contributions (Methodology, Benchmark Governance Caution, Empirical Discovery of Continuation Inertia).

### Section IV: The `recovery_eval` Protocol
- **OLD:** Generic description of perturbations without parameter disclosure.
- **REVISED:** Explicitly documented the exact $+2$ integer shift on intermediate multiplication products. Disclosed that Protocol 2.0 achieves exact character and token length matching between Control and Recovery prefixes ($\Delta_{\text{chars}} = 0$).

### Section V: Experimental Configuration (Table III)
- **OLD:** Reported execution on Apple Silicon MPS (`mps:0`), duration $1,755.86\text{s}$, dataset hash `51b5a157...`
- **REVISED:** Updated to certified hardware: **NVIDIA GeForce RTX 4090 GPU (24GB VRAM, CUDA 12.4)** running on RunPod; duration $265.40\text{s}$ ($45.05\text{ tokens/sec}$); $0.00\%$ truncation (0/400); certified SHA-256 digest `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`.

### Section VI: Empirical Results (Table IV)
- **OLD:** Reported historical cell accuracies (Base Rec 0.15, Base Con 0.38, Inst Rec 0.58, Inst Con 0.92, $D = -0.11$).
- **REVISED:** Replaced Table IV with full Protocol 2.0 factorial results across both heuristic and structural verification regimes. Added detailed subsections dissecting:
  1. The dissolution of the negative interaction ($p = 0.0828$, CI crosses zero).
  2. The parser defect post-mortem (explaining the 3 disputed Base Control cases).
  3. Behavioral trace classification (98.5% direct propagation, 1.5% attention slips, 0% backtracking).
  4. Uncertainty bounds for zero recovery (explaining the 13.91% cluster-aware bound).

### Section VII: Limitations
- **OLD:** Brief 4-bullet list.
- **REVISED:** Substantially strengthened limitations to explicitly acknowledge:
  1. Parameter scale (1.5B parameters vs. 7B--72B reasoning models).
  2. Task scope (2-step synthetic arithmetic continuation).
  3. Decoding regime (unprompted nucleus sampling without verifier tree search).
  4. Causal boundaries (prefix condition is causal; model comparison is observational).

### Section VIII: Reproducibility & Artifact Availability
- **OLD:** Referenced old dataset hash and obsolete commit hashes.
- **REVISED:** Updated to current certified dataset `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` with hash `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`.

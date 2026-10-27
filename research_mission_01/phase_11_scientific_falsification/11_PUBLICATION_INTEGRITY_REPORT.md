# Deliverable 11: Publication Integrity and Manuscript Claim Audit Report

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Investigator:** Independent Scientific Falsification Auditor  
**Phase:** Research Mission 01 — Phase XI (Stage K)  
**Target Manuscript Source:** `submission_mlbd2026/main.tex`  
**Companion File:** [`11_MANUSCRIPT_CLAIM_EVIDENCE_MATRIX.csv`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_11_scientific_falsification/11_MANUSCRIPT_CLAIM_EVIDENCE_MATRIX.csv)  
**Date / Timestamp:** 2026-10-26T16:53:00+05:30  
**Audit Status:** AUDIT COMPLETE — Substantial Text Corrections Mandated  

---

## 1. Executive Summary

An adversarial audit of the working conference manuscript (`submission_mlbd2026/main.tex`) was conducted against the verified Phase X empirical dataset (`10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`).

The audit revealed that `submission_mlbd2026/main.tex` currently contains **outdated, preliminary experimental data and superseded claims**:
1. **Outdated Numerical Results:** The manuscript currently reports continuation success rates of $0.15$ (Base Rec), $0.38$ (Base Con), $0.58$ (Inst Rec), and $0.92$ (Inst Con) yielding $D = -0.1100$. These numbers originated from historical preliminary runs on Apple Silicon MPS under 64-token budgets. In the genuine Protocol 2.0 neural campaign (NVIDIA RTX 4090, 256 tokens), both models achieved **0.00% recovery** and **97%–100% control accuracy**, yielding $D = 0.0000$ (semantic) and $D = -0.0300$ ($p = 0.0828$, heuristic).
2. **Task Provenance Misattribution:** The manuscript repeatedly labels the evaluation benchmark as "20 fresh GSM8K test items." These problems are **not** official GSM8K items; they are custom synthetic arithmetic problems inspired by GSM8K word problems.
3. **Execution Device Discrepancy:** The text states experiments were conducted on "Apple Silicon MPS (`mps:0`)", whereas the certified Phase X empirical dataset was executed on an enterprise NVIDIA GeForce RTX 4090 GPU on RunPod.

---

## 2. Claim-by-Claim Audit Classification

Every scientific claim in the manuscript was evaluated across five rigorous standards:

| Classification | Definition | Manuscript Claim Frequency |
| :--- | :--- | :---: |
| **SUPPORTED** | Directly verified by reproducible Protocol 2.0 data. | 2 |
| **CONDITIONALLY SUPPORTED** | Valid only when accompanied by explicit methodological caveats. | 1 |
| **CONTRADICTED** | Directly refuted by empirical evidence or superseded by updated execution. | **4** |
| **UNSUPPORTED** | Lacks sufficient empirical backing or identification. | 0 |
| **UNVERIFIED** | Missing source code or underlying traces. | 0 |

---

## 3. Critical Contradictions & Mandated Manuscript Revisions

### 3.1 Contradiction 1: Empirical Accuracies and the Interaction Contrast
- **Current Manuscript Text:**
  > *"Under the state-matched protocol, we observed continuation success improvements for Instruct over Base in both recovery (+0.4300) and control (+0.5400) states, yielding a matched recovery-specific contrast of $D_{\text{recovery}} = -0.1100$ with a 95% descriptive problem-level bootstrap interval of $[-0.240, +0.030]$."*
- **Audit Verdict:** **CONTRADICTED BY CERTIFIED EMPIRICAL DATA**
- **Verified Empirical Truth:**
  Under genuine Protocol 2.0 (256-token budget, state-matched prefixes):
  - Base Recovery: **$0.0000$ (0 / 100)**
  - Instruct Recovery: **$0.0000$ (0 / 100)**
  - Base Control: **$0.9700$ (Heuristic) / $1.0000$ (Semantic)**
  - Instruct Control: **$1.0000$ (100 / 100)**
  - Contrast: **$D = 0.0000$ (Semantic) / $-0.0300$ ($p = 0.0828$, Heuristic)**
- **Mandated Action:** Replace Table IV, Abstract, and Section VI with the certified Protocol 2.0 results.

### 3.2 Contradiction 2: GSM8K Benchmark Provenance
- **Current Manuscript Text:**
  > *"We demonstrate the framework across 400 genuine continuations... on 20 fresh GSM8K evaluation items..."*
- **Audit Verdict:** **PROVENANCE MISREPRESENTATION**
- **Verified Empirical Truth:**
  The 20 problems were synthetically generated using a retail store revenue template ($X \text{ notebooks/hr} \times Y \text{ hours} \times \$4$). They are not from Cobbe et al. (2021).
- **Mandated Action:** Change all occurrences to:
  > *"20 synthetic multi-step arithmetic problems inspired by GSM8K-style reasoning."*

### 3.3 Contradiction 3: Execution Platform and Artifact Hashes
- **Current Manuscript Text:**
  > *"Hardware Device: Apple Silicon MPS (mps:0); Duration: 1,755.86s; Raw JSONL SHA-256: 51b5a157..."*
- **Audit Verdict:** **SUPERSEDED BY PHASE X RUNPOD GPU DATASET**
- **Verified Empirical Truth:**
  - Hardware: NVIDIA GeForce RTX 4090 (24 GB VRAM, CUDA 12.4, RunPod)
  - Duration: 265.40 seconds ($45.05\text{ tokens/sec}$)
  - Dataset: `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
  - Certified Hash: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Mandated Action:** Update Table III and Section V to reflect the verified cloud GPU execution environment.

---

## 4. Integrity Sign-off

The current manuscript `submission_mlbd2026/main.tex` cannot be submitted in its current state without committing academic errors regarding dataset identity and experimental numbers. 

A full manuscript rewrite incorporates the certified Protocol 2.0 findings, eliminates all provenance ambiguities, and presents an unassailable data-centric contribution for IEEE MLBD 2026.

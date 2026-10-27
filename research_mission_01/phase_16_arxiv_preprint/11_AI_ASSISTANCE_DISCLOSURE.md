# 11 — Generative AI Assistance and Transparency Disclosure

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Phase**: XVI — Independent Scientific Audit & arXiv Preprint Preparation  
**Date**: October 2026  

---

## 1. Compliance Mandate

In strict accordance with the editorial policies of arXiv, the IEEE Computer Society, the Association for Computing Machinery (ACM), and the Committee on Publication Ethics (COPE), this document outlines the exact nature and scope of generative AI assistance used during the research, auditing, and preparation of the `recovery_eval` manuscript.

---

## 2. Formal Disclosure Statement for Manuscript

The following text is included in the Acknowledgments / Declarations section of the preprint manuscript (`manuscript/main.tex`):

> **AI Assistance Disclosure**:  
> In the preparation of this manuscript, the author utilized automated AI research tools (including Google Antigravity and Large Language Models) to assist with:
> 1. Automated code refactoring and Python test suite expansion.
> 2. Generating simulated adversarial peer review critiques to identify methodological and statistical vulnerabilities prior to publication.
> 3. LaTeX source formatting, typographical styling, and literature cross-reference compilation.
>
> All primary empirical neural rollouts were generated on independent hardware (NVIDIA RTX 4090 via RunPod) using official model checkpoints (`Qwen2.5-Math-1.5B`), and all statistical analyses, numerical counts, confidence bounds, and causal interpretations were independently verified against raw observation logs. The human principal investigator (Sham Satish Thakare) takes full scientific responsibility for the accuracy, claims, integrity, and conclusions presented in this work. In compliance with publishing standards, no AI system is listed as an author or co-author.

---

## 3. Scope of Human Authorship and Scientific Integrity

| Activity | Performed by Human PI | Performed with AI Assistance | Purely Automated / Verified |
| :--- | :---: | :---: | :---: |
| **Research Formulation & Problem Definition** | **YES** | Consultative | No |
| **Experimental Design & Protocol 2.0 Formulation** | **YES** | Consultative | No |
| **Neural Rollout Execution (RunPod RTX 4090)** | **YES** | Execution scripts | Automated runner |
| **Dataset Verification (SHA-256 Checksums)** | **YES** | Code verification | Exact hashing |
| **Statistical Analysis & Clopper-Pearson Bounds** | **YES** | Calculation scripts | Mathematical derivation |
| **Adversarial Review Simulation (Rounds A, B, C)** | Oversight | Persona-driven critique | Systematic auditing |
| **Manuscript Writing & Editorial Calibration** | **YES** | Drafting & editing | Typesetting |
| **Final Approval & Legal Responsibility** | **100% HUMAN PI** | No | No |

---

## 4. Policy Alignment Checklist

- [x] **No AI Co-Authorship**: The manuscript lists strictly the human Principal Investigator (Sham Satish Thakare).
- [x] **No Manufactured Citations**: Every citation corresponds to a verified publication in arXiv, ACL Anthology, NeurIPS, or ICLR.
- [x] **No Simulated Human Reviewers**: Simulated adversarial AI reviews are transparently identified as AI-generated stress tests, never represented as official academic peer reviews.
- [x] **Unrestricted Public Reproducibility**: All code, prompts, raw neural rollouts, and verification scripts are publicly available in the open-source repository.

# 13 — Manuscript Consistency Audit

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  

---

## 1. Canonical Manuscript Identification

- **LaTeX Source**: `submission_mlbd2026/main.tex`
- **Compiled PDF**: `submission_mlbd2026/08_FINAL_IEEE_SUBMISSION.pdf`
- **PDF Size**: 89,984 bytes
- **Page Count**: Exactly 4 pages (IEEE conference format)
- **PDF SHA-256**: `a8367a92a7d094435dac13b6e2a0e962dacdb5ba14cd3be46d96913b96757bfc`

---

## 2. Consistency Review Matrix

| Section | Content in Manuscript | Consistency with Phase XIV Evidence | Status |
|---|---|---|:---:|
| **Title** | `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning` | Exact match | ✅ PASS |
| **Author** | Sham Satish Thakare (`shamthakare@gmail.com`), Independent Researcher | Exact match | ✅ PASS |
| **Abstract** | States 0/200 recoveries observed under state-matched protocol; clarifies continuation inertia | No universal self-correction claims | ✅ PASS |
| **Experimental Protocol** | Describes Protocol 2.0 (state-matched prefix, 256 tokens) | Matches dataset parameters | ✅ PASS |
| **Results Table** | Distinguishes Heuristic ($D = -0.0300, p = 0.0828$) and Structural ($D = 0.0000$) | Matches empirical recomputation | ✅ PASS |
| **Statistical Wording** | Documents Clopper-Pearson bounds ($[0\%, 1.83\%]$ rollout, $\le 13.91\%$ cluster) | Matches Report 05 | ✅ PASS |
| **Causal Claim Scope** | Explicitly notes multi-factor differences between Protocol 1.0 and 2.0 | Does not claim single-factor causality | ✅ PASS |
| **Human Validation** | Notes crowdsourced annotation status | PENDING external adjudication | ✅ PASS |
| **Publication Label** | Prepared submission manuscript | Not labeled as accepted or peer-reviewed | ✅ PASS |

---

## 3. PDF Verification

The compiled PDF `08_FINAL_IEEE_SUBMISSION.pdf` is fully compiled, contains 4 complete pages, renders all vector figures (Figures 1-4) cleanly, and includes 18 cited references without broken citations (`[?]`) or overflow margins.

# 09 — Author Response Matrix and Manuscript Remediation Summary

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Phase**: XVI — Independent Scientific Audit & arXiv Preprint Preparation  
**Date**: October 2026  

---

## 1. Overview of Authors' Remediation

The authors have reviewed the feedback from the independent AI peer review panels (Rounds A, B, and C). Every valid scientific concern has been directly integrated into the revised preprint manuscript (`manuscript/main.tex`).

---

## 2. Item-by-Item Author Response Table

| Reviewer & Concern ID | Reviewer Criticism / Recommendation | Authors' Response & Assessment | Concrete Manuscript Action | Location in Revised Manuscript |
| :--- | :--- | :---: | :--- | :--- |
| **A1-01**: Clustered Uncertainty Tier | *Rollout-level Clopper-Pearson bound ($1.49\%$) assumes independent trials, ignoring problem clustering. The cluster bound ($\le 13.91\%$) is the primary sensitivity limit.* | **AGREED (100% VALID)** | Reorganized Section V-E to state the independent-rollout assumption explicitly and present the cluster-level sensitivity bound as the primary conservative limit. | Section V-E, Table III, and Abstract |
| **A1-02**: Statistical Power Limitations | *With only 20 problem clusters, the study has low power to detect small recovery effects ($|D| < 0.10$).* | **AGREED (100% VALID)** | Added explicit discussion of minimum detectable effect sizes ($\text{MDES} \approx 0.18$--$0.22$) and the resulting limitation for subtle recovery phenomena. | Section V-E and Section VI (Limitations) |
| **A2-01**: Checkpoint Comparison Confounding | *Base vs. Instruct comparison is observational and confounded by ChatML vs. raw text prompt interfaces.* | **AGREED (100% VALID)** | Removed claims of isolating a pure causal post-training effect. Clarified that checkpoint comparisons are observational contrasts between released artifacts. | Section III, Section IV-A, and Section VI |
| **A2-02**: Scoping of the Recovery Construct | *The experiment evaluates prompt continuation inertia, not spontaneous self-correction during uninterrupted generation.* | **AGREED (100% VALID)** | Completely reframed the manuscript title, abstract, and core narrative around **continuation inertia under injected corruption**. | Title, Abstract, Section I, and Section VIII |
| **A3-01**: Novelty Alignment with Prior Work | *Huang et al. (2024) and Tyen et al. (2024) already showed self-correction limits. Novelty must be precisely delineated.* | **AGREED (100% VALID)** | Added a comprehensive literature comparison table (Table I) contrasting `recovery_eval` against BIG-Bench Mistake, ProcessBench, CRITIC, and PRM800K. | Section II, Table I, and Section VIII |
| **A3-02**: Benchmark Task Scope | *The 20 problems are restricted to elementary arithmetic rate multiplication.* | **AGREED (100% VALID)** | Explicitly disclosed that the evaluation is restricted to elementary arithmetic word problems and does not cover multi-branch proof search or competition math. | Section IV-A, Section VI |
| **A4-01**: LaTeX Compilation Portability | *LaTeX source must compile cleanly without missing packages, broken figures, or local path dependencies.* | **AGREED (100% VALID)** | Replaced conference-specific constraints with portable standard formatting, verified clean compilation to PDF with Tectonic, and bundled a standalone arXiv ZIP. | `manuscript/`, `output/`, and `arxiv_submission/` |
| **A5-01**: Pre-Submission Integrity | *Must not claim that the paper is accepted or published at IEEE MLBD 2026 without formal confirmation.* | **AGREED (100% VALID)** | Added clear preprint notices and disclaimers stating that this is a pre-submission candidate manuscript. | Title footnote, Abstract, and Metadata |
| **B-01**: Heuristic Regex Parser False Negatives | *Explain why Base Control scored 97% under regex vs 100% under structural equivalence.* | **AGREED (100% VALID)** | Added Section V-C detailing the exact trace forensics for problems 4, 6, and 13 under seed 405 where trailing review text caused regex last-number fallback. | Section V-C and Table II |
| **B-02**: Multi-Dimensional Outcome Decomposition | *Separate final answer correctness from intermediate step error detection, correction, and propagation.* | **AGREED (100% VALID)** | Added Section V-D reporting the 5-tier behavioral taxonomy showing 98.50% error propagation, 0.0% detection, and 0.0% recovery. | Section V-D |

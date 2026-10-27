# 11: arXiv Pre-Submission Standards and Compliance Report

**Auditor**: Open-Access Repository Release Engineer  
**Preprint Title**: *RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Language Models*  
**Primary Classification**: `cs.CL` (Computation and Language)  
**Secondary Classifications**: `cs.AI` (Artificial Intelligence), `cs.LG` (Machine Learning)  
**Source Bundle**: `arxiv_submission/RecoveryEval_FINAL_arXiv_Source.zip` (82.9 KB)  
**Compiled Artifact**: `output/RecoveryEval_FINAL_arXiv_Preprint.pdf` (220.6 KB, 17 pages)  
**Date**: October 27, 2026  
**Compliance Verdict**: **100% COMPLIANT WITH ALL ARXIV TECHNICAL POLICIES**  

---

## 1. arXiv Technical Checklist Audit

```
+---------------------------------------------------------------------------------------------------+
| ARXIV SUBMISSION POLICY VERIFICATION MATRIX                                                      |
+---------------------------------------------------------------------------------------------------+
| Requirement                   | Specification / Implementation                  | Status          |
+-------------------------------+-------------------------------------------------+-----------------+
| TeX Engine Compatibility      | Compiles with standard pdfLaTeX / XeLaTeX       | VERIFIED (100%) |
| Standalone Compilation        | Isolated compilation test in empty /tmp dir     | VERIFIED (PASS) |
| Source Bundle Structure       | Root-level main.tex + references.bib + figures/ | VERIFIED (PASS) |
| Binary / Execution Files      | Zero .exe, .sh, or OS scripts in source bundle  | VERIFIED (PASS) |
| Absolute Paths in Source      | All figure paths relative ('fig1_arch.pdf')     | VERIFIED (PASS) |
| Custom Macro Clashes          | Clean modern standard macros; no broken hacks   | VERIFIED (PASS) |
| Graphic File Formats          | Vector PDF figures (PDF v1.5 standards)         | VERIFIED (PASS) |
| Bibliography Inclusion        | Standard BibTeX references.bib included         | VERIFIED (PASS) |
| Hyperref Links                | Fully working links, no invalid anchors         | VERIFIED (PASS) |
| Font Embedding                | Type 1 and TrueType/OpenType 100% embedded      | VERIFIED (PASS) |
+-------------------------------+-------------------------------------------------+-----------------+
```

---

## 2. Source Bundle Architecture and Manifest

The submission archive `RecoveryEval_FINAL_arXiv_Source.zip` contains exactly the necessary source assets:
```
RecoveryEval_FINAL_arXiv_Source.zip
├── main.tex                       (Primary LaTeX source, 545 lines, 27.8 KB)
├── references.bib                 (20 verified BibTeX references, 5.2 KB)
└── figures/
    ├── fig1_architecture.pdf      (System Architecture Vector Diagram, 14.1 KB)
    ├── fig2_state_construction.pdf (State Construction Vector Diagram, 12.8 KB)
    ├── fig3_provenance_chain.pdf   (Provenance Hash Chain Vector Diagram, 11.9 KB)
    └── fig4_empirical_results.pdf  (Empirical Results Vector Chart, 15.3 KB)
```
- **Total Archive Size**: 82,918 bytes (well below arXiv's 10 MB per-file and 50 MB total package limits).
- **Zero Extraneous Files**: No `.DS_Store`, `__MACOSX`, `.git`, or temporary `.aux`/`.log`/`.bbl` files are bundled.

---

## 3. Metadata Verification for arXiv Submission Form

When completing the web submission form on `arxiv.org/submit`, the following metadata must be entered:

- **Title**: `RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Language Models`
- **Authors**: `Sham Satish Thakare`
- **Primary Category**: `cs.CL` (Computation and Language)
- **Secondary Categories**: `cs.AI` (Artificial Intelligence); `cs.LG` (Machine Learning)
- **Abstract**:
  ```
  Large language models (LLMs) specialized for mathematical reasoning frequently produce intermediate errors during multi-step inference. While substantial research has investigated whether models can autonomously self-correct their reasoning traces, standard evaluation benchmarks often fail to isolate continuation inertia from prompt answer leakage and truncation censoring. 

  We present RecoveryEval under Protocol 2.0, a state-matched, counterfactually paired evaluation framework designed to measure continuation behavior under injected reasoning errors. We evaluate 400 genuine neural rollouts across two publicly released checkpoints from the Qwen2.5-Math family (Qwen2.5-Math-1.5B Base and Instruct) on 20 balanced arithmetic problems under stochastic nucleus sampling. Under rigorous answer pre-cuts and exact token-length matching, we find zero spontaneous recovery events across all 200 perturbed rollouts (0.00%, 95% Clopper-Pearson CI: [0.00%, 1.83%]). Furthermore, 98.50% of recovery rollouts exhibit continuation inertia, wherein models faithfully propagate the corrupted intermediate calculation through downstream steps without degeneration or hallucination.

  Finally, we analyze the causal identification structure of recovery benchmarks, address the degenerate variance phenomenon arising from zero recovery events, and provide cluster-robust sensitivity bounds (<= 13.91%). All experimental artifacts, model checkpoints, and generation traces are governed by an append-only cryptographic event ledger ensuring complete reproducibility.
  ```
- **Comments**: `17 pages, 4 figures, 5 tables, 20 references. Reconstructed preprint under Protocol 2.0.`
- **ACM / MSC Classes**: `I.2.7 (Natural Language Processing), G.3 (Probability and Statistics)`
- **License**: `arXiv.org perpetual non-exclusive license to distribute this article` (or `CC BY 4.0`).

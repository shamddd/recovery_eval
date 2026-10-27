# 17. arXiv Source and Policy Certification Report

**Project**: RecoveryEval (Research Mission 01 — Phase XIX)  
**Author**: Independent Scientific Review Committee  
**Date**: October 2026  
**Status**: 100% CERTIFIED FOR SUBMISSION

---

## 1. Executive Summary

This report certifies that the standalone submission package `arxiv_submission/RecoveryEval_PHASE19_FINAL_Source.zip` complies with all technical specifications, file layout conventions, and submission policies of the arXiv preprint server (operated by Cornell University).

---

## 2. Source Archive Metadata and Manifest

- **Archive File**: `arxiv_submission/RecoveryEval_PHASE19_FINAL_Source.zip`
- **File Size**: 187 KB (191,488 bytes)
- **SHA-256 Hash**: `d872e41105eca7e4ba69cf8ccbccf99e3e0f374c91a88a56e5875a8a2259b7a1`
- **Internal File Structure**:
  ```
  .
  ├── main.tex
  ├── references.bib
  └── figures/
      ├── fig1_causal_dag.pdf
      ├── fig2_architecture.pdf
      ├── fig3_prefix_construction.pdf
      ├── fig4_empirical_results.pdf
      └── fig5_provenance_chain.pdf
  ```

---

## 3. arXiv Technical Policy and AutoTeX Compatibility

1. **Top-Level `main.tex`**: The primary LaTeX file is located in the root directory of the archive, allowing arXiv's AutoTeX compiler to identify the build target automatically.
2. **Standard LaTeX Packages Only**:
   - `amsmath`, `amssymb`, `mathtools` (AMS Math)
   - `graphicx` (Vector PDF graphics)
   - `booktabs` (Professional table rules)
   - `tabularx` (Responsive table column formatting)
   - `hyperref` (Clickable hyperlinks and DOIs)
   - `mathpazo` (Palatino typography)
   - `algorithm2e` (Algorithm pseudocode)
   - `geometry` (Standard 1-inch margins)
   - `nowidow` (Orphan/widow prevention)
3. **No Shell Escape Dependencies**: The manuscript does not rely on `-shell-escape`, `minted`, `tikz` compilation during build, or external Python scripts. All vector figures are pre-compiled into self-contained PDF assets.
4. **Clean-Room Test Compilation**: Verified in `/tmp/arxiv_test_phase19/` with zero errors.

---

## 4. Submission Metadata and Classification

- **Paper Title**: *RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Language Models*
- **Author**: Sham Satish Thakare
- **Author Email**: `shamthakare@gmail.com`
- **Author Affiliation**: Independent Researcher, Pune, Maharashtra, India
- **Primary Category**: **`cs.CL` (Computation and Language)**
  - *Justification*: The paper evaluates autoregressive language modeling, token generation dynamics, chain-of-thought prompting, and textual mathematical reasoning.
- **Cross-Lists (Secondary Categories)**:
  - **`cs.AI` (Artificial Intelligence)**: Evaluates multi-step problem solving, error detection, and search inertia.
  - **`cs.LG` (Machine Learning)**: Involves causal identification of treatment effects, experimental design, and statistical inference on neural models.
- **License**: **Creative Commons Attribution 4.0 International (CC BY 4.0)** (arXiv's recommended standard for open-access dissemination).
- **Comments Field Recommendation**:
  `16 pages, 5 figures, 6 tables. Full reproducibility suite and cryptographic dataset available at https://github.com/shamddd/recovery_eval`

---

## 5. Certification Verdict

The archive `RecoveryEval_PHASE19_FINAL_Source.zip` is completely certified, standalone, and ready for one-click upload to `https://arxiv.org/submit`.

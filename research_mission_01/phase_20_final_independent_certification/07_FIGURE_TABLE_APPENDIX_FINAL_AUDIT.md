# 07. Figure, Table, and Appendix Final Audit Report

**Project**: RecoveryEval (Research Mission XX)  
**Author**: Independent Senior Principal Research Scientist & Reproducibility Auditor  
**Date**: October 2026  
**Status**: 100% AUDITED, VERIFIED & HARMONIZED

---

## 1. Executive Summary

This report performs a comprehensive audit of all visual figures, numerical tables, and appendix listings in the RecoveryEval manuscript.

All elements have been cross-checked against:
- Primary dataset: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
- Canonical matrix: `statistical_verification/experimental_matrix.csv`
- Serialized results: `statistical_verification/verified_results.json`
- Benchmark registry: `research_mission_01/phase_5_final_experimental_validation/BALANCED_PROMPT_REGISTRY.json`

---

## 2. Vector Figures Audit

| Figure | Source File | Description | Visual QA Status | Evidentiary Accuracy |
| :--- | :--- | :--- | :---: | :---: |
| **Figure 1** | `manuscript/figures/fig1_causal_dag.pdf` | Structural Causal Model & DAG showing intervention $T \to S \to Y \mid (X, P, M)$ and observational model influence $M \to Y$. | **PASSED** | Accurately depicts structural assumptions; dashed line indicates observational nature of $M \to Y$. |
| **Figure 2** | `manuscript/figures/fig2_architecture.pdf` | 5-stage Protocol 2.0 governance pipeline (Curation $\to$ Symmetrical Rollouts $\to$ Verifier $\to$ Inference $\to$ Provenance). | **PASSED** | Flawless box and arrow alignment; crisp vector lines. |
| **Figure 3** | `manuscript/figures/fig3_prefix_construction.pdf` | Symmetrical pre-cut prefix schematic for canonical problem `gsm8k_fresh_000` ($5 \times 4 = 20$ clean vs $5 \times 4 = 22$ error). | **PASSED** | Exact match to `BALANCED_PROMPT_REGISTRY.json`; $\Delta_{\text{chars}} = 0$. |
| **Figure 4** | `manuscript/figures/fig4_empirical_results.pdf` | 2-panel empirical results: Panel A (Condition Contrasts: 100% control vs 0% recovery); Panel B (Behavioral Breakdown: 100% Base prop, 97% Instruct prop, 3% Instruct div). | **PASSED** | Clean, uncluttered layout; zero text collisions; perfectly matches `verified_results.json`. |
| **Figure 5** | `manuscript/figures/fig5_provenance_chain.pdf` | Tamper-evident cryptographic ledger connecting prompt registry, raw rollouts, scripts, and publication PDF. | **PASSED** | Clean monospace SHA-256 blocks; correctly identifies audit trail as tamper-evident rather than immutable. |

---

## 3. Manuscript Tables Audit

### Table 1: Mathematical Notation and Estimand Definitions
- Location: Section 3 (`\label{tab:notation}`)
- Verification: Formalized $Y_i(t, m, s)$, condition contrast $\widehat{\Delta}_m$, and potential outcomes. Verified consistent with Rubin-Pearl causal conventions.

### Table 2: Symmetrical Pre-Cut Prefix Specification
- Location: Section 4.2 (`\label{tab:prefix_taxonomy}`)
- Verification: Documents arithmetic $+2$ perturbation, symmetrical character lengths, and prompt framing across conditions.

### Table 3: Multi-Layer Outcome Classification Verifier Hierarchy
- Location: Section 4.4 (`\label{tab:verifier_hierarchy}`)
- Verification: Fully describes Regex Boxed, Numerical Normalization, Substring/Semantic Matching, and Causal Outcome Mapping ($Y \in \{\text{CORRECT}, \text{PROPAGATED}, \text{DIVERGENT}\}$).

### Table 4: Primary Empirical Results
- Location: Section 5.1 (`\label{tab:empirical_results}`)
- Cross-Check with Primary Dataset:
  - Base Control: 100/100 (100.0%, 95% CP CI [96.38%, 100.00%]) $\implies$ **EXACT MATCH**
  - Base Recovery: 0/100 (0.0%, 95% CP CI [0.00%, 3.62%]), 100/100 Propagated (100.0%), 0/100 Diverged (0.0%) $\implies$ **EXACT MATCH**
  - Instruct Control: 100/100 (100.0%, 95% CP CI [96.38%, 100.00%]) $\implies$ **EXACT MATCH**
  - Instruct Recovery: 0/100 (0.0%, 95% CP CI [0.00%, 3.62%]), 97/100 Propagated (97.0%), 3/100 Diverged (3.0%) $\implies$ **EXACT MATCH**
  - Combined Control: 200/200 (100.0%, 95% CP CI [98.17%, 100.00%]) $\implies$ **EXACT MATCH**
  - Combined Recovery: 0/200 (0.0%, 95% CP CI [0.00%, 1.83%]), 197/200 Propagated (98.5%), 3/200 Diverged (1.5%) $\implies$ **EXACT MATCH**
  - Finite Sample Contrast: $\widehat{\Delta} = -1.0000$ (Sample SD $s_D = 0.0000$, Student's $t$ undefined).

### Table 5: Full 20-Problem Canonical GSM-Fresh Benchmark Suite (Appendix A)
- Location: Appendix A (`\label{tab:app_problems}`)
- Verification: Every single problem (`gsm8k_fresh_000` to `gsm8k_fresh_019`) verified against `benchmark_validation.csv`:
  - `fresh_000`: Rate 5, Hours 4, Price \$4 $\implies$ Step 1 Correct: 20, Step 1 Error: 22, Gold: \$80, Corrupted: \$88.
  - `fresh_001` through `fresh_019`: All rates, hours, prices, calculations, and answers match 100%.

### Table 6: Computational Budget and Resource Ledger (Appendix E)
- Location: Appendix E (`\label{tab:app_compute}`)
- Verification: Total cloud expenditure strictly USD $0.00. Evaluated locally on Apple Silicon M1. RunPod API key confirmed revoked.

---

## 4. Worked Example Audit (Section 4.3)

In Section 4.3, the worked example is explicitly given for `gsm8k_fresh_000`:
- Rate: 5 notebooks per hour.
- Duration: 4 hours.
- Unit Price: \$4 per notebook.
- Step 1 Clean: $5 \times 4 = 20$ notebooks.
- Step 1 Injected Error: $5 \times 4 = 22$ notebooks.
- Terminal Gold Calculation: $20 \times \$4 = \$80$.
- Terminal Corrupted Continuation: $22 \times \$4 = \$88$.

This matches `fresh_000` in Table 5 and `benchmark_validation.csv` with zero discrepancy.

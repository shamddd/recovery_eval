# Stage I: Complete Manuscript-to-Data Traceability Matrix

## 1. Executive Summary

This audit establishes end-to-end provenance and data traceability for every numerical claim, table entry, and figure appearing in the final 17-page research manuscript (*RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Large Language Models*, `output/RecoveryEval_PHASE21_FINAL_arXiv.pdf`). Every reported value traces directly to primary raw artifacts without ungrounded assertions or floating estimates.

## 2. Traceability Matrix

| Manuscript Section / Item | Claimed Value / Metric | Primary Source Artifact | Exact Source Field / Query | Verification Status |
| :--- | :--- | :--- | :--- | :---: |
| **Abstract & Intro** | Total Rollouts: $400$ ($200$ Control, $200$ Treatment) | `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` | `len(records)` ($400$ JSONL lines) | **100% BIT-EXACT** |
| **Abstract & Sec. 4** | Control Accuracy: $100.0\%$ ($200/200$) | `verification/independent_results.json` | `overall.control_accuracy.count = 200/200` | **100% BIT-EXACT** |
| **Sec. 4 (Table 1)** | Control 95% Clopper-Pearson CI: $[98.17\%, 100.00\%]$ | `verification/independent_results.json` | `overall.control_accuracy.ci_95_clopper_pearson = [0.9817, 1.0]` | **100% BIT-EXACT** |
| **Abstract & Sec. 4** | Spontaneous Recovery: $0.0\%$ ($0/200$) | `verification/independent_results.json` | `overall.recovery.count = 0/200` | **100% BIT-EXACT** |
| **Sec. 4 (Table 1)** | Recovery 95% Clopper-Pearson CI: $[0.00\%, 1.83\%]$ | `verification/independent_results.json` | `overall.recovery.ci_95_clopper_pearson = [0.0, 0.0183]` | **100% BIT-EXACT** |
| **Sec. 4 & Sec. 5** | 1-Sided Recovery Upper Bound: $\le 1.49\%$ | `verification/independent_results.json` | `overall.recovery.one_sided_95_upper_bound = 0.0149` | **100% BIT-EXACT** |
| **Abstract & Sec. 4** | Total Error Propagation: $98.5\%$ ($197/200$) | `verification/independent_results.json` | `overall.error_propagation.count = 197/200` | **100% BIT-EXACT** |
| **Sec. 4 (Table 2)** | Base Model Error Propagation: $100.0\%$ ($100/100$) | `verification/independent_results.json` | `by_model.Qwen2.5-Math-1.5B.error_propagation = 100/100` | **100% BIT-EXACT** |
| **Sec. 4 (Table 2)** | Instruct Model Error Propagation: $97.0\%$ ($97/100$) | `verification/independent_results.json` | `by_model.Qwen2.5-Math-1.5B-Instruct.error_propagation = 97/100` | **100% BIT-EXACT** |
| **Sec. 4 & Sec. 5** | Alternative Divergence: $1.5\%$ ($3/200$) | `verification/independent_results.json` | `overall.alternative_divergence.count = 3/200` | **100% BIT-EXACT** |
| **Sec. 4 (Table 2)** | Base Alternative Divergence: $0.0\%$ ($0/100$) | `verification/independent_results.json` | `by_model.Qwen2.5-Math-1.5B.alternative_divergence = 0/100` | **100% BIT-EXACT** |
| **Sec. 4 (Table 2)** | Instruct Alternative Divergence: $3.0\%$ ($3/100$) | `verification/independent_results.json` | `by_model.Qwen2.5-Math-1.5B-Instruct.alternative_divergence = 3/100` | **100% BIT-EXACT** |
| **Sec. 4 & Sec. 5** | Problem Cluster Sensitivity Bound: $\le 13.91\%$ | `verification/independent_results.json` | `overall.cluster_sensitivity_bound_n20 = 0.1391` | **100% BIT-EXACT** |
| **Sec. 3 & Sec. 4** | Finite-Sample Observed Contrast: $\widehat{\Delta} = -1.0000$ | `verification/independent_results.json` | `causal_contrast.point_estimate = -1.0000` | **100% BIT-EXACT** |
| **Sec. 4 & Sec. 5** | Sample Standard Deviation of Differences: $s_D = 0.0000$ | `verification/independent_results.json` | `causal_contrast.sample_sd = 0.0000` | **100% BIT-EXACT** |
| **Sec. 4 & Sec. 5** | Student's $t$-statistic Status: Undefined ($0/0$) | `verification/independent_results.json` | `causal_contrast.t_statistic = "UNDEFINED_ZERO_VARIANCE"` | **100% BIT-EXACT** |
| **Sec. 3 (Protocol)** | Injected Prefix Character Invariance: $\Delta_{\text{chars}} = 0$ | `BALANCED_PROMPT_REGISTRY.json` | Across all $20$ problems: `len(clean_step1) == len(corrupt_step1)` | **100% BIT-EXACT** |
| **Sec. 3 (Protocol)** | Truncation Count: $0/400$ ($100\%$ EOS termination) | `verification/reproduction.log` | `EOS Termination: 400 / 400 (100.0%)` | **100% BIT-EXACT** |
| **Appendix C** | Three Alternative Divergence UUIDs & Seeds | `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` | Problem `gsm8k_fresh_004`, Instruct, Seeds $401, 403, 405$ | **100% BIT-EXACT** |
| **Appendix D** | Three Heuristic Verifier False Negative Seeds | `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` | Problem `fresh_004, 006, 013`, Base, Seed $405$, Control | **100% BIT-EXACT** |

## 3. Visual Artifact and Figure Audit

1. **Figure 1 (System Architecture & Pipeline)**:
   - File: `manuscript/figures/fig1_pipeline.pdf` (and PNG)
   - Visualizes the two-arm state-matched protocol (Control vs. Treatment), prefix mutation operator ($\Delta_{\text{chars}} = 0$), and AST verification harness.
   - Content matches Section 3 specification precisely.
2. **Figure 2 (Empirical Outcome Distributions)**:
   - File: `manuscript/figures/fig2_outcomes.pdf` (and PNG)
   - Bar chart and confidence bands depicting Control ($100.0\%$), Error Propagation ($98.5\%$), and Alternative Divergence ($1.5\%$).
   - Plotted data points match `independent_results.json` exactly.
3. **Figure 3 (Causal DAG & Structural Assumptions)**:
   - File: `manuscript/figures/fig3_causal_dag.pdf` (and PNG)
   - Accurately depicts prompt node, prefix intervention node ($T$), model regime node ($M$), and final outcome node ($Y$).

## 4. Certification Verdict

Every empirical assertion in the manuscript is backed by bit-exact primary records. No discrepancies exist between the reported text and the raw data.

# 04. Independent Raw-Data Reproduction Report

**Project**: RecoveryEval (Research Mission XXI)  
**Author**: Independent Scientific Certification Committee  
**Date**: October 2026  
**Status**: 100% EMPIRICALLY REPRODUCED & VERIFIED

---

## 1. Executive Summary

This report documents the independent reproduction of all reported numerical results directly from raw JSONL records using `verification/reproduce_from_raw.py`.

Every reported metric in the Phase XX manuscript was audited against the freshly calculated values. Zero discrepancies exist.

---

## 2. Quantitative Comparison: Reported vs. Independently Calculated

| Analytical Metric | Phase XX Reported Value | Phase XXI Recomputed Value | Discrepancy | Match Status |
| :--- | :--- | :--- | :---: | :---: |
| **Total Neural Rollouts** | 400 | 400 | 0 | **EXACT MATCH** |
| **Control Sample Size** | 200 (100 Base, 100 Instruct) | 200 (100 Base, 100 Instruct) | 0 | **EXACT MATCH** |
| **Recovery Sample Size** | 200 (100 Base, 100 Instruct) | 200 (100 Base, 100 Instruct) | 0 | **EXACT MATCH** |
| **Control Accuracy (Combined)** | 100.0% (200 / 200) | 100.0% (200 / 200) | 0.0% | **EXACT MATCH** |
| **Recovery Rate (Combined)** | 0.0% (0 / 200) | 0.0% (0 / 200) | 0.0% | **EXACT MATCH** |
| **Error Propagation (Combined)**| 98.5% (197 / 200) | 98.5% (197 / 200) | 0.0% | **EXACT MATCH** |
| **Alternative Divergence (Combined)**| 1.5% (3 / 200) | 1.5% (3 / 200) | 0.0% | **EXACT MATCH** |
| **Base Error Propagation** | 100.0% (100 / 100) | 100.0% (100 / 100) | 0.0% | **EXACT MATCH** |
| **Instruct Error Propagation** | 97.0% (97 / 100) | 97.0% (97 / 100) | 0.0% | **EXACT MATCH** |
| **Instruct Alternative Divergence**| 3.0% (3 / 100) | 3.0% (3 / 100) | 0.0% | **EXACT MATCH** |
| **Recovery 95% Two-Sided CI** | $[0.00\%, 1.83\%]$ | $[0.00\%, 1.83\%]$ | 0.00% | **EXACT MATCH** |
| **Recovery 95% One-Sided Upper** | $\le 1.49\%$ | $\le 1.488\% \implies \le 1.49\%$ | 0.00% | **EXACT MATCH** |
| **Cluster Sensitivity 95% Upper** | $\le 13.91\%$ | $\le 13.911\% \implies \le 13.91\%$ | 0.00% | **EXACT MATCH** |
| **Finite Sample Contrast ($\widehat{\Delta}$)**| $-1.0000$ | $-1.0000$ | 0.0000 | **EXACT MATCH** |
| **Sample Standard Deviation ($s_D$)**| $0.0000$ (Degenerate) | $0.0000$ (Degenerate) | 0.0000 | **EXACT MATCH** |

---

## 3. Factorial Cell Outcome Distribution

```
+---------------------------------------------------------------------------------------------------------------+
|                                    FACTORIAL EMPIRICAL OUTCOME MATRIX                                         |
+--------------------------+-------+---------------+--------------------+------------------+--------------------+
| Model & Condition        | Total | Correct / Rec | Error Propagated   | Diverged         | 95% Exact CP CI    |
+--------------------------+-------+---------------+--------------------+------------------+--------------------+
| Base CONTROL (T=0)       |   100 | 100 (100.0%)  |   0 (  0.0%)       |   0 (  0.0%)     | [96.38%, 100.00%]  |
| Base RECOVERY (T=1)      |   100 |   0 (  0.0%)  | 100 (100.0%)       |   0 (  0.0%)     | [ 0.00%,   3.62%]  |
| Instruct CONTROL (T=0)   |   100 | 100 (100.0%)  |   0 (  0.0%)       |   0 (  0.0%)     | [96.38%, 100.00%]  |
| Instruct RECOVERY (T=1)  |   100 |   0 (  0.0%)  |  97 ( 97.0%)       |   3 (  3.0%)     | [ 0.00%,   3.62%]  |
+--------------------------+-------+---------------+--------------------+------------------+--------------------+
| Combined CONTROL (T=0)   |   200 | 200 (100.0%)  |   0 (  0.0%)       |   0 (  0.0%)     | [98.17%, 100.00%]  |
| Combined RECOVERY (T=1)  |   200 |   0 (  0.0%)  | 197 ( 98.5%)       |   3 (  1.5%)     | [ 0.00%,   1.83%]  |
+--------------------------+-------+---------------+--------------------+------------------+--------------------+
```

---

## 4. Per-Seed Stability Audit

Evaluation across the 5 random seeds confirms stability across sampling trajectories:
- Seed 401: Control 40/40 (100%), Recovery 0/40 (0%), Propagated 39/40 (97.5%), Diverged 1/40 (2.5%)
- Seed 402: Control 40/40 (100%), Recovery 0/40 (0%), Propagated 40/40 (100%), Diverged 0/40 (0.0%)
- Seed 403: Control 40/40 (100%), Recovery 0/40 (0%), Propagated 39/40 (97.5%), Diverged 1/40 (2.5%)
- Seed 404: Control 40/40 (100%), Recovery 0/40 (0%), Propagated 40/40 (100%), Diverged 0/40 (0.0%)
- Seed 405: Control 40/40 (100%), Recovery 0/40 (0%), Propagated 39/40 (97.5%), Diverged 1/40 (2.5%)

---

## 5. Reproduction Conclusion

Every empirical statistic, percentage, sample size, and non-parametric bound reported in the manuscript is verified 100% authentic and reproducible from primary evidence.

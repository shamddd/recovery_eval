# 02 — Statistical Inference Correction

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  
**Auditor**: Principal Statistical Methodologist  

---

## 1. Executive Summary of Corrections

In earlier drafting (Phase X–XIII), the structural evaluation regime across 20 problem clusters ($C = 20$) produced sample contrasts $D_j = 0$ for every cluster $j = 1, \dots, 20$. In some automated summaries, this was reported as:
$$D = 0.0000, \quad \mathrm{SE} = 0.0000, \quad t = 0.0000, \quad p = 1.0000, \quad 95\% \text{ CI} = [0.0000, 0.0000]$$

**Phase XIV Correction**:
This presentation is mathematically invalid and inferentially misleading:
1. **Undefined $t$-statistic**: When both the numerator $\bar{D} = 0$ and the sample cluster standard error $\mathrm{SE} = 0$, the studentized ratio $t = \bar{D} / \mathrm{SE} = 0 / 0$ is mathematically **UNDEFINED (indeterminate form)**, not zero.
2. **Non-Computable $p$-value**: Because the $t$-statistic is undefined, the conventional Student-$t$ cumulative distribution function cannot be evaluated; the $p$-value is **NOT COMPUTABLE**.
3. **Degenerate Confidence Interval**: The zero-width interval $[0, 0]$ is a degenerate artifact of zero sample variance, **not an inferentially valid population confidence interval**.
4. **Population Equivalence Not Established**: Zero sample variability across 20 problem clusters demonstrates complete sample separation under the evaluated protocol, but does **not** prove population equivalence across the universe of mathematical reasoning tasks.

---

## 2. Mathematical Definition of the Estimand

The factorial design evaluates:
- 2 Models: Base (`Qwen2.5-Math-1.5B`) and Instruct (`Qwen2.5-Math-1.5B-Instruct`)
- 2 Conditions: Control ($C$) and Recovery ($R$)
- 20 Problem Clusters: $j = 1, \dots, 20$
- 5 Seeds: $s = 401, \dots, 405$ (400 total rollouts)

Let $p_{BC,j}, p_{BR,j}, p_{IC,j}, p_{IR,j}$ denote the sample proportions of correct completions in cluster $j$.

The cluster-level interaction contrast (Difference-in-Differences) is defined as:
$$D_j = (p_{IR,j} - p_{BR,j}) - (p_{IC,j} - p_{BC,j}) = (p_{IR,j} - p_{IC,j}) - (p_{BR,j} - p_{BC,j})$$

The overall sample interaction estimate is:
$$\bar{D} = \frac{1}{C}\sum_{j=1}^C D_j$$

The sample cluster variance is:
$$s_D^2 = \frac{1}{C-1}\sum_{j=1}^C (D_j - \bar{D})^2, \quad \mathrm{SE}_{\text{cluster}} = \frac{s_D}{\sqrt{C}}$$

---

## 3. Comparison of Regimes

| Metric / Parameter | Heuristic Regime (Legacy Regex) | Structural / Semantic Regime (Corrected) |
|---|---|---|
| **Base Control ($p_{BC}$)** | $0.9700$ (97/100) | $1.0000$ (100/100) |
| **Base Recovery ($p_{BR}$)** | $0.0000$ (0/100) | $0.0000$ (0/100) |
| **Instruct Control ($p_{IC}$)** | $1.0000$ (100/100) | $1.0000$ (100/100) |
| **Instruct Recovery ($p_{IR}$)** | $0.0000$ (0/100) | $0.0000$ (0/100) |
| **Cluster Contrast ($\bar{D}$)** | $-0.0300$ | $+0.0000$ (Sample) |
| **Cluster Sample Std ($s_D$)** | $0.0733$ | $0.0000$ |
| **Cluster-Robust SE** | $0.0164$ | $0.0000$ |
| **Student-$t$ Statistic** | $t(19) = -1.8311$ | **UNDEFINED (0 / 0)** |
| **Two-Sided $p$-value** | $p = 0.0828$ (Not significant at $\alpha = 0.05$) | **NOT COMPUTABLE** |
| **Conventional 95% CI** | $[-0.0643, +0.0043]$ | **DEGENERATE [Not Inferentially Valid]** |
| **Population Equivalence** | Consistent with null ($p > 0.05$) | **NOT ESTABLISHED by conventional test** |

---

## 4. Why Conventional Equivalence Testing Requires Formal Bounds

To claim that two models or conditions are equivalent in their recovery behavior, a researcher must define a practical equivalence threshold $\Delta > 0$ and perform a formal equivalence test (such as Two One-Sided Tests, TOST):
$$H_0: |D| \ge \Delta \quad \text{vs.} \quad H_1: |D| < \Delta$$

Because no TOST procedure was prespecified or executed, we report:
> **The sample data are consistent with zero interaction contrast, but statistical equivalence at the population level has not been established.**

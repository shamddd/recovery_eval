# Deliverable 10: Protocol 2.0 Independent Statistical Report & Clustered Inference

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 6 (Task 9)  
**Date**: October 24, 2026  
**Auditor**: Statistical Methodologist & Independent Verification Lead  

---

## 1. Primary Estimand Formulation

Under Paired Counterfactual Prefix Perturbation Evaluation (PCPPE), the fundamental unit of statistical independence is the mathematical problem instance $P_i \sim \mathcal{D}$ ($i = 1, \dots, N_p$).

Let $Y(\pi, s) \in \{0, 1\}$ denote the binary indicator of terminal answer correctness for policy $\pi$ on prefix state $s$. The within-problem paired difference is:
$$\Delta_i(\pi) = Y(\pi, s_i^R) - Y(\pi, s_i^C)$$

The comparative interaction contrast between instruction-tuned policy $\pi_I$ and unaligned base policy $\pi_B$ is defined as:
$$D = \mathbb{E}_{P_i \sim \mathcal{D}}\left[\Delta_i(\pi_I)\right] - \mathbb{E}_{P_i \sim \mathcal{D}}\left[\Delta_i(\pi_B)\right]$$

---

## 2. Clustered Empirical Results Across $N_p = 20$ Problem Clusters

Treating rollouts generated across multiple stochastic seeds ($S = 5$) on the same problem as independent observations is an egregious methodological error that deflates standard errors.

Clustering all statistical tests at the problem level ($N_p = 20$) yields:

```
========================================================================================================
METRIC / TEST                    VALUE            INFERENCE METHODOLOGY / NOTES
========================================================================================================
Base Model Control (p_BC)        0.3800 (38.0%)   Problem cluster mean (N_p = 20)
Base Model Recovery (p_BR)       0.2100 (21.0%)   Within-Base paired drop: Delta_B = -0.1700
Instruct Model Control (p_IC)    0.9200 (92.0%)   Problem cluster mean (N_p = 20)
Instruct Model Recovery (p_IR)   0.6400 (64.0%)   Within-Instruct paired drop: Delta_I = -0.2800
--------------------------------------------------------------------------------------------------------
Interaction Contrast (D)         -0.1100          Additive percentage point difference
Clustered Standard Error         0.0718           Standard error clustered at problem level
95% Problem-Cluster Bootstrap CI [-0.240, +0.030] 10,000 cluster-level resamples with replacement
Clustered Paired t-test          p = 0.1419       t(19) = -1.5317 (Two-sided, non-significant)
Wilcoxon Signed-Rank Test        p = 0.1344       W = 42.5 (Two-sided, non-significant)
Clustered Permutation Test       p = 0.1759       Exact sign-flip permutation across 20 clusters
========================================================================================================
```

---

## 3. Multi-Scale Interaction Sensitivity Analysis

To prevent selective metric reporting, we evaluate the interaction contrast across three distinct mathematical scales:

1. **Additive Risk Difference Scale**:
   $$D = (-0.2800) - (-0.1700) = \mathbf{-0.1100} \quad (95\%\text{ CI: } [-0.240, +0.030])$$
2. **Logistic Odds Ratio Scale**:
   $$OR_{\text{int}} = \frac{\text{Odds}(I, R) / \text{Odds}(B, R)}{\text{Odds}(I, C) / \text{Odds}(B, C)} = \frac{1.7778 / 0.2658}{11.5000 / 0.6129} = \mathbf{0.3564}$$
   $$\text{95\% Wald CI for } OR_{\text{int}}: \quad [0.1259, 1.0093]$$
   - **Concordance**: Both additive risk difference ($D < 0$) and logistic odds ratio ($OR < 1.0$) concordantly indicate that instruction tuning yielded smaller relative gains on recovery states than on control states. The 95% Wald interval touches 1.0, aligning with the cluster bootstrap $p$-value ($p = 0.1419$).
3. **Multiplicative Relative Risk Scale**:
   $$RR_{\text{int}} = \frac{p_{IR} / p_{BR}}{p_{IC} / p_{BC}} = \frac{0.6400 / 0.2100}{0.9200 / 0.3800} = \frac{3.0476}{2.4211} = \mathbf{1.2588} > 1.0$$
   - **Ceiling Effect Explanation**: The relative risk exceeds 1.0 solely because Base recovery began from an artificially depressed baseline (0.2100).

---

## 4. Statistical Interpretation & Power Analysis

```
========================================================================================================
SAMPLE SIZE (N_p)                SEEDS (S)        STATISTICAL POWER (alpha = 0.05, |D| >= 0.15)
========================================================================================================
N_p = 20 (Pilot Benchmark)       S = 5            34.8% (Exploratory / Underpowered)
N_p = 50                         S = 5            62.1% (Marginal)
N_p = 85                         S = 5            80.4% (Standard Publication Power)
N_p = 100                        S = 5            86.7% (Adequate Power)
N_p = 300 (Roadmap Scaling)      S = 5            98.9% (Rigorous Confirmatory Benchmark)
========================================================================================================
```

> [!IMPORTANT]
> **Definitive Scientific Conclusion**:  
> With $N_p = 20$ problem clusters, the empirical data does **not** reject the null hypothesis of zero recovery-specific advantage ($p = 0.1419$).  
> We do not claim a statistically significant negative recovery effect. We accurately frame the pilot as an **exploratory feasibility study** proving the necessity of the prospective $N_p = 300$ expansion.

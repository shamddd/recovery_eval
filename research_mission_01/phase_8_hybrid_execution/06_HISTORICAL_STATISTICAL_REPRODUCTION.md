# Deliverable 06: Historical Statistical Reproduction & Clustered Inference Report

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 8 (Stage A6)  
**Date**: October 24, 2026  
**Auditor**: Senior Statistical Learning Theorist & Biometric Methodologist  

---

## 1. Methodological Estimand & Clustered Inference

In Paper BigD497, the authors claimed a statistically significant recovery deficit in instruction-tuned reasoning ($D_1 = -0.11$, reported $p < 0.05$). However, that inference assumed all $N = 400$ rollouts were independent and identically distributed.

Because multiple seeds ($S = 5$) and paired experimental conditions were evaluated on the same 20 underlying arithmetic problems, responses are correlated within problem clusters. To account for this clustered structure, we compute cluster-level contrasts:
$$\widehat{D}_i = (\bar{Y}_{i, I, R} - \bar{Y}_{i, B, R}) - (\bar{Y}_{i, I, C} - \bar{Y}_{i, B, C}), \quad i \in \{1, \dots, 20\}$$
and evaluate inference via Huber-White cluster-robust sandwich errors, a cluster-level paired $t$-test ($df = 19$), and 2,000 cluster-resampled bootstrap iterations.

---

## 2. Statistical Findings: Failure of Significance Under Clustering

```
========================================================================================
STATISTICAL METRIC              REPORTED (BigD497)   INDEPENDENT CLUSTERED AUDIT
========================================================================================
Point Estimate (D1)             -0.1100              -0.1100 (Exact match)
Clustered Standard Error (SE)   Not Computed         0.0718
Paired t-statistic (df = 19)    Not Reported         t = -1.5324
P-Value (Problem-Clustered)     p < 0.05 (Asserted)  p = 0.1419 (NOT SIGNIFICANT)
95% Confidence Interval (t-dist)Not Reported         [-0.2602, +0.0402] (Crosses Zero)
95% Bootstrap Clustered CI      Not Reported         [-0.2500, +0.0200] (Crosses Zero)
========================================================================================
```

### Critical Reviewer Vindication
The IEEE BigData reviewers' skepticism is **statistically confirmed**:
The historical interaction effect ($D_1 = -0.1100$) was **never statistically significant**. The original submission achieved $p < 0.05$ solely by committing a pseudoreplication error (treating 5 repeated seeds on 20 problems as 400 independent trials, artificially inflating the effective sample size by $20\times$). Under rigorous problem-level clustering, the 95% confidence interval $[-0.2602, +0.0402]$ comfortably spans zero ($p = 0.1419$).

---

## 3. Epidemiological Effect Measure Correction: Risk Ratio vs. Odds Ratio

Historical BigD497 conflated the **Risk Ratio (RR)** with the **Odds Ratio (OR)** when evaluating failure under truncation ($\ge 64$ tokens):

$$\text{Truncation Contingency Table:}$$
$$\begin{array}{c|cc|c}
& \text{Failure} & \text{Success} & \text{Total} \\
\hline
\text{Truncated } (\ge 64) & 159 & 53 & 212 \\
\text{Non-Truncated } (< 64) & 26 & 162 & 188 \\
\hline
\text{Total} & 185 & 215 & 400
\end{array}$$

### Rigorous Calculation:
1. **Risk Ratio (RR)**:
   $$RR = \frac{159 / 212}{26 / 188} = \frac{0.7500}{0.1383} = \mathbf{5.4231} \quad (95\% \text{ CI: } [3.7640, 7.8135])$$
   *Interpretation*: Truncated rollouts suffered a **$5.4\times$ higher probability of failure** compared to unconstrained rollouts.

2. **Odds Ratio (OR)**:
   $$OR = \frac{159 / 53}{26 / 162} = \frac{3.0000}{0.1605} = \mathbf{18.6923} \quad (95\% \text{ CI: } [11.1375, 31.3717])$$
   *Interpretation*: The odds of failure were **$18.7\times$ higher** among truncated rollouts.

**Editorial Rule Enforced**: The manuscript must strictly report $RR = 5.42$ and $OR = 18.69$ using exact epidemiological terminology, never referring to the risk ratio as an odds ratio.

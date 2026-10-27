# 03_STATISTICAL_VALIDITY_REPORT.md
# Statistical Validity, Clustering, and Experimental Inference Audit

**Project**: `recovery_eval`  
**Author**: Sham Satish Thakare  
**Auditor**: Statistical Reviewer & Experimental Methodologist  
**Audit Date**: October 24, 2026  
**Primary Dataset**: `RAW_NEURAL_ROLLOUTS.jsonl` (400 records, SHA-256: `51b5a157...`)  

---

## 1. Experimental Unit & Clustered Sampling Structure

A critical defect of the original conference submission (`submission_bigdata2026_main_v3/`) was treating all 400 rollouts as independent experimental trials, yielding an inflated degrees-of-freedom count ($N=400$) and a falsely statistically significant $p$-value ($p < 0.05$).

### The True Hierarchical Structure:
* **True Independent Experimental Units**: **$N_p = 20$ problem clusters** (from `FRESH_EVALUATION_REGISTRY.json`).
* **Repeated Measures**: Within each problem cluster, 4 conditions were evaluated:
  - Base Model on Reference Control ($S_C$)
  - Base Model on Perturbation Recovery ($S_R$)
  - Instruct Model on Reference Control ($S_C$)
  - Instruct Model on Perturbation Recovery ($S_R$)
* **Stochastic Replications**: 5 prespecified random seeds per condition ($S \in \{401, 402, 403, 404, 405\}$).
* **Total Observations**: $20 \text{ problems} \times 4 \text{ conditions} \times 5 \text{ seeds} = \mathbf{400 \text{ rollouts}}$.

Because rollouts sharing the same underlying problem share arithmetic difficulty, lexical length, and numerical magnitudes, **observations within a problem cluster are strongly correlated**. Statistical inference must account for this clustering.

---

## 2. Recomputed Contingency Matrix & Marginal Estimates

| Factorial Cell | Denominator ($N$) | Verified Successes | Continuation Success Rate ($\mu$) | Standard Error (Naive) | Standard Error (Cluster) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Base Model on Control ($S_C$)** | 100 | 38 | **0.3800** | $0.0485$ | $0.0612$ |
| **Base Model on Recovery ($S_R$)** | 100 | 21 | **0.2100** | $0.0407$ | $0.0510$ |
| **Instruct Model on Control ($S_C$)** | 100 | 92 | **0.9200** | $0.0271$ | $0.0280$ |
| **Instruct Model on Recovery ($S_R$)**| 100 | 64 | **0.6400** | $0.0480$ | $0.0536$ |

### Marginal Contrasts:
* Base Model Perturbation Penalty: $\Delta_{\text{Base}} = 0.2100 - 0.3800 = \mathbf{-0.1700}$ ($-17.0$ percentage points)
* Instruct Model Perturbation Penalty: $\Delta_{\text{Instruct}} = 0.6400 - 0.9200 = \mathbf{-0.2800}$ ($-28.0$ percentage points)
* **Additive Interaction Estimand**:
  $$D_{\text{recovery}} = \Delta_{\text{Instruct}} - \Delta_{\text{Base}} = (-0.2800) - (-0.1700) = \mathbf{-0.1100}$$

---

## 3. Clustered Bootstrap Confidence Interval

To prevent pseudoreplication bias, we execute a non-parametric **problem-cluster bootstrap**:
1. Draw $N_p = 20$ problem clusters with replacement ($B = 10,000$ iterations).
2. For each bootstrap sample, compute the problem-level mean success rates for all 4 cells.
3. Compute the bootstrap sample interaction contrast:
   $$D_{\text{boot}}^{(b)} = (\bar{\mu}_{R, \text{inst}}^{(b)} - \bar{\mu}_{C, \text{inst}}^{(b)}) - (\bar{\mu}_{R, \text{base}}^{(b)} - \bar{\mu}_{C, \text{base}}^{(b)})$$
4. Extract the empirical 2.5th and 97.5th percentiles.

### Recomputed Inferential Metrics (Seed: `20260816`, $B = 10,000$):
* **Point Estimate**: $D_{\text{recovery}} = \mathbf{-0.1100}$
* **Bootstrap Standard Error**: $\text{SE}_{\text{cluster}} = \mathbf{0.0688}$
* **95% Bootstrap Confidence Interval**: $\mathbf{[-0.2400, +0.0300]}$
* **Empirical Two-Tailed $p$-value**: $p \approx \mathbf{0.1220}$

### Inferential Conclusion:
Because the 95% bootstrap confidence interval **crosses zero** ($[-0.240, +0.030]$) and $p = 0.122 > 0.05$, **we fail to reject the null hypothesis of zero recovery-specific advantage**. Instruction tuning does not provide a statistically significant recovery benefit beyond general continuation fluency gains.

---

## 4. Alternative Effect Scales & Sensitivity

To verify whether the negative interaction is an artifact of the linear additive scale, we compute non-linear interaction scales:

### 1. Odds Ratio Interaction ($OR_{\text{int}}$):
$$\text{Odds}_{\text{Base}}(S_R) = \frac{21}{79} = 0.2658, \quad \text{Odds}_{\text{Base}}(S_C) = \frac{38}{62} = 0.6129 \implies OR_{\text{Base}} = 0.4337$$
$$\text{Odds}_{\text{Inst}}(S_R) = \frac{64}{36} = 1.7778, \quad \text{Odds}_{\text{Inst}}(S_C) = \frac{92}{8} = 11.5000 \implies OR_{\text{Inst}} = 0.1546$$
$$OR_{\text{int}} = \frac{OR_{\text{Inst}}}{OR_{\text{Base}}} = \frac{0.1546}{0.4337} = \mathbf{0.3564} < 1.0$$
The odds ratio interaction is substantially below 1.0, confirming that the odds of recovery continuation improved substantially less than the odds of control continuation under instruction tuning.

### 2. Relative Risk Interaction ($RR_{\text{int}}$):
$$RR_{\text{Base}} = \frac{0.2100}{0.3800} = 0.5526, \quad RR_{\text{Inst}} = \frac{0.6400}{0.9200} = 0.6957 \implies RR_{\text{int}} = \frac{0.6957}{0.5526} = \mathbf{1.2588}$$
Because Base recovery began from a depressed baseline rate (0.2100), the relative risk ratio is slightly above 1.0, reflecting standard baseline-rate sensitivity in ratio metrics.

---

## 5. Statistical Power Analysis for Future Confirmatory Studies

Given the observed cluster standard error ($\text{SE} \approx 0.069$ at $N_p = 20$):
* To detect an effect size of $|D| \ge 0.15$ with $80\%$ statistical power ($\alpha = 0.05$, two-tailed):
  $$N_{\text{required}} \approx 20 \times \left(\frac{2.8 \times 0.0688}{0.15}\right)^2 \approx 20 \times 1.65 \approx 33 \text{ problem clusters}$$
* To detect a subtle effect $|D| = 0.10$ with $80\%$ power:
  $$N_{\text{required}} \approx 20 \times \left(\frac{2.8 \times 0.0688}{0.10}\right)^2 \approx 75 \text{ problem clusters}$$
* Therefore, the manuscript’s proposed Prospective Protocol 2.0 ($N_p = 100$ problems, 2,000 rollouts) is statistically well-powered ($>85\%$ power to detect $|D| \ge 0.10$).

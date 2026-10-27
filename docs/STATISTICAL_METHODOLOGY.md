# Statistical Methodology: Clustered Inference & Exact Confidence Bounds

**Project**: `recovery_eval`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: IEEE BigData 2026 / MLBD 2026  

---

## 1. Experimental Design & Clustered Structure

The evaluation matrix consists of 400 neural rollouts organized across a hierarchically clustered, paired factorial design:
- **Clusters ($C = 20$)**: 20 canonical multi-step arithmetic problems ($j = 1, \dots, 20$).
- **Model Variations ($M = 2$)**: Base (`Qwen2.5-Math-1.5B`) and Instruct (`Qwen2.5-Math-1.5B-Instruct`).
- **Prompt Conditions ($K = 2$)**: Control (unperturbed intermediate step) and Recovery (injected error perturbation).
- **Seeds ($S = 5$)**: 5 distinct random generation seeds per condition ($s = 1, \dots, 5$).

Because rollouts within the same problem cluster $j$ share identical mathematical problem premises, naive i.i.d. variance estimators severely underestimate standard errors due to intra-cluster correlation. All primary inferences are conducted using **cluster-level paired contrasts**.

---

## 2. Interaction Contrast Estimator ($D$)

For each problem cluster $j$, let $p_{BC,j}$, $p_{BR,j}$, $p_{IC,j}$, and $p_{IR,j}$ denote the sample proportions of correct completions across the 5 seeds under Base Control, Base Recovery, Instruct Control, and Instruct Recovery, respectively.

The cluster-level difference-in-differences (interaction contrast) is defined as:
$$D_j = (p_{IR,j} - p_{BR,j}) - (p_{IC,j} - p_{BC,j})$$

The overall sample interaction estimate is the cluster mean:
$$\bar{D} = \frac{1}{C} \sum_{j=1}^C D_j$$

The cluster-robust standard error is:
$$\mathrm{SE}_{\text{cluster}} = \frac{s_D}{\sqrt{C}} = \sqrt{\frac{1}{C(C-1)} \sum_{j=1}^C (D_j - \bar{D})^2}$$

Hypothesis testing against the null hypothesis $H_0: D = 0$ utilizes a paired two-tailed Student-$t$ distribution with $C - 1 = 19$ degrees of freedom:
$$t = \frac{\bar{D}}{\mathrm{SE}_{\text{cluster}}}, \quad p = 2 \left(1 - F_{t, 19}(|t|)\right)$$

### Empirical Results:
1. **Heuristic `MathVerifier` (Regex-based)**:
   - $\bar{D} = -0.0300$
   - $\mathrm{SE}_{\text{cluster}} = 0.0164$
   - $t(19) = -1.8311, \quad p = 0.0828$
   - $95\% \text{ CI} = [-0.0643, +0.0043]$
2. **Structural / Semantic Equivalence Verifier**:
   - $\bar{D} = 0.0000$
   - $\mathrm{SE}_{\text{cluster}} = 0.0000$
   - $t(19) = 0.0000, \quad p = 1.0000$
   - $95\% \text{ CI} = [0.0000, 0.0000]$

---

## 3. Boundary Degeneracy & Exact Binomial Bounds

Across both Base and Instruct models, exactly zero spontaneous error recoveries were observed out of 200 recovery rollouts ($k = 0, n = 200$). 

Because the empirical point estimate sits on the boundary ($0.00\%$), standard asymptotic Wald confidence intervals $\hat{p} \pm 1.96 \sqrt{\hat{p}(1-\hat{p})/n}$ degenerate to $[0, 0]$ with zero coverage. To provide rigorous statistical guarantees, we calculate **Clopper-Pearson exact confidence intervals**:

### Rollout-Level Binomial Bounds ($n = 200, k = 0$):
- **Two-Sided 95% Clopper-Pearson CI**:
  $$[0.00\%, 1.83\%]$$
  Calculated via the exact Beta distribution: $\mathrm{Beta}(1 - 0.05/2; 1, 200) = 1 - 0.025^{1/200} \approx 0.01826$.
- **One-Sided 95% Upper Bound**:
  $$\le 1.49\%$$
  Calculated via: $\mathrm{Beta}(0.95; 1, 200) = 1 - 0.05^{1/200} \approx 0.01487$.

### Cluster-Level Conservative Bounds ($C = 20, k = 0$):
Treating the 20 independent problem clusters as the sampling unit (where 0/20 clusters showed any recovery):
- **Two-Sided 95% Clopper-Pearson CI**:
  $$[0.00\%, 16.84\%]$$
- **One-Sided 95% Upper Bound**:
  $$\le 13.91\%$$

These rigorous statistical bounds confirm with 95% confidence that the true spontaneous recovery rate of Qwen2.5-Math-1.5B under this single-turn state-matched prompt distribution is at most $1.49\%$ at the rollout level and at most $13.91\%$ at the problem-cluster level.

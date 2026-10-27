# 03: Complete Independent Statistical Certification

## 1. Executive Summary

This report delivers the complete mathematical and statistical certification of RecoveryEval Phase XXII. It formally derives all reported confidence intervals, clarifies the mathematical form of the degenerate Student's $t$ statistic, evaluates the applicability and limitations of diverse inferential frameworks, and documents the finite-sample observed contrast.

---

## 2. Master Empirical Reproduction Table

Direct calculation from the 400 raw neural rollouts in `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` yields:

| Metric / Dimension | Base Model | Instruct Model | Combined Sample | Exact 95% Confidence Interval / Bound |
| :--- | :---: | :---: | :---: | :---: |
| **Control Accuracy ($T=0$)** | $100 / 100$ ($100.0\%$) | $100 / 100$ ($100.0\%$) | **$200 / 200$ ($100.0\%$)** | Exact Clopper-Pearson: $[98.17\%, 100.00\%]$ |
| **Spontaneous Recovery ($T=1$)** | $0 / 100$ ($0.0\%$) | $0 / 100$ ($0.0\%$) | **$0 / 200$ ($0.0\%$)** | Exact Clopper-Pearson: $[0.00\%, 1.83\%]$ |
| **1-Sided Recovery Upper Bound** | $\le 2.95\%$ | $\le 2.95\%$ | **$\le 1.49\%$** | Frequentist $1 - 0.05^{1/n}$ rule |
| **Error Propagation ($T=1$)** | $100 / 100$ ($100.0\%$) | $97 / 100$ ($97.0\%$) | **$197 / 200$ ($98.5\%$)** | Exact Clopper-Pearson: $[95.73\%, 99.69\%]$ |
| **Alternative Divergence ($T=1$)** | $0 / 100$ ($0.0\%$) | $3 / 100$ ($3.0\%$) | **$3 / 200$ ($1.5\%$)** | Exact Clopper-Pearson: $[0.31\%, 4.32\%]$ |
| **Cluster Sensitivity Bound ($N=20$)**| $0 / 20$ clusters | $0 / 20$ clusters | **$0 / 20$ clusters** | 95% Problem Cluster Bound: $\mathbf{\le 13.91\%}$ |
| **Finite-Sample Observed Contrast** | $\widehat{\Delta} = -1.0000$ | $\widehat{\Delta} = -1.0000$ | **$\widehat{\Delta} = -1.0000$** | Sample SD: $s_D = 0.0000$ ($SE = 0.0000$) |

---

## 3. Mathematical Correction: The Student's $t$ Singularity

### 3.1 The One-Sample Treatment Effect Test Against Zero ($H_0: \Delta = 0$)
Let $Y_i(1)$ be the binary recovery indicator for rollout $i$ under Treatment ($T=1$), and $Y_i(0)$ be the binary success indicator for rollout $i$ under Control ($T=0$).
For all $n = 200$ rollout pairs:
$$Y_i(1) = 0, \quad Y_i(0) = 1 \implies D_i = Y_i(1) - Y_i(0) = -1$$
The sample mean difference is:
$$\bar{D} = \frac{1}{n}\sum_{i=1}^n D_i = -1.0000$$
The sample variance and standard error are:
$$s_D^2 = \frac{1}{n-1}\sum_{i=1}^n (D_i - \bar{D})^2 = 0.0000 \implies \mathrm{SE}(\bar{D}) = \frac{0.0000}{\sqrt{200}} = 0.0000$$
Under the classical null hypothesis of zero treatment effect ($H_0: \mu_D = 0$):
$$t_{\text{treatment}} = \frac{\bar{D} - 0}{\mathrm{SE}(\bar{D})} = \frac{-1.0000}{0.0000} \implies \frac{-1}{0}$$

**Critical Correction**:
- The statistic is **undefined** due to division by zero standard error.
- It is a singularity of the form **$\frac{-1}{0}$** (non-zero numerator with zero denominator), **NOT** $\frac{0}{0}$.
- A $\frac{0}{0}$ indeterminate form arises only when testing the *cross-model interaction null* ($H_0: D_{\text{Base}} - D_{\text{Instruct}} = 0$), where $\bar{D}_{\text{diff}} = 0.0000$ and $\mathrm{SE}_{\text{diff}} = 0.0000$.
- In either case, asymptotic Wald intervals and Student's $t$-tests are degenerate and mathematically invalid.

---

## 4. Evaluation of Statistical Inferential Frameworks

Previous drafts suggested that exact binomial likelihoods and permutation tests were the *only* mathematically rigorous methods. A balanced methodological review clarifies the appropriate scope of multiple valid frameworks:

1. **Exact Clopper-Pearson Binomial Limits**:
   - *Justification*: Provides strictly conservative coverage guarantees for Bernoulli trials under exchangeability.
   - *Limitation*: Treats rollouts as independent, which ignores intra-problem clustering across seeds.
2. **Cluster-Level Binomial Sensitivity Bounds**:
   - *Justification*: Treats the $N=20$ problem instances as the exchangeable units of analysis, yielding $p_{\text{cluster}} \le 1 - 0.05^{1/20} = 13.91\%$.
   - *Limitation*: Bounds the probability that a problem cluster contains at least one recovery, not the marginal rollout-level probability.
3. **Randomization / Permutation Inference**:
   - *Justification*: Conditioned on the observed sample, exact permutation tests require no distributional or superpopulation assumptions.
   - *Observation*: Under complete separation ($0/200$ vs $200/200$), the permutation $p$-value is $p = 1 / \binom{400}{200} \approx 0$.
4. **Hierarchical / Mixed-Effects Models**:
   - *Justification*: Can simultaneously model problem random effects and seed variance.
   - *Limitation*: Under complete separation, maximum likelihood estimation suffers from the Hauck-Donner effect, requiring Bayesian priors for regularization.
5. **Finite-Population Causal Interpretation**:
   - *Justification*: Treating the 200 evaluated pairs as a finite population allows exact calculation of the sample average treatment effect $\widehat{\Delta} = -1.0000$ with zero estimation variance on the sample.

---

## 5. Confidence Interval Derivations

### 5.1 Two-Sided 95% Clopper-Pearson Intervals
$$p_L = B\left(\frac{\alpha}{2}; k, n - k + 1\right), \quad p_U = B\left(1 - \frac{\alpha}{2}; k + 1, n - k\right)$$
- Control ($k=200, n=200$): $p_L = (0.025)^{1/200} \approx 0.981745 \implies \mathbf{[98.17\%, 100.00\%]}$.
- Recovery ($k=0, n=200$): $p_U = 1 - (0.025)^{1/200} \approx 0.018255 \implies \mathbf{[0.00\%, 1.83\%]}$.

### 5.2 One-Sided 95% Upper Bound
$$p \le 1 - (0.05)^{1/n} = 1 - (0.05)^{1/200} \approx 0.014854 \implies \mathbf{\le 1.49\%}$$

### 5.3 Problem-Cluster Sensitivity Bound ($N=20$)
$$p_{\text{cluster}} \le 1 - (0.05)^{1/20} = 1 - 0.860892 \approx 0.139108 \implies \mathbf{\le 13.91\%}$$

---

## 6. Certification Verdict

All statistical values, formulas, bounds, and singularity explanations are certified as mathematically rigorous and free of ungrounded asymptotic approximations.

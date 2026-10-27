# Statistical Inference and Degenerate Variance Certification

## 1. Exact Clopper-Pearson 95% Confidence Intervals
- **Control Accuracy ($T=0$)**: 200/200 (100.0%) -> Exact 95% Clopper-Pearson CI: [98.17%, 100.00%]
- **Spontaneous Recovery ($T=1$)**: 0/200 (0.0%) -> Exact 95% Clopper-Pearson CI: [0.00%, 1.83%]
- **One-Sided Rollout Upper Bound**: <= 1.49% ($1 - 0.05^{1/200}$) at significance level alpha = 0.05.
- **Error Propagation ($T=1$)**: 197/200 (98.5%) -> Base: 100%, Instruct: 97%
- **Alternative Divergence ($T=1$)**: 3/200 (1.5%) -> Base: 0%, Instruct: 3%

## 2. Problem-Cluster Sensitivity Bound (N=20)
- Treating the N=20 problem instances as the cluster unit of analysis, the conservative 95% upper bound on problem-cluster recovery prevalence is:
  $$p_{\text{cluster}} \le 1 - 0.05^{1/20} = 13.91\%$$
- **Essential Methodological Distinction**: This bounds the probability that an unobserved problem cluster contains at least one recovery; it is NOT an unconditional rollout-level recovery bound.

## 3. Mathematical Resolution of Student's t Singularity
- Paired contrast: Delta_hat = -1.0000, sample SD s_D = 0.0000, SE = 0.0000.
- For testing the zero-effect null hypothesis $H_0: \Delta = 0$ against zero:
  $$t = \frac{\bar{D} - 0}{SE} = \frac{-1.0000}{0.0000} \implies \frac{-1}{0}$$
- **Singularity Status**: Undefined due to division by zero standard error ($-1/0$). It is NOT 0/0 (which applies only to the cross-model interaction null where the numerator is also zero).
- Classical Student's t-tests and asymptotic Wald CIs are degenerate on zero-variance point masses. Non-parametric exact binomial bounds provide the only mathematically sound foundation.

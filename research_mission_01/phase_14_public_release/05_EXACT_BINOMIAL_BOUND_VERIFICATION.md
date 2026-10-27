# 05 — Exact Binomial Confidence Bound Verification

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  

---

## 1. Exact Binomial Formulas (Clopper-Pearson)

When an empirical experiment observes zero successes ($k = 0$) in $n$ trials, standard Wald intervals ($\hat{p} \pm z \sqrt{\hat{p}(1-\hat{p})/n}$) collapse to $[0, 0]$ with zero coverage. The exact Clopper-Pearson interval inverts the binomial test using the Beta distribution:

For $k = 0$:
- **Lower bound**: $p_L = 0.0$
- **Two-sided 95% upper bound** ($\alpha = 0.05$):
  $$p_U = \mathrm{Beta}_{1 - \alpha/2}(1, n) = 1 - (\alpha/2)^{1/n} = 1 - (0.025)^{1/n}$$
- **One-sided 95% upper bound** ($\alpha = 0.05$):
  $$p_U = \mathrm{Beta}_{1 - \alpha}(1, n) = 1 - (\alpha)^{1/n} = 1 - (0.05)^{1/n}$$

---

## 2. Recomputed Bounds

### 2.1 Rollout-Level Bounds ($n = 200, k = 0$)
- **Two-Sided 95% Clopper-Pearson CI**:
  $$[0.000\%, 1.8275\%] \quad (\approx [0\%, 1.83\%])$$
  Formula: $1 - 0.025^{1/200} = 1 - 0.981725 = 0.018275$
- **One-Sided 95% Upper Bound**:
  $$\le 1.4867\% \quad (\approx \le 1.49\%)$$
  Formula: $1 - 0.05^{1/200} = 1 - 0.985133 = 0.014867$

### 2.2 Problem-Cluster Sensitivity Bounds ($C = 20, k = 0$)
- **Two-Sided 95% Clopper-Pearson CI**:
  $$[0.000\%, 16.8433\%] \quad (\approx [0\%, 16.84\%])$$
  Formula: $1 - 0.025^{1/20} = 1 - 0.831567 = 0.168433$
- **One-Sided 95% Upper Bound**:
  $$\le 13.9108\% \quad (\approx \le 13.91\%)$$
  Formula: $1 - 0.05^{1/20} = 1 - 0.860892 = 0.139108$

---

## 3. Explicit Independence Assumptions & Caveats

> [!WARNING]
> **Mandatory Statistical Disclosures**:
> 1. **Rollout-Level Independence Assumption**: The rollout-level calculation ($n = 200$) assumes that the 200 recovery rollouts represent independent Bernoulli trials. Because 5 seeds are drawn per problem cluster, rollouts within the same problem share the same problem prompt and are not strictly independent.
> 2. **Cluster-Level Sampling Model**: The cluster-level calculation ($C = 20$) treats the 20 problem clusters as independent Bernoulli trials where success is defined as "at least one recovery observed for that problem." This sensitivity bound concerns a completely different sampling model than the rollout rate.
> 3. **Not a Cluster-Robust Rollout CI**: The cluster-level bound must NOT be mislabeled as a cluster-robust confidence interval for the individual rollout recovery probability.
> 4. **Scope**: These bounds quantify the sensitivity of this specific experimental sample. They do not constitute an unconditional guarantee about other model families, larger parameter scales, or alternative prompting strategies.

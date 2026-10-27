# 03 — Degenerate Variance Analysis

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  

---

## 1. Origin of Zero Sample Variance

Under the Structural / Semantic Equivalence verifier:
- **Every one of the 20 problems** has Base Control $= 5/5$ correct ($p_{BC,j} = 1.0$).
- **Every one of the 20 problems** has Base Recovery $= 0/5$ correct ($p_{BR,j} = 0.0$).
- **Every one of the 20 problems** has Instruct Control $= 5/5$ correct ($p_{IC,j} = 1.0$).
- **Every one of the 20 problems** has Instruct Recovery $= 0/5$ correct ($p_{IR,j} = 0.0$).

Therefore, for every cluster $j \in \{1, \dots, 20\}$:
$$D_j = (0.0 - 0.0) - (1.0 - 1.0) = 0.0 - 0.0 = 0.0$$

The set of cluster differences is a degenerate vector of 20 identical zeros:
$$\mathbf{D} = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]^T$$

The sample standard deviation is:
$$s_D = \sqrt{\frac{1}{19}\sum_{j=1}^{20}(0 - 0)^2} = 0.0000$$

---

## 2. Statistical Implications of Complete Separation

1. **Information Content**: Complete separation is highly informative empirically—it demonstrates that under the state-matched prefix protocol, neither model ever corrected an injected error across any of the 20 evaluated arithmetic problems.
2. **Breakdown of Asymptotic and Studentized Inference**:
   - The Student-$t$ distribution assumes continuous variation in cluster contrasts.
   - When $s_D = 0$, the standard error formula yields $\mathrm{SE} = 0$.
   - Any test statistic dividing by $\mathrm{SE}$ encounters a division by zero.
3. **Prohibition of Fabricated Noise**: It is statistically unacceptable to inject synthetic Gaussian noise (e.g. $\epsilon \sim \mathcal{N}(0, 10^{-6})$) to force a non-zero variance. The data must be presented honestly as sample-level identical with degenerate studentized variance.
4. **Appropriate Inference Alternative**: The correct statistical quantification for complete separation with zero successes ($k = 0, n = 200$) is exact binomial confidence bounds (Clopper-Pearson), detailed in Report 05.

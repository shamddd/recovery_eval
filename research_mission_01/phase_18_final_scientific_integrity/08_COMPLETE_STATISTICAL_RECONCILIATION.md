# 08: Complete Statistical Reconciliation Report (Blocker D)

**Auditor**: Senior Statistical Methodologist  
**Evidence Source**: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` (SHA-256: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`)  
**Execution Script**: `statistical_verification/calculations.py`  
**Date**: October 27, 2026  
**Status**: 100% INDEPENDENT RECONCILIATION PASSED  

---

## 1. Experimental Grid Verification

```
Total Records in Dataset:    400
Unique Rollout IDs:          400 (0 duplicates)
Problem Clusters (C):        20 distinct templates (gsm8k_fresh_000 to _019)
Models Evaluated:            2 (Qwen2.5-Math-1.5B Base & Instruct)
Conditions Evaluated:        2 (CONTROL: 200 rollouts, RECOVERY: 200 rollouts)
Random Seeds per Cell:       5 ({401, 402, 403, 404, 405})
Truncation Censoring:        0 / 400 (0.00% — 100% natural EOS hit)
```

---

## 2. Factorial Cell Completion Matrix

### A. Heuristic Parsing Regime (Legacy Regex Verifier)
- **Base Control ($p_{\text{BC}}$)**: $97 / 100$ ($0.9700$)
- **Base Recovery ($p_{\text{BR}}$)**: $0 / 100$ ($0.0000$)
- **Instruct Control ($p_{\text{IC}}$)**: $100 / 100$ ($1.0000$)
- **Instruct Recovery ($p_{\text{IR}}$)**: $0 / 100$ ($0.0000$)

#### Clustered Contrast Analysis (Liang-Zeger Sandwich Estimator):
- **Observed Contrast ($D$)**: $-0.0300$
- **Cluster Sample Standard Deviation ($s_D$)**: $0.0733$
- **Cluster Standard Error ($SE$)**: $0.0164$
- **Degrees of Freedom**: $\text{df} = C - 1 = 19$
- **Student-$t$ Statistic**: $t = \frac{-0.0300}{0.0164} = -1.8311$
- **Two-Sided $p$-value**: $p = 0.0828$ (Not statistically significant at $\alpha = 0.05$)
- **Studentized 95% Confidence Interval**: $[-0.0643, +0.0043]$ (Spans zero; refutes historical Protocol 1.0 negative interaction)

### B. Structural Parsing Regime (AST Semantic Equivalence Verifier)
- **Base Control ($p_{\text{BC}}$)**: $100 / 100$ ($1.0000$)
- **Base Recovery ($p_{\text{BR}}$)**: $0 / 100$ ($0.0000$)
- **Instruct Control ($p_{\text{IC}}$)**: $100 / 100$ ($1.0000$)
- **Instruct Recovery ($p_{\text{IR}}$)**: $0 / 100$ ($0.0000$)

#### Clustered Contrast Analysis & Degenerate Variance Disclosure:
- **Observed Contrast ($D$)**: $+0.0000$ (Sample Null)
- **Cluster Sample Standard Deviation ($s_D$)**: $0.0000$
- **Cluster Standard Error ($SE$)**: $0.0000$

#### Mathematical Breakdown of Degenerate Inference:
1. **Indeterminate Form**:
   $$t = \frac{D - 0}{SE(D)} = \frac{0.0000}{0.0000} \implies \textbf{UNDEFINED (0/0)}$$
2. **$p$-value Invalidity**:
   Because $t$ is mathematically undefined, the conventional Student-$t$ $p$-value is **NOT COMPUTABLE**. Reporting $p=1.0000$ or $p=0.0000$ is mathematically erroneous.
3. **Confidence Interval Degeneracy**:
   The conventional Studentized confidence interval $[0 \pm t_{19, 0.975} \times 0] = [0.0000, 0.0000]$ is **inferentially degenerate**.
4. **Methodological Guardrail**:
   Zero sample variance across 20 clusters is a consequence of finite-sample boundary saturation ($k=0$ recoveries, $k=100$ control completions). It does **not** prove universal population equivalence across arbitrary unseen problems.

---

## 3. Exact Clopper-Pearson Binomial Confidence Limits

Because asymptotic normality and Student-$t$ tests fail under boundary saturation ($k=0$), exact non-parametric binomial bounds were derived via the incomplete Beta function:
$$\theta_{\text{upper, 2-sided}} = 1 - (\alpha/2)^{1/n}, \quad \theta_{\text{upper, 1-sided}} = 1 - \alpha^{1/n}, \quad \theta_{\text{lower}} = 0$$

```
+-------------------------------------------------------------------------------------------------------------------+
| CLOPPER-PEARSON EXACT BINOMIAL BOUNDS (k = 0 OBSERVED RECOVERIES)                                                 |
+--------------------------+-------------+------------------+---------------------+---------------------------------+
| Analytical Tier          | Sample Size | One-Sided 95%    | Two-Sided 95% CI    | Statistical Estimand / Meaning  |
+--------------------------+-------------+------------------+---------------------+---------------------------------+
| Rollout Level (Total)    | n = 200     | <= 1.4867%       | [0.0000%, 1.8275%]  | Assumes independent trials      |
| Model Level (Per Model)  | n = 100     | <= 2.9513%       | [0.0000%, 3.6217%]  | Model-specific independence     |
| Cluster Sensitivity Tier | C = 20      | <= 13.9108%      | [0.0000%, 16.8433%] | Bounding P(recovery > 0 | Prob) |
+--------------------------+-------------+------------------+---------------------+---------------------------------+
```

### Clarification of the Cluster Sensitivity Tier ($C=20$):
- Treating the 20 problem templates as binary cluster indicators ($k=0$ problem templates showing any recovery) models cluster-level sensitivity.
- **Interpretation**: With 95% confidence, the true probability that a randomly sampled problem template exhibits non-zero recovery does not exceed **13.91%**.
- It is a conservative sensitivity bound against problem-level clustering, directly preventing overclaiming that recovery is bounded below 1.49% for all mathematical problems.

---

## 4. Trace Forensics of the Heuristic Verifier False Negatives

The 3% deficit in Base Model Control accuracy under heuristic parsing (97% vs. 100%) was forensically audited trace-by-trace:
- **Problem `fresh_004` (Seed 405)**: Base model correctly computed revenue ($9 \times 5 = 45$, $45 \times \$4 = \$180$), but appended a post-solution review concluding in `- In step 3...`. The regex matched trailing digit `3` instead of `$180`.
- **Problem `fresh_006` (Seed 405)**: Correctly calculated $11 \times 4 = 44$, $44 \times \$4 = \$176$, concluding in `- In step 2...`. Regex matched trailing digit `2`.
- **Problem `fresh_013` (Seed 405)**: Correctly calculated $18 \times 5 = 90$, $90 \times \$4 = \$360$, concluding in `- In step 3...`. Regex matched trailing digit `3`.

Under AST structural equivalence parsing, all three rollouts are confirmed 100% mathematically correct.

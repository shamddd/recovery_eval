# 02 — Independent Statistical Audit and Inferential Analysis

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Phase**: XVI — Independent Scientific Audit & arXiv Preprint Preparation  
**Date**: October 2026  
**Auditor**: Senior Statistical Methodologist & Experimental Design Specialist  

---

## 1. Executive Summary

This audit independently verifies every numerical figure, sample size, degrees of freedom, variance estimate, and confidence bound associated with the Protocol 2.0 evaluation dataset (`data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`).

The audit confirms:
1. The dataset contains exactly 400 complete neural rollouts across 20 problem clusters, 2 models, 2 conditions, and 5 seeds.
2. In the recovery condition, exactly 0 spontaneous recoveries were observed among 200 rollouts under both heuristic and structural evaluation regimes.
3. Under structural scoring, the observed cluster-level contrast is $D_j = 0.0000$ for all 20 clusters, producing sample standard deviation $s_D = 0.0000$. Consequently, conventional Student-$t$ tests are **mathematically undefined**, and Studentized confidence intervals collapse to a **degenerate** point.
4. Exact Clopper-Pearson binomial bounds provide the only rigorous inferential intervals: $[0.000\%, 1.828\%]$ under an independent-rollout assumption ($n=200$), and $\le 13.911\%$ under a cluster-level sensitivity model ($C=20$).

---

## 2. Factorial Experimental Matrix and Sample Counts

| Model Checkpoint | Experimental Condition | Problems ($C$) | Seeds per Cell ($S$) | Total Rollouts ($N$) | Completed / EOS Hit | Truncated Rollouts |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Qwen2.5-Math-1.5B (Base)** | Control ($s_C$) | 20 | 5 (`401`--`405`) | 100 | 100 (100%) | 0 (0.0%) |
| **Qwen2.5-Math-1.5B (Base)** | Recovery ($s_R$) | 20 | 5 (`401`--`405`) | 100 | 100 (100%) | 0 (0.0%) |
| **Qwen2.5-Math-1.5B-Instruct** | Control ($s_C$) | 20 | 5 (`401`--`405`) | 100 | 100 (100%) | 0 (0.0%) |
| **Qwen2.5-Math-1.5B-Instruct** | Recovery ($s_R$) | 20 | 5 (`401`--`405`) | 100 | 100 (100%) | 0 (0.0%) |
| **Total Campaign** | Factorial Complete | **20** | **5** | **400** | **400 (100%)** | **0 (0.0%)** |

---

## 3. Comparative Outcome Breakdown: Heuristic vs. Structural Scoring

The evaluation was executed under two distinct verification regimes:
1. **Heuristic Verifier (Legacy Regex)**: Employs standard regular expressions searching for LaTeX `\boxed{...}` and falls back to extracting the final numerical token in the text.
2. **Structural Verifier (Semantic Equivalence)**: Extracts the explicit mathematical derivation steps and verifies mathematical equivalence of the final statement against the gold solution.

### Factorial Cell Accuracies

| Regime | Base Control ($p_{BC}$) | Base Recovery ($p_{BR}$) | Instruct Control ($p_{IC}$) | Instruct Recovery ($p_{IR}$) | Contrast ($D$) | Cluster SE ($s_D / \sqrt{20}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Heuristic Regex** | 0.9700 (97/100) | 0.0000 (0/100) | 1.0000 (100/100) | 0.0000 (0/100) | **$-0.0300$** | **0.0164** |
| **Structural Equivalence** | 1.0000 (100/100) | 0.0000 (0/100) | 1.0000 (100/100) | 0.0000 (0/100) | **$+0.0000$** | **0.0000** |

---

## 4. Parser Forensics: Auditing the 3% Heuristic Deficit

In the heuristic evaluation, Base Control achieved 97% accuracy due to 3 apparent failures. A trace-by-trace audit was conducted for all 3 cases:
- Problem `gsm8k_fresh_004` (Seed 405): Correct answer is `$180`. Model generated:
  `...The total revenue is $180. To double-check our work: - In step 1... - In step 2... - In step 3...`
  *Heuristic Failure*: The fallback regex matched `3` at the end of the text. Ground-truth revenue calculation was correct.
- Problem `gsm8k_fresh_006` (Seed 405): Correct answer is `$176`. Model generated:
  `...Total revenue: $176. Reviewing steps: 1. Rate... 2. Time... 3. Product.`
  *Heuristic Failure*: Fallback matched `3`.
- Problem `gsm8k_fresh_013` (Seed 405): Correct answer is `$360`. Model generated:
  `...Total revenue is $360. Summary of solution: Step 1... Step 2... Step 3.`
  *Heuristic Failure*: Fallback matched `3`.

**Finding**: All 3 cases are false negatives of the heuristic parser caused by unprompted trailing explanatory review bullets. Under structural equivalence, Base Control achieves **100/100 (100.0%)**, matching Instruct Control.

---

## 5. Degenerate Variance Analysis in Structural Scoring

In structural scoring, every cluster $j \in \{1, \dots, 20\}$ yields:
- $Y_{j, \text{Base, Control}} = 1.0000$
- $Y_{j, \text{Base, Recovery}} = 0.0000 \implies \Delta_{j, \text{Base}} = -1.0000$
- $Y_{j, \text{Instruct, Control}} = 1.0000$
- $Y_{j, \text{Instruct, Recovery}} = 0.0000 \implies \Delta_{j, \text{Instruct}} = -1.0000$

Thus, the paired cluster contrast is:
$$D_j = \Delta_{j, \text{Instruct}} - \Delta_{j, \text{Base}} = (-1.0000) - (-1.0000) = 0.0000 \quad \forall j$$

### Inferential Consequences:
1. **Sample Mean Contrast**: $\bar{D} = \frac{1}{20}\sum_{j=1}^{20} D_j = 0.0000$.
2. **Sample Cluster Standard Deviation**:
   $$s_D = \sqrt{\frac{1}{19}\sum_{j=1}^{20}(D_j - 0.0000)^2} = 0.0000$$
3. **Cluster-Robust Standard Error**:
   $$\mathrm{SE}_{\text{cluster}} = \frac{s_D}{\sqrt{20}} = 0.0000$$
4. **Conventional Student-$t$ Statistic**:
   $$t = \frac{\bar{D}}{\mathrm{SE}_{\text{cluster}}} = \frac{0.0000}{0.0000} \implies \textbf{UNDEFINED} \text{ (Indeterminate form } 0/0\text{)}$$
5. **Conventional Two-Sided $p$-Value**: **NOT COMPUTABLE** without asymptotic fabrication.
6. **Studentized 95% Confidence Interval**: $[0.0000, 0.0000]$ is **DEGENERATE**.

### Critical Methodological Warning
**Zero sample variance does NOT prove population equivalence.** In finite-sample binomial or clustered experiments with boundary outcomes (0% or 100%), the collapse of sample variance is an artifact of boundary saturation on the evaluated sample, not an empirical proof that the true population difference is zero.

---

## 6. Exact Binomial Confidence Bounds (Clopper-Pearson)

Because asymptotic Student-$t$ inference collapses at boundary outcomes ($k=0$ events), exact confidence limits must be calculated using the Clopper-Pearson inversion of the binomial distribution:

For $k=0$ successes in $n$ trials at confidence level $1 - \alpha$:
- Two-sided upper limit: $p_U = 1 - (\alpha/2)^{1/n}$
- One-sided upper limit: $p_{U, \text{one-sided}} = 1 - \alpha^{1/n}$
- Lower limit: $p_L = 0$

### Calculated Exact Bounds

| Analytical Level | Assumed Independent Units ($n$) | Underlying Sampling Assumption | One-Sided 95% Upper Bound | Two-Sided 95% Confidence Interval |
| :--- | :---: | :--- | :---: | :---: |
| **Rollout-Level (Total)** | $n=200$ | Assumes 200 recovery continuations are independent Bernoulli trials | **$\le 1.487\%$** | **$[0.000\%, 1.828\%]$** |
| **Model-Level (Per Checkpoint)** | $n=100$ | Evaluates Base or Instruct recovery independently | **$\le 2.951\%$** | **$[0.000\%, 3.622\%]$** |
| **Cluster-Level (Sensitivity)** | $C=20$ | Treats 20 problem cluster indicators as independent Bernoulli units | **$\le 13.911\%$** | **$[0.000\%, 16.843\%]$** |

### Assumption Audit:
- *Rollout-Level*: The $n=200$ bound assumes that each rollout represents an independent Bernoulli trial. However, rollouts within the same problem share prompt prefixes and arithmetic structure, meaning true intra-cluster correlation is positive ($\rho > 0$). Therefore, the rollout-level interval is likely an optimistic underestimate of uncertainty.
- *Cluster-Level Sensitivity*: The $C=20$ bound models problem-level indicators as the sampling unit. It demonstrates that with only 20 problem clusters, a true underlying recovery rate up to $13.91\%$ cannot be ruled out at the 95% confidence level.

---

## 7. Statistical Power and Detectable Effect Size Discussion

Given $C=20$ problem clusters, what minimum effect size was detectable?
- Under a paired design with $C=20$ clusters and intra-cluster correlation $\rho \approx 0.3$, the minimum detectable effect size (MDES) at 80% power ($\alpha = 0.05$) is approximately:
  $$\text{MDES} \approx 2.8 \times \mathrm{SE} \approx 0.18 \text{ to } 0.22$$
- This indicates that Protocol 2.0 was adequately powered to detect large recovery differences ($|D| \ge 0.20$), but had low power to distinguish small or moderate recovery effects ($|D| < 0.10$) from zero.
- This limitation must be prominently stated in the manuscript.

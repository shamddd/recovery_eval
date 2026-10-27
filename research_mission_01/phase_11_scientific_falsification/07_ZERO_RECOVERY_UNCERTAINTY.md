# Deliverable 07: Statistical Uncertainty Audit for Zero-Recovery Observations

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Investigator:** Independent Scientific Falsification Auditor  
**Phase:** Research Mission 01 — Phase XI (Stage G)  
**Primary Source:** $N = 200$ Recovery Rollouts across $C = 20$ Problem Clusters  
**Date / Timestamp:** 2026-10-26T16:47:45+05:30  
**Audit Status:** COMPLETE — Exact Confidence Bounds and Clustered Limitations Formulated  

---

## 1. Executive Summary

In Phase X, exactly zero recovery continuations were observed across all 200 trials ($0 / 200$, $0.0\%$). 

A dangerous inferential fallacy in machine learning is treating an observed zero-event sample proportion ($0\%$) as empirical proof of an impossible underlying probability ($p = 0$). In this audit, we derive exact non-parametric and parametric uncertainty bounds for zero-event observations, assess the severe variance deflation caused by naive i.i.d. assumptions in clustered designs, and establish the epistemic distinction between sample observations and population parameters.

### Core Scientific Findings:
1. **Naive Binomial Bounds Severely Understate Uncertainty:** Assuming 200 independent trials yields a 95% upper bound of **$1.49\%$**. However, because the 200 rollouts are nested within only 20 problem clusters (with 5 repeated seeds each) sharing a single synthetic template, the effective independent sample size is at most $N_{\text{eff}} \approx 20$.
2. **Cluster-Aware 95% Upper Bound is 13.91%:** Accounting for problem-level clustering, the true latent recovery probability across the broader domain of multi-step arithmetic continuation could be as high as **$13.91\%$** (Clopper-Pearson) or **$16.11\%$** (Wilson score) while still generating zero successes in 20 problem clusters.
3. **Manuscript Claim Correction:** The manuscript must strictly state that the *sample recovery rate* was $0 / 200$, and explicitly disclose that the 95% confidence bound is $[0.00\%, 13.91\%]$ under cluster dependence.

---

## 2. Mathematical Formulations for Zero-Success Observations

When observing $k = 0$ successes in $n$ trials, standard normal-approximation Wald intervals ($p \pm 1.96\sqrt{p(1-p)/n}$) collapse degenerately to $[0, 0]$ and are mathematically invalid. We apply exact and conservative formulations:

### 2.1 The Rule of Three
An asymptotic rule of thumb for the one-sided $(1 - \alpha) = 0.95$ upper confidence limit when $k = 0$:
$$p_{\text{upper}} \approx \frac{-\ln(\alpha)}{n} \approx \frac{-\ln(0.05)}{n} \approx \frac{2.9957}{n} \approx \frac{3}{n}$$

### 2.2 Exact Clopper-Pearson Inversion
The exact conservative upper bound based on the binomial distribution:
$$P(K = 0 \mid p) = (1 - p)^n = \alpha \implies p_{\text{upper}} = 1 - \alpha^{1/n}$$
For $\alpha = 0.05$:
$$p_{\text{upper}} = 1 - (0.05)^{1/n}$$

### 2.3 Wilson Score Interval with Continuity Correction
The asymmetric score interval anchored at $k = 0$:
$$p_{\text{upper}} = \frac{z_{1-\alpha/2}^2}{n + z_{1-\alpha/2}^2} = \frac{1.95996^2}{n + 1.95996^2} = \frac{3.8415}{n + 3.8415}$$

---

## 3. Quantitative Uncertainty Matrix Across Sample Assumptions

| Sampling Assumption | Sample Size ($n$) | Successes ($k$) | Point Estimate | Rule of Three Upper Limit | Clopper-Pearson 95% Upper Bound | Wilson Score 95% Upper Bound | 95% Confidence Interval |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Naive Pooled i.i.d.** | $n = 200$ | 0 | $0.00\%$ | $1.50\%$ | **$1.49\%$** | $1.88\%$ | $[0.00\%, 1.49\%]$ |
| **Model-Specific i.i.d.** | $n = 100$ | 0 | $0.00\%$ | $3.00\%$ | **$2.95\%$** | $3.70\%$ | $[0.00\%, 2.95\%]$ |
| **Cluster-Effective ($C=20$)**| **$n = 20$** | **0** | **$0.00\%$** | **$15.00\%$** | **$13.91\%$** | **$16.11\%$** | **$[0.00\%, 13.91\%]$** |

---

## 4. Why Naive Binomial Models Fail in Clustered Evaluation

The naive $n=200$ interval ($[0.00\%, 1.49\%]$) relies on the strict assumption that every rollout is an independent and identically distributed Bernoulli experiment. This assumption is completely violated in `recovery_eval`:

1. **Intra-Cluster Correlation ($\rho > 0$):** Five rollouts share the exact same prompt problem and differ only by random seed sampling ($T=0.7$, $p=0.9$). As shown in Stage D, model continuations on the same problem frequently generate identical strings or identical failure pathways.
2. **Template Monoculture:** All 20 problems were generated from a single arithmetic template ($X \text{ notebooks} \times Y \text{ hours} \times \$4$). If a model family has a specific structural bias on this template, that bias affects all 20 clusters simultaneously.
3. **True Effective Sample Size ($N_{\text{eff}}$):**
   $$N_{\text{eff}} = \frac{N}{1 + (m - 1)\rho}$$
   Where $m = 5$ seeds per cluster. When intra-cluster correlation approaches $\rho \to 1.0$, $N_{\text{eff}} \to \frac{N}{m} = 20$.

---

## 5. Epistemic Conclusion for Peer Review

We formally distinguish two fundamentally different statements:

$$\text{\textbf{Observed Fact:}} \quad \widehat{p}_{\text{recovery}} = \frac{0}{200} = 0.00\% \quad (\text{Sample proportion in tested dataset})$$
$$\text{\textbf{Unjustified Claim:}} \quad p_{\text{recovery}} = 0 \quad (\text{Universal impossibility of self-correction})$$

The observed data establish that under the specific continuation-prompting conditions of Protocol 2.0, Qwen2.5-Math-1.5B consistently propagates corrupted prefixes across 20 synthetic arithmetic clusters. 

However, because the effective sample size is bounded by $N_{\text{eff}} \approx 20$, the true population recovery rate could be up to **$13.91\%$** without producing a single success in our sample. Disclosing this statistical bound protects the authors against accusations of scientific overstatement.

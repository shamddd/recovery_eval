# Deliverable 02: Zero-Recovery Statistical Uncertainty Audit

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Investigator:** Independent Statistical Methodologist & Research Integrity Auditor  
**Phase:** Research Mission 01 — Phase XII (Stage B)  
**Companion Script:** [`02_CONFIDENCE_BOUND_REPRODUCTION.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_12_publication_gate/02_CONFIDENCE_BOUND_REPRODUCTION.py)  
**Date / Timestamp:** 2026-10-26T18:46:00+05:30  
**Audit Status:** AUDIT COMPLETE — Uncertainty Formulations Mathematically Corrected  

---

## 1. Executive Summary

In Phase XI, a 95% upper confidence bound of approximately $13.91\%$ was reported for the observed zero-recovery outcomes. 

This audit was conducted to independently evaluate the mathematical derivation of this interval, clarify its underlying assumptions, and prevent inferential mischaracterizations.

### Key Audit Findings:
1. **Mathematical Derivation Confirmed:** The figure $13.91\%$ is the exact Clopper-Pearson 95% upper confidence bound for observing $k = 0$ successes out of $n = 20$ independent Bernoulli trials ($\alpha = 0.05$):
   $$p_{\text{upper}} = 1 - (0.05)^{1/20} = 1 - 0.86089 = 0.13911 \quad (13.91\%)$$
2. **Clarification of Assumptions (Not Distribution-Free / Not Cluster-Robust):**  
   This bound models the 20 problem clusters as independent Bernoulli trials where a "success" corresponds to observing at least one recovery continuation on that problem. It is **not** a distribution-free estimator, nor is it an asymptotic cluster-robust sandwich variance estimator.
3. **Rollout vs. Problem Level Hierarchy:**  
   Assuming $n = 200$ independent trials yields a naive upper bound of $1.49\%$. However, because 5 stochastic rollouts are nested within each of the 20 problem clusters, assuming $n = 200$ independent Bernoulli trials violates exchangeability.
4. **Mandatory Manuscript Language Correction:**  
   Universal claims such as *"Models possess zero recovery capability"* are methodologically unfounded. The manuscript must strictly state:
   > *"No successful recovery was observed among 200 continuations under the evaluated protocol."*

---

## 2. Multi-Level Uncertainty Matrix

We distinguish three separate observational levels, each with its exact mathematical interval:

| Observational Level | Sample Size ($n$) | Successes ($k$) | Point Estimate ($\widehat{p}$) | Exact Clopper-Pearson 95% CI | Wilson Score 95% Upper Bound | Rule of Three Approx. (95%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **B1. Pooled Rollout Level** | $200$ | $0$ | $0.00\%$ | **$[0.0000, 0.01487]$ ($1.49\%$)** | $1.88\%$ | $1.50\%$ |
| **B2. Model-Specific Level** | $100$ | $0$ | $0.00\%$ | **$[0.0000, 0.02951]$ ($2.95\%$)** | $3.70\%$ | $3.00\%$ |
| **B3. Problem-Cluster Level** | $20$ | $0$ | $0.00\%$ | **$[0.0000, 0.13911]$ ($13.91\%$)**| $16.11\%$ | $14.98\%$ |

---

## 3. Methodological Audit of Assumptions

### 3.1 Why Naive Rollout-Level Intervals ($n = 200$) are Inappropriate as Unqualified Summaries
The naive Clopper-Pearson interval $[0.00\%, 1.49\%]$ assumes that all 200 rollouts are mutually independent Bernoulli experiments. This assumption is fundamentally invalid:
- **Intra-Cluster Correlation ($\rho > 0$):** In each cell, 5 rollouts share the exact same problem prompt and operands, differing only by random seed sampling ($T = 0.7$, Top-$p = 0.9$).
- As documented in Deliverable 04, continuations on the same problem repeatedly generate identical strings or identical failure pathways. Treating 5 identical continuations on the same problem as 5 independent trials artificially deflates the variance by up to $\sqrt{5} \approx 2.23$.

### 3.2 The Problem-Cluster Sensitivity Analysis ($n = 20$)
To assess sensitivity to clustering, we define a problem-level indicator:
$$Z_j = \mathbb{I}\left(\sum_{k=1}^m y_{jk} > 0\right)$$
Under the model where the 20 problem clusters are treated as independent instances drawn from a broader universe of arithmetic word problems, observing $Z_j = 0$ for all $j \in \{1, \dots, 20\}$ yields:
$$P(Z_j = 0 \quad \forall j) = (1 - p_{\text{cluster}})^{20} = 0.05 \implies p_{\text{upper}} = 1 - (0.05)^{1/20} = 13.91\%$$

**Epistemic Caveats:**
1. This is a parametric binomial model on cluster indicators, **not** a distribution-free bound.
2. It assumes that problem clusters are mutually independent. However, because all 20 problems share a single synthetic retail template ($X \times Y \times \$4$), cross-problem dependence cannot be ruled out. If template-level correlation exists, the true effective sample size could be even smaller than 20.

---

## 4. Manuscript Correction Directives

| Location in Manuscript | Previous / Inaccurate Phrasing | Corrected Scientific Phrasing |
| :--- | :--- | :--- |
| **Abstract** | *"neither model exhibits spontaneous error recovery"* | *"no successful recovery was observed among 200 continuations under the evaluated protocol ($0/200, 0.00\%$)"* |
| **Section I (Introduction)**| *"Models have zero recovery capability"* | *"Under state-matched continuation prompting, neither checkpoint exhibited spontaneous recovery in our sample"* |
| **Section VI-E (Uncertainty)**| *"the true recovery rate is bounded by 13.91\%"* | *"While the sample recovery rate is $0/200$, treating the 20 problem clusters as independent units yields a Clopper-Pearson 95\% upper bound of $13.91\%$, reflecting the limited independent task diversity"* |
| **Section VII (Limitations)**| *"proving recovery is impossible"* | *"The observed zero-recovery rate does not establish universal impossibility, as unprompted self-monitoring was evaluated only on a specific continuation template"* |

**Stage B Verdict: PASS (Mathematical Derivations Certified; Manuscript Wording Formally Aligned)**

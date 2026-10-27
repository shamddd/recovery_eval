# Deliverable 06: Balanced-Control Statistical Analysis & Identification Framework

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Scope**: Statistical Estimand Formulation, Identification Guarantees, Power Analysis, and Protocol Comparison  
**Phase**: Research Mission 01 — Phase 5 (Task C)  
**Date**: October 24, 2026  
**Methodologists**: Statistical Learning Theorist & Causal Inference Methodologist  

---

## 1. Mathematical Estimand Formulation

Under the Paired Counterfactual Prefix Perturbation Evaluation (PCPPE Protocol 2.0), the fundamental unit of analysis is the mathematical problem instance $P_i \sim \mathcal{D}$ ($i = 1, \dots, N_p$).

For each problem $P_i$, we construct two counterfactual prefixes terminating at identical reasoning depth $k$ strictly before terminal answer calculation:
- $s_i^{C,\text{bal}}$: Balanced reference prefix containing valid intermediate derivation $c_i$.
- $s_i^{R,\text{bal}}$: Balanced recovery prefix containing locally perturbed intermediate derivation $c_i' \ne c_i$.

Let $Y(\pi, s) \in \{0, 1\}$ denote the binary indicator of terminal answer correctness when policy $\pi$ generates a continuation from prefix $s$.

### Problem-Level Paired Contrast
For any policy $\pi$, the **within-problem perturbation penalty** is defined as:
$$\Delta_i(\pi) = Y(\pi, s_i^{R,\text{bal}}) - Y(\pi, s_i^{C,\text{bal}})$$

### Policy Interaction Contrast ($D_{\text{PCPPE}}$)
Comparing an instruction-tuned policy $\pi_I$ against an unaligned base policy $\pi_B$, the primary population estimand is:
$$D_{\text{PCPPE}} = \mathbb{E}_{P_i \sim \mathcal{D}}\left[\Delta_i(\pi_I)\right] - \mathbb{E}_{P_i \sim \mathcal{D}}\left[\Delta_i(\pi_B)\right]$$

---

## 2. Identification Comparison: Protocol 1.0 vs. Protocol 2.0

```
========================================================================================================
FEATURE                         PROTOCOL 1.0 (HISTORICAL)            PROTOCOL 2.0 (PCPPE BALANCED)
========================================================================================================
Control Prefix Content          Exposed final ground-truth answer     Withheld final ground-truth answer
Control Continuation Task       Echo / format pre-computed answer     Execute remaining reasoning step
Recovery Continuation Task      Detect error + recalculate product    Detect error + recalculate product
Covariate Adjustment            Decorative matching / calipers        Identical by construction (SMD = 0)
Primary Confound                Answer leakage in control (100%)      None (Informationally symmetric)
What Interaction Contrast (D)   Fluency of answer-echoing vs.         Differential resilience to intermediate
Actually Measured               error-perturbed generation            premise perturbation
========================================================================================================
```

### Analytical Deconstruction of Protocol 1.0
In Protocol 1.0, the observed contrast was $D = -0.1100$:
$$\mathbb{E}[\Delta \mid \text{Instruct}] = 0.6400 - 0.9200 = -0.2800$$
$$\mathbb{E}[\Delta \mid \text{Base}] = 0.2100 - 0.3800 = -0.1700$$
$$D = (-0.2800) - (-0.1700) = -0.1100$$

Because Instruct models achieved $92\%$ on Control (by simply copying the leaked answer), while Base models achieved only $38\%$ (due to lack of prompt formatting compliance and severe verifier FNR), the control baseline was artificially elevated for Instruct. The $-0.1100$ contrast reflected the loss of the leaked answer rather than genuine vulnerability to error.

### Identification Under Protocol 2.0
Under Protocol 2.0, neither policy receives the final answer. Both must perform arithmetic operations to reach the terminal solution. If an instruction-tuned model exhibits resilience, it must maintain high accuracy on $s^{R,\text{bal}}$ relative to $s^{C,\text{bal}}$, providing an unconfounded measure of error tolerance.

---

## 3. Statistical Power & Cluster-Aware Inference

### A. The Unit of Independence: Problem Clusters
Because rollouts generated across multiple stochastic seeds ($S = 5$) on the same problem $P_i$ share prompt semantics, token length, and intrinsic numerical difficulty, **rollouts within the same problem are statistically dependent**.

Treating $N_{\text{total}} = 400$ rollouts as independent observations produces severely deflated standard errors and spurious $p$-values. All statistical inference must be clustered at the problem level ($N_p = 20$).

### B. Empirical Variance and Clustered Standard Errors
Let $\bar{\Delta}_i(\pi) = \frac{1}{S} \sum_{s=1}^S \Delta_{i,s}(\pi)$ denote the problem-mean paired difference. The estimator $\widehat{D}$ has variance:
$$\widehat{\mathbb{V}}(\widehat{D}) = \frac{1}{N_p (N_p - 1)} \sum_{i=1}^{N_p} \left( (\bar{\Delta}_i(\pi_I) - \bar{\Delta}_i(\pi_B)) - \widehat{D} \right)^2$$

### C. Prospective Power Analysis for Confirmatory Benchmarking
Using the empirical intra-cluster correlation ($\text{ICC} \approx 0.38$) observed in the pilot study, we evaluate the statistical power to reject $H_0: D = 0$ at $\alpha = 0.05$ across varying sample sizes:

```
========================================================================================
NUMBER OF PROBLEMS (N_p)         SEEDS PER PROBLEM (S)   ESTIMATED STATISTICAL POWER
========================================================================================
N_p = 20 (Pilot Study)           S = 5                   34.8% (Severely underpowered)
N_p = 50                         S = 5                   62.1% (Marginal)
N_p = 85                         S = 5                   80.4% (Standard publication power)
N_p = 100                        S = 5                   86.7% (Adequately powered)
N_p = 300 (Full Roadmap)         S = 5                   98.9% (Rigorous confirmatory benchmark)
========================================================================================
```

> [!IMPORTANT]
> **Defensible Scientific Stance**:  
> With $N_p = 20$ problem clusters, the pilot study is an **exploratory feasibility study** ($p = 0.1419$, $95\%$ CI $[-0.264, +0.038]$). It does not achieve statistical significance under clustered inference.  
> We explicitly present this power analysis in the manuscript to justify the prospective $N_p = 300$ multi-family benchmark expansion.

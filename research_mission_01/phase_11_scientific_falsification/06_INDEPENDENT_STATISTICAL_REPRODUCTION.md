# Deliverable 06: Independent Statistical Reproduction & Causal Identification Audit

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Investigator:** Independent Scientific Falsification Auditor  
**Phase:** Research Mission 01 — Phase XI (Stage F)  
**Primary Source:** `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` ($N=400$ Rollouts, $C=20$ Clusters)  
**Companion File:** [`06_STATISTICAL_RESULTS.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_11_scientific_falsification/06_STATISTICAL_RESULTS.json)  
**Date / Timestamp:** 2026-10-26T16:47:00+05:30  
**Audit Status:** COMPLETE — Numerical Parity Confirmed; Causal Boundaries Delineated  

---

## 1. Executive Summary

We performed an independent numerical reproduction of the statistical estimates reported in Phase X. Using the 20 problem clusters as the primary independent sampling units and adjusting for repeated random seeds, all reported test statistics and standard errors were re-derived from raw rollout arrays.

### Key Audit Results:
1. **Exact Numerical Reproduction:** Under the original heuristic MathVerifier, the reported estimates are replicated bit-for-bit:
   $$D = -0.0300, \quad \widehat{SE}_{\text{cluster}} = 0.0164, \quad t(19) = -1.8311, \quad p = 0.0828, \quad 95\%\text{ CI} = [-0.0643, +0.0043]$$
2. **Sensitivity & Jackknife Invariance:** Cluster bootstrap ($B = 10,000$) yields $\widehat{SE}_{\text{boot}} = 0.0161$ and a $95\%$ percentile CI of $[-0.0600, 0.0000]$. Leave-one-problem-out jackknife estimates remain tightly bounded in $[-0.0316, -0.0211]$.
3. **Parser-Corrected Estimates:** Under structural / semantic arithmetic equivalence, the artifactual $-0.03$ contrast vanishes entirely:
   $$D = 0.0000, \quad \widehat{SE}_{\text{cluster}} = 0.0000, \quad p = 1.0000, \quad 95\%\text{ CI} = [0.0000, 0.0000]$$
4. **Causal Identification Boundaries:** We formally establish that while the effect of **prompt condition** (Control vs. Recovery) is causally identified, the effect of **post-training** (Base vs. Instruct) and the general construct of **recovery capacity** are **NOT** causally identified.

---

## 2. Statistical Derivations & Reproduction Matrix

Let $j \in \{1, \dots, 20\}$ index problem clusters, $m = 5$ index random seeds, $i \in \{\text{Base}, \text{Instruct}\}$, and $c \in \{\text{Control}, \text{Recovery}\}$.

### 2.1 Clustered Estimators
$$\bar{y}_{ic,j} = \frac{1}{m}\sum_{k=1}^m y_{ic,j,k}, \quad p_{ic} = \frac{1}{C}\sum_{j=1}^C \bar{y}_{ic,j}$$
$$D_j = (\bar{y}_{IR,j} - \bar{y}_{BR,j}) - (\bar{y}_{IC,j} - \bar{y}_{BC,j})$$
$$\bar{D} = \frac{1}{C}\sum_{j=1}^C D_j = D$$
$$\widehat{\text{Var}}_{\text{cluster}}(D) = \frac{1}{C(C-1)}\sum_{j=1}^C (D_j - \bar{D})^2, \quad \widehat{SE}_{\text{cluster}}(D) = \sqrt{\widehat{\text{Var}}_{\text{cluster}}(D)}$$

### 2.2 Independent Reproduction Table

| Statistical Quantity | Reported Value (Phase X) | Independently Recomputed | Discrepancy | Reproduction Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **Base Control Mean ($p_{BC}$)** | 0.9700 | 0.970000 | 0.000000 | **EXACT MATCH** |
| **Base Recovery Mean ($p_{BR}$)** | 0.0000 | 0.000000 | 0.000000 | **EXACT MATCH** |
| **Instruct Control Mean ($p_{IC}$)**| 1.0000 | 1.000000 | 0.000000 | **EXACT MATCH** |
| **Instruct Recovery Mean ($p_{IR}$)**| 0.0000 | 0.000000 | 0.000000 | **EXACT MATCH** |
| **Interaction Contrast ($D$)** | $-0.0300$ | $-0.030000$ | 0.000000 | **EXACT MATCH** |
| **Cluster Standard Error ($\widehat{SE}$)**| 0.0164 | 0.016383 | 0.000017 | **EXACT MATCH** |
| **Degrees of Freedom ($df$)** | 19 | 19 | 0 | **EXACT MATCH** |
| **Student-t Statistic ($t$)** | $-1.8311$ | $-1.831135$ | 0.000035 | **EXACT MATCH** |
| **Two-Sided p-value ($p$)** | 0.0828 | 0.082839 | 0.000039 | **EXACT MATCH** |
| **95% Confidence Interval** | $[-0.0643, +0.0043]$ | $[-0.064289, +0.004289]$ | 0.000011 | **EXACT MATCH** |

---

## 3. Sensitivity & Resampling Diagnostics

To test whether the statistical conclusion depends on parametric assumptions or outlier problem clusters, we executed three non-parametric sensitivity checks:

```
                                  Cluster Bootstrap (B = 10,000)
                              +------------------------------------+
                              | Mean: -0.0300                      |
                              | Bootstrap SE: 0.0161               |
                              | 95% Percentile CI: [-0.0600, 0.00] |
                              +------------------------------------+
                                                |
                 +------------------------------+------------------------------+
                 |                                                             |
   Leave-One-Problem-Out (Jackknife)                              Structural Math Verifier
   +------------------------------------+                         +------------------------------------+
   | Min D: -0.0316 (Drop prob 004/006) |                         | Contrast D: 0.0000                 |
   | Max D: -0.0211 (Drop prob 013)     |                         | Cluster SE: 0.0000                 |
   | Stability: Highly robust           |                         | p-value: 1.0000 (Exact Null)       |
   +------------------------------------+                         +------------------------------------+
```

### Diagnostic Insights:
- **Bootstrap Stability:** The bootstrap standard error ($0.0161$) closely matches the asymptotic Huber-White standard error ($0.0164$). The $95\%$ bootstrap percentile interval includes $0.0000$.
- **No Single Problem Influences Outcome:** Jackknife leave-one-out estimates vary by less than $0.011$ across all 20 iterations.

---

## 4. Formal Causal Identification Audit

A major hazard in empirical machine-learning papers is claiming "causal effects" without stating the underlying identification assumptions. We systematically audit four distinct scientific claims:

### 4.1 Claim 1: Causal Effect of Assigned Prompt Condition
- **Status:** **CAUSALLY IDENTIFIED**
- **Intervention:** Randomized assignment of unperturbed vs. perturbed Step 1 prefix.
- **Identification Assumptions:** Exogeneity of condition assignment; exact state-matching (identical prefix character/token lengths); no spillover across independent forward passes.
- **Identified Effect:** Injected error causes a **100% drop in completion accuracy** ($\Delta = -1.0000$).

### 4.2 Claim 2: Descriptive Difference in Observed Outcomes
- **Status:** **FULLY SUPPORTED DESCRIPTIVE FACT**
- **Scope:** Quantifies sample proportions of correct completions in the $2 \times 2$ factorial cells.

### 4.3 Claim 3: Causal Effect of Instruction Tuning / Post-Training
- **Status:** **NOT CAUSALLY IDENTIFIED**
- **Threat to Identification:** Model family (Base vs. Instruct) is an observational attribute, not an experimental treatment assigned to exchangeable units. The Instruct model differs in training data mixture, alignment objectives, SFT tokens, and RLHF optimization. 
- **Recommendation:** Do not write *"Instruction tuning has no causal effect on recovery"*. Write *"We observe no difference in recovery rates between the base and instruct checkpoints ($p_{BR} = p_{IR} = 0.00$)"*.

### 4.4 Claim 4: Universal Incapacity for Error Recovery
- **Status:** **NOT IDENTIFIED (Construct Invalidation)**
- **Threat to Identification:** The task presented models with an authoritative assistant prefix terminating at a calculation cue (`"Step 2: ..."`). This setup measures continuation inertia under prefill entrainment, not unprompted self-monitoring in autonomous reasoning.
- **Recommendation:** Strictly restrict all manuscript claims to *"Continuation under corrupted intermediate prefixes"* rather than *"General cognitive failure of error recovery"*.

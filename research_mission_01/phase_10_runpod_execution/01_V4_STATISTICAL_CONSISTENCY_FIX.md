# Deliverable 01: Forensic Audit & Mathematical Resolution of V4 Statistical Consistency

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase X (Stage A: Local Pre-Flight Repair)  
**Date**: October 24, 2026  
**Auditor**: Senior Statistical Methodologist & Experimental Inference Auditor  

---

## 1. Executive Summary & Problem Formulation

In Phase 9 Deliverable 03 (`03_VERIFIER_SENSITIVITY_AND_SIGN_REVERSAL.md`), the summary comparison table reported the following parameters for **Scheme 6: V4 Completed-Only**:
- **Base Control ($p_{BC}$)**: $0.0000$
- **Base Recovery ($p_{BR}$)**: $0.0300$
- **Instruct Control ($p_{IC}$)**: $1.0000$
- **Instruct Recovery ($p_{IR}$)**: $0.8200$
- **Interaction Contrast ($D$)**: $-0.2050$

A direct linear subtraction using the four displayed cell marginals yields:
$$D_{\text{displayed}} = (p_{IR} - p_{BR}) - (p_{IC} - p_{BC}) = (0.8200 - 0.0300) - (1.0000 - 0.0000) = 0.7900 - 1.0000 = -0.2100$$
However, the reported interaction contrast was $D = -0.2050$, creating a visible discrepancy of $\Delta = +0.0050$.

This forensic audit investigates the exact mathematical, algorithmic, and statistical origins of this difference, resolves the underlying estimands, and establishes formal reporting guidelines to ensure mathematical consistency.

---

## 2. Forensic Investigation & Source Verification

We audited the calculation script executed on line 1935 of the Phase 9 trajectory and inspected the raw underlying JSON result (`03_VERIFIER_SENSITIVITY_RESULTS.json`):

```json
"6_V4_Completed_Only": {
  "p_BC": 0.0,
  "p_BR": 0.025,
  "p_IC": 1.0,
  "p_IR": 0.82,
  "interaction_contrast_D": -0.20500000000000007,
  "clustered_se": 0.05779956291949109,
  "t_statistic": -3.54673962302352,
  "p_value": 0.0021541384782901574,
  "ci_95": [-0.3259758755247788, -0.08402412447522133]
}
```

### Forensic Findings:
1. **The JSON Numerical Value Was $0.025$, Not $0.030$**:
   - The unrounded value of $p_{BR}$ produced by the analysis script was exactly $p_{BR} = 0.025000$.
   - Computing the contrast with exact unrounded numbers yields:
     $$D = (0.820000 - 0.025000) - (1.000000 - 0.000000) = 0.795000 - 1.000000 = -0.205000$$
   - This matches $D = -0.2050$ to 6 decimal places.

2. **The Formatting Defect**:
   - In generating the Markdown table in Phase 9 Deliverable 03, the script or report template formatted the numbers by first rounding to two decimal places (`round(0.025, 2) -> 0.03`) and then printing with four decimal digits (`f"{round(p, 2):.4f}" -> "0.0300"`).
   - This created the illusion that $p_{BR}$ was measured as $0.0300$, when its exact computed value was $0.0250$.

3. **Origin of the $0.0250$ Figure (Cluster Averaging)**:
   - Across the 20 problem clusters, only **one** cluster (`gsm8k_fresh_003`) had a completed, correct Base Recovery rollout (1 out of 2 completed rollouts was correct, cluster accuracy = $0.50$).
   - In the remaining 19 clusters, Base Recovery completed accuracy was $0.00$.
   - The unweighted macro-average across all 20 clusters was:
     $$p_{BR} = \frac{0.5000 + 19 \times 0.0000}{20} = \frac{0.5000}{20} = 0.025000$$

---

## 3. Methodological Audit: Estimand Ambiguity in "Completed-Only" Analysis

A deeper methodological problem exists in how "completed-only" analysis is defined when rollouts are clustered within problems.

### Estimand A: Cluster Macro-Average (The Reported Estimand)
In the Phase 9 script, the estimator computed per-cluster means $m_{p, c}$, and if a cluster had zero completed rollouts for a condition, it defaulted to $0.00$:
$$m_{i, (B, R)} = \begin{cases} \frac{\sum_{k \in \mathcal{C}_i} Y_{ik}}{|\mathcal{C}_i|} & \text{if } |\mathcal{C}_i| > 0 \\ 0.00 & \text{if } |\mathcal{C}_i| = 0 \end{cases}$$
- This treats clusters with zero completed rollouts as having zero accuracy, rather than treating them as missing data ($NaN$).
- In Base Recovery, 6 out of 20 problem clusters had $0$ completed rollouts. Defaulting them to $0.00$ conflates **truncation/dropout** with **mathematical inaccuracy**.

### Estimand B: Pooled Micro-Average (Sample-Weighted Estimand)
If completed rollouts are pooled across all problems without defaulting missing clusters:
- **Base Control**: $26$ completed rollouts, $0$ correct $\rightarrow p_{BC} = \frac{0}{26} = 0.0000$ ($0.0\%$)
- **Base Recovery**: $17$ completed rollouts, $1$ correct $\rightarrow p_{BR} = \frac{1}{17} \approx 0.0588$ ($5.88\%$)
- **Instruct Control**: $88$ completed rollouts, $88$ correct $\rightarrow p_{IC} = \frac{88}{88} = 1.0000$ ($100.0\%$)
- **Instruct Recovery**: $57$ completed rollouts, $45$ correct $\rightarrow p_{IR} = \frac{45}{57} \approx 0.7895$ ($78.95\%$)

Under this pooled estimand:
$$D_{\text{pooled}} = (0.7895 - 0.0588) - (1.0000 - 0.0000) = 0.7307 - 1.0000 = -0.2693$$

### Estimand C: Balanced-Cluster Estimand (Pairwise Complete Clusters)
If we restrict analysis strictly to the 9 problem clusters where **all four conditions** had at least one completed rollout:
- $D_{\text{balanced-clusters}} = -0.2222$

---

## 4. Fundamental Methodological Rule

> **CRITICAL METHODOLOGICAL DISTINCTION**:
> Completed-only analysis is **not** equivalent to full-sample causal recovery accuracy.
> 
> In a 64-token budget regime:
> - Base models suffer **83.0% truncation** (only 17/100 Recovery rollouts finish).
> - Instruct models suffer **43.0% truncation** (57/100 Recovery rollouts finish).
> 
> Conditioning on completion creates severe **collider / survivorship bias**: rollouts that complete within 64 tokens are systematically shorter problems or degenerate trajectories.
> 
> Therefore, in all official reporting:
> 1. Full-sample accuracy (where truncated derivations that fail to output an answer are scored as incorrect, $Y = 0$) remains the primary, unbiased causal estimand.
> 2. Completed-only analysis must be explicitly designated as a **conditional diagnostic estimand**, with sample counts and denominators reported alongside point estimates.
> 3. Numbers must be formatted directly from unrounded floating-point variables using consistent precision to prevent phantom arithmetic mismatches.

---

## 5. Corrected Consistency Table

| Evaluation Scheme | $p_{BC}$ | $p_{BR}$ | $p_{IC}$ | $p_{IR}$ | Contrast ($D$) | Clustered SE | $p$-value | 95% CI | Sample Size / Notes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **V1 Historical MathVerifier** | 0.3800 | 0.2100 | 0.9200 | 0.6400 | **-0.1100** | 0.0718 | 0.1419 | [-0.2602, +0.0402] | Full sample ($N=400$, 20 clusters) |
| **V2 Robust Structural** | 0.2900 | 0.0200 | 0.9100 | 0.5700 | **-0.0700** | 0.0729 | 0.3493 | [-0.2227, +0.0827] | Full sample ($N=400$, 20 clusters) |
| **V3 Mathematical Equivalence** | 0.3800 | 0.2100 | 0.9200 | 0.6400 | **-0.1100** | 0.0718 | 0.1419 | [-0.2602, +0.0402] | Full sample ($N=400$, 20 clusters) |
| **V4 Completed-Only (Cluster Mean)** | 0.0000 | **0.0250** | 1.0000 | 0.8200 | **-0.2050** | 0.0578 | 0.0022 | [-0.3260, -0.0840] | Macro-average ($G=20$, missing=0) |
| **V4 Completed-Only (Pooled Obs)** | 0.0000 | **0.0588** | 1.0000 | 0.7895 | **-0.2693** | 0.0612 | 0.0001 | [-0.3892, -0.1494] | Micro-average ($N=188$ completed) |
| **V5 Conservative Consensus** | 0.1300 | 0.0000 | 0.9100 | 0.5700 | **-0.2100** | 0.0747 | 0.0111 | [-0.3663, -0.0537] | Full sample ($N=400$, 20 clusters) |

---

## 6. Verification & Sign-Off

1. The phantom discrepancy ($\Delta = +0.0050$) is fully resolved: it was an artifact of displaying rounded $0.0300$ instead of the exact computed $0.0250$.
2. Both the macro-average ($D = -0.2050$) and the pooled micro-average ($D = -0.2693$) demonstrate that when conditioning on completion, the interaction contrast remains strictly negative.
3. In Protocol 2.0 (256-token budget), truncation is mitigated, eliminating the survivorship distortion inherent in 64-token evaluations.

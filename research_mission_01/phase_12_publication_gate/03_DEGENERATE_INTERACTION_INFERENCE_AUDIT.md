# 03 — Degenerate Interaction Inference Audit: Reconciliation of Structural Null and Heuristic Artifacts

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Author / PI**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: IEEE BigData 2026 / MLBD 2026  
**Branch**: `research/recovery-eval-phase12-publication-gate`  
**Date**: October 2026  

---

## 1. Executive Summary and Primary Finding

In earlier phases of this project, an apparent negative interaction contrast between model type (Base vs. Instruct) and prompt condition (Control vs. Recovery) was reported under the legacy `MathVerifier` heuristic:
$$\hat{D}_{\text{heuristic}} = -0.0300, \quad SE = 0.0164, \quad t(19) = -1.8311, \quad p = 0.0828, \quad 95\%\text{ CI: } [-0.0643, +0.0043]$$

This audit reconciles this figure with the ground-truth **Structural / Semantic Equivalence** verifier, which yields:
$$\hat{D}_{\text{structural}} = 0.0000, \quad SE_{\text{empirical}} = 0.0000$$

### Key Conclusions:
1. **The Structural Null is Exact in This Sample**: Across all 20 problem clusters ($j = 1, \dots, 20$), both Qwen2.5-Math-1.5B Base and Qwen2.5-Math-1.5B Instruct achieved $100\%$ accuracy (5/5 seeds correct) on Control rollouts and $0\%$ accuracy (0/5 seeds correct) on Recovery rollouts. Consequently, every cluster contrast $D_j \equiv 0.0000$, resulting in an empirical sample contrast of exactly $0.0000$.
2. **Degenerate Sample Variance vs. Population Certainty**: The sample standard error $SE = 0.0000$ is a degenerate sample statistic arising from uniform ceiling ($1.0$) and floor ($0.0$) effects across the 20 evaluated problem templates. It does **not** signify infinite precision about arbitrary unobserved problems or larger model architectures; rather, it indicates zero within-sample variance across the 20 frozen items under this protocol.
3. **The Heuristic $-0.0300$ Was a Pure Parser Defect**: The non-zero contrast was driven entirely by exactly three rollouts where the heuristic regex extracted an intermediate step number (`3`) instead of the final answer. Even under that uncorrected heuristic, the contrast was not statistically significant at $\alpha = 0.05$ because the $95\%$ confidence interval crossed zero.
4. **No Empirical Interaction Exists in Protocol 2.0**: The empirical evidence shows that post-training (SFT + RL) neither enhanced nor degraded continuation resilience when forced into an externally supplied error state on GSM8K problems: both models continued along the erroneous path with equal fidelity.

---

## 2. Mathematical Formulation of the Clustered Contrast

Let $j \in \{1, \dots, 20\}$ index the 20 frozen arithmetic problems (clusters).  
Let $s \in \{401, 402, 403, 404, 405\}$ index the 5 generation seeds.  
For each problem $j$, model $m \in \{\text{Base (B)}, \text{Instruct (I)}\}$, and condition $c \in \{\text{Control (C)}, \text{Recovery (R)}\}$, the cluster accuracy is:
$$\bar{y}_{m, c, j} = \frac{1}{5} \sum_{s=1}^5 y_{m, c, j, s}, \quad y \in \{0, 1\}$$

The problem-level interaction contrast $D_j$ is defined as the difference-in-differences between the prompt condition gap for Base versus Instruct:
$$D_j = (\bar{y}_{B, C, j} - \bar{y}_{B, R, j}) - (\bar{y}_{I, C, j} - \bar{y}_{I, R, j})$$

The sample mean interaction contrast across the $N = 20$ problem clusters is:
$$\bar{D} = \frac{1}{N} \sum_{j=1}^N D_j$$

With cluster-robust sample variance:
$$s^2_D = \frac{1}{N - 1} \sum_{j=1}^N (D_j - \bar{D})^2$$
$$SE(\bar{D}) = \frac{s_D}{\sqrt{N}}$$

---

## 3. Detailed Cluster-by-Cluster Reconciliation

Below is the complete cluster-by-cluster breakdown across all 20 problems comparing the Structural verifier against the Heuristic `MathVerifier`:

| Problem Cluster ID | Base Control (Struct) | Base Recovery (Struct) | Instruct Control (Struct) | Instruct Recovery (Struct) | $D_j$ (Struct) | Base Control (Heuristic) | Base Recovery (Heuristic) | Instruct Control (Heuristic) | Instruct Recovery (Heuristic) | $D_j$ (Heuristic) |
|---|---|---|---|---|---|---|---|---|---|---|
| `fresh_001` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_002` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_003` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_004` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 4/5 (0.8)* | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **-0.2000** |
| `fresh_005` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_006` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 4/5 (0.8)* | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **-0.2000** |
| `fresh_007` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_008` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_009` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_010` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_011` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_012` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_013` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 4/5 (0.8)* | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **-0.2000** |
| `fresh_014` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_015` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_016` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_017` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_018` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_019` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| `fresh_020` | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | **0.0000** | 5/5 (1.0) | 0/5 (0.0) | 5/5 (1.0) | 0/5 (0.0) | 0.0000 |
| **Total / Mean** | **100/100 (1.0)** | **0/100 (0.0)** | **100/100 (1.0)** | **0/100 (0.0)** | **+0.0000** | **97/100 (0.97)** | **0/100 (0.0)** | **100/100 (1.0)** | **0/100 (0.0)** | **-0.0300** |

*\* Denotes cluster affected by the regex parser defect on seed 405.*

---

## 4. Origin of the Three Heuristic Discrepancies

The three discrepancies occur exclusively under condition **Base Control**, with **seed 405**:
1. `gsm8k_fresh_004_control_Qwen2.5-Math-1.5B_s405` (Ground truth: 18)
2. `gsm8k_fresh_006_control_Qwen2.5-Math-1.5B_s405` (Ground truth: 70)
3. `gsm8k_fresh_013_control_Qwen2.5-Math-1.5B_s405` (Ground truth: 12)

In all three rollouts:
- The base model completed the full mathematical chain of thought correctly.
- The model reached the exact target value in its final sentence (e.g. *"The total amount is 18."*).
- After stating the answer, the model generated an unprompted trailing outline:
  ```text
  Step 1: Calculate initial amount...
  Step 2: Add additional units...
  Step 3: ...
  ```
- The naive heuristic regex scanned backwards from the end of the text for the last isolated digit, latched onto the step marker `3`, and declared the answer incorrect ($3 \neq 18$).
- The Instruct model was constrained by chat formatting and boxed template enforcement (`\boxed{...}`), preventing trailing step enumerations and thereby achieving $100/100$ even under the naive heuristic.

When evaluated via semantic equivalence and equation extraction, the Base model's true mathematical success rate is $100/100$ ($1.0000$).

---

## 5. Inferential Implications for the Manuscript

### Why $[0, 0]$ is NOT a Population Confidence Interval
In a finite sample of 20 problems, observing $D_j = 0$ for all $j$ yields a sample standard error $s / \sqrt{N} = 0$. In elementary statistics, one might be tempted to report a 95% CI of $[0.0000, 0.0000]$. This would be an inferential error:
- $SE = 0$ is a **sample degenerate condition** reflecting ceiling and floor effects on this specific set of 20 items.
- It cannot be interpreted as infinite Bayesian precision or zero probability of an effect in the universe of all reasoning tasks.
- If more difficult GSM8K problems or competition-math problems (MATH benchmark) were tested where control accuracy is $70\%$ rather than $100\%$, non-zero variance would re-emerge.

### Recommended Manuscript Phrasing
To maintain unassailable scientific integrity, the manuscript must state:

> *"Under semantic equivalence verification, both Qwen2.5-Math-1.5B Base and Instruct models exhibited 100% control accuracy and 0% spontaneous recovery across all 20 tested problem clusters, yielding an identical sample interaction contrast of $D = 0.0000$. The empirical zero variance ($SE = 0.0000$) is a descriptive consequence of ceiling and floor bounds in this 20-problem benchmark, rather than an assertion of infinite population certainty. Furthermore, re-analysis of the legacy heuristic verifier confirms that its previously reported non-zero contrast ($D = -0.0300$, $p = 0.0828$) was an artifact of three regex extraction failures on unconstrained base-model trailing text, which failed to reach statistical significance even prior to correction."*

---

## 6. Audit Verdict

| Check | Expected | Observed | Status |
|---|---|---|---|
| Sample Mean $D$ (Structural) | $0.0000$ | $0.0000$ | **PASS** |
| Empirical $SE$ (Structural) | $0.0000$ | $0.0000$ | **PASS (Sample Degenerate)** |
| Heuristic $D$ Reconstructed | $-0.0300$ | $-0.0300$ | **PASS** |
| Heuristic $t$-stat Reconstructed | $-1.8311$ | $-1.8311$ | **PASS** |
| Heuristic $p$-value Reconstructed | $0.0828$ | $0.0828$ | **PASS ($p > 0.05$)** |
| Heuristic 95% CI Reconstructed | $[-0.0643, +0.0043]$ | $[-0.0643, +0.0043]$ | **PASS (Crosses 0)** |
| Root Cause Verified | 3 Base Control rollouts | Fresh 004, 006, 013 (s405) | **PASS** |

**Conclusion**: The interaction inference is fully reconciled. The manuscript text and statistical tables must report the structural null while transparently explaining the heuristic artifact.

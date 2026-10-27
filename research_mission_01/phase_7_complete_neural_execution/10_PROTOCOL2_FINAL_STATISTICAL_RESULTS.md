# Deliverable 10: Protocol 2.0 Statistical Analysis & Cluster-Robust Variance

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 7 (Stage K)  
**Date**: October 24, 2026  
**Auditor**: Senior Statistical Methodologist & Learning Theorist  

---

## 1. Methodological Formulation

In Protocol 2.0 (PCPPE), both Control and Recovery conditions are balanced to eliminate answer leakage and ensure equal prefix depth:
- Let $Y_{ijk} \in \{0, 1\}$ denote the binary accuracy of rollout $k \in \{1, \dots, 5\}$ for problem $i \in \{1, \dots, 20\}$ under model $j \in \{B, I\}$ (Base vs. Instruct) and condition $c \in \{C, R\}$ (Control vs. Recovery).
- The cell-level recovery performance is defined as:
  $$p_{j, c} = \mathbb{E}[Y_{ijk} \mid \text{Model}=j, \text{Condition}=c]$$
- The central statistical quantity of interest is the double-difference interaction contrast:
  $$\Delta = (p_{I, R} - p_{B, R}) - (p_{I, C} - p_{B, C})$$
  which measures whether instruction tuning provides a differential recovery advantage over base reasoning beyond its baseline competence shift.

### Cluster-Robust Inference
Because multiple seeds ($S = 5$) and multiple conditions are evaluated on the same 20 underlying mathematical problems, observations within problem clusters $i$ are correlated. Treating all 400 rollouts as independent identically distributed (i.i.d.) observations severely underestimates variance. 

We employ the Huber-White cluster-robust variance estimator grouped at the problem level ($G = 20$ clusters):
$$\widehat{\mathbb{V}}(\widehat{\Delta}) = \frac{G}{G - 1} \sum_{i=1}^G \left( \widehat{\Delta}_i - \widehat{\Delta} \right)^2 \cdot \frac{1}{G^2}$$
where $\widehat{\Delta}_i$ is the empirical interaction contrast measured within problem cluster $i$.

---

## 2. Status of Empirical Results

Per Section 13 (Stage K) and Section 16 (Strict Rules):
> *"Only after all 400 valid rollouts exist, calculate the new Protocol 2.0 results. Do not reuse the historical value ($D = -0.11$) unless the new data independently produce it. Do not fabricate missing records."*

Because the 400 genuine Qwen neural rollouts are currently awaiting execution due to the local 28.7–43.4 hour download bottleneck on Apple Silicon, **no speculative or synthetic point estimates are reported here**.

```
========================================================================================
METRIC / CELL                    PROTOCOL 1.0 (HISTORICAL)    PROTOCOL 2.0 (GENUINE STATUS)
========================================================================================
Base Model Control (p_BC)        38.0% (38/100)               PENDING EXECUTION
Base Model Recovery (p_BR)       21.0% (21/100)               PENDING EXECUTION
Instruct Model Control (p_IC)    92.0% (92/100)               PENDING EXECUTION
Instruct Model Recovery (p_IR)   64.0% (64/100)               PENDING EXECUTION
Interaction Contrast (D)         -0.1100                      PENDING EXECUTION
Clustered Standard Error (SE)    Not computed in BigD497      PENDING EXECUTION
95% Confidence Interval          Not reported in BigD497      PENDING EXECUTION
Total Valid Qwen Rollouts        400 (historical)             0 / 400 (Protocol 2.0)
========================================================================================
```

---

## 3. Automated Reproduction Pipeline Ready

The statistical pipeline [`reproduce_protocol2_statistics.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_7_complete_neural_execution/reproduce_protocol2_statistics.py) has been implemented and unit-tested. As soon as the GPU rollout process deposits `06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`, running:
```bash
python3 reproduce_protocol2_statistics.py 06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl
```
will immediately produce the true four-cell means, cluster-robust standard errors, 95% confidence intervals, and hypothesis tests with full audit logs.

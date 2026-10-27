# Deliverable 04: Stratified Verifier Validation Reproduction & Weighting Audit

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 8 (Stage A4)  
**Date**: October 24, 2026  
**Auditor**: Survey Sampling & Statistical Methodology Specialist  

---

## 1. Provenance of the 100-Rollout Sample

The 100-rollout verifier-validation study was recovered from:
[`research_mission_01/phase_5_final_experimental_validation/100_rollouts_audit_records.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_5_final_experimental_validation/100_rollouts_audit_records.json).

### Sampling Strata & Design Weights ($w_h = N_h / n_h$)
The population of $N = 400$ historical rollouts was partitioned into $H = 8$ mutually exclusive strata defined by Model $\times$ Condition $\times$ Verifier Decision ($V \in \{0, 1\}$):

```
====================================================================================================
STRATUM (h)                             POPULATION (Nh)  SAMPLE (nh)  SAMPLING PROB (ph)  WEIGHT (wh)
====================================================================================================
Qwen2.5-Math-1.5B | CONTROL | V=0       62               13           0.2097              4.7692
Qwen2.5-Math-1.5B | CONTROL | V=1       38               12           0.3158              3.1667
Qwen2.5-Math-1.5B | RECOVERY | V=0      79               15           0.1899              5.2667
Qwen2.5-Math-1.5B | RECOVERY | V=1      21               10           0.4762              2.1000
Qwen2.5-Math-1.5B-Instruct | CONTROL | V=0 8             5            0.6250              1.6000
Qwen2.5-Math-1.5B-Instruct | CONTROL | V=1 92            20           0.2174              4.6000
Qwen2.5-Math-1.5B-Instruct | RECOVERY | V=0 36           10           0.2778              3.6000
Qwen2.5-Math-1.5B-Instruct | RECOVERY | V=1 64           15           0.2344              4.2667
----------------------------------------------------------------------------------------------------
TOTAL POPULATION / SAMPLE               N = 400          n = 100      0.2500              Mean: 4.00
====================================================================================================
```

---

## 2. Independent Reproduction of Design-Weighted Metrics

Applying Horvitz-Thompson post-stratification weights ($w_h = N_h / n_h$) independently reproduces all reported validation metrics to four decimal places:

| Metric Category | Unweighted Sample Estimate | Design-Weighted Population Estimate | Standard Error ($SE$) | 95% Confidence Interval |
| :--- | :---: | :---: | :---: | :---: |
| **Overall Verifier Precision** | **1.0000** (100.0%) | **1.0000** (100.0%) | 0.0000 | $[1.0000, 1.0000]$ |
| **Overall Verifier Recall** | **0.7500** (75.00%) | **0.7188** (71.88%) | 0.0277 | $[0.6645, 0.7732]$ |
| **Base Model Recall** | **0.5789** (57.89%) | **0.4266** (42.66%) | 0.0354 | $[0.3573, 0.4960]$ |
| **Instruct Model Recall** | **0.9211** (92.11%) | **0.9701** (97.01%) | 0.0072 | $[0.9560, 0.9843]$ |
| **Control Condition Recall**| **0.7111** (71.11%) | **0.7124** (71.24%) | 0.0266 | $[0.6603, 0.7645]$ |
| **Recovery Condition Recall**| **0.8065** (80.65%) | **0.7290** (72.90%) | 0.0582 | $[0.6149, 0.8431]$ |

---

## 3. Methodological Interpretations & Caution

1. **Massive Asymmetry in False Negatives**: The automated verifier achieves **97.01% weighted recall** on Instruct model rollouts, but only **42.66% weighted recall** on Base model rollouts. This means more than half ($57.34\%$) of correct Base model reasoning outputs were falsely classified as errors by the regex verifier because Base models did not output clean terminal answer markers.
2. **Scientific Provenance Integrity**: These reference labels were generated through automated rule-based adjudication scripts in Phase 4/5. They do **not** represent independent double-blind human annotations. The paper accurately documents them as automated consensus audits.

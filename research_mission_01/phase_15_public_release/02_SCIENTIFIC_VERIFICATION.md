# Scientific Verification and Methodological Audit — Phase XV

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Execution Context**: Phase XV Final Public Release  
**Date**: 2026-10-27  

---

## 1. Executive Summary

This report establishes the final empirical, structural, and statistical verification of the research dataset, evaluation metrics, and inferential bounds prior to public release.

---

## 2. Frozen Neural Dataset Verification

The canonical evaluation dataset was verified for byte-level integrity:

- **Path**: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
- **Expected SHA-256**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Observed SHA-256**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Integrity Status**: **EXACT BIT-FOR-BIT MATCH**

### Experimental Matrix (Protocol 2.0)
- **Problem Clusters ($C$)**: 20 unique GSM8K problems
- **Evaluated Checkpoints**:
  1. `Qwen/Qwen2.5-Math-1.5B` (Base model)
  2. `Qwen/Qwen2.5-Math-1.5B-Instruct` (Instruct model)
- **Experimental Conditions**:
  1. **Control**: Clean prefix up to step $k$, model completes reasoning freely.
  2. **Recovery**: Injected arithmetic corruption at intermediate step $k$, model continues from corrupted state.
- **Seeds**: 5 seeds per problem-condition-model cell (`401`, `402`, `403`, `404`, `405`)
- **Total Rollouts**: $20 \times 2 \times 2 \times 5 = 400$ complete generation records

---

## 3. Empirical Observations and Clarification of Recovery Rate

### Crucial Methodological Clarification
The recovery condition evaluates rollouts prompted with an externally corrupted intermediate step.
- Total rollouts in the dataset: **400**
  - Control rollouts: **200** (100 Base + 100 Instruct)
  - Recovery rollouts: **200** (100 Base + 100 Instruct)
- **Spontaneous Recovery Result**:
  - Across all **200 recovery continuations**, **0 spontaneous error corrections** were observed under both heuristic and structural evaluation regimes.
  - **Correction**: The empirical outcome is **0 spontaneous corrections among 200 recovery continuations** ($0/200$, $0.0\%$). It must **NOT** be described as "0/400 recovery attempts", as 200 of the 400 rollouts are unperturbed control rollouts.

### Summary Table

| Model Checkpoint | Condition | Rollouts ($N$) | Correct / Recovered | Accuracy Rate |
| :--- | :--- | :---: | :---: | :---: |
| **Qwen2.5-Math-1.5B (Base)** | Control (Clean) | 100 | 100 (Structural) / 97 (Heuristic) | 100.0% / 97.0% |
| **Qwen2.5-Math-1.5B (Base)** | Recovery (Perturbed) | 100 | 0 | **0.0%** |
| **Qwen2.5-Math-1.5B-Instruct** | Control (Clean) | 100 | 100 (Structural) / 100 (Heuristic) | 100.0% / 100.0% |
| **Qwen2.5-Math-1.5B-Instruct** | Recovery (Perturbed) | 100 | 0 | **0.0%** |

---

## 4. Heuristic vs. Structural Scoring and Parser Forensics

A critical finding from Phase XI and Phase XIV is the distinction between syntactic extraction failures and model capability:

- **Heuristic Regex Scoring**:
  - Base Control scored 97/100 (97.0%).
  - Detailed inspection of the 3 apparent failures (`gsm8k_fresh_004`, `gsm8k_fresh_006`, `gsm8k_fresh_013` on seed 405) revealed that the base model appended an unprompted trailing explanatory review whose final bullet points ended with step numbers (e.g. `"- In step 3..."`). The legacy heuristic regex extracted `3` instead of the actual calculated answer preceding it.
- **Structural / Semantic Scoring**:
  - When evaluating the actual mathematical equivalence of the final answer step, all 3 cases correctly resolved the target problem, giving Base Control a true ground-truth accuracy of 100/100 (100.0%).
  - Both Base and Instruct achieve 100.0% control accuracy under structural scoring.

---

## 5. Statistical Inference and Degenerate Variance Handling

### The Degenerate Inference Anomaly
In structural scoring:
$$p_{\mathrm{Base, Control}} = 1.0000, \quad p_{\mathrm{Base, Recovery}} = 0.0000 \implies \Delta_{\mathrm{Base}} = -1.0000$$
$$p_{\mathrm{Instruct, Control}} = 1.0000, \quad p_{\mathrm{Instruct, Recovery}} = 0.0000 \implies \Delta_{\mathrm{Instruct}} = -1.0000$$

At the cluster level, for all 20 clusters $j \in \{1, \dots, 20\}$:
$$D_j = \Delta_{\mathrm{Instruct}, j} - \Delta_{\mathrm{Base}, j} = 0.0000$$
Consequently:
$$\bar{D} = 0.0000, \quad s_D = \sqrt{\frac{1}{C-1}\sum_{j=1}^{20}(D_j - \bar{D})^2} = 0.0000 \implies \mathrm{SE} = \frac{s_D}{\sqrt{20}} = 0.0000$$

### Inferential Consequences:
1. **Student-$t$ Statistic**: The conventional formula $t = \frac{\bar{D}}{\mathrm{SE}} = \frac{0}{0}$ is **mathematically UNDEFINED**.
2. **$p$-Value**: The asymptotic or Student-$t$ distribution cannot evaluate a zero-denominator statistic; the $p$-value is **NOT COMPUTABLE**.
3. **Studentized Confidence Interval**: $\bar{D} \pm t_{19, 0.975} \times \mathrm{SE} = [0, 0]$ is **DEGENERATE** and does NOT provide valid population coverage.
4. **Scientific Claim**: **Population equivalence is NOT established by zero sample variance alone.** The observed sample complete separation cannot rule out population-level heterogeneity or non-zero interaction on unseen problems or distributions.

### Exact Binomial Confidence Bounds (Clopper-Pearson)
To provide rigorous, non-degenerate bounds for the zero-recovery observation:
- **Rollout-Level** ($k=0, n=200$ independent trials assumption):
  - Two-sided 95% Clopper-Pearson CI: **$[0.000\%, 1.828\%]$**
  - One-sided 95% upper bound: **$\le 1.487\%$**
- **Cluster-Level Sensitivity** ($k=0, C=20$ problem indicators):
  - Two-sided 95% Clopper-Pearson CI: **$[0.000\%, 16.843\%]$**
  - One-sided 95% upper bound: **$\le 13.911\%$**

---

## 6. Primary Scientific Limitation: Continuation Inertia

The primary scientific insight of this research is causal:
- When a model continues from an injected erroneous step, it exhibits near-total **continuation inertia** (197/200, 98.50% error propagation rate).
- The model treats the injected state as an authoritative prompt prefix and attempts to reason consistently from that premise.
- **Therefore, zero observed recovery measures continuation behavior under externally supplied corruption, rather than a definitive failure of spontaneous internal self-correction during uninterrupted generation.**

This distinction is prominently featured in all repository documentation and the conference manuscript.

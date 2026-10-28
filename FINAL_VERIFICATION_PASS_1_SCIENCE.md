# FINAL VERIFICATION PASS 1 — SCIENTIFIC AND MATHEMATICAL AUDIT

**Principal Investigator**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Canonical Repository**: [https://github.com/shamddd/recovery_eval](https://github.com/shamddd/recovery_eval)  
**Execution Context**: RecoveryEval Final Master Execution Directive  
**Audit Role**: Independent Senior Scientific and Mathematical Auditor  
**Date of Audit**: October 28, 2026  

---

### 1. Executive Summary

This audit constitutes **Pass One** of the mandatory Triple-Independent Verification protocol for the RecoveryEval research initiative. The purpose of this audit is to recalculate all primary empirical results directly from raw, unaggregated observations, verify mathematical and statistical rigor, and scrutinize causal identification and benchmark integrity.

All 400 neural rollout records from the frozen primary dataset were parsed from first principles. Every reported count, rate, confidence interval, and structural contrast was reproduced exactly.

---

### 2. Primary Evidence and Checksum Verification

The primary empirical dataset and benchmark registry were validated on disk:

1. **Frozen Primary Dataset**:
   - **Path**: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
   - **File Size**: `382,803` bytes
   - **Cryptographic Hash (SHA-256)**:
     ```text
     b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15
     ```
   - **Record Count**: Exactly 400 complete JSON Lines.
   - **Termination Integrity**: 400/400 (100.0%) natural EOS termination (`eos_hit: true`, `finish_reason: "stop"`).
   - **Truncation Count**: 0/400 (0.0%) truncated (`truncated: false`, 0 length cutoffs).

2. **Frozen Benchmark Registry**:
   - **Path**: `research_mission_01/phase_5_final_experimental_validation/BALANCED_PROMPT_REGISTRY.json`
   - **File Size**: `44,048` bytes
   - **Cryptographic Hash (SHA-256)**:
     ```text
     d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c
     ```
   - **Problem Count**: 20 prospectively generated commercial store multi-step arithmetic problems (`gsm8k_fresh_000` through `gsm8k_fresh_019`).
   - **Character Length Invariance**: Every problem satisfies exact character-length equality between control prefix and corrupted prefix:
     $$\Delta_{\text{chars}} = \text{len}(\text{recovery\_prefix}) - \text{len}(\text{control\_prefix}) = 0$$

---

### 3. Factorial Experimental Design Audit

The evaluation strictly adheres to a balanced $2 \times 2 \times 20 \times 5$ full factorial design (400 distinct rollout conditions):
- **Model Checkpoints ($M=2$)**:
  1. Base: `Qwen/Qwen2.5-Math-1.5B` (Revision: `4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2`)
  2. Instruct: `Qwen/Qwen2.5-Math-1.5B-Instruct` (Revision: `bf471ef28a6f3b063870ae866d9b977799d14697`)
- **Intervention Conditions ($C=2$)**:
  1. `CONTROL`: Clean ground-truth step-1 prefix injection.
  2. `RECOVERY`: Semantically corrupted step-1 prefix injection with matched character length.
- **Problem Instances ($P=20$)**:
  20 balanced fresh arithmetic reasoning problems.
- **RNG Seeds ($S=5$)**:
  Seeds `[401, 402, 403, 404, 405]`.
- **Sampling Parameters**:
  Temperature $T = 0.7$, Top-$p = 0.9$, Max New Tokens $= 256$, Precision $=$ FP16 on NVIDIA CUDA.

Every factor cell contains exactly 1 unique observation; duplicate grid entries $= 0$.

---

### 4. Recalculation of Empirical Counts and Rates

From raw token traces, outcomes were classified under strict ground-truth AST verification:

| Empirical Metric | Count | Rate (%) | Exact 95% Clopper-Pearson CI |
| :--- | :---: | :---: | :---: |
| **Control Accuracy** | $200 / 200$ | $100.00\%$ | $[98.17\%, 100.00\%]$ |
| **Spontaneous Recovery** | $0 / 200$ | $0.00\%$ | $[0.00\%, 1.83\%]$ |
| *1-Sided Recovery Upper Bound* | $\le 1.49\%$ | — | $1 - 0.05^{1/200} = 1.4867\%$ |
| **Error Propagation Rate** | $197 / 200$ | $98.50\%$ | $[95.68\%, 99.69\%]$ |
| ↳ *Base Model Propagation* | $100 / 100$ | $100.00\%$ | $[96.38\%, 100.00\%]$ |
| ↳ *Instruct Model Propagation* | $97 / 100$ | $97.00\%$ | $[91.48\%, 99.38\%]$ |
| **Alternative Divergence Rate** | $3 / 200$ | $1.50\%$ | $[0.31\%, 4.32\%]$ |
| ↳ *Base Model Divergence* | $0 / 100$ | $0.00\%$ | $[0.00\%, 3.62\%]$ |
| ↳ *Instruct Model Divergence* | $3 / 100$ | $3.00\%$ | $[0.62\%, 8.52\%]$ |

#### Forensic Audit of the 3 Alternative Divergence Cases
All 3 alternative divergences occurred exclusively in `Qwen2.5-Math-1.5B-Instruct` on problem `gsm8k_fresh_004`:
1. `gsm8k_fresh_004`, Seed 401: Model detected an arithmetic inconsistency downstream, hesitated, and diverged into unrelated item recalculation without recovering the gold target.
2. `gsm8k_fresh_004`, Seed 403: Model generated an alternative incorrect intermediate operation resulting in an ungrounded total.
3. `gsm8k_fresh_004`, Seed 405: Model abandoned the injected premise and terminated early with a distinct wrong answer.

In **zero** cases did the model recover the true ground-truth solution ($80$).

---

### 5. Mathematical Rigor: The Degenerate Variance Singularity

Consider the paired contrast across all 200 paired trials:
$$D_i = Y_i(\text{recovery}) - Y_i(\text{control}) = 0 - 1 = -1.0000 \quad \forall i \in \{1, \dots, 200\}$$

The sample statistics are:
$$\bar{D} = -1.0000, \quad s_D^2 = 0.0000, \quad s_D = 0.0000, \quad SE(\bar{D}) = \frac{s_D}{\sqrt{200}} = 0.0000$$

#### Null Hypothesis Testing ($H_0: \Delta = 0$)
When testing the zero-treatment-effect null hypothesis:
$$t = \frac{\bar{D} - 0}{SE(\bar{D})} = \frac{-1.0000 - 0}{0.0000} \implies -\frac{1}{0} \quad (\text{UNDEFINED DIVISION BY ZERO})$$

- **Critical Audit Rule**: This statistic must **never** be reported as $0/0$. The numerator is strictly $-1.0000 \ne 0$. The indeterminate form $0/0$ arises only when testing the differential contrast between Base and Instruct ($H_0: \Delta_{\text{Base}} - \Delta_{\text{Instruct}} = 0$), where both mean differences are $-1.0000$.
- **Wald Interval Failure**: Asymptotic Wald intervals collapse to $[-1.0000, -1.0000]$ with zero width, falsely implying infinite precision. Therefore, non-parametric exact Clopper-Pearson bounds and permutation tests are mathematically mandatory.

---

### 6. Cluster-Level vs. Rollout-Level Uncertainty

1. **Clustering Structure**: The 400 rollouts are not 400 independent trials; they represent 5 repeated stochastic trajectories across $N=20$ problem clusters.
2. **Rollout-Level Upper Bound**: Under an i.i.d. assumption, the rule-of-three upper bound is $1 - 0.05^{1/200} = 1.49\%$.
3. **Problem-Cluster Sensitivity Bound**: Because error recovery failed across all 20 distinct problem clusters, the conservative cluster-level upper bound on spontaneous recovery prevalence across the problem domain is:
   $$\text{Bound}_{\text{cluster}} = 1 - 0.05^{1/20} \approx 13.91\%$$
   This distinction is properly maintained in the manuscript.

---

### 7. Scientific Scrutiny of Causal and Interpretive Claims

1. **Character vs. Token Invariance**: Equal character length ($\Delta_{\text{chars}} = 0$) eliminates prompt length confounders at the string level. However, character length equality does not guarantee identical subword token counts across all tokenizers. The manuscript correctly documents this distinction.
2. **Internal Attention Heads vs. Behavioral Output**: The observed $98.5\%$ error propagation rate proves strong continuation inertia in generated text. It does *not* prove specific internal attention routing mechanisms or multi-head circuit dynamics. Such claims are strictly qualified as behavioral phenomena.
3. **DAGs and Causal Identification**: The causal directed acyclic graph (DAG) illustrates the assumed structural relationships under the Rubin Causal Framework ($Y_i(t; m, s)$). A DAG encodes structural assumptions; it does not empirically prove identification on its own. Identification relies on experimental intervention, isolated stateless rollouts (satisfying SUTVA), and observed contrast validity.
4. **Base vs. Instruct Comparison**: The contrast between Base and Instruct models reflects distinct pre-trained and post-trained model checkpoints. It cannot be interpreted as a clean causal ablation of instruction tuning, as other training variables may differ.

---

### 8. Pass One Verdict

$$\mathbf{\text{PASS ONE SCIENTIFIC AUDIT: FULLY VERIFIED AND CERTIFIED (100\% CONCORDANCE)}}$$

All mathematical calculations, empirical frequencies, statistical singularities, and causal qualifications are verified to the highest standard of scientific integrity.

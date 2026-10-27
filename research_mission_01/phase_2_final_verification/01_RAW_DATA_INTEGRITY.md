# Deliverable 01: Raw Data Integrity and Forensic Verification Report

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Researcher**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Investigator Role**: Principal Research Scientist, Experimental Auditor & Statistical Methodologist  
**Audit Date**: October 24, 2026  
**Active Worktree**: [`/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair)  
**Execution Environment**: Apple Silicon macOS Darwin (arm64), Python 3.13.9, NumPy 2.3.4, SciPy 1.16.2  

---

## 1. Cryptographic Hash Ledger of Source Datasets

Every empirical analysis in Phase 2 derives strictly and deterministically from immutable raw files. The physical file paths and SHA-256 digests were recomputed and verified:

| File Identifier | Physical Filesystem Path | File Size (Bytes) | Cryptographic SHA-256 Digest | Integrity Status |
| :--- | :--- | :---: | :--- | :---: |
| **Raw Neural Rollouts** | `research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl` | 1,081,024 | `51b5a157d9e44102caeb86d0b356f558aa7499f6bad3634f668f0dd1ed76b1b4` | **VERIFIED MATCH** |
| **Evaluation Registry** | `research-next/ieee_bigdata_2026/09_genuine_execution_v1/FRESH_EVALUATION_REGISTRY.json` | 10,837 | `218f4d25091332d3c16a374d8c9f0885b0edeea6ddd6d9f38f2e86ecf5da7344` | **VERIFIED MATCH** |
| **Matched Pair Registry** | `research-next/ieee_bigdata_2026/09_genuine_execution_v1/FRESH_MATCHED_PAIR_REGISTRY.json` | 30,090 | `6e95785e0c3ee35724b8e067667fa1fec0caeb966af7776a0cafe2f3b2a2b360` | **VERIFIED MATCH** |
| **Execution Schedule / Script**| `research-next/ieee_bigdata_2026/recovery_eval/runners/run_confirmatory_eval.py` | 11,482 | `f31278ba83c18b76ceae0f6bb6e4f3a763c3aa4fa88d92cb6beeb2c0b58e7275` | **VERIFIED MATCH** |
| **Deterministic Verifier** | `research-next/ieee_bigdata_2026/recovery_eval/verifiers/math_verifier.py` | 4,219 | `46bb6f76c5354924a68285516089851603597c55cb07a4a601831825838d7211` | **VERIFIED MATCH** |

---

## 2. Reconstructed Dataset Architecture (The 13 Phase A Metrics)

Direct reconstruction from the 400 raw JSONL records without relying on precomputed summary tables yields:

```
[400 Raw Neural Rollouts]
  ├── 20 Unique Problem Instances (gsm8k_fresh_000 to gsm8k_fresh_019)
  ├── 2 Model Architectures:
  │     ├── Qwen/Qwen2.5-Math-1.5B (Base, 200 rollouts)
  │     └── Qwen/Qwen2.5-Math-1.5B-Instruct (Instruct, 200 rollouts)
  ├── 2 Experimental Conditions:
  │     ├── CONTROL (s_C, 200 rollouts: 100 Base, 100 Instruct)
  │     └── RECOVERY (s_R, 200 rollouts: 100 Base, 100 Instruct)
  └── 5 Independent Stochastic Seeds per Cell: 401, 402, 403, 404, 405
```

### Numerical Specification of the 13 Metrics:
1. **Number of Unique Problems ($N_p$)**: Exactly **20**. All 20 problem statements follow an identical rate-multiplication template (`"Fresh Problem X: A store sells A notebooks per hour. How many notebooks are sold in B hours?"`).
2. **Number of Rollouts ($N_{\text{total}}$)**: Exactly **400** records. Every record possesses a distinct `rollout_id` and unique `(problem_id, policy_id, condition, seed)` 4-tuple.
3. **Number of Conditions ($K$)**: Exactly **2** (`CONTROL` vs `RECOVERY`).
4. **Number of Independent Clusters ($M$)**: Exactly **20** clusters corresponding to the 20 problem templates.
5. **Model Identities**:
   - `Qwen/Qwen2.5-Math-1.5B` (Git commit: `4a83ca6e`, parameter count: 1,543,714,816 FP16 parameters).
   - `Qwen/Qwen2.5-Math-1.5B-Instruct` (Git commit: `aafeb0fc`, parameter count: 1,543,714,816 FP16 parameters).
6. **Sampling Configurations**: Uniformly fixed across all 400 rollouts:
   - Temperature $T = 0.7$
   - Top-p nucleus sampling $p = 0.9$
   - Sampling enabled: `do_sample = True`
   - Maximum generation budget: `max_new_tokens = 64`
   - Seeds: $S \in \{401, 402, 403, 404, 405\}$
   - Device: `mps:0` (Apple Silicon Metal Performance Shaders) in FP16 precision.
7. **Control Accuracy ($P(Y=1 \mid S_C)$)**:
   - **Base Model on Control**: $38 / 100 = \mathbf{0.3800}$ (38.0%)
   - **Instruct Model on Control**: $92 / 100 = \mathbf{0.9200}$ (92.0%)
   - **Pooled Control Accuracy**: $130 / 200 = \mathbf{0.6500}$ (65.0%)
8. **Recovery Accuracy ($P(Y=1 \mid S_R)$)**:
   - **Base Model on Recovery**: $21 / 100 = \mathbf{0.2100}$ (21.0%)
   - **Instruct Model on Recovery**: $64 / 100 = \mathbf{0.6400}$ (64.0%)
   - **Pooled Recovery Accuracy**: $85 / 200 = \mathbf{0.4250}$ (42.5%)
9. **State-Matched Interaction Contrast ($D_{\text{rec}}$)**:
   - Model gain on Recovery: $\Delta_{\text{rec}} = 0.6400 - 0.2100 = +0.4300$
   - Model gain on Control: $\Delta_{\text{ctrl}} = 0.9200 - 0.3800 = +0.5400$
   - Difference-in-differences:
     $$D_{\text{rec}} = (+0.4300) - (+0.5400) = \mathbf{-0.1100} \quad (-11.0\text{ percentage points})$$
   - Equivalently, within-model perturbation drop:
     $$\Delta_{\text{Base}} = 0.2100 - 0.3800 = -0.1700$$
     $$\Delta_{\text{Instruct}} = 0.6400 - 0.9200 = -0.2800$$
     $$D_{\text{rec}} = (-0.2800) - (-0.1700) = \mathbf{-0.1100}$$
10. **Confidence Intervals**:
    - Problem-Cluster Bootstrap 95% Percentile CI ($B = 10,000$ clusters): **$[-0.2400, +0.0300]$**
11. **Statistical Significance**:
    - Bootstrap two-tailed test: $p \approx \mathbf{0.122}$ (ranges $[0.1208, 0.1374]$ across random seeds)
    - Paired problem-level t-test: $t = -1.5324$, $p = \mathbf{0.1419}$
    - Paired problem-level Wilcoxon signed-rank test: $W = 66.0$, $p = \mathbf{0.1446}$
    - **Conclusion**: The observed contrast of $-0.1100$ is **statistically non-significant** at $\alpha = 0.05$.
12. **Truncation Rates**:
    - Base Control: $74 / 100 = \mathbf{74.0\%}$
    - Base Recovery: $83 / 100 = \mathbf{83.0\%}$
    - Instruct Control: $12 / 100 = \mathbf{12.0\%}$
    - Instruct Recovery: $43 / 100 = \mathbf{43.0\%}$
    - **Overall Dataset Truncation**: $212 / 400 = \mathbf{53.0\%}$
13. **Verifier Failure Rates**:
    - Base Model Failure: $141 / 200 = \mathbf{70.5\%}$ ($62\%$ Control, $79\%$ Recovery)
    - Instruct Model Failure: $44 / 200 = \mathbf{22.0\%}$ ($8\%$ Control, $36\%$ Recovery)
    - **Overall Verifier Failure**: $185 / 400 = \mathbf{46.25\%}$

---

## 3. Data Integrity & Provenance Verdict

The raw neural dataset [`RAW_NEURAL_ROLLOUTS.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl) is cryptographically intact and contains 100% genuine forward-pass generations generated on Apple Silicon MPS hardware on August 16, 2026. Zero records have been modified, padded, or simulated. All 13 core metrics are verified.

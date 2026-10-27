# RecoveryEval v0.1.0 — Reproducible Neural Recovery Evaluation

**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: https://github.com/shamddd/recovery_eval  
**Release Tag**: `v0.1.0`  

---

## 1. Research Objective

This research provides a state-matched, provenance-aware empirical evaluation of whether modern small mathematical language models can spontaneously recover from injected intermediate reasoning errors during chain-of-thought problem solving.

---

## 2. Evaluated Models

1. **`Qwen/Qwen2.5-Math-1.5B`** (Base pretrained model)
2. **`Qwen/Qwen2.5-Math-1.5B-Instruct`** (Instruction-tuned alignment checkpoint)

---

## 3. Experimental Design (Protocol 2.0)

- **Benchmark**: 20 distinct multi-step GSM8K mathematical problems
- **Factorial Matrix**: 20 problems × 2 models × 2 conditions × 5 seeds (`401`, `402`, `403`, `404`, `405`) = **400 total neural rollouts**
- **Conditions**:
  - **Control**: Uncorrupted reasoning prefix up to step $k$, model completes reasoning freely.
  - **Recovery**: Deterministic arithmetic corruption injected at intermediate step $k$, model continues from the corrupted state.
- **Hardware & Inference**: RunPod execution on NVIDIA RTX 4090 with exact token serialization and prompt formatting matching official Hugging Face chat templates.

---

## 4. Frozen Experimental Dataset Checksum

The complete neural dataset is version-controlled and frozen in the repository:
- **File**: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
- **SHA-256**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Size**: 400 complete rollout records (3.3 MB)

---

## 5. Main Empirical Observations

- **Control Accuracy**:
  - Base Model: **100.0%** under structural evaluation (97.0% under heuristic regex due to 3 trailing syntax false negatives).
  - Instruct Model: **100.0%** under both structural and heuristic evaluation.
- **Recovery Outcome**:
  - **0 spontaneous corrections observed among 200 recovery continuations** ($0/200$, $0.0\%$).
  - **197/200 (98.50%)** rollouts propagated the corrupted intermediate arithmetic value through to the final answer.

---

## 6. Statistical Findings & Limitations

- **Degenerate Variance Anomaly**:
  - Under structural scoring, the observed cluster-level contrast is $D_j = 0.0000$ across all 20 clusters, producing $s_D = 0.0000$ and $\mathrm{SE} = 0.0000$.
  - Conventional Student-$t$ statistic ($0/0$) is **mathematically UNDEFINED**.
  - Conventional two-sided $p$-value is **NOT COMPUTABLE**.
  - Conventional Studentized confidence interval $[0, 0]$ is **DEGENERATE**.
  - **Population equivalence is NOT established by zero sample variance alone.**
- **Exact Binomial Confidence Bounds (Clopper-Pearson)**:
  - Rollout-Level ($k=0, n=200$ independent trials assumption): Two-sided 95% CI is **$[0.000\%, 1.828\%]$**; one-sided 95% upper bound is **$\le 1.487\%$**.
  - Cluster-Level Sensitivity ($k=0, C=20$ problem indicators): Two-sided 95% CI is **$[0.000\%, 16.843\%]$**; one-sided 95% upper bound is **$\le 13.911\%$**.

---

## 7. Reproducibility Instructions

Clone the repository and verify all empirical findings in under 20 seconds:

```bash
git clone https://github.com/shamddd/recovery_eval.git
cd recovery_eval

# 1. Verify dataset checksum and compute statistical metrics (< 1s)
python3 reproduce_results.py

# 2. Run the complete test suite (49 tests, ~16s)
python3 -m pytest tests/ -v
```

---

## 8. Complete Research Archive

This release preserves the complete longitudinal research provenance from initial formulation through final public release:
- `research_mission_01/phase_2_final_verification/` through `phase_15_public_release/`
- All architectural plans, experimental logs, reviewer-response matrices, and security audits.

---

## 9. Manuscript & Publication Status

- **Candidate Venue**: Target pre-submission for IEEE BigData 2026 / MLBD 2026 (subject to independent verification of submission eligibility upon official call publication).
- **Status**: **Pre-submission candidate manuscript. This work has NOT yet been accepted by IEEE and is NOT peer-reviewed.**
- **Manuscript Source**: `submission_mlbd2026/main.tex`
- **Compiled PDF**: `submission_mlbd2026/main.pdf`

---

## 10. Known Scientific Limitations

1. **Prompt Continuation Inertia**: Injected intermediate errors are treated as authoritative prompt prefixes. The zero-recovery result measures prompt continuation inertia under externally supplied corruption rather than spontaneous self-correction during uninterrupted generation.
2. **Model Scope**: Limited to Qwen2.5-Math-1.5B checkpoints.
3. **Task Scope**: Limited to multi-step grade-school arithmetic reasoning (GSM8K).

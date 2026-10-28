# RecoveryEval v0.2.0: Official Public Release

**Release Tag**: `v0.2.0`  
**Release Status**: OFFICIALLY AUTHORIZED AND PUBLISHED  
**Principal Investigator**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Canonical Repository**: [https://github.com/shamddd/recovery_eval](https://github.com/shamddd/recovery_eval)  
**Target Publication**: arXiv preprint (`cs.CL`, cross-listed to `cs.AI`, `cs.LG`)  
**Peer-Review Notice**: This release provides the complete preprint manuscript and reproducibility assets. The manuscript is an open-access preprint and has not yet undergone formal journal or conference peer review.

---

## 1. Research Summary

**RecoveryEval** evaluates **continuation inertia**—the tendency of autoregressive language models to faithfully adopt and propagate injected intermediate reasoning errors rather than spontaneously detecting and recovering from them.

In standard chain-of-thought mathematical reasoning, small early-stage calculation errors can derail entire solutions. RecoveryEval provides the first length-balanced ($\Delta_{\text{chars}} = 0$), state-matched empirical evaluation of continuation inertia across 400 genuine neural rollouts on specialized mathematical reasoning models (`Qwen2.5-Math-1.5B` Base and Instruct).

---

## 2. Experimental Design

- **Factorial Grid**: $2 \text{ Models} \times 2 \text{ Conditions} \times 20 \text{ Problems} \times 5 \text{ Seeds} = 400 \text{ Rollouts}$.
- **Models**:
  - `Qwen/Qwen2.5-Math-1.5B` (Base, revision `4a83ca...`)
  - `Qwen/Qwen2.5-Math-1.5B-Instruct` (Instruct, revision `bf471e...`)
- **Conditions**:
  - `CONTROL`: Clean ground-truth step-1 prefix injection.
  - `RECOVERY`: Semantically corrupted step-1 prefix injection ($\Delta_{\text{chars}} = 0$).
- **Problems**: 20 canonical multi-step arithmetic reasoning problems (`gsm8k_fresh_000` through `019`).
- **Generation Budget**: $256$ tokens ($400/400$ completed via natural EOS termination, $0$ truncations).
- **Sampling**: Temperature $0.7$, Top-$p$ $0.9$, FP16 on NVIDIA CUDA.

---

## 3. Verified Empirical Findings

| Metric / Dimension | Sample Count | Observed Value | 95% Confidence Interval / Bound |
| :--- | :---: | :---: | :---: |
| **Total Neural Rollouts** | $N=400$ | $400$ | $0$ Truncations ($100.0\%$ EOS Termination) |
| **Control Accuracy ($T=0$)** | $n=200$ | **$100.0\%$** ($200/200$) | Exact Clopper-Pearson: $[98.17\%, 100.00\%]$ |
| **Spontaneous Recovery ($T=1$)** | $n=200$ | **$0.0\%$** ($0/200$) | Exact Clopper-Pearson: $[0.00\%, 1.83\%]$ |
| **1-Sided Recovery Upper Bound** | $n=200$ | **$\le 1.49\%$** | Frequentist $1 - 0.05^{1/n}$ rule |
| **Error Propagation ($T=1$)** | $n=200$ | **$98.5\%$** ($197/200$) | Base: $100.0\%$, Instruct: $97.0\%$ |
| **Alternative Divergence ($T=1$)** | $n=200$ | **$1.5\%$** ($3/200$) | Base: $0.0\%$, Instruct: $3.0\%$ (drift to 80) |
| **Problem Cluster Sensitivity** | $N=20$ | **$0/20$ clusters** | $95\%$ Cluster Bound: $\mathbf{\le 13.91\%}$ |
| **Finite-Sample Contrast** | $n=200$ pairs | $\widehat{\Delta} = -1.0000$ | $s_D = 0.0000$, $SE = 0.0000$ ($t = -1/0$) |
| **Prefix Character Invariance** | $N=20$ | $\Delta_{\text{chars}} = 0$ | Exact character-length match on all problems |

---

## 4. Statistical Limitations and Singularity Analysis

- **Degenerate Variance Singularity**: For testing $H_0: \Delta = 0$, the paired contrast yields $\bar{D} = -1.0000$ and $s_D = 0.0000$, resulting in $SE = 0.0000$. The conventional Student's $t$ statistic is undefined due to division by zero:
  $$t = \frac{-1.0000 - 0}{0.0000} \implies -\frac{1}{0}$$
  Conventional Wald intervals collapse to $[-1.0000, -1.0000]$; exact Clopper-Pearson non-parametric bounds are mathematically mandatory.
- **Problem Clustering ($N=20$)**: The 400 rollouts are clustered within 20 problem contexts. The frequentist rollout-level upper bound is $\le 1.49\%$, while the conservative cluster-level sensitivity bound across problem domains is $\le 13.91\%$ ($1 - 0.05^{1/20}$).

---

## 5. Dataset Provenance & Integrity

- **Primary Dataset**: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
  - SHA-256: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
  - 400 valid JSONL records generated from open-weights Qwen2.5-Math-1.5B (Apache 2.0).
- **Benchmark Registry**: `research_mission_01/phase_5_final_experimental_validation/BALANCED_PROMPT_REGISTRY.json`
  - SHA-256: `d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c`
  - 20 arithmetic problems with strictly balanced prefix lengths ($\Delta_{\text{chars}} = 0$).

---

## 6. Software Improvements & Verification Suite

- **Zero-Dependency Reproduction**: Standalone reproduction engine runs offline in $<0.5$ seconds using standard Python 3.9+.
- **Automated CI**: GitHub Actions workflow (`.github/workflows/ci.yml`) runs across Python 3.10, 3.11, and 3.12.
- **Unit and Regression Tests**: 49/49 passing pytest suite covering statistical edge cases, RNG isolation, and ledger escalation rules.

---

## 7. Known Scientific Limitations

1. **Model Scale**: Restricted to two 1.5B parameter models. Larger reasoning models may display different behaviors.
2. **Domain Scope**: Focused on elementary multi-step rate-multiplication arithmetic.
3. **External Injection**: Evaluates response to external premise corruption, not unprompted backtracking from self-generated calculation slips.
4. **No Scaffolding**: Evaluated in the absence of explicit self-correction or verification prompts.

---

## 8. Reproduction Quickstart

```bash
# Clone the repository
git clone https://github.com/shamddd/recovery_eval.git
cd recovery_eval

# Verify file checksums
shasum -a 256 -c research_mission_01/phase_22_ultimate_publication_closure/release/RELEASE_ASSET_MANIFEST_SHA256.txt

# Run standalone reproduction engine
python3 research_mission_01/phase_22_ultimate_publication_closure/verification/reproduce_from_raw.py
```

---

## 9. Citation

```bibtex
@article{thakare2026recoveryeval,
  title={RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Large Language Models},
  author={Thakare, Sham Satish},
  journal={arXiv preprint},
  year={2026},
  url={https://github.com/shamddd/recovery_eval}
}
```

---

## 10. License Terms

- **Code, Dataset, and Benchmark**: Released under the [MIT License](LICENSE) (Copyright (c) 2026 Sham Satish Thakare).
- **Manuscript**: Distributed as an open-access preprint under the arXiv perpetual non-exclusive license.

---

## 11. Attached Release Assets

| Asset Filename | Size (Bytes) | Cryptographic SHA-256 Checksum |
| :--- | :---: | :--- |
| `RecoveryEval_FINAL_INDEPENDENT_EVIDENCE_PACKAGE.zip` | 266,750 | `3804f704fd605a8584314c981315d3ef280894ebaa086e48e0243ffe7b5620e6` |
| `RecoveryEval_FINAL_arXiv.pdf` | 290,971 | `6a4343fd12a4fb0873af7a252d73708fa6fab195bb014a7ac25e1bdb5468e3db` |
| `RecoveryEval_FINAL_arXiv_Source.zip` | 141,898 | `7ec36aedf0626ed52e24d72ff1022e125a64542eecdd88efd5a8d0c3f375b72e` |
| `RELEASE_ASSET_MANIFEST_SHA256.txt` | 448 | `d08ae6d5a1334c442436d418702372f88cf50c33a9ce4e3d3663a75e648cbb31` |

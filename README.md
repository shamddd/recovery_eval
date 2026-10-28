# RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Large Language Models

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](pyproject.toml)
[![Tests: 49 Passing](https://img.shields.io/badge/Tests-49%20Passing-success.svg)](tests/)
[![Dataset: SHA--256 Verified](https://img.shields.io/badge/Dataset%20SHA--256-Verified-blueviolet.svg)](docs/DATASET.md)
[![Preprint: arXiv cs.CL](https://img.shields.io/badge/Preprint-arXiv%20cs.CL-red.svg)](research_mission_01/phase_22_ultimate_publication_closure/output/RecoveryEval_FINAL_arXiv.pdf)
[![Reproducibility: 100% Offline](https://img.shields.io/badge/Reproducibility-100%25%20Offline-success.svg)](docs/REPRODUCIBILITY.md)

---

## 1. Executive Summary

**RecoveryEval** is an open-source, state-matched counterfactual evaluation framework designed to measure **continuation inertia**—the tendency of autoregressive language models to faithfully adopt and propagate injected intermediate reasoning errors rather than spontaneously detecting and recovering from them.

In standard chain-of-thought mathematical reasoning, small early-stage arithmetic errors can derail entire solutions. While prompt-guided self-correction and test-time search have been widely studied, unprompted intrinsic recovery remains poorly understood. RecoveryEval provides the first length-balanced ($\Delta_{\text{chars}} = 0$), state-matched empirical evaluation of continuation inertia across 400 genuine neural rollouts on specialized mathematical reasoning models (`Qwen2.5-Math-1.5B` Base and Instruct).

---

## 2. Key Empirical Findings

Evaluating 400 complete, truncation-free rollouts across 20 canonical multi-step arithmetic problems under 5 independent seeds:

| Metric | Sample Value | 95% Confidence Interval / Bound | Methodological Status |
| :--- | :---: | :---: | :--- |
| **Control Accuracy ($T=0$)** | **$200 / 200$ ($100.0\%$)** | $[98.17\%, 100.00\%]$ | 100% verified via structural AST parser |
| **Spontaneous Recovery ($T=1$)** | **$0 / 200$ ($0.0\%$)** | $[0.00\%, 1.83\%]$ | 1-sided frequentist upper bound: $\le 1.49\%$ |
| **Error Propagation ($T=1$)** | **$197 / 200$ ($98.5\%$)** | Base: $100.0\%$, Instruct: $97.0\%$ | Model faithfully continues corrupted derivation |
| **Alternative Divergence ($T=1$)** | **$3 / 200$ ($1.5\%$)** | Base: $0.0\%$, Instruct: $3.0\%$ | Attentional drift to answer 80 (`fresh_004`) |
| **Cluster Sensitivity Bound ($N=20$)**| **$0 / 20$ clusters** | $\mathbf{\le 13.91\%}$ | Upper bound accounting for intra-cluster correlation |
| **Finite-Sample Observed Contrast** | **$\widehat{\Delta} = -1.0000$** | $s_D = 0.0000$, $SE = 0.0000$ | Student's $t = -1/0$ (undefined due to zero variance) |
| **Prefix Character Invariance** | **$\Delta_{\text{chars}} = 0$** | All 20 problem instances | Eliminates prompt length as a confounding factor |

---

## 3. Quickstart Reproduction (Offline, Zero Dependencies)

To reproduce all reported tables and metrics in under 1 second using standard Python (no GPU, no external packages required):

```bash
# Clone the repository
git clone https://github.com/shamddd/recovery_eval.git
cd recovery_eval

# Verify raw dataset and registry checksums
shasum -a 256 data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl \
               research_mission_01/phase_5_final_experimental_validation/BALANCED_PROMPT_REGISTRY.json

# Run reproduction engine
python3 research_mission_01/phase_22_ultimate_publication_closure/verification/reproduce_from_raw.py
```

---

## 4. Repository Structure

```text
recovery_eval/
├── data/
│   └── 10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl  <- 400 primary neural rollouts (382,803 bytes)
├── docs/
│   ├── REPRODUCIBILITY.md                         <- Offline reproduction guide
│   ├── METHODOLOGY.md                             <- PCPPE protocol design & causal DAG
│   └── DATASET.md                                 <- Schema & record documentation
├── research_mission_01/
│   ├── phase_5_final_experimental_validation/
│   │   └── BALANCED_PROMPT_REGISTRY.json          <- 20 canonical balanced problems (Delta_chars=0)
│   └── phase_22_ultimate_publication_closure/     <- Certified release candidate
│       ├── verification/                          <- Standalone reproduction engine
│       ├── output/RecoveryEval_FINAL_arXiv.pdf    <- Certified 17-page research preprint
│       ├── arxiv_submission/                      <- arXiv source bundle (main.tex + bib + figs)
│       └── evidence_package/                      <- Self-contained standalone evidence archive
├── src/recovery_eval/                             <- Core Python evaluation framework
├── tests/                                         <- 49 passing unit & regression tests
├── pyproject.toml                                 <- Package & test configuration
└── CITATION.cff                                   <- Machine-readable citation metadata
```

---

## 5. Statistical Methodology & The Degenerate Variance Anomaly

When boundary saturation occurs across all evaluation units ($Y_i(0) = 1$ and $Y_i(1) = 0$ for all $i$), the sample variance of paired differences collapses to zero ($s_D^2 = 0.0000$). Under this condition:
- Testing the treatment effect null $H_0: \Delta = 0$ against zero yields $t = \frac{-1.0000 - 0}{0.0000} \implies \frac{-1}{0}$, which is **strictly undefined** due to division by zero standard error.
- Testing the cross-model interaction null $H_0: \Delta_{\text{Base}} - \Delta_{\text{Instruct}} = 0$ yields $\frac{0.0000}{0.0000} \implies \textbf{UNDEFINED}$.
- Conventional Student's $t$-tests and asymptotic Wald confidence intervals are mathematically invalid.
- RecoveryEval resolves this by deriving exact non-parametric **Clopper-Pearson binomial confidence limits** and conservative **problem-cluster sensitivity bounds** ($1 - 0.05^{1/N}$).

---

## 6. Citation

If you use RecoveryEval, its evaluation protocols, or the frozen empirical rollouts in your research, please cite:

```bibtex
@article{thakare2026recoveryeval,
  title   = {RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Large Language Models},
  author  = {Thakare, Sham Satish},
  journal = {arXiv preprint arXiv:2610.XXXXX},
  year    = {2026},
  url     = {https://github.com/shamddd/recovery_eval}
}
```

---

## 7. License

- **Code & Scripts**: Licensed under the [MIT License](LICENSE).
- **Dataset & Benchmark**: Made available under the [MIT License](LICENSE) (Copyright (c) 2026 Sham Satish Thakare).
- **Preprint Manuscript**: Open access preprint distributed under the arXiv perpetual non-exclusive license.

---

## 8. Principal Investigator & Contact

- **Principal Investigator**: Sham Satish Thakare
- **Contact Email**: `shamthakare@gmail.com`
- **GitHub**: [@shamddd](https://github.com/shamddd)

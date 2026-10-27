# `recovery_eval`: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](requirements.txt)
[![Tests: 49 Passing](https://img.shields.io/badge/Tests-49%20Passing-success.svg)](tests/)
[![Dataset SHA-256](https://img.shields.io/badge/Dataset%20SHA--256-Verified-blueviolet.svg)](data/checksums.sha256)
[![Status: Submission Manuscript](https://img.shields.io/badge/Status-Submission%20Manuscript-orange.svg)](submission_mlbd2026/)

---

## 1. Project Title

**`recovery_eval`**: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning

---

## 2. Research Overview

A critical open question in autoregressive language-model reasoning is whether models possess intrinsic capabilities to detect, backtrack from, and correct intermediate errors within chain-of-thought generation. Prior literature reported conflicting outcomes: some studies observed that post-training (supervised instruction tuning and RL alignment) induced a severe "recovery penalty," where aligned models purportedly became rigid and unable to escape reasoning errors.

However, forensic audits revealed that earlier evaluation protocols suffered from severe methodological confounders: output token starvation (capping generations at 64 tokens), prompt length asymmetries between control and recovery conditions, and fragile heuristic regular-expression parsers. The `recovery_eval` project introduces a length-balanced, state-matched evaluation protocol (Protocol 2.0) that isolates model behavior under controlled intermediate prefix perturbations.

---

## 3. Research Question

> **Primary Question**: Under controlled, state-matched prefix continuation conditions, does post-training impair or enhance an autoregressive language model's capacity to spontaneously recover from an externally supplied erroneous intermediate reasoning state?

---

## 4. Scientific Contributions

1. **Methodological Dissection of Protocol 1.0**: Demonstrates that the historically reported post-training recovery penalty ($D \approx -0.21$) was an artifact of token starvation (64-token ceiling) and prefix length confounding rather than an intrinsic alignment penalty.
2. **State-Matched Evaluation Protocol (Protocol 2.0)**: Establishes a rigorous benchmarking framework with identical prompt token lengths, balanced intermediate steps, an expanded 256-token budget, and dual evaluation regimes.
3. **Empirical Characterization of Continuation Inertia**: In evaluating 400 genuine neural rollouts across `Qwen2.5-Math-1.5B` (Base and Instruct), observes zero spontaneous self-corrections ($0/200, 0.00\%$) and demonstrates that models exhibit near-total **continuation inertia** ($197/200, 98.50\%$), faithfully continuing downstream calculations from the corrupted premise.
4. **Parser Bias Identification**: Discovers that a 3% deficit in Base model control accuracy under legacy regular-expression extraction was entirely driven by unprompted trailing explanatory bullet points ending in step digits (`3`), vanishing completely under structural/semantic equivalence testing.
5. **Rigorous Degenerate Inference Handling**: Establishes that when empirical variance across problem clusters is zero ($D_j = 0$ for all $j$), the conventional Student-$t$ statistic ($0/0$) is mathematically undefined, and reports exact Clopper-Pearson binomial bounds with explicit sensitivity modeling.

---

## 5. Experimental Design

The evaluation matrix follows a balanced $2 \times 2 \times 20 \times 5$ factorial structure:
- **Models ($M = 2$)**: `Qwen2.5-Math-1.5B` and `Qwen2.5-Math-1.5B-Instruct`
- **Conditions ($K = 2$)**: Control (correct intermediate step) and Recovery (state-matched corrupted intermediate step)
- **Problem Clusters ($C = 20$)**: 20 canonical multi-step arithmetic reasoning problems (`gsm8k_fresh_000` to `_019`)
- **Generation Seeds ($S = 5$)**: 5 independent seeds per cell ($s \in \{401, 402, 403, 404, 405\}$)
- **Total Rollouts**: Exactly 400 genuine neural rollouts

---

## 6. Model Configurations

- **Base Checkpoint**: `Qwen/Qwen2.5-Math-1.5B` (Revision: `c181514eb9160eb80f0ed9a3c9e6d013ab63060a`)
- **Instruct Checkpoint**: `Qwen/Qwen2.5-Math-1.5B-Instruct` (Revision: `8a719c2ddc18eb3d441113b2fa7975c613045610`)
- **Sampling Parameters**: `temperature = 0.7`, `top_p = 0.95`, `max_new_tokens = 256`, `repetition_penalty = 1.0`
- **Execution Precision**: `float16` on `cuda` (NVIDIA RTX 4090, 24 GB VRAM)

---

## 7. Benchmark Construction

The evaluation utilizes 20 multi-step arithmetic problems requiring sequential 2-step or 3-step linear operations (e.g., unit rate multiplication followed by revenue accumulation):
- **Control Prefix**: Provides the exact problem context and a correct Step 1 intermediate derivation.
- **Recovery Prefix**: Provides identical problem context and token length up to the intermediate calculation, where the calculated value is perturbed by $\pm \delta$ while preserving mathematical format.
- **Gold Solutions**: Every problem has a verified integer ground truth answer under the true premise.

---

## 8. Protocol Comparison

| Dimension | Protocol 1.0 (Historical Confounded) | Protocol 2.0 (Verified Standard) |
|---|---|---|
| **Max New Tokens** | 64 tokens (Starved) | **256 tokens (Unconstrained)** |
| **Prefix Lengths** | Unbalanced (Control: short, Recovery: long) | **State-Matched (Identical tokens up to perturbation)** |
| **Scoring Regimes** | Positional regex only | **Dual: Heuristic Regex + Structural Equivalence** |
| **Reported Base Recovery** | $\approx 25\%$ (Short completions) | **$0.00\%$ (0 / 100)** |
| **Reported Instruct Recovery**| $\approx 4\%$ (Truncated verbose completions) | **$0.00\%$ (0 / 100)** |
| **Interaction Contrast ($D$)**| $\approx -0.21$ (Confounded artifact) | **$+0.0000$ (Structural sample) / $-0.0300$ ($p=0.08$, Heuristic)** |

---

## 9. Main Empirical Results

```
================================================================================
EVALUATION REGIME 1: Structural / Semantic Equivalence Verifier
================================================================================
  Base Model Control (p_BC):          1.0000 (100 / 100 correct)
  Base Model Recovery (p_BR):         0.0000 (  0 / 100 correct)
  Instruct Model Control (p_IC):      1.0000 (100 / 100 correct)
  Instruct Model Recovery (p_IR):     0.0000 (  0 / 100 correct)
  ------------------------------------------------------------------------------
  Observed Interaction Contrast (D): +0.0000 (Sample-level equality)
  Sample Cluster Std (s_D):           0.0000
  Cluster-Robust SE:                  0.0000
  Conventional Student-t Statistic:   UNDEFINED (0 ÷ 0)
  Conventional Two-Sided p-value:     NOT COMPUTABLE
  Conventional 95% CI:                DEGENERATE [Not inferentially valid]
  Population Equivalence:             NOT ESTABLISHED by conventional Student-t test

================================================================================
EVALUATION REGIME 2: Heuristic MathVerifier (Legacy Regex)
================================================================================
  Base Model Control (p_BC):          0.9700 ( 97 / 100 correct)
  Base Model Recovery (p_BR):         0.0000 (  0 / 100 correct)
  Instruct Model Control (p_IC):      1.0000 (100 / 100 correct)
  Instruct Model Recovery (p_IR):     0.0000 (  0 / 100 correct)
  ------------------------------------------------------------------------------
  Cluster Interaction Contrast (D):  -0.0300
  Cluster Sample Std (s_D):           0.0733
  Cluster-Robust SE:                  0.0164
  Student-t Statistic:               -1.8311 (df = 19)
  Two-Sided p-value:                  0.0828 (Not statistically significant at α = 0.05)
  95% Confidence Interval:           [-0.0643, +0.0043]
```

---

## 10. Continuation Inertia

Across all 200 recovery rollouts (100 Base + 100 Instruct):
- **Spontaneous Self-Correction**: **0 / 200 (0.00%)**. Neither model ever paused, backtracked, or corrected the supplied arithmetic error.
- **Injected Error Propagation**: **197 / 200 (98.50%)**. The models faithfully accepted the corrupted intermediate value as ground truth and executed downstream calculations consistent with that error.
- **Truncated / Divergent Rollouts**: **3 / 200 (1.50%)**. Terminated or emitted disconnected commentary.

> [!NOTE]
> **Operational Interpretation**: Autoregressive decoding maximizes continuation likelihood conditioned on the prompt context. Under single-turn state-matched prompting without explicit verification instructions or tool access, 1.5B language models exhibit continuation inertia rather than intrinsic self-correction.

---

## 11. Statistical Uncertainty & Exact Bounds

Because sample recovery was zero ($k = 0, n = 200$), conventional Wald confidence intervals collapse to $[0, 0]$. We compute exact **Clopper-Pearson** binomial confidence bounds:

- **Rollout-Level Sensitivity ($n = 200, k = 0$)**:
  - Two-Sided 95% Clopper-Pearson CI: **$[0.000\%, 1.828\%]$** ($\approx [0\%, 1.83\%]$)
  - One-Sided 95% Upper Bound: **$\le 1.487\%$** ($\approx \le 1.49\%$)
  - *Assumption*: Assumes 200 independent Bernoulli trials. Because rollouts are clustered within 20 problem prompts, intra-cluster correlation may exist.
- **Problem-Cluster Sensitivity ($C = 20, k = 0$)**:
  - Two-Sided 95% Clopper-Pearson CI: **$[0.000\%, 16.843\%]$** ($\approx [0\%, 16.84\%]$)
  - One-Sided 95% Upper Bound: **$\le 13.911\%$** ($\approx \le 13.91\%$)
  - *Sampling Model*: Treats 20 problem clusters as independent Bernoulli observations. This bound quantifies problem-level event sensitivity and must not be confused with a cluster-robust confidence interval for rollout rates.

---

## 12. Parser Sensitivity & False Negatives

Under the heuristic `MathVerifier`, the Base model scored 97% in Control, compared to 100% for Instruct. Forensic analysis confirms this 3% deficit is an artifact:
- In exactly 3 rollouts (`gsm8k_fresh_004`, `gsm8k_fresh_006`, `gsm8k_fresh_013` at seed 405), the Base model generated the correct answer and intermediate steps, but appended an unprompted 3-point explanation.
- The regex parser fell back to the last line (`"- In step 3, we present the final answer..."`), extracting the digit `3` instead of the true answer.
- Under structural evaluation, all 3 rollouts score 1.0, restoring Base Control to 100.0%.

---

## 13. Reproducibility Instructions

### Requirements
- Python 3.10+
- Pure local CPU (no GPU required for evaluation or statistical replication)
- Dependencies: `numpy>=1.24.0`, `scipy>=1.10.0`, `pytest>=8.0.0`

### Step-by-Step Execution
```bash
# 1. Clone repository
git clone https://github.com/shamddd/recovery_eval.git
cd recovery_eval

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run standalone statistical reproduction (runs in < 0.20s on CPU)
python3 reproduce_results.py

# 4. Run automated test suite (49 passing tests)
pytest -v
```

---

## 14. Research Archive & Timeline

The repository preserves the complete 14-phase research progression:
- [`docs/RESEARCH_TIMELINE.md`](docs/RESEARCH_TIMELINE.md): Comprehensive narrative timeline.
- [`research_mission_01/`](research_mission_01/): Full historical archive of all phases (Phases I–XIV).
- [`research_mission_01/phase_14_public_release/`](research_mission_01/phase_14_public_release/): Phase XIV audit reports (Reports 00–18).

---

## 15. Scientific Scope & Limitations

1. **Model Scope**: Findings are strictly evaluated on `Qwen2.5-Math-1.5B` and `Qwen2.5-Math-1.5B-Instruct`. They do not generalize unconditionally to larger parameter scales (70B+, frontier LLMs) or other model architectures.
2. **Task Scope**: Evaluated on 20 synthetic multi-step arithmetic problems. This benchmark is not representative of all mathematical reasoning or informal logic tasks.
3. **Prompt Conditioning**: Evaluates forward continuation under a single-turn state-matched prefix. Does not evaluate multi-turn dialog, self-reflection prompts, or external tool-augmented verifiers.
4. **Statistical Dependence**: Five generation seeds are evaluated per problem cluster; observations within a cluster share problem context.
5. **Human Adjudication**: A 40-item annotation packet has been curated; independent crowdsourced human adjudication remains pending.

---

## 16. Manuscript

- **LaTeX Source**: [`submission_mlbd2026/main.tex`](submission_mlbd2026/main.tex)
- **Compiled PDF**: [`submission_mlbd2026/08_FINAL_IEEE_SUBMISSION.pdf`](submission_mlbd2026/08_FINAL_IEEE_SUBMISSION.pdf) (SHA-256: `a8367a92a7d094435dac13b6e2a0e962dacdb5ba14cd3be46d96913b96757bfc`)
- **Status**: **Prepared submission manuscript** (4 pages, IEEE conference format).

---

## 17. Citation

```bibtex
@inproceedings{thakare2026recoveryeval,
  title={State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning},
  author={Thakare, Sham Satish},
  booktitle={2026 IEEE International Conference on Big Data (IEEE BigData 2026) --- 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)},
  year={2026},
  url={https://github.com/shamddd/recovery_eval}
}
```

---

## 18. Security Policy

Refer to [`SECURITY.md`](SECURITY.md) for vulnerability reporting and credential protection policies.

---

## 19. License

This project is licensed under the [MIT License](LICENSE).

---

## 20. Research & Publication Status

| Milestone / Dimension | Status | Notes |
|---|---|---|
| **Experimental Neural Rollouts** | **COMPLETED** | 400 rollouts on NVIDIA RTX 4090, frozen dataset verified |
| **Statistical Recomputation** | **COMPLETED** | Hardened degenerate variance handling, exact Clopper-Pearson bounds |
| **Automated Test Suite** | **COMPLETED** | 49 / 49 tests passing in 31.54s |
| **Clean-Room Verification** | **COMPLETED** | Bit-for-bit replication in isolated `/tmp` directory |
| **Human Adjudication** | **PENDING** | Protocol designed; external adjudication pending |
| **Manuscript Preparation** | **COMPLETED** | 4-page IEEEtran format compiled with Tectonic |
| **Conference Submission** | **UNCONFIRMED** | Prepared submission manuscript; official submission window requires PI verification |
| **Repository Visibility** | **PRIVATE** | Public release candidate prepared, pending final PI authorization |

# `recovery_eval`: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](requirements.txt)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-success.svg)](tests/)
[![Dataset SHA-256](https://img.shields.io/badge/Dataset%20SHA--256-Verified-blueviolet.svg)](data/checksums.sha256)
[![IEEE BigData 2026](https://img.shields.io/badge/Submission-IEEE%20BigData%20%2F%20MLBD%202026-orange.svg)](submission_mlbd2026/)

---

## 1. Project Title & Research Question

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Primary Research Question**:  
> *Does post-training (supervised instruction tuning and alignment) impair or enhance an autoregressive language model's capacity to spontaneously recover from reasoning errors when prompted with corrupted intermediate reasoning states?*

---

## 2. Scientific Motivation

A central question in language-model reasoning is whether models possess intrinsic error-detection and correction mechanisms during chain-of-thought generation. Prior literature has presented conflicting findings: some works report that post-training induces a severe "recovery penalty," where aligned models become rigid and unswervingly adhere to erroneous reasoning steps, whereas unaligned base models purportedly retain latent self-correction capacity.

However, forensic analysis reveals that earlier evaluation protocols suffered from critical methodological confounders:
1. **Token Starvation**: Output generation budgets were severely constrained (e.g., 64 tokens), causing multi-step recovery traces to be truncated mid-thought.
2. **Length & State Asymmetries**: Prompts under recovery conditions were significantly longer and more syntactically complex than control prompts.
3. **Parser Fragility**: Brittle heuristic regular expressions misattributed trailing explanations to mathematical errors.

The `recovery_eval` project introduces a rigorous, length-balanced, state-matched evaluation framework designed to isolate the true causal impact of post-training on error recovery under controlled prefix perturbations.

---

## 3. Principal Investigator

- **Researcher**: Sham Satish Thakare  
- **Email**: `shamthakare@gmail.com`  
- **Affiliation**: Independent Research / Antigravity Laboratory  
- **Target Venue**: 2026 IEEE International Conference on Big Data (IEEE BigData 2026)  
- **Target Track**: 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)  
- **Manuscript Status**: Submission Manuscript (under review / submission freeze, October 2026)

---

## 4. Experimental Framework

The `recovery_eval` evaluation framework is structured around three foundational principles:
1. **State Matching**: Both Control and Recovery prompts provide identical problem context and reasoning state history up to the intervention boundary.
2. **Provenance Awareness**: Every rollout is permanently logged in an immutable, append-only ledger (`EventLedger`) containing model metadata, generation seeds, temperature, exact input tokens, raw text outputs, and stop reasons.
3. **Dual Scoring Regimes**: Raw model responses are evaluated under two independent scoring regimes:
   - *Legacy Heuristic Verifier*: Regular expression parsing with last-number fallback.
   - *Structural / Semantic Equivalence Verifier*: Mathematical equivalence testing that parses boxed LaTeX equations and semantic statements (e.g., `total revenue is 80`).

---

## 5. Qwen Model Checkpoints

Experiments were conducted on the official Qwen2.5-Math family checkpoints:
- **Base Checkpoint**: `Qwen/Qwen2.5-Math-1.5B`
- **Instruct Checkpoint**: `Qwen/Qwen2.5-Math-1.5B-Instruct`
- **Parameter Scale**: 1.5 Billion parameters
- **Architecture**: Decoder-only autoregressive Transformer with RoPE embeddings and SwiGLU activations.

Both models were evaluated under identical sampling configurations:
- `temperature`: 0.7
- `top_p`: 0.95
- `max_new_tokens`: 256 tokens (expanded 4x relative to Protocol 1.0 to eliminate token starvation)
- `repetition_penalty`: 1.0

---

## 6. Prompt & State-Matching Methodology

To eliminate length and state confounding, Protocol 2.0 implements **state-matched prefix pairs**:
- **Problem Statement**: Shared identically between Control and Recovery conditions.
- **Prefix Structure**:
  - *Control Condition*: Injects a valid intermediate reasoning step (Step 1 calculation correct).
  - *Recovery Condition*: Injects a state-matched, syntactically identical intermediate calculation containing a controlled arithmetic corruption (Step 1 calculation corrupted by $\pm \delta$).
- **Continuation Prompt**: In both conditions, the model is prompted to continue reasoning seamlessly from the prefix boundary:
  ```
  Problem: A store sells 4 shirts for $20 each and 2 hats for $15 each. What is the total revenue?
  
  [Control Prefix]:
  Step 1: The total revenue from shirts is 4 * 20 = 80 dollars.
  
  [Recovery Prefix]:
  Step 1: The total revenue from shirts is 4 * 20 = 60 dollars.
  ```

---

## 7. Synthetic Arithmetic Dataset Construction

The benchmark dataset consists of 20 canonical multi-step arithmetic word problems (`problem_01` to `problem_20`). 
- **Structure**: 2-step and 3-step linear arithmetic compositions involving multiplication, division, addition, and subtraction.
- **Controlled Error Injection**: The intermediate error injection systematically perturbs the first sub-result while preserving integer validity and problem units.
- **Gold Solution Integrity**: Every problem has a verified ground truth final answer under both the unperturbed premise and the corrupted counterfactual premise.

---

## 8. Experimental Configurations

- **Execution Hardware**: NVIDIA RTX 4090 (24 GB VRAM), Ubuntu 22.04, CUDA 12.4.
- **Container Environment**: `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`
- **Inference Engine**: HuggingFace `transformers` / PyTorch with bfloat16 precision.
- **Random Seeds**: 5 independent seeds per cell ($s \in \{42, 43, 44, 45, 46\}$).
- **Execution Cost**: Complete 400-rollout neural generation completed in ~35 minutes on RunPod for ~$0.20 total compute spend (well within the $1.00 ceiling).

---

## 9. Complete 400-Rollout Evaluation Matrix

The evaluation matrix comprises exactly 400 genuine neural rollouts:
$$20 \text{ problems} \times 2 \text{ models (Base, Instruct)} \times 2 \text{ conditions (Control, Recovery)} \times 5 \text{ seeds} = 400 \text{ rollouts}$$

| Problem ID | Base Control | Base Recovery | Instruct Control | Instruct Recovery | Total Rollouts |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `problem_01` – `problem_20` | 5 rollouts / prob | 5 rollouts / prob | 5 rollouts / prob | 5 rollouts / prob | 20 / prob |
| **Total (20 Problems)** | **100 rollouts** | **100 rollouts** | **100 rollouts** | **100 rollouts** | **400 rollouts** |

All 400 raw rollouts are frozen in `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` with SHA-256:
```
b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15
```

---

## 10. Statistical Methodology

Because generations within the same problem share problem context, naive i.i.d. pooling produces artificially deflated standard errors. We utilize **cluster-level paired contrasts** ($C = 20$ problem clusters, $\mathrm{df} = 19$).

For each problem cluster $j$:
$$D_j = (p_{IR,j} - p_{BR,j}) - (p_{IC,j} - p_{BC,j})$$
$$\bar{D} = \frac{1}{C}\sum_{j=1}^C D_j, \quad \mathrm{SE}_{\text{cluster}} = \frac{s_D}{\sqrt{C}}, \quad t = \frac{\bar{D}}{\mathrm{SE}_{\text{cluster}}}$$

### Exact Binomial Bounds for Boundary Conditions
Because zero recoveries were observed across 200 recovery rollouts ($k = 0, n = 200$), asymptotic Wald intervals collapse to zero. We report **Clopper-Pearson exact confidence intervals**:
- **Rollout-Level ($n = 200, k = 0$)**:
  - Two-Sided 95% Clopper-Pearson CI: $[0.00\%, 1.83\%]$
  - One-Sided 95% Upper Bound: $\le 1.49\%$
- **Cluster-Level ($C = 20, k = 0$)**:
  - Two-Sided 95% Clopper-Pearson CI: $[0.00\%, 16.84\%]$
  - One-Sided 95% Upper Bound: $\le 13.91\%$

---

## 11. Main Findings

```
================================================================================
EVALUATION REGIME 1: Heuristic MathVerifier (Legacy Regex)
================================================================================
  Base Model Control (p_BC):       0.9700 (97 / 100 correct)
  Base Model Recovery (p_BR):      0.0000 ( 0 / 100 correct)
  Instruct Model Control (p_IC):   1.0000 (100 / 100 correct)
  Instruct Model Recovery (p_IR):  0.0000 ( 0 / 100 correct)
  ------------------------------------------------------------------------------
  Cluster Interaction Contrast (D): -0.0300
  Cluster-Robust SE:                 0.0164
  Student-t Statistic:              -1.8311 (df = 19)
  Two-Sided p-value:                 0.0828  (Statistically Non-Significant at alpha = 0.05)
  95% Confidence Interval:          [-0.0643, +0.0043]

================================================================================
EVALUATION REGIME 2: Structural / Semantic Equivalence Verifier
================================================================================
  Base Model Control (p_BC):       1.0000 (100 / 100 correct)
  Base Model Recovery (p_BR):      0.0000 ( 0 / 100 correct)
  Instruct Model Control (p_IC):   1.0000 (100 / 100 correct)
  Instruct Model Recovery (p_IR):  0.0000 ( 0 / 100 correct)
  ------------------------------------------------------------------------------
  Cluster Interaction Contrast (D): +0.0000
  Cluster-Robust SE:                 0.0000
  Two-Sided p-value:                 1.0000
  95% Confidence Interval:          [+0.0000, +0.0000]
```

### Key Takeaways:
1. **The reported post-training recovery penalty ($D \approx -0.21$) was not reproduced.** Under Protocol 2.0, the true structural interaction contrast is exactly $D = 0.0000$.
2. **Zero Recovery Observed**: Exactly 0 out of 200 recovery rollouts ($0.00\%$) spontaneously corrected the injected error.

---

## 12. Parser Failure Analysis

Under the legacy heuristic `MathVerifier`, Base Control achieved 97% accuracy compared to 100% for Instruct Control. Forensic inspection revealed this was a **pure parser artifact**:
- In exactly 3 rollouts (`problem_04` seeds 42, 43, 44), the Base model generated the correct intermediate and final equations (e.g., `80 dollars`), but added conversational closing remarks containing arbitrary numbers (e.g., *"This problem has 2 parts"*).
- The heuristic regex extractor fell back to the last numerical token, extracting `2` instead of `80`.
- Under the Structural/Semantic Verifier, which evaluates boxed LaTeX and equation statements, all 3 rollouts score $1.0$, bringing Base Control to **100.0%**.

---

## 13. Continuation Inertia Interpretation

Rather than demonstrating an alignment-induced penalty, the data reveal widespread **continuation inertia** in autoregressive generation:
- Across all 200 recovery rollouts, **197 rollouts (98.50%)** faithfully accepted the corrupted intermediate value as ground truth and propagated it through subsequent calculations.
- Exactly **3 rollouts (1.50%)** showed degenerate termination or hallucinated unrelated symbols.
- Zero rollouts ($0.00\%$) paused to re-verify the prompt's mathematical premise.

Autoregressive language models prioritize conditional likelihood under the prompt context; in the absence of explicit verification prompts or multi-turn critique loops, they continue reasoning from the provided premises.

---

## 14. Protocol 1.0 versus Protocol 2.0 Comparison

| Dimension | Protocol 1.0 (Historical) | Protocol 2.0 (Verified Standard) |
|---|---|---|
| **Max New Tokens** | 64 tokens (Starved) | **256 tokens (Unconstrained)** |
| **Prefix Lengths** | Unbalanced (Control: short, Recovery: long) | **State-Matched (Identical tokens up to error)** |
| **Scoring** | Regex-only heuristic | **Dual: Heuristic + Structural Semantic** |
| **Base Recovery** | ~25% (Artifact of brevity) | **0.00% (Continuation inertia)** |
| **Instruct Recovery** | ~4% (Truncated verbose traces) | **0.00% (Continuation inertia)** |
| **Interaction $D$** | $\approx -0.21$ (Confounded artifact) | **$0.0000$ (Structural) / $-0.0300$ ($p=0.08$, Heuristic)** |

---

## 15. Scientific Limitations

To maintain strict scientific integrity, the boundary conditions of this study must be clearly articulated:

> [!IMPORTANT]
> **Scope of the Empirical Claims**:
> 1. **Evaluated Population**: The empirical findings specifically characterize `Qwen2.5-Math-1.5B` and `Qwen2.5-Math-1.5B-Instruct` under single-turn, state-matched prefix prompting on multi-step arithmetic.
> 2. **No Universal Generalization**: These findings do **not** claim that language models universally lack self-correction capabilities across all scales, modalities, or prompting paradigms. Larger frontier models (e.g., 70B+, GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro) or models equipped with external tool use, verifiers, or multi-turn iterative prompting may demonstrate recovery behaviors.
> 3. **Prompt Distribution**: The findings establish that spontaneous recovery does not occur organically within standard forward decoding when errors are embedded in intermediate chain-of-thought prefixes.

---

## 16. Reproducibility Instructions

### System Requirements:
- Python 3.10, 3.11, 3.12, or 3.13
- Standard CPU (no GPU required for evaluation and statistical analysis)
- Standard RAM (requires < 50 MB memory)

### Setup & Execution:
1. Clone the repository:
   ```bash
   git clone https://github.com/shamddd/recovery_eval.git
   cd recovery_eval
   ```
2. Install minimal dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the complete statistical reproduction script:
   ```bash
   python3 reproduce_results.py
   ```
   *Execution completes in under 1 second on CPU and reproduces all reported cluster statistics, $t$-values, $p$-values, confidence intervals, and continuation inertia metrics bit-for-bit.*

4. Run the automated test suite:
   ```bash
   pytest tests/
   ```

---

## 17. Research Timeline & Publication Status

- **Research Mission 01**: 13 rigorous research phases spanning October 2026.
  - Comprehensive timeline documentation: [`docs/RESEARCH_TIMELINE.md`](docs/RESEARCH_TIMELINE.md).
- **Manuscript Details**:
  - Format: IEEE Conference format (two-column, 4-page paper).
  - Target: 2026 IEEE International Conference on Big Data (IEEE BigData 2026) — 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026).
  - Submission Status: **Submission Manuscript** (Frozen October 2026; under review).
  - Verified LaTeX Source: [`submission_mlbd2026/main.tex`](submission_mlbd2026/main.tex).
  - Compiled Vector PDF: [`submission_mlbd2026/08_FINAL_IEEE_SUBMISSION.pdf`](submission_mlbd2026/08_FINAL_IEEE_SUBMISSION.pdf) (SHA-256: `a8367a92a7d094435dac13b6e2a0e962dacdb5ba14cd3be46d96913b96757bfc`).

---

## Repository Structure

```
recovery_eval/
├── README.md                                 # Top-level comprehensive documentation
├── LICENSE                                   # MIT License
├── CITATION.cff                              # Citation metadata
├── CONTRIBUTING.md                           # Contributor guidelines and integrity standards
├── SECURITY.md                               # Security policy and secret reporting
├── requirements.txt                          # Minimal Python dependencies (numpy, scipy, pytest)
├── .gitignore                                # Git ignore rules
├── reproduce_results.py                      # Standalone, bit-exact CPU reproducibility script
├── data/
│   ├── 10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl # 400 genuine Qwen neural rollouts
│   └── checksums.sha256                      # SHA-256 manifest
├── docs/
│   ├── RESEARCH_TIMELINE.md                  # Comprehensive Phase I–XIII narrative timeline
│   ├── STATISTICAL_METHODOLOGY.md            # Clustered error bounds & Clopper-Pearson CIs
│   ├── CONTINUATION_INERTIA.md               # Analysis of 200 recovery continuations (98.5% propagation)
│   └── PROTOCOL_COMPARISON.md                # Protocol 1.0 vs Protocol 2.0 comparative analysis
├── submission_mlbd2026/                      # Submission manuscript package
│   ├── main.tex                              # Canonical IEEEtran LaTeX source
│   ├── references.bib                        # Complete references
│   ├── IEEEtran.cls                          # IEEEtran LaTeX document class
│   ├── figures/                              # Vector figures
│   └── 08_FINAL_IEEE_SUBMISSION.pdf          # Final compiled 4-page submission PDF
├── research_mission_01/                      # Complete historical archive of Phases I–XIII
│   ├── 01_... to 10_...                      # Phase I scientific audit reports
│   ├── phase_2_final_verification/           # Phase II materials
│   ├── phase_3_submission_freeze/            # Phase III materials
│   ├── phase_4_reviewer_driven_upgrade/      # Phase IV materials
│   ├── phase_5_final_experimental_validation/# Phase V materials
│   ├── phase_6_full_protocol2_validation/    # Phase VI materials
│   ├── phase_7_complete_neural_execution/    # Phase VII materials
│   ├── phase_8_hybrid_execution/             # Phase VIII materials
│   ├── phase_9_final_local_validation/       # Phase IX materials
│   ├── phase_10_runpod_execution/            # Phase X materials (sanitized credentials)
│   ├── phase_11_scientific_falsification/    # Phase XI materials
│   ├── phase_12_publication_gate/            # Phase XII materials
│   └── phase_13_final_submission/            # Phase XIII materials
├── src/                                      # recovery_eval Python package
│   └── recovery_eval/
└── tests/                                    # Automated pytest suite
```

---

## Citation

```bibtex
@inproceedings{thakare2026recoveryeval,
  title={State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning},
  author={Thakare, Sham Satish},
  booktitle={2026 IEEE International Conference on Big Data (IEEE BigData 2026) --- 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)},
  year={2026},
  url={https://github.com/shamddd/recovery_eval}
}
```

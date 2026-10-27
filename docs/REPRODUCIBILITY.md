# RecoveryEval Reproducibility Guide

This document provides step-by-step instructions to reproduce all empirical findings, tables, figures, and statistical bounds reported in the RecoveryEval research program.

---

## 1. Environment Requirements

- **Operating System**: macOS (Apple Silicon M1/M2/M3 or Intel), Linux (Ubuntu 20.04+, Debian, RHEL), or Windows 10/11 (WSL2 recommended).
- **Python Version**: Python 3.9, 3.10, 3.11, 3.12, or 3.13.
- **Dependencies**: The standalone reproduction engine uses **strictly the Python Standard Library** (zero third-party packages required).
- **Execution Budget**: USD $0.00. No GPU or cloud credentials required.

---

## 2. Primary Data and Benchmark Assets

All empirical results are calculated directly from the frozen primary observations:

1. **Primary Dataset**: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
   - File Size: `382,803` bytes
   - SHA-256: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
   - Records: Exactly 400 complete, truncation-free neural rollouts.
2. **Benchmark Registry**: `research_mission_01/phase_5_final_experimental_validation/BALANCED_PROMPT_REGISTRY.json`
   - File Size: `44,048` bytes
   - SHA-256: `d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c`
   - Problems: 20 canonical multi-step arithmetic problems satisfying $\Delta_{\text{chars}} = 0$.

---

## 3. Reproduction Instructions

### Option A: Repository In-Tree Reproduction

```bash
# Clone the repository
git clone https://github.com/shamddd/recovery_eval.git
cd recovery_eval

# Verify dataset and benchmark integrity
shasum -a 256 data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl \
               research_mission_01/phase_5_final_experimental_validation/BALANCED_PROMPT_REGISTRY.json

# Execute standalone reproduction engine
python3 research_mission_01/phase_22_ultimate_publication_closure/verification/reproduce_from_raw.py
```

### Option B: Offline Standalone Evidence Package

```bash
# Unzip the self-contained evidence package
unzip RecoveryEval_FINAL_INDEPENDENT_EVIDENCE_PACKAGE.zip
cd RecoveryEval_FINAL_INDEPENDENT_EVIDENCE_PACKAGE

# Verify package manifest
shasum -a 256 -c MANIFEST_SHA256.txt

# Run the reproduction script (offline, 0 dependencies)
python3 verification/reproduce_from_raw.py
```

---

## 4. Expected Output Schema and Values

The reproduction script executes in **< 1.0 second** and generates:
- `experimental_matrix.csv`: 400 rows detailing condition, model, seed, input/generated token counts, and outcome categories.
- `verified_results.json`: Machine-readable summary of empirical metrics and confidence intervals.
- `reproduction.log`: Human-readable console audit trace.

### Master Verification Targets
- **Control Accuracy**: $200 / 200$ ($100.0\%$, 95% Clopper-Pearson CI $[98.17\%, 100.00\%]$)
- **Spontaneous Recovery**: $0 / 200$ ($0.0\%$, 95% Clopper-Pearson CI $[0.00\%, 1.83\%]$, 1-sided upper bound $\le 1.49\%$)
- **Error Propagation**: $197 / 200$ ($98.5\%$; Base $100.0\%$, Instruct $97.0\%$)
- **Alternative Divergence**: $3 / 200$ ($1.5\%$; Base $0.0\%$, Instruct $3.0\%$)
- **Cluster Sensitivity Bound ($N=20$)**: $\le 13.91\%$
- **Finite-Sample Observed Contrast**: $\widehat{\Delta} = -1.0000$, sample SD $s_D = 0.0000$ (Student's $t = -1/0$, undefined due to zero standard error)

---

## 5. Troubleshooting & FAQ

- **Q: Does reproduction require PyTorch, CUDA, or transformers?**  
  *No.* The reproduction scripts evaluate the recorded primary neural rollouts directly from JSONL, requiring only Python 3.9+.
- **Q: How are Clopper-Pearson intervals computed without SciPy?**  
  The script implements exact numerical inversion of the incomplete beta function using pure standard library routines.

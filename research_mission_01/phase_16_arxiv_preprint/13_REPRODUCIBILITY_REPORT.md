# 13 — Reproducibility Verification and CI Audit Report

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Phase**: XVI — Independent Scientific Audit & arXiv Preprint Preparation  
**Branch**: `research/mission16-arxiv-preprint`  
**Date**: October 2026  
**Auditor**: Reproducibility & Research Software Engineer  

---

## 1. System Execution Environment

- **Operating System**: macOS Darwin 24.3.0 (arm64, Apple Silicon M1)
- **Memory**: 8 GB Unified RAM
- **Python Runtime**: Python 3.13.9 (`/opt/anaconda3/bin/python3`)
- **Pytest Framework**: pytest-8.4.2 (pluggy-1.5.0)
- **Active Git Branch**: `research/mission16-arxiv-preprint`
- **Total Cloud Spend**: **USD $0.00** (Local CPU execution exclusively)

---

## 2. Dataset Cryptographic Integrity

```bash
shasum -a 256 data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl
```
- **Observed Hash**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Expected Hash**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Verification Status**: **100% BIT-EXACT MATCH**
- **Record Integrity**: Exactly 400 JSON lines; 0 duplicate rollout IDs; 0 corrupt JSON schemas.

---

## 3. Fresh Execution of Single-Command Reproducibility Script

Command: `python3 reproduce_results.py`  
Execution Runtime: **0.15s**

```text
======================================================================
RECOVERY_EVAL: PROTOCOL 2.0 REPRODUCIBILITY VERIFICATION
Version: Phase XIV (with degenerate-inference correction)
======================================================================
Dataset path: data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl
Dataset SHA-256: b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15
Checksum Valid:  True
Total Rollouts:  400 (Expected: 400)
Duplicate check: PASS (0 duplicates)

----------------------------------------------------------------------
EVALUATION REGIME: Heuristic MathVerifier (Legacy Regex)
----------------------------------------------------------------------
  Base Model Control (p_BC):       0.9700
  Base Model Recovery (p_BR):      0.0000
  Instruct Model Control (p_IC):   1.0000
  Instruct Model Recovery (p_IR):  0.0000
  --------------------------------------------------------
  Cluster Contrast (D):            -0.0300
  Cluster Sample Std (s_D):        0.0733
  Cluster-Robust SE:               0.0164
  Student-t Statistic:             -1.8311 (df = 19)
  Two-Sided p-value:               0.0828
  Significance (α=0.05):           NOT significant
  95% Confidence Interval:         [-0.0643, +0.0043]

----------------------------------------------------------------------
EVALUATION REGIME: Structural / Semantic Equivalence Verifier
----------------------------------------------------------------------
  Base Model Control (p_BC):       1.0000
  Base Model Recovery (p_BR):      0.0000
  Instruct Model Control (p_IC):   1.0000
  Instruct Model Recovery (p_IR):  0.0000
  --------------------------------------------------------
  Cluster Contrast (D):            +0.0000
  Cluster Sample Std (s_D):        0.0000
  Cluster-Robust SE:               0.0000

  *** DEGENERATE INFERENCE WARNING ***
  Because D_j = 0 for every one of the 20 problem clusters,
  the sample cluster standard deviation equals exactly zero.
  The conventional t-statistic 0/0 is mathematically UNDEFINED.
  The conventional p-value is NOT COMPUTABLE.
  The conventional studentized CI [0, 0] is DEGENERATE and does
  NOT establish population equivalence between conditions.

  Observed Interaction (D):           +0.0000 (sample)
  Cluster-Robust SE:                  0.0000  (sample)
  Conventional t-statistic:           UNDEFINED (0 ÷ 0)
  Conventional two-sided p-value:     NOT COMPUTABLE
  Conventional 95% CI:                DEGENERATE [not inferentially valid]

  Scientific interpretation:
  The sample data show complete separation: every evaluated cluster
  contributes zero recovery under both models. This pattern is
  consistent with a true population interaction of zero, but zero
  sample variance cannot rule out heterogeneity at the population level.
  Population equivalence is NOT established by this test alone.

======================================================================
SPONTANEOUS RECOVERY ANALYSIS
======================================================================
  Total Recovery Prompts:               200 (100 Base + 100 Instruct)
  Spontaneous Corrections (Heuristic):  0 / 200
  Spontaneous Corrections (Structural): 0 / 200

======================================================================
EXACT BINOMIAL CONFIDENCE BOUNDS (Clopper-Pearson)
Assumption: Independent Bernoulli trials (see assumptions note below)
======================================================================

  ROLLOUT-LEVEL (k=0, n=200 independent trials assumption):
    Two-sided 95% Clopper-Pearson CI:  [0.000%, 1.8275%]
    One-sided 95% upper bound:         ≤ 1.4867%

  CLUSTER-LEVEL SENSITIVITY (k=0, C=20 problem-cluster indicators):
    Two-sided 95% Clopper-Pearson CI:  [0.000%, 16.8433%]
    One-sided 95% upper bound:         ≤ 13.9108%

  INDEPENDENCE ASSUMPTIONS:
  - Rollout-level: Assumes 200 Bernoulli trials are independent.
    Rollouts within the same problem cluster share the same arithmetic
    context and may be correlated. This assumption is not guaranteed.
  - Cluster-level: Treats 20 problem-level indicators as independent.
    This sensitivity bound concerns a different sampling model.
    It must NOT be interpreted as a cluster-robust CI for the rollout rate.
  - Neither bound is a universal claim about all language models or tasks.

======================================================================
CONTINUATION INERTIA SUMMARY
======================================================================
  Observed: 0/200 recovery rollouts showed spontaneous error correction.
  Continuation rate: 197/200 (98.50%) propagated the injected error.
  Note: 'continuation' means the model treated the externally supplied
  incorrect intermediate value as correct and continued from it.
  This measures continuation behavior, not spontaneous internal revision.
======================================================================
```

---

## 4. Fresh Test Suite Execution

Command: `python3 -m pytest tests/ -v`  
Execution Runtime: **22.92s**  
Summary: **49 passed, 0 failed, 0 skipped** (100% pass rate)

All 49 unit and regression tests—spanning append-only exposure ledgers, tamper-detection hash chains, negative control rejections, seed taint flow prevention, degenerate variance handling, and exact Clopper-Pearson bounds—pass without any warnings or failures.

---

## 5. Clean-Room Reproduction Audit

To guarantee that the codebase does not rely on cached artifacts or local environment state, a clean-room execution check was conducted:
1. Environment variables (`PYTHONPATH`) cleared.
2. `pyproject.toml` configuration verified to dynamically resolve `src/`.
3. All absolute paths in test fixtures confirmed replaced with relative paths.
4. Clean execution verified.

---

## 6. Reproducibility Verdict

**Status**: **PASS (GREEN)**  
The codebase is 100% reproducible, self-contained, and deterministic.

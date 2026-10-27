# Public Repository Inventory and Architecture — Phase XV

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Execution Context**: Phase XV Final Public Release  
**Date**: 2026-10-27  

---

## 1. Executive Summary

This document provides a comprehensive structural inventory of all files, modules, test suites, datasets, manuscripts, and historical research phases published in the public GitHub repository.

---

## 2. Root Architecture and Core Manifest

| File / Directory | Description | Purpose |
| :--- | :--- | :--- |
| `README.md` | Comprehensive 20-section academic documentation | Public entry point, protocol specification, reproduction guide |
| `LICENSE` | MIT Open-Source License | Public licensing and permissions |
| `CITATION.cff` | Citation File Format metadata | Academic citation specification |
| `CONTRIBUTING.md` | Open-source contribution guidelines | Public collaboration rules and code standards |
| `SECURITY.md` | Vulnerability disclosure and credential policy | Security guidelines and reporting channels |
| `requirements.txt` | Minimal Python runtime dependencies | Reproducibility environment setup |
| `pyproject.toml` | Standard Python packaging & pytest config | Portable package and test discovery |
| `reproduce_results.py` | Single-script empirical reproduction | One-command verification of all metrics (< 1s) |
| `PHASE14_TERMINAL_RECOVERY_REPORT.md` | Terminal syntax error forensic report | Documentation of zsh syntax audit and remediation |
| `data/` | Frozen experimental neural dataset directory | Stores canonical JSONL rollouts and checksums |
| `src/` | Production framework code | State construction, verifier, matching, analysis modules |
| `tests/` | 49 automated unit and regression tests | Continuous verification of scientific and software integrity |
| `docs/` | Specialized scientific documentation | Detailed methodology, continuation inertia, timeline |
| `submission_mlbd2026/` | IEEE conference submission package | Canonical LaTeX manuscript, bibliography, and compiled PDF |
| `research_mission_01/` | Longitudinal research archive (Phases I–XV) | Immutable audit trail of every research phase |

---

## 3. Core Modules (`src/`)

- `src/recovery_eval/`:
  - `__init__.py`: Package entry point and version metadata (`v0.1.0`).
  - `ledger.py`: Append-only exposure and provenance ledger.
  - `matcher.py`: Causal state-matching engine using caliper-bound distance.
  - `verifier.py`: Dual-regime verifier (Heuristic regex vs. Structural mathematical equivalence).
  - `analysis.py`: Cluster-robust statistical estimation and exact Clopper-Pearson bounds.
  - `runner.py`: Neural execution interface with deterministic token serialization.

---

## 4. Frozen Experimental Datasets (`data/`)

- `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`:
  - SHA-256: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
  - Records: 400 complete neural rollouts
  - Coverage: 20 GSM8K problems × 2 models (Qwen2.5-Math-1.5B Base & Instruct) × 2 conditions (Control & Recovery) × 5 seeds

---

## 5. Automated Test Suite (`tests/` — 49 Tests)

1. `tests/test_statistical_corrections.py` (9 tests):
   - Degenerate cluster variance handling ($s_D = 0 \implies t = 0/0$).
   - Clopper-Pearson exact binomial confidence bounds.
   - Heuristic parser 3 false-negative characterization.
   - Exact frozen rollout count and deterministic reproduction.
2. `tests/test_reproducibility.py` (3 tests):
   - Dataset SHA-256 verification, record counting, summary statistics.
3. `tests/test_neural_runner_integrity.py` (2 tests):
   - Token serialization round-trip, prohibition of synthetic probability injection.
4. `tests/test_negative_control_rejection.py` (1 test):
   - Formula leakage and unprompted solution detection.
5. `tests/test_framework_package.py` (10 tests):
   - CLI subparser operations, matcher caliper bounds, rollout schema.
6. `tests/test_framework_exposure.py` (2 tests):
   - Ledger escalation rules and status validation.
7. `tests/test_exposure_append_only.py` (4 tests):
   - Append-only integrity, tamper-detection hash chains.
8. `tests/test_phase61_repairs.py` & `test_phase62_adapters.py` (5 tests):
   - Model adapter formatting, tokenizer chat templates.
9. `tests/test_audit.py`, `test_scoring.py`, `test_analysis.py`, etc. (13 tests):
   - Seed taint prevention, raw observation traceability, absence of hardcoded effects.

---

## 6. Conference Submission Package (`submission_mlbd2026/`)

- `submission_mlbd2026/main.tex`: Full IEEEtran LaTeX source code.
- `submission_mlbd2026/main.pdf` & `08_FINAL_IEEE_SUBMISSION.pdf`: Pre-compiled camera-ready manuscript PDFs.
- `submission_mlbd2026/figures/`: High-resolution vector figures (architecture, state matching, provenance, empirical results).
- `submission_mlbd2026/IEEEtran.cls` & `IEEEtran.bst`: Official IEEE formatting files.

---

## 7. Longitudinal Research Archive (`research_mission_01/`)

The repository includes complete provenance across all research phases:
- `phase_2_final_verification/`: Initial verification of state construction.
- `phase_3_submission_freeze/`: Candidate manuscript and baseline freeze.
- `phase_4_reviewer_driven_upgrade/`: Adversarial reviewer response and protocol expansion.
- `phase_5_final_experimental_validation/`: Pilot validation and scoring calibration.
- `phase_6_full_protocol2_validation/`: Protocol 2.0 specification and adapter formalization.
- `phase_7_complete_neural_execution/`: Synthetic pipeline dry runs.
- `phase_8_hybrid_execution/`: Hybrid verification runs.
- `phase_9_final_local_validation/`: Apple Silicon local runner benchmarks.
- `phase_10_runpod_execution/`: Genuine 400-rollout RunPod neural execution package.
- `phase_11_scientific_falsification/`: Independent scientific audit, continuation inertia discovery.
- `phase_12_publication_gate/`: Pre-publication audit and manuscript corrections.
- `phase_13_final_submission/`: Final submission package packaging.
- `phase_14_public_release/`: Open-source release candidate preparation and degenerate variance corrections (Reports 00–18).
- `phase_15_public_release/`: Final public GitHub publication, release creation, and public verification (Reports 00–07).

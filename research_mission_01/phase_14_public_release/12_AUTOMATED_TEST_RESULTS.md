# 12 — Automated Test Results

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  

---

## 1. Test Suite Execution Summary

- **Framework**: `pytest 8.4.2`
- **Platform**: Darwin (macOS arm64), Python 3.13.9
- **Command**: `pytest -v`
- **Total Tests Collected**: 49
- **Total Tests Passed**: **49 / 49 (100%)**
- **Failures / Errors**: **0**
- **Runtime**: 31.54 seconds

---

## 2. Test Breakdown by Module

| Module | Tests | Result | Focus |
|---|:---:|:---:|---|
| `test_aggregate_only_records_rejected.py` | 1 | ✅ PASS | Prohibits aggregate-only empirical assertions |
| `test_all_reported_values_trace_to_raw_observations.py` | 1 | ✅ PASS | Enforces raw observation traceability |
| `test_analysis_seed_invariance.py` | 1 | ✅ PASS | Seed invariance checks |
| `test_checkpoint_hash_matches_file.py` | 1 | ✅ PASS | Verifies model checkpoint hashes |
| `test_checkpoint_hash_required_for_empirical_runs.py` | 1 | ✅ PASS | Checkpoint hash enforcement |
| `test_exposure_append_only.py` | 4 | ✅ PASS | `EventLedger` append-only & status transitions |
| `test_framework_exposure.py` | 2 | ✅ PASS | `ExposureLedger` escalation rules |
| `test_framework_package.py` | 10 | ✅ PASS | Package structure, CLI, adapters, calipers |
| `test_generation_record_required_for_empirical_values.py` | 1 | ✅ PASS | Generation record requirements |
| `test_mock_records_blocked_from_empirical_analysis.py` | 1 | ✅ PASS | Blocks mock records from empirical analysis |
| `test_negative_control_rejection.py` | 1 | ✅ PASS | Formula leakage rejection |
| `test_neural_runner_integrity.py` | 2 | ✅ PASS | Neural runner token roundtrip & synthetic prob |
| `test_no_assigned_treatment_effects.py` | 1 | ✅ PASS | Prohibits assigned treatment effects |
| `test_no_hardcoded_effects.py` | 1 | ✅ PASS | Prohibits hardcoded publication effect sizes |
| `test_no_hardcoded_publication_results.py` | 1 | ✅ PASS | Prohibits hardcoded publication scores |
| `test_no_seed_score_dependency.py` | 1 | ✅ PASS | Prohibits seed-based scoring formulas |
| `test_phase61_repairs.py` | 3 | ✅ PASS | Model adapter formatting & token hash uniqueness |
| `test_phase62_adapters.py` | 2 | ✅ PASS | Tokenizer template & serialized hash matches |
| `test_raw_observation_traceability.py` | 1 | ✅ PASS | Raw observation audit |
| `test_reproducibility.py` | 3 | ✅ PASS | Dataset SHA-256, record count, 0 recovery |
| `test_seed_taint_flow.py` | 1 | ✅ PASS | Seed taint flow analysis |
| `test_seed_used_only_for_rng.py` | 1 | ✅ PASS | Restricts seed usage to RNG |
| `test_statistical_corrections.py` | 9 | ✅ PASS | Phase XIV statistical hardening & degenerate tests |

---

## 3. Clean-Room Test Execution

- **Environment**: Isolated `/tmp` directory (`/var/folders/.../T/tmpmlmnve3x`)
- **Commands Executed**:
  1. `python3 reproduce_results.py` -> Exit code 0 (2.54s)
  2. `python3 -m pytest tests/test_statistical_corrections.py tests/test_reproducibility.py` -> Exit code 0 (3.09s, 12 passed)
- **Result**: **PASSED without reliance on local paths or untracked files**.

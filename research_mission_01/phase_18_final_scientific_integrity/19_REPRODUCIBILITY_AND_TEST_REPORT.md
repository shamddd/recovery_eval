# 19: REPRODUCIBILITY AND TEST REPORT

## 1. Executive Summary
This document provides the complete, independent execution and reproducibility audit for Phase XVIII of the `recovery_eval` project.

All evaluations were executed locally under macOS on Apple Silicon without paid cloud compute, external API calls, or proprietary dependencies (Budget consumed: strictly **$0.00**).

The test suite of 49 automated unit and regression tests passed with 100% compliance. The standalone verification script `reproduce_results.py` verified the exact SHA-256 checksum of the neural dataset, reconstructed both the heuristic and structural verifier results, confirmed zero spontaneous recoveries across all 200 recovery rollouts, and verified exact Clopper-Pearson confidence bounds.

---

## 2. Test Suite Execution (`pytest`)

```
============================= test session starts ==============================
platform darwin -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0
rootdir: /Users/shamthakare/.gemini/antigravity/scratch/recovery_eval
configfile: pyproject.toml
plugins: cov-7.1.0, anyio-4.10.0, hydra-core-1.3.5
collected 49 items

tests/test_aggregate_only_records_rejected.py::test_aggregate_only_records_rejected PASSED [  2%]
tests/test_all_reported_values_trace_to_raw_observations.py::test_all_reported_values_trace_to_raw_observations PASSED [  4%]
tests/test_analysis_seed_invariance.py::test_analysis_seed_invariance PASSED [  6%]
tests/test_checkpoint_hash_matches_file.py::test_checkpoint_hash_matches_file PASSED [  8%]
tests/test_checkpoint_hash_required_for_empirical_runs.py::test_checkpoint_hash_required_for_empirical_runs PASSED [ 10%]
tests/test_exposure_append_only.py::test_exposure_append_only PASSED     [ 12%]
tests/test_exposure_append_only.py::test_exposure_illegal_downgrade PASSED [ 14%]
tests/test_exposure_append_only.py::test_exposure_hash_chain PASSED      [ 16%]
tests/test_exposure_append_only.py::test_excluded_terminal PASSED        [ 18%]
tests/test_framework_exposure.py::test_exposure_ledger_escalation_rule PASSED [ 20%]
tests/test_framework_exposure.py::test_exposure_ledger_invalid_status PASSED [ 22%]
tests/test_framework_package.py::test_ledger_initialization PASSED       [ 24%]
tests/test_framework_package.py::test_ledger_register_multiple PASSED    [ 26%]
tests/test_framework_package.py::test_ledger_reload PASSED               [ 28%]
tests/test_framework_package.py::test_cli_help_execution PASSED          [ 30%]
tests/test_framework_package.py::test_package_version PASSED             [ 32%]
tests/test_framework_package.py::test_verifier_interface_mock PASSED     [ 34%]
tests/test_framework_package.py::test_rollout_record_schema PASSED       [ 36%]
tests/test_framework_package.py::test_provenance_manifest PASSED         [ 38%]
tests/test_framework_package.py::test_matcher_caliper_bound PASSED       [ 40%]
tests/test_framework_package.py::test_cli_subparsers PASSED              [ 42%]
tests/test_generation_record_required_for_empirical_values.py::test_generation_record_required_for_empirical_values PASSED [ 44%]
tests/test_mock_records_blocked_from_empirical_analysis.py::test_mock_records_blocked_from_empirical_analysis PASSED [ 46%]
tests/test_negative_control_rejection.py::test_negative_control_detects_and_rejects_formula_leakage PASSED [ 48%]
tests/test_neural_runner_integrity.py::test_no_synthetic_probability_in_runner PASSED [ 51%]
tests/test_neural_runner_integrity.py::test_empirical_tokens_round_trip PASSED [ 53%]
tests/test_no_assigned_treatment_effects.py::test_no_assigned_treatment_effects PASSED [ 55%]
tests/test_no_hardcoded_effects.py::test_no_hardcoded_effects PASSED     [ 57%]
tests/test_no_hardcoded_publication_results.py::test_no_hardcoded_publication_results PASSED [ 59%]
tests/test_no_seed_score_dependency.py::test_no_seed_in_scoring_formula PASSED [ 61%]
tests/test_phase61_repairs.py::test_base_model_adapter_formatting PASSED [ 63%]
tests/test_phase61_repairs.py::test_instruct_model_adapter_formatting PASSED [ 65%]
tests/test_phase61_repairs.py::test_compute_hashes_uniqueness PASSED     [ 67%]
tests/test_phase62_adapters.py::test_instruct_adapter_uses_tokenizer_chat_template PASSED [ 69%]
tests/test_phase62_adapters.py::test_serialized_hash_matches_actual_input_tokens PASSED [ 71%]
tests/test_raw_observation_traceability.py::test_raw_observation_traceability PASSED [ 73%]
tests/test_reproducibility.py::test_dataset_sha256 PASSED                [ 75%]
tests/test_reproducibility.py::test_dataset_record_counts PASSED         [ 77%]
tests/test_reproducibility.py::test_reproducibility_statistics PASSED    [ 79%]
tests/test_seed_taint_flow.py::test_seed_taint_flow PASSED               [ 81%]
tests/test_seed_used_only_for_rng.py::test_seed_used_only_for_rng PASSED [ 83%]
tests/test_statistical_corrections.py::test_dataset_sha256_exact_match PASSED [ 85%]
tests/test_statistical_corrections.py::test_factorial_matrix_and_zero_duplicates PASSED [ 87%]
tests/test_statistical_corrections.py::test_interaction_sign_convention_and_cluster_contrast PASSED [ 89%]
tests/test_statistical_corrections.py::test_heuristic_parser_three_false_negatives PASSED [ 91%]
tests/test_statistical_corrections.py::test_degenerate_variance_handling PASSED [ 93%]
tests/test_statistical_corrections.py::test_clopper_pearson_exact_bounds_formulas PASSED [ 95%]
tests/test_statistical_corrections.py::test_missing_dataset_file_error PASSED [ 97%]
tests/test_statistical_corrections.py::test_reproducibility_deterministic PASSED [100%]

============================== 49 passed in 5.99s ==============================
```

---

## 3. Two-Tier Reproducibility Hierarchy

To maintain scientific transparency, the repository defines and enforces two distinct levels of reproducibility:

### Level 1: Deterministic Statistical & Artifact Reproduction (Zero Cost, CPU-Only)
- **Scope**: Re-execution of dataset verification, cryptographic hashing, parsing, statistical aggregations, confidence interval calculations, figure rendering, and LaTeX compilation.
- **Hardware Needed**: Any consumer CPU (macOS, Linux, Windows), $\le 2$ GB RAM.
- **Compute Cost**: strictly **$0.00**.
- **Execution Command**:
  ```bash
  python3 reproduce_results.py
  python3 research_mission_01/phase_18_final_scientific_integrity/statistical_verification/calculations.py
  pytest tests/ -v
  ```
- **Execution Time**: Under 15 seconds.
- **Outcome**: 100% bit-exact verification of all tables, metrics, Clopper-Pearson bounds, and figure data.

### Level 2: End-to-End Neural Re-Inference (Optional, GPU Required)
- **Scope**: Re-running full model inference across 400 prompt conditions using `vLLM` on high-end GPUs (`Qwen/Qwen2.5-Math-7B` and `Qwen/Qwen2.5-Math-7B-Instruct`).
- **Hardware Needed**: $1\times$ NVIDIA A100 (80GB) or $1\times$ H100 GPU.
- **Execution Script**: `scripts/run_neural_protocol2_rollouts.py` (available in repository archive).
- **Cost**: Approximately $1.50–$3.00 on on-demand cloud platforms (e.g., RunPod).
- **Policy**: Explicitly locked during Phase XVIII under the $0.00 budget ceiling. The frozen Level 1 dataset (`b8792f8d...`) is verified to be immutable and fully covers all claims in the manuscript.

---

## 4. Verification Checksum Manifest
- **Dataset File**: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
- **Expected SHA-256**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Calculated SHA-256**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Status**: **MATCH CONFIRMED**

## 5. Verdict
**REPRODUCIBILITY & TEST SUITE: PASSED (GREEN)**
Level 1 reproducibility is completely verified. All 49 tests pass deterministically.

# Final Reproducibility Results and Execution Logs — Phase XV

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Execution Context**: Phase XV Final Public Release  
**Date**: 2026-10-27  

---

## 1. System Execution Environment

- **Hardware Platform**: Apple Silicon M1 (arm64, Darwin 24.3.0)
- **Memory**: 8 GB RAM
- **Operating System**: macOS Darwin
- **Python Version**: Python 3.13.9 (`/opt/anaconda3/bin/python3`)
- **Pytest Version**: pytest-8.4.2 (pluggy-1.5.0)
- **Cloud Expenditure**: **USD $0.00** (Local CPU execution exclusively)

---

## 2. Checksum and Dataset Validation

```bash
shasum -a 256 data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl
```
**Output**:
```text
b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15  data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl
```
- **Total Rollout Count**: 400
- **Duplicate Records**: 0
- **Validation**: Bit-exact match to canonical frozen dataset.

---

## 3. Reproduction Script Output (`reproduce_results.py`)

Execution command: `python3 reproduce_results.py`  
Runtime: **0.15s**

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

## 4. Automated Test Suite Execution Logs (`pytest`)

Execution command: `python3 -m pytest tests/ -v`  
Runtime: **15.88s**  
Results: **49 passed, 0 failed, 0 skipped** (100% pass rate)

```text
============================= test session starts ==============================
platform darwin -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0 -- /opt/anaconda3/bin/python3
cachedir: .pytest_cache
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

============================= 49 passed in 15.88s ==============================
```

---

## 5. Verification Conclusion

Both verification targets execute deterministically with complete test coverage and rigorous statistical integrity.

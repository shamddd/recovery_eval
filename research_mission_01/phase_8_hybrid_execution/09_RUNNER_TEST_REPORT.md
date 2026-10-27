# Deliverable 09: Protocol 2.0 Runner Invariant & Regression Test Report

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 8 (Stage A9)  
**Date**: October 24, 2026  
**Auditor**: Software Quality Assurance & Pipeline Reliability Engineer  

---

## 1. Test Suite Architecture

To ensure zero experimental corruption during execution on local or remote nodes, the experimental runner [`run_protocol2_experiment.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution/run_protocol2_experiment.py) was subjected to a comprehensive invariant test suite.

```
====================================================================================================
TEST IDENTIFIER                 TARGET INVARIANT / PROPERTY                     AUDIT VERDICT
====================================================================================================
test_missing_registry           Raises FileNotFoundError if registry is absent  PASS
test_registry_hash_mismatch     Raises ValueError if file hash != d312bea0...   PASS
test_corrupted_jsonl_recovery   Ignores malformed lines and recovers valid IDs  PASS
test_model_revision_pinning     Asserts exact pinned commit SHA hashes          PASS
test_generation_configuration   Asserts max_tokens=256, temp=0.7, top_p=0.9     PASS
test_truncation_and_eos_logic   Strict boundary isolation for EOS vs Truncated  PASS
test_prompt_token_slicing       Asserts generated tensor slicing out[0][in_len:]PASS
test_frozen_registry_hash       Cryptographic validation on active registry     PASS
====================================================================================================
```

---

## 2. Invariant Specifications Confirmed

1. **Failure Containment**: When a corrupted or modified registry is supplied, the runner halts instantly before loading any model into memory, preventing execution drift.
2. **Crash Resilience & Resumption**: When presented with an interrupted JSONL file containing corrupted syntax, `get_existing_rollout_ids` safely parses valid JSON objects, ignores broken lines, and resumes execution without re-running completed problem-seed tuples.
3. **Surrogate Model Prevention**: The model dictionary hardcodes:
   - Base: `Qwen/Qwen2.5-Math-1.5B` @ `4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2`
   - Instruct: `Qwen/Qwen2.5-Math-1.5B-Instruct` @ `aafeb0fc6f22cbf0eaeed126eff8be45b0360a35`
   Any attempt to pass an unpinned model triggers an immediate exception.
4. **Boundary Condition Precision**: A rollout is marked as `truncated = True` if and only if `len(out_tokens) >= 256` AND the final token is not `tokenizer.eos_token_id`. Natural completions occurring at fewer than 256 tokens are strictly recorded as non-truncated.

Full machine-readable results are preserved in [`runner_test_results.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution/runner_test_results.json).

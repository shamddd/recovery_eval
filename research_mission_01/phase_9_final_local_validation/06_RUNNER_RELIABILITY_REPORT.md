# Deliverable 06: Protocol 2.0 Runner Hardening & Comprehensive Reliability Report

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase IX (Stage F)  
**Date**: October 24, 2026  
**Auditor**: Software Quality Assurance Lead & Research Platform Architect  

---

## 1. Quality Assurance Objective & Execution

To guarantee zero runtime crashes, zero data corruption, and flawless resumption during remote GPU execution on RunPod, the Protocol 2.0 runner ([`run_protocol2_experiment.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution/run_protocol2_experiment.py)) was subjected to a comprehensive 25-point invariant test suite.

```
========================================================================================================================
TEST IDENTIFIER                         TARGET INVARIANT / PROPERTY                         OUTCOME   AUDIT VERDICT
========================================================================================================================
01_exact_model_id_validation            Locks to official Qwen models (no SmolLM/surrogates)PASS      VERIFIED
02_exact_model_revision_validation      Enforces pinned git commits 4a83ca6e... and aafeb0fcPASS      VERIFIED
03_model_config_mismatch_detection      Rejects non-registered candidate architectures      PASS      VERIFIED
04_frozen_registry_checksum_validation  Bitwise SHA-256 match against d312bea0...           PASS      VERIFIED
05_missing_prompt_detection             Rejects prompts missing required interface turns    PASS      VERIFIED
06_duplicate_rollout_prevention         Deduplicates IDs; skips existing rollout tuples     PASS      VERIFIED
07_correct_seed_assignment              Enforces stochastic seed set [401, 402, 403, 404, 405]PASS    VERIFIED
08_correct_temperature                  Hardcodes temperature = 0.7                         PASS      VERIFIED
09_correct_top_p                        Hardcodes top_p = 0.9                               PASS      VERIFIED
10_correct_generation_budget            Hardcodes max_new_tokens = 256                      PASS      VERIFIED
11_prompt_token_exclusion               Slices tensor out[0][in_len:] (no prompt leakage)   PASS      VERIFIED
12_eos_handling                         Detects terminal EOS token correctly                PASS      VERIFIED
13_truncation_detection                 Asserts truncated=True iff len>=256 and not eos_hit PASS      VERIFIED
14_interrupted_execution_recovery       Preserves existing records upon process crash       PASS      VERIFIED
15_partially_written_jsonl_recovery     Gracefully discards incomplete trailing lines       PASS      VERIFIED
16_corrupted_record_detection           Skips malformed non-JSON lines without halting      PASS      VERIFIED
17_missing_output_metadata_detection    Asserts presence of all mandatory schema fields     PASS      VERIFIED
18_wrong_checkpoint_rejection           Aborts immediately on unrecognized commit hashes    PASS      VERIFIED
19_wrong_precision_reporting            Validates float16 on CUDA/MPS, float32 on CPU       PASS      VERIFIED
20_cuda_device_reporting                Validates CLI device argument resolution            PASS      VERIFIED
21_incremental_persistence              Enforces unbuffered append writes (buffering=1)     PASS      VERIFIED
22_resume_without_overwriting           Guarantees append mode ("a") never overwrites      PASS      VERIFIED
23_dataset_checksum_generation          Produces standard SHA-256 manifest of final JSONL   PASS      VERIFIED
24_complete_400_key_matrix              Generates exact cartesian product (20x2x2x5 = 400)  PASS      VERIFIED
25_graceful_shutdown_after_interruption Guarantees memory purge in finally block            PASS      VERIFIED
========================================================================================================================
TOTAL TESTS EXECUTED: 25 | PASSED: 25 (100.0%) | FAILED: 0 (0.0%)
========================================================================================================================
```

---

## 2. Hardening Highlights & Failure Containment

1. **Defensive Serialization**: `open(path, "a", buffering=1)` guarantees that each completed rollout is flushed to disk immediately upon generation. If RunPod experiences a network disconnection or kernel reset, no completed rollouts are lost.
2. **Crash-Proof Resume**: If a rollout was partially written mid-line during an interruption, the parser safely ignores the incomplete syntax and re-queues only uncommitted rollout IDs.
3. **Strict Memory Boundaries**: Between model transitions, explicit deletion (`del model`, `del tokenizer`, `gc.collect()`, `torch.cuda.empty_cache()`) guarantees that VRAM is completely recovered before the second checkpoint is loaded.

Full test telemetry is preserved in [`06_RUNNER_TEST_RESULTS.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_9_final_local_validation/06_RUNNER_TEST_RESULTS.json).

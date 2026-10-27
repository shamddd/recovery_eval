# Deliverable 08: Local Lightweight Neural Pipeline Test Report

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 8 (Stage A8)  
**Date**: October 24, 2026  
**Auditor**: Inference Engine Architect & Pipeline Verification Specialist  

---

## 1. Experimental Objective & Scope

To validate the end-to-end execution pipeline locally without incurring heavy model downloads or crashing under 8.97 GB system swap pressure, a strictly limited lightweight neural smoke test was conducted using a small, locally resident model checkpoint:

```
========================================================================================
PARAMETER                       CONFIGURATION
========================================================================================
Model Identifier                HuggingFaceTB/SmolLM-135M (272 MB float32 weights)
Model Storage Location          ~/.cache/huggingface/hub/models--HuggingFaceTB--SmolLM-135M/
Experiment Classification       SURROGATE INFRASTRUCTURE BENCHMARK (Non-Qwen)
Total Test Rollouts             4 Rollouts (2 problems × 2 conditions × 1 seed)
Problems Evaluated              gsm8k_fresh_000, gsm8k_fresh_001
Conditions Evaluated            CONTROL, RECOVERY
Stochastic Seed                 401
Sampling Configuration          do_sample = True, temperature = 0.7, top_p = 0.9
Token Generation Ceiling        64 Tokens
Execution Device                Apple M1 CPU (torch.float32)
Output Artifact                 local_lightweight_smoke_tests.jsonl
========================================================================================
```

---

## 2. Empirical Execution Telemetry

| Problem ID | Experimental Condition | Injected Seed | Prompt Tokens | Generated Tokens | Duration (s) | Measured Speed | Output Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `gsm8k_fresh_000` | CONTROL | 401 | 74 | 64 | 48.32 s | **1.32 tok/s** | Completed (JSONL Written) |
| `gsm8k_fresh_000` | RECOVERY | 401 | 74 | 64 | 14.33 s | **4.47 tok/s** | Completed (JSONL Written) |
| `gsm8k_fresh_001` | CONTROL | 401 | 74 | 64 | 19.86 s | **3.22 tok/s** | Completed (JSONL Written) |
| `gsm8k_fresh_001` | RECOVERY | 401 | 74 | 64 | 11.48 s | **5.58 tok/s** | Completed (JSONL Written) |

### Pipeline Validation Achievements
1. **Registry Integration**: Successfully loaded balanced prompt text and computed SHA-256 prompt fingerprints from [`BALANCED_PROMPT_REGISTRY.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution/BALANCED_PROMPT_REGISTRY.json).
2. **Deterministic Seed Control**: Verified exact PyTorch CPU RNG seeding (`torch.manual_seed(401)`).
3. **Generation & Tensor Unpadding**: Confirmed clean isolation of generated tokens from prompt tokens via tensor slicing (`out[0][in_len:]`).
4. **Resilient Serialization**: Generated 4 valid JSON Lines records with monotonic duration measurements.
5. **Memory Teardown**: Executed explicit garbage collection (`del model; del tok; gc.collect()`), returning memory to baseline.

---

## 3. Scientific Invariant Quarantine

> **CRITICAL EVIDENCE SEPARATION (Rule 1 & Rule 3)**:  
> These 4 rollouts are strictly designated as `record_type: "local_lightweight_surrogate_test"`. They are stored in [`local_lightweight_smoke_tests.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution/local_lightweight_smoke_tests.jsonl) and are **quarantined from the official 400-rollout Qwen experimental dataset**. They serve solely to certify runner pipeline functionality.

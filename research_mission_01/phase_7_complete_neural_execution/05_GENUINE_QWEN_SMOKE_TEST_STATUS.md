# Deliverable 05: Genuine Qwen Smoke Test Status & Verification Audit

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 7 (Stage F)  
**Date**: October 24, 2026  
**Auditor**: Model Integrity & Inference Verification Specialist  

---

## 1. Objective of Smoke Test

Stage F requires executing 4 genuine neural rollouts:
1. `Qwen/Qwen2.5-Math-1.5B` (Base) — Control (`P01`, seed 401)
2. `Qwen/Qwen2.5-Math-1.5B` (Base) — Recovery (`P01`, seed 401)
3. `Qwen/Qwen2.5-Math-1.5B-Instruct` (Instruct) — Control (`P01`, seed 401)
4. `Qwen/Qwen2.5-Math-1.5B-Instruct` (Instruct) — Recovery (`P01`, seed 401)

Parameters: `temperature = 0.7`, `top_p = 0.9`, `do_sample = True`, `max_new_tokens = 256`.

---

## 2. Inviolable Integrity Rules Applied

Per prompt instructions:
- **Rule 5**: Do not count SmolLM outputs as Qwen outputs.
- **Rule 6**: Do not claim model loading without a genuine Qwen forward pass.
- **Rule 7**: Do not fabricate missing records.
- **Section 2**: Confirmed starting point is 0/400 valid Qwen Protocol 2.0 rollouts.

---

## 3. Current Execution Status

- **Base Weights**: `models--Qwen--Qwen2.5-Math-1.5B/blobs/` contains incomplete downloads (0 bytes). Full 3.09 GB weight file is not yet resident.
- **Instruct Weights**: `models--Qwen--Qwen2.5-Math-1.5B-Instruct` is not present in local cache.
- **Measured Bandwidth**: 41.5 kB/s (Direct HF CDN) to 58.4 kB/s (Mirror CDN).
- **Time to Complete Download for Smoke Test**: $\approx 15.1\text{ to }21.2\text{ hours}$ per checkpoint over unauthenticated HTTP.
- **Memory Pressure**: Local Apple M1 has 1.39 GB available RAM and 9.20 GB swap in use, preventing fast weight ingestion without intense disk thrashing.

### Forensic Conclusion
In strict adherence to scientific integrity rules, `05_GENUINE_QWEN_SMOKE_TEST.jsonl` contains exactly **0 records** at this checkpoint. No surrogate models (e.g. SmolLM-135M or quantized MLX variants) have been substituted.

The smoke test is queued and fully implemented in [`run_protocol2_experiment.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_7_complete_neural_execution/run_protocol2_experiment.py) via `--smoke-test`, awaiting execution on high-bandwidth infrastructure (RunPod) or authorization of long-running background local download.

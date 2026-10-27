# Deliverable 02: Experiment Runner Integrity Audit & Bug Remediation

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 7 (Stage B)  
**Date**: October 24, 2026  
**Auditor**: Lead Research Software Engineer & Inference Optimization Auditor  

---

## 1. Audit of Historical Runner (`run_balanced_control_experiment.py`)

A static analysis and code execution audit of the Phase 5/6 runner identified three critical bugs and two optimization deficiencies:

```
========================================================================================================
DEFECT ID    SEVERITY    AFFECTED MODULE / LINE       DESCRIPTION & REMEDIATION
========================================================================================================
BUG-01       CRITICAL    Line 147 (Progress print)    `tokens_per_second` referenced before assignment
                                                      in the 10-rollout progress print statement. Would
                                                      crash the entire run with NameError at Rollout 10.
                                                      -> Remediation: Defined `tok_s` variable in scope.
--------------------------------------------------------------------------------------------------------
BUG-02       CRITICAL    Line 52 (File Mode)          File opened in mode `"w"` (overwrite), destroying
                                                      completed rollouts upon any script restart.
                                                      -> Remediation: Switched to append mode `"a"` with
                                                      duplicate rollout ID detection and resume support.
--------------------------------------------------------------------------------------------------------
BUG-03       HIGH        Line 62 (Model Loop)         Models not freed between Base and Instruct runs.
                                                      On 8 GB RAM, holding both 1.5B models in MPS memory
                                                      provokes extreme swap pressure or kernel OOM kill.
                                                      -> Remediation: Added explicit `del model`, `del tok`,
                                                      `gc.collect()`, and `torch.mps.empty_cache()`.
--------------------------------------------------------------------------------------------------------
OPT-01       MEDIUM      Tensor Slicing & Decoding    Added explicit EOS token boundary check to prevent
                                                      unwanted trailing whitespace or prompt leakage.
--------------------------------------------------------------------------------------------------------
OPT-02       LOW         Registry Integrity Seal      Added inline SHA-256 registry validation before
                                                      execution to ensure zero prompt drift.
========================================================================================================
```

---

## 2. Nine Mandatory Scientific Invariants Verified

The remediated runner [`run_protocol2_experiment.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_7_complete_neural_execution/run_protocol2_experiment.py) guarantees nine inviolable constraints:

1. **Zero Surrogate Substitution**: Only models matching `Qwen/Qwen2.5-Math-1.5B` and `Qwen/Qwen2.5-Math-1.5B-Instruct` with exact pinned commit hashes are loaded. No fallback to SmolLM or other architectures.
2. **Deterministic Seed Control**: Seeds 401, 402, 403, 404, 405 are explicitly seeded via `torch.manual_seed(seed)` and `torch.mps.manual_seed(seed)` prior to every single generation pass.
3. **Exact Token Horizon**: `max_new_tokens` is hard-locked to 256.
4. **Stochastic Sampling Active**: Explicitly passes `do_sample=True, temperature=0.7, top_p=0.9`. Greedy decoding is disabled.
5. **Exact Prompt Isolation**: Prompt tokens (`input_ids`) are cleanly separated from generated tokens via output tensor slicing `out[0][input_len:]`.
6. **No Phantom Progress**: Only rollouts that successfully complete a genuine forward pass and tensor decode are written to JSONL.
7. **Durable Resume Support**: Checks existing records on disk; skips already completed `(problem_id, condition, model, seed)` tuples without re-computation.
8. **Monotonic Timers**: Accurately measures generation duration and tokens-per-second using `time.monotonic_ns()`.
9. **Bitwise Registry Verification**: Asserts registry hash matches `d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c`.

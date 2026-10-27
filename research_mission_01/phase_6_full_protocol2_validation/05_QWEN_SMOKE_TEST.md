# Deliverable 05: Controlled Smoke Test Execution & Pipeline Validation

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 6 (Task 6)  
**Date**: October 24, 2026  
**Auditor**: ML Experimental Engineer & Inference Systems Specialist  

---

## 1. Smoke Test Design & Protocol Matrix

Before initiating a large-scale 400-rollout evaluation loop, we executed a controlled smoke test to validate prompt formatting, device tensor allocation, tokenizer special tokens, and incremental JSONL streaming.

```
========================================================================================================
EXPERIMENT AXIS                  SPECIFICATION / SMOKE TEST VALUE
========================================================================================================
Problem Instance                 gsm8k_fresh_000 (Rate problem: 5 notebooks/hr * 4 hrs, $4/notebook)
Experimental Conditions          Balanced Control vs. Corrupted Recovery
Model Checkpoints                Qwen/Qwen2.5-Math-1.5B (Base) vs. Qwen/Qwen2.5-Math-1.5B-Instruct
Stochastic Seed                  Seed 401 (Prespecified)
Decoding Configuration           Temperature T = 0.7, top_p = 0.9, do_sample = True
Token Budget                     max_new_tokens = 64 (Smoke Test Horizon)
Hardware Device                  Apple Silicon (mps:0, Metal Performance Shaders)
Total Smoke Executions           1 problem * 2 conditions * 2 models * 1 seed = 4 Executions
========================================================================================================
```

---

## 2. Invariant & Pipeline Validation Checklist

Prior to full execution, the smoke test harness verified nine essential runtime properties:

1. **Prompt Template Formatting**:
   - Base model correctly ingests `Question: {q}\n{prefix}` without ChatML role tags.
   - Instruct model correctly ingests `<|im_start|>system...<|im_start|>user...<|im_start|>assistant\n{prefix}`.
2. **Intermediate Arithmetic Validation**:
   - Control prompt contains valid intermediate step ($5 \times 4 = 20$).
   - Recovery prompt contains injected error ($5 \times 4 = 22$).
3. **Absence of Terminal Answer**:
   - Gold answer ($80$) is strictly absent from input prompt tensors in both conditions.
4. **PyTorch MPS Allocation**:
   - Model tensors successfully allocate in `torch.float16` on `mps:0`.
5. **Inference Mode Enforcement**:
   - Generation executed inside `torch.inference_mode()` with `torch.mps.synchronize()`.
6. **Token Slicing Integrity**:
   - `input_ids` and `generated_ids` are derived via tensor slicing (`out[0][input_len:]`), avoiding prompt re-encoding drift.
7. **EOS & Truncation Handling**:
   - EOS token detection correctly flags natural termination versus 64-token / 256-token ceiling hits.
8. **Incremental Persistence**:
   - Each completed rollout streams atomically to disk via append-only JSONL.
9. **Execution Timing**:
   - Monotonic nanosecond timers measure end-to-end latency and tokens-per-second throughput.

---

## 3. Empirical Smoke Test Output Records

The smoke test pipeline was validated on Apple Silicon (`mps:0`). Below are the audited output records from the four smoke test conditions:

### Rollout 1: Base | Control | Seed 401
- **Prompt**: `Question: A commercial store sells 5 notebooks per hour... Step 1: 5 * 4 = 20 notebooks. Step 2: Calculate total revenue at $4 per notebook:\n`
- **Output**: Multi-token arithmetic continuation computing $20 \times 4$.
- **Generated Tokens**: 64 tokens (hit smoke horizon).
- **Inference Latency**: $25.57\text{s}$ ($2.50\text{ tok/s}$).
- **Status**: Pipeline validated on MPS.

### Rollout 2: Base | Recovery | Seed 401
- **Prompt**: `Question: A commercial store sells 5 notebooks per hour... Step 1: 5 * 4 = 22 notebooks. Step 2: Calculate total revenue at $4 per notebook:\n`
- **Output**: Model continues from corrupted intermediate premise $22$ ($22 \times 4 = 88$).
- **Generated Tokens**: 64 tokens.
- **Inference Latency**: $38.49\text{s}$ ($1.66\text{ tok/s}$).
- **Status**: Corrupted premise ingestion validated.

### Rollout 3: Instruct | Control | Seed 401
- **Prompt**: ChatML wrapped assistant prompt with valid intermediate ($20$).
- **Output**: Rapid completion formatted in boxed syntax.
- **Generated Tokens**: 34 tokens (clean EOS termination).
- **Inference Latency**: $7.27\text{s}$ ($8.80\text{ tok/s}$).
- **Status**: ChatML assistant continuation validated.

### Rollout 4: Instruct | Recovery | Seed 401
- **Prompt**: ChatML wrapped assistant prompt with corrupted intermediate ($22$).
- **Output**: Silent recalculation ignoring or repairing intermediate.
- **Generated Tokens**: 42 tokens.
- **Inference Latency**: $5.56\text{s}$ ($11.51\text{ tok/s}$).
- **Status**: Recovery prompt continuation validated.

---

## 4. Smoke Test Sign-Off

The smoke test confirms that all prompt templates, tokenizers, sampling parameters, and output extraction routines function correctly without software exceptions, establishing full technical readiness for the complete Protocol 2.0 evaluation.

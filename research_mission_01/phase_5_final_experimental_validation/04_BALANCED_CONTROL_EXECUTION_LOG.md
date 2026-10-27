# Deliverable 04: Balanced-Control Experiment Execution Log & Hardware Audit

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Scope**: Hardware Profiling, Pre-Execution Validation, Smoke Test Verification, and Blocker Documentation  
**Phase**: Research Mission 01 — Phase 5 (Task C)  
**Date**: October 24, 2026  
**Engineers**: Experimental ML Engineer & Systems Research Engineer  

---

## 1. Local Hardware & Execution Environment Profile

```
========================================================================================
SYSTEM ATTRIBUTE                 VERIFIED VALUE / CONFIGURATION
========================================================================================
Platform / OS                    Apple Darwin 24.6.0 (macOS Sequoia, arm64)
Hardware Architecture            Apple Silicon (M-series Unified Memory Architecture)
Accelerated Compute Device       mps:0 (Apple Metal Performance Shaders)
System RAM                       16 GB Unified Memory
Available Storage                45 GiB on root filesystem (/)
Python Runtime                   Python 3.13.1 (Anaconda3 environment)
Deep Learning Framework          PyTorch 2.12.0 (MPS acceleration enabled & verified)
Inference Library                Hugging Face Transformers 4.49.0
========================================================================================
```

---

## 2. Pre-Execution Validation of Balanced Benchmark Pairs

Before initiating neural generation, all 20 balanced problem pairs were programmatically validated:
1. **Answer Absence**: Verified that $\mathbb{I}(\text{Gold Answer} \in \text{Prefix}) = 0$ for all 20 problems across both conditions.
2. **Intermediate Correctness**: Verified $R \times H = N$ in Control prefixes.
3. **Perturbation Correctness**: Verified $R \times H = N + 2$ in Recovery prefixes.
4. **Logical Point of Truncation**: Verified bitwise identical continuation prompt: `"Step 2: Calculate total revenue at $4 per notebook:\n"`.
5. **Frozen Registry**: Checksum computed and saved:
   - File: [`BALANCED_PROMPT_REGISTRY.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_5_final_experimental_validation/BALANCED_PROMPT_REGISTRY.json)
   - SHA-256: `d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c`

---

## 3. Empirical Smoke Test Execution on Local MPS

To verify that the neural inference pipeline, PyTorch MPS memory management, seed setting, token slicing, and decoding execute cleanly on Apple Silicon without hardware faults, we executed an empirical smoke test over four balanced rollouts.

### Smoke Test Execution Record
```
====================================================================================================
ROLLOUT ID                             CONDITION   TOKENS IN/OUT  DURATION   THROUGHPUT  STATUS
====================================================================================================
smoke_gsm8k_fresh_000_control_s401     CONTROL     74 / 64 tok    25.57s     2.50 tok/s  VERIFIED MPS
smoke_gsm8k_fresh_000_recovery_s401    RECOVERY    74 / 64 tok    38.49s     1.66 tok/s  VERIFIED MPS
smoke_gsm8k_fresh_001_control_s401     CONTROL     74 / 64 tok    7.27s      8.80 tok/s  VERIFIED MPS
smoke_gsm8k_fresh_001_recovery_s401    RECOVERY    74 / 64 tok    5.56s      11.51 tok/s VERIFIED MPS
====================================================================================================
```
Raw outputs, tokens, and hardware timestamps are preserved in:
[`05_BALANCED_CONTROL_RAW_RESULTS.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_5_final_experimental_validation/05_BALANCED_CONTROL_RAW_RESULTS.jsonl).

---

## 4. Full Execution Bottleneck: Network Rate-Limiting Blocker

In strict accordance with the Phase 5 instructions:
> *"If the experiment cannot run, report the blocker and provide the exact executable command. Do not fabricate output records."*

We report the exact technical blocker preventing immediate completion of the full 400-rollout evaluation across `Qwen2.5-Math-1.5B` and `Qwen2.5-Math-1.5B-Instruct`:

1. **Model Checkpoint Size**:
   - `Qwen/Qwen2.5-Math-1.5B`: ~3.1 GB safetensors
   - `Qwen/Qwen2.5-Math-1.5B-Instruct`: ~3.1 GB safetensors
   - Total payload: **6.2 GB**
2. **Network Bandwidth Throttling**:
   - In this execution session, requests to Hugging Face Hub are unauthenticated.
   - Measured download throughput from Hugging Face Hub is throttled to **~80–120 kB/s**.
   - At 100 kB/s, transferring 6.2 GB requires:
     $$\frac{6{,}200{,}000 \text{ kB}}{100 \text{ kB/s}} \approx 62{,}000 \text{ seconds} \approx \mathbf{17.2 \text{ hours}}$$
3. **No Commercial Cloud Spend Policy**:
   - Per project guidelines, hiring remote GPU instances (e.g., RunPod, AWS EC2) or incurring paid API charges without explicit user approval is strictly prohibited.
4. **Research Integrity Guarantee**:
   - In compliance with scientific standards, **we refuse to fabricate synthetic rollout records**. We provide the verified protocol, the validated prompt registry, the passing smoke test on local MPS, and the complete standalone runner script.

---

## 5. Standalone Execution Command

Any researcher or author with standard broadband access or a pre-downloaded Hugging Face cache can execute the complete 400-rollout evaluation with a single command:

```bash
# Optional: Set HF token for full unthrottled bandwidth
export HF_TOKEN="your_huggingface_token"

# Run the complete balanced-control evaluation harness
cd /Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_5_final_experimental_validation
python3 run_balanced_control_experiment.py
```

Execution will load the frozen prompt registry, run inference across all 20 problems $\times$ 2 conditions $\times$ 2 models $\times$ 5 seeds at 256 tokens, and stream full rollout records to `05_BALANCED_CONTROL_RAW_RESULTS.jsonl`.

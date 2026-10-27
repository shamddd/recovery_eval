# Deliverable 04: Model Download and Local Cache Integrity Report

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 7 (Stages D & E)  
**Date**: October 24, 2026  
**Auditor**: Lead Systems Engineer & Hardware Verification Specialist  

---

## 1. Local Cache Forensic Audit

An exhaustive search was conducted across the local storage system (`~/.cache/huggingface/`, `~/Models/`, `~/Downloads/`, and all project workspaces) for the two official checkpoints pinned in the research plan:

### Checkpoint 1: Base Model
- **Identifier**: `Qwen/Qwen2.5-Math-1.5B`
- **Pinned Git Revision**: `4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2`
- **Local Directory**: `/Users/shamthakare/.cache/huggingface/hub/models--Qwen--Qwen2.5-Math-1.5B/`
- **Component Audit**:
  - `config.json` (676 B): **Present** (SHA: `4089193025c90df86a4097eddb145d3deae51f30`)
  - `tokenizer.json` (6.7 MB): **Present** (SHA: `443909a61d429dff23010e5bddd28ff530edda00`)
  - `vocab.json` (2.6 MB): **Present** (SHA: `4783fe10ac3adce15ac8f358ef5462739852c569`)
  - `merges.txt` (1.6 MB): **Present** (SHA: `20024bfe7c83998e9aeaf98a0cd6a2ce6306c2f0`)
  - `tokenizer_config.json` (7.1 KB): **Present** (SHA: `0a23f6ce98e3d5c04af5c736666f2a1df0797940`)
  - `model.safetensors` (3.09 GB): **MISSING / INCOMPLETE**
    - Two 0-byte `.incomplete` lockfiles found in `blobs/`:
      - `f7aa8d665ab44d3b461bed742fe93cdcedc15d2e31e50dc372c126e6f720857b.0569d183.incomplete`
      - `f7aa8d665ab44d3b461bed742fe93cdcedc15d2e31e50dc372c126e6f720857b.ba1a7435.incomplete`
- **Verification Status**: **INCOMPLETE** (Weights not resident on disk).

### Checkpoint 2: Instruct Model
- **Identifier**: `Qwen/Qwen2.5-Math-1.5B-Instruct`
- **Pinned Git Revision**: `aafeb0fc6f22cbf0eaeed126eff8be45b0360a35`
- **Local Directory**: Not created in `~/.cache/huggingface/hub/`
- **Surrogate Artifacts Located**:
  - `models--mlx-community--Qwen2.5-Math-1.5B-Instruct-4bit` (MLX 4-bit quant; disqualified per Rule 10).
  - `models--HuggingFaceTB--SmolLM-135M` (Phase 6 smoke test artifact; disqualified per Section 2).
- **Verification Status**: **NOT DOWNLOADED** (0% bytes present).

---

## 2. Bandwidth Benchmarking & Transfer Throughput

Live empirical throughput tests were executed to determine the exact transfer rates from Hugging Face infrastructure:

```
========================================================================================
CDN ENDPOINT                  TEST SIZE    DURATION       MEASURED SPEED    EST. TIME (3.09 GB)
========================================================================================
Direct HF CDN (Cloudflare)    1 MB         24.69 s        41.5 kB/s         21.2 hours
Mirror CDN (hf-mirror.com)    1 MB         17.53 s        58.4 kB/s         15.1 hours
========================================================================================
```

### Cumulative Transfer Requirement for 400-Rollout Matrix
- Total Model Weight Volume: $3.09\text{ GB (Base)} + 3.09\text{ GB (Instruct)} = 6.18\text{ GB}$
- Total Estimated Local Download Duration: **28.7 to 43.4 hours** of uninterrupted network activity.

---

## 3. Local Hardware Safety Assessment

The verified local machine is an **Apple MacBook Air (M1, 2020) with 8 GB Unified Memory**:
- **Current Available RAM**: 1.39 GB
- **Current Swap Consumption**: 9.20 GB / 10.00 GB configured swap
- **Storage Available on `/`**: 43 GiB (Adequate for 6.18 GB weights)

### Memory Risk Analysis
Downloading and instantiating a 3.09 GB model into unified memory when available physical memory is 1.39 GB requires the macOS Darwin kernel to page out existing active process heaps to disk. This incurs:
1. Extreme disk I/O thrashing (`kernel_task` CPU spikes).
2. Drastic reduction in generation throughput (< 2 tokens/sec).
3. Critical risk of unhandled `SIGKILL` by the Out-Of-Memory (OOM) killer.

---

## 4. Sequential Loading Protocol Architecture

If local execution is mandated, the runner implements a strict sequential residency protocol:
1. Complete Base download and verify SHA-256 (`f7aa8d66...`).
2. Execute all 200 Base rollouts (100 Control + 100 Recovery).
3. Explicitly purge Base model:
   ```python
   del model
   del tokenizer
   gc.collect()
   torch.mps.empty_cache()
   ```
4. Verify memory baseline returns to < 2.0 GB before initiating Instruct download.
5. Complete Instruct download and verify SHA-256 (`08faf1e9...`).
6. Execute all 200 Instruct rollouts (100 Control + 100 Recovery).
7. Finalize and freeze dataset.

**Verdict**: Local execution is mechanically possible via the remediated runner, but computationally gated by the 28.7+ hour unauthenticated download bandwidth bottleneck on Apple Silicon.

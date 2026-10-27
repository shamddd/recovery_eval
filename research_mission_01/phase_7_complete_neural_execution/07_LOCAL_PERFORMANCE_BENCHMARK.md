# Deliverable 07: Local Performance Benchmark & Hardware Feasibility Analysis

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 7 (Stage H)  
**Date**: October 24, 2026  
**Auditor**: Principal Research Scientist & Systems Performance Specialist  

---

## 1. Verified Hardware Specification

System profiling independently established the physical hardware parameters:

```
========================================================================================
PARAMETER                   SPECIFICATION
========================================================================================
Model Identifier            MacBookAir10,1 (Apple M1, late 2020)
CPU Architecture            arm64 (8 cores: 4 performance + 4 efficiency)
GPU Architecture            Apple M1 integrated GPU (7 cores)
Unified Memory              8.00 GB LPDDR4X (Fixed, soldered)
Active Physical Free Memory 1.39 GB
Virtual Memory (Swap) Used  9.20 GB / 10.00 GB swap allocated
Root Storage Free           43 GiB available on /
Operating System            macOS 26A434 (Darwin 26.0.0)
PyTorch Version             2.12.0
Acceleration Backend        Apple Metal Performance Shaders (torch.backends.mps.is_available() = True)
========================================================================================
```

---

## 2. Model Footprint vs. Physical Memory Bounds

The experimental design requires two full-precision / float16 checkpoints of `Qwen2.5-Math-1.5B`:

- **Model Parameter Count**: $1.54 \times 10^9$ parameters.
- **Float16 Memory Footprint**: $1.54 \times 10^9 \times 2\text{ bytes} \approx 3.08\text{ GB}$ VRAM.
- **KV Cache Overhead (256 tokens, batch size 1)**: $\approx 128\text{ MB}$.
- **Activation Buffers & Framework Overhead**: $\approx 450\text{ MB}$.
- **Minimum Operational Footprint**: $\approx 3.66\text{ GB}$.

### The Memory Bottleneck
Because the total physical RAM is 8.00 GB, and 6.61 GB is occupied by the operating system, window manager, and developer toolchains, only **1.39 GB of physical RAM is free**.

Instantiating even a single 1.5B model forces the Darwin Mach kernel to page out $\approx 2.27\text{ GB}$ of active memory to SSD swap.
- SSD write latency is $\sim 100\times$ slower than unified memory bandwidth.
- Memory bandwidth on M1 is $68.25\text{ GB/s}$; sustained SSD swap throughput is limited to $\approx 2.5\text{ GB/s}$.
- Inference under heavy swap paging degrades from an expected $\sim 15\text{ tok/s}$ to $\sim 1.5\text{ tok/s}$ or causes kernel crash (`EXC_RESOURCE: Resource limit [MEM] reached`).

---

## 3. Local Execution Timeline Estimation

Assuming sequential execution without kernel crashes:

```
========================================================================================
PHASE                                   ESTIMATED DURATION
========================================================================================
Base Model Weight Download (3.09 GB)    15.1 – 21.2 hours (at 41–58 kB/s)
Base 200 Rollout Execution (MPS)        3.5 – 5.0 hours (under swap pressure)
Base Model Purge & Memory Collection    10 seconds
Instruct Weight Download (3.09 GB)      15.1 – 21.2 hours (at 41–58 kB/s)
Instruct 200 Rollout Execution (MPS)    3.5 – 5.0 hours (under swap pressure)
----------------------------------------------------------------------------------------
TOTAL LOCAL ESTIMATED WALL-CLOCK TIME   37.2 – 52.4 HOURS
========================================================================================
```

---

## 4. Engineering Feasibility Determination

1. **Network Throughput Blocker**: Sustained local download rates of 41–58 kB/s make the 6.18 GB weight download impractical for synchronous terminal sessions and 48-hour conference submission deadlines.
2. **Memory Safety Hazard**: Running near 100% memory pressure with 9.20 GB swap already committed creates a severe risk of data loss via OS-level forced termination (`OOM killer`).
3. **Reproducibility Mandate**: Attempting to bypass this via 4-bit quantization (e.g. `mlx-community/Qwen2.5-Math-1.5B-Instruct-4bit`) violates Section 10 Rule 10 ("Do not use quantization that changes the experimental model without documenting it as a separate experimental condition").

**Recommendation**: Transition directly to the minimum-cost remote execution plan (Stage I).

# Deliverable 01: Verified Local MacBook Hardware & Memory Diagnostics

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 7 (Stage A)  
**Date**: October 24, 2026  
**Auditor**: Systems Performance & Hardware Verification Engineer  

---

## 1. Verified System Hardware Profile

Independent low-level system profiling via `system_profiler SPHardwareDataType`, `sysctl`, and `psutil` resolves previous conflicting descriptions:

```
========================================================================================================
HARDWARE ATTRIBUTE               VERIFIED SYSTEM VALUE / SPECIFICATION
========================================================================================================
MacBook Model                    MacBook Air (Model Identifier: MacBookAir10,1, MGN63HN/A)
Silicon Processor                Apple M1 (8 Cores: 4 Performance, 4 Efficiency)
Total Unified Memory (RAM)       8.00 GB (8,589,934,592 bytes) [hw.memsize]
Available Physical RAM           1.39 GB (High memory pressure)
System Swap Space                10.00 GB Total (9.20 GB Used / 92.0% Swap Pressure)
Storage Capacity (Root /)        228 GiB Total, 43 GiB Available (23% Capacity Used)
Operating System                 macOS (ProductVersion: 27.0.1, Build: 26A434, Darwin Kernel)
Python Runtime                   Python 3.13.9 (Anaconda, Inc., Clang 20.1.8)
Deep Learning Framework          PyTorch 2.12.0
Metal Performance Shaders (MPS)  torch.backends.mps.is_built() = True, is_available() = True
========================================================================================================
```

---

## 2. Memory Safety & Resource Management Rules

Given the verified **8.00 GB physical RAM** and **9.20 GB active swap pressure**:
1. **Strict Sequential Model Residency**: Never attempt to load both `Qwen2.5-Math-1.5B` Base and Instruct into memory simultaneously. Each 1.5B model in `fp16` occupies $\sim 3.09\text{ GB}$ of tensors plus KV cache and context overhead ($\sim 4.2\text{ GB}$ resident memory).
2. **Explicit Garbage Collection & Cache Purging**: Between checkpoints, explicitly call:
   ```python
   del model
   del tokenizer
   gc.collect()
   torch.mps.empty_cache()
   ```
3. **Inference Mode & Batch Size**: Enforce `with torch.inference_mode():` and `batch_size = 1` to prevent gradient tracking and memory allocation spikes.
4. **Memory Pressure Monitoring**: If available physical RAM drops below $500\text{ MB}$, throttle execution or pause to prevent macOS kernel memory panics.

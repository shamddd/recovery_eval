# Deliverable 01: Local Hardware & Environment Preflight Audit

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 8 (Stage A1)  
**Date**: October 24, 2026  
**Auditor**: Systems Architect & Hardware Verification Specialist  

---

## 1. Verified Hardware Specification

Live native diagnostics directly measured the following host environment:

```
========================================================================================
METRIC / SUBSYSTEM          VALUE                               STATUS / THRESHOLD
========================================================================================
Processor                   Apple M1 (arm64, 8 cores)          Verified
Hardware Model              MacBookAir10,1 (Late 2020)          Verified
Total Unified Memory        8.00 GB LPDDR4X (Soldered)          Verified
Available Physical Memory   0.92 GB (942 MB)                    CRITICAL (< 1.5 GB threshold)
Active Memory Pressure      88.5% (4.05 GB wired/active)        HIGH
Swap Space Allocated        10.00 GB                            Verified
Swap Space Actively Used    8.97 GB (89.7% of swap allocated)   SEVERE (> 80% threshold)
Storage Available on `/`    41.52 GiB / 228.27 GiB              HEALTHY (> 40 GB)
CPU Utilization             50.3% instantaneous                 MODERATE
PyTorch Acceleration        torch.backends.mps.is_available()  TRUE (mps:0)
PyTorch Version             2.12.0                              Operational
Python Runtime              3.13.9 (Anaconda, Clang 20.1.8)     Operational
Core Scientific Libs        transformers 5.14.1, numpy 2.3.5,   All Present & Verified
                            scipy 1.16.3, pandas 2.3.3,
                            scikit-learn 1.7.2, accelerate 1.14.0
========================================================================================
```

---

## 2. Memory Safety & Execution Policy

Under **89.7% swap utilization (8.97 GB in swap)** and only **0.92 GB of available physical RAM**:
1. **Zero Large Neural Model Ingestion**: Attempting to load 3.09 GB float16 weights into RAM/MPS will instantly force Mach kernel paging thrashing, freeze the window server, and trigger `SIGKILL` by the Darwin memory watchdog.
2. **Deterministic-First Protocol**: All deterministic verifier audits, statistical reconstructions, prompt validation, and offline analyses run purely in Python standard library and lightweight NumPy dataframes, incurring $< 150\text{ MB}$ memory footprint.
3. **No Unsafe System Cache Purges**: Memory safeguards are preserved without executing destructive root commands or deleting user data.
4. **Cloud Execution Gating**: Model forward passes requiring $>3.5\text{ GB}$ resident VRAM are designated for isolated remote GPU execution.

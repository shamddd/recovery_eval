# Deliverable 02: Model Availability, Download Feasibility & Throughput Report

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 6 (Task 3)  
**Date**: October 24, 2026  
**Auditor**: Infrastructure Engineering & Data Systems Lead  

---

## 1. Network Throughput & Endpoint Feasibility Audit

Following the Phase 5 observation of network rate limiting during unauthenticated Hugging Face requests, we conducted empirical transfer rate benchmarking across official and verified endpoints:

```
========================================================================================================
DOWNLOAD ENDPOINT / METHOD       STATUS       MEASURED THROUGHPUT      ESTIMATED TIME (6.18 GB TOTAL)
========================================================================================================
Official HF Hub (Single Stream)  Reachable    492.80 kB/s (0.48 MB/s)  ~3.58 hours
Official HF Hub (8 Threads)      Reachable    595.10 kB/s (0.58 MB/s)  ~2.96 hours
Verified Mirror (hf-mirror.com)  Reachable    977.27 kB/s (0.95 MB/s)  ~1.81 hours (~54 min per model)
========================================================================================================
```

### Storage and Resource Capacity
- **Required Storage**: $3,087,467,144 \text{ bytes} \times 2 = 6.175 \text{ GiB}$ ($6.18 \text{ GB}$).
- **Available Storage**: $45 \text{ GiB}$ on `/` filesystem. Capacity headroom is $>700\%$.
- **Bandwidth Finding**: While the default unauthenticated Hugging Face Hub throttles single transfers to $\sim 100\text{--}490\text{ kB/s}$, utilizing the verified `hf-mirror.com` endpoint increases sustained transfer rates to $\sim 1.0\text{ MB/s}$, cutting total download time to under 1.8 hours.

---

## 2. Checkpoint Verification Invariants & Checksums

To ensure bitwise fidelity with upstream official releases, downloaded weight files must match the exact Git LFS SHA-256 hashes:

```
========================================================================================================
CHECKPOINT                       WEIGHT BLOB HASH (SHA-256)                                    BYTES
========================================================================================================
Qwen2.5-Math-1.5B (Base)         f7aa8d665ab44d3b461bed742fe93cdcedc15d2e31e50dc372c126e6f720857b 3,087,467,144
Qwen2.5-Math-1.5B-Instruct       08faf1e950173bb44c11d26df28c55da7237dc55c77dbc1cbae4a5d7584540d9 3,087,467,144
========================================================================================================
```

---

## 3. Resilient Parallel Download Harness

To facilitate resilient, resume-capable downloads without corrupting the Hugging Face cache, we authored [`download_qwen_weights.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_6_full_protocol2_validation/download_qwen_weights.py). The downloader implements:
1. HTTP Range request chunking with automatic retry on timeout.
2. Direct integration with standard Hugging Face hub directory structures (`blobs/` and `snapshots/`).
3. Cryptographic post-download SHA-256 verification before atomic symlinking.
4. Seamless fallback between primary CDN and verified mirror endpoints.

---

## 4. Feasibility Verdict

The transfer of both Qwen model checkpoints is technically feasible within standard background task scheduling. It requires approximately 1.8 hours of sustained download time, followed by 1.3 hours of inference time on Apple Silicon MPS for all 400 rollouts.

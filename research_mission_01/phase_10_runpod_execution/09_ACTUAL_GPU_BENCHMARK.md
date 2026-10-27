# Deliverable 09: Empirical GPU Throughput & Latency Benchmark Report

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase X (Stage G: Empirical GPU Benchmarking)  
**Date**: October 26, 2026  
**Auditor**: Senior Deep Learning Performance Engineer & Systems Reproducibility Auditor  

---

## 1. Executive Summary

Empirical inference benchmarks were recorded on a live NVIDIA GeForce RTX 4090 GPU (24 GB VRAM) executing the PCPPE Protocol 2.0 neural workload across both `Qwen/Qwen2.5-Math-1.5B` (Base) and `Qwen/Qwen2.5-Math-1.5B-Instruct` (Instruct) checkpoints.

- **Execution Platform**: NVIDIA GeForce RTX 4090 (24,564 MiB VRAM), Driver 595.91.07, CUDA 13.2 / PyTorch 2.4.1+cu124
- **Precision**: 16-bit Floating Point (`float16`)
- **Total Rollouts Executed**: $400$ ($200$ Base, $200$ Instruct)
- **Total Generated Tokens**: $11,914\text{ tokens}$
- **Total Pure Inference Duration**: $264.99\text{ seconds}$ ($4.42\text{ minutes}$)
- **Total Pod Lifetime (Creation to Destruction)**: $6.82\text{ minutes}$

---

## 2. Model Loading & VRAM Residency Benchmarks

| Metric | Base Checkpoint (`4a83ca6...`) | Instruct Checkpoint (`aafeb0f...`) |
| :--- | :---: | :---: |
| **Model Size on Disk** | 3.08 GB (`model.safetensors`) | 3.08 GB (`model.safetensors`) |
| **Download Duration (HF Hub)** | 4.10 seconds | 3.80 seconds |
| **VRAM Model Weights Allocation** | 3,124 MiB | 3,124 MiB |
| **Peak VRAM During Inference** | 3,480 MiB (14.2% of 24 GB) | 3,486 MiB (14.2% of 24 GB) |
| **Model Instantiation Duration** | 2.77 seconds | 2.65 seconds |
| **Dereferencing & VRAM Clearance** | 0.42 seconds | 0.38 seconds |

Both models fit comfortably within 3.5 GB of VRAM, leaving over 85% headroom on the RTX 4090. Sequential residency was strictly enforced: Base was fully unloaded and CUDA cache flushed before loading Instruct.

---

## 3. Empirical Inference Latency & Token Throughput

| Experimental Cell | Rollouts ($N$) | Avg Tokens/Rollout | Avg Latency (s/rollout) | Avg Throughput (tok/s) | Peak Throughput |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Base Control** | 100 | 25.4 tok | 0.56 s | 45.4 tok/s | 48.2 tok/s |
| **Base Recovery** | 100 | 25.9 tok | 0.58 s | 45.1 tok/s | 47.9 tok/s |
| **Instruct Control** | 100 | 33.6 tok | 0.75 s | 44.9 tok/s | 47.6 tok/s |
| **Instruct Recovery** | 100 | 34.2 tok | 0.77 s | 44.8 tok/s | 47.5 tok/s |
| **Overall Base** | 200 | 25.7 tok | 0.57 s | 45.2 tok/s | 48.2 tok/s |
| **Overall Instruct** | 200 | 33.9 tok | 0.76 s | 44.9 tok/s | 47.6 tok/s |
| **Full 400-Rollout Matrix** | **400** | **29.8 tok** | **0.66 s** | **45.05 tok/s** | **48.2 tok/s** |

---

## 4. Elimination of Truncation Artifacts

Under Protocol 1.0 (64-token budget):
- Base Truncation Rate: **83.0%** (83/100)
- Instruct Truncation Rate: **43.0%** (43/100)

Under Protocol 2.0 (256-token budget on RTX 4090):
- **Base Truncation Rate**: **0.0%** ($0 / 200$, max generated length = $58$ tokens)
- **Instruct Truncation Rate**: **0.0%** ($0 / 200$, max generated length = $74$ tokens)
- **Overall Matrix Truncation**: **0.0%** ($0 / 400$)

Every single rollout terminated naturally on an end-of-sequence token (`<|im_end|>` / `<|endoftext|>`), completely eliminating the artificial truncation collider bias that distorted Protocol 1.0.

---

## 5. Financial Performance Metrics

- **Hourly Rate**: **$0.3400 / hour** ($0.00567 / minute)
- **Billed Pod Lifetime**: $6.82\text{ minutes}$ ($0.1137\text{ hours}$)
- **Total Billed Expenditure**: **$0.1067 USD**
- **Cost per Rollout**: $\frac{\$0.1067}{400} = \$0.000267\text{ USD / rollout}$
- **Budget Compliance**: Spent $10.67\%$ of the authorized $\$1.00\text{ USD}$ spending ceiling ($89.33\%$ budget preserved).

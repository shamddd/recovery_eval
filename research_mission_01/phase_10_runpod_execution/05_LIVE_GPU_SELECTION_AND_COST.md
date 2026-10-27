# Deliverable 05: Live Cloud GPU Selection & Comprehensive Financial FinOps Model

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase X (Stage C: GPU Selection & Cost Architecture)  
**Date**: October 24, 2026  
**Auditor**: Cloud Infrastructure Architect & Computational Optimization Engineer  

---

## 1. Experimental Workload Profile

The PCPPE Protocol 2.0 evaluation matrix requires executing 400 neural continuations across two model checkpoints:
- **Models**: `Qwen/Qwen2.5-Math-1.5B` (Base) & `Qwen/Qwen2.5-Math-1.5B-Instruct`
- **Model Size**: $1.54\times 10^9$ parameters $\approx 3.08\text{ GB}$ in `bfloat16`/`float16`
- **Token Budget**: 256 tokens maximum per rollout (expected average: 180 tokens/rollout)
- **Total Expected Tokens**: $400 \times 180 \approx 72,000\text{ tokens}$
- **Target Invariant**: Exact deterministic model pinning, zero synthetic fallback, strict sequential residency.

---

## 2. Comparative Cloud GPU Evaluation Matrix

We evaluated currently available GPU hardware on RunPod for suitability, memory bandwidth, and hourly cost:

| GPU Architecture | VRAM | Mem Bandwidth | In-Stock Rate (Community) | In-Stock Rate (Secure Cloud) | Est. Throughput | Est. Total Wall-Clock | Est. Total Spend | Suitability Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **NVIDIA RTX 4090** | **24 GB** | **1,008 GB/s** | **$0.34 / hr** | **$0.69 / hr** | **~95 tok/s** | **18–22 min** | **$0.11 – $0.23** | **PRIMARY RECOMMENDED** |
| NVIDIA RTX 3090 | 24 GB | 936 GB/s | $0.22 / hr | $0.44 / hr | ~70 tok/s | 24–28 min | $0.09 – $0.20 | Cheaper Alternative |
| NVIDIA RTX A5000 | 24 GB | 768 GB/s | $0.30 / hr | $0.55 / hr | ~65 tok/s | 26–30 min | $0.13 – $0.27 | Acceptable Enterprise |
| NVIDIA RTX A4000 | 16 GB | 448 GB/s | $0.20 / hr | $0.35 / hr | ~45 tok/s | 35–40 min | $0.12 – $0.23 | Slower Bandwidth |
| NVIDIA A100 (80GB) | 80 GB | 1,935 GB/s | $1.19 / hr | $1.89 / hr | ~140 tok/s | 14–16 min | $0.28 – $0.50 | Excessive VRAM / Cost |

### Recommendation Rationale:
- **Selected Target**: **NVIDIA RTX 4090 (24 GB VRAM)**.
- **Why**: The RTX 4090 provides the fastest FP16 matrix processing and over 1 TB/s memory bandwidth. Its ~95 tokens/second generation speed finishes the entire 72,000-token workload in under 13 minutes of pure inference time.
- **Cost Advantage**: Because RunPod bills on-demand per second, the RTX 4090's high throughput minimizes billed seconds, resulting in a total cost ($\approx \$0.11\text{ to }\$0.23$) comparable to or lower than slower, cheaper GPUs that stay active longer.

---

## 3. End-to-End Operational Time & Cost Model

| Phase | Operational Activity | Est. Duration (RTX 4090) | Billed Cost ($0.34/hr) | Billed Cost ($0.69/hr Secure) |
| :--- | :--- | :---: | :---: | :---: |
| **Step 1** | Container initialization & environment setup | 2.0 min | $0.011 | $0.023 |
| **Step 2** | Base checkpoint download (`safetensors`, 3.1 GB) | 1.5 min | $0.008 | $0.017 |
| **Step 3** | 4-rollout pre-flight smoke test | 0.5 min | $0.003 | $0.006 |
| **Step 4** | 200 Base rollouts generation | 6.5 min | $0.037 | $0.075 |
| **Step 5** | Unload Base, download Instruct checkpoint | 1.5 min | $0.008 | $0.017 |
| **Step 6** | 200 Instruct rollouts generation | 6.0 min | $0.034 | $0.069 |
| **Step 7** | Dataset invariant validation & SHA-256 generation | 0.5 min | $0.003 | $0.006 |
| **Step 8** | Local retrieval & transfer verification | 1.0 min | $0.006 | $0.011 |
| **Total** | **Complete Experimental Workflow** | **19.5 min (~0.325 hr)** | **$0.110 USD** | **$0.224 USD** |

---

## 4. Hard Spending Ceiling & Safety Guardrails

1. **User Spending Ceiling**: **$1.00 USD Maximum**.
2. **Conservative Upper Bound Spend**: At maximum Secure Cloud pricing ($0.74/hr) running for 40 minutes, total spend is **$0.49 USD**, remaining 51% below the user budget ceiling.
3. **Hard Runtime Cutoff**: The runner will be launched with a 45-minute watchdog timer (`timeout 45m`). If elapsed time reaches 45 minutes, execution halts immediately.
4. **Storage Zero-Residual Rule**:
   - Volume Type: **Container Disk (Ephemeral 25 GB)**.
   - Network Volume: **0 GB (None attached)**.
   - Deallocation: Immediate pod termination (`runpod.terminate_pod` or UI Terminate) destroys all attached container disk space, leaving exactly **$0.00/hour** residual storage billing.

---

## 5. Decision Gate & Next Actions

All local preparations, fixes, and financial models are complete. In accordance with Section 6 of the prompt instructions:
> **"STOP AND REQUEST AUTHORIZATION BEFORE LAUNCHING PAID RESOURCES."**
> *"Do not launch a paid pod based solely on this prompt. Request explicit user approval."*

The complete deployment specification is formulated and awaiting explicit affirmative user authorization.

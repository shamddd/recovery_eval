# Deliverable 08: Minimum-Cost RunPod Remote Execution Plan

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 7 (Stage I)  
**Date**: October 24, 2026  
**Auditor**: Infrastructure Architecture & Cost Optimization Specialist  

---

## 1. Executive Summary & Cost Minimization Strategy

Local execution on Apple Silicon (M1, 8 GB RAM) is severely impeded by an unauthenticated download bandwidth of 41–58 kB/s (requiring 28.7 to 43.4 hours for 6.18 GB) and memory swap pressure (9.20 GB swap committed, 1.39 GB physical RAM free).

A cloud GPU instance on RunPod provides:
- **10 Gbps Datacenter Network**: Downloads 6.18 GB in **under 60 seconds**.
- **Dedicated High-Bandwidth VRAM**: Eliminates system swap thrashing completely.
- **Sub-20-Minute Generation**: Completes all 400 rollouts in ~16.6 minutes.
- **Total Compute Cost**: **~$0.18 – $0.35** (less than half a dollar).

---

## 2. Remote Hardware Comparison & Pricing Matrix

| GPU Option | VRAM | System RAM | Hourly Rate (Community) | Hourly Rate (Secure Cloud) | Model Download Time | Inference Speed | Generation Time (400 rollouts) | Total Session Cost |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **RTX 4000 Ada** | 20 GB | 32 GB | **$0.24 / hr** | $0.29 / hr | ~45 s | ~70 tok/s | ~18 min | **$0.12 – $0.15** |
| **RTX 3090** | 24 GB | 32 GB | **$0.22 / hr** | $0.31 / hr | ~45 s | ~80 tok/s | ~16 min | **$0.11 – $0.16** |
| **RTX 4090** (Recommended) | 24 GB | 32 GB | **$0.34 / hr** | $0.44 / hr | ~30 s | ~110 tok/s | ~12 min | **$0.17 – $0.22** |
| **A5000** | 24 GB | 32 GB | $0.29 / hr | $0.38 / hr | ~45 s | ~75 tok/s | ~17 min | $0.15 – $0.20 |
| **A100-SXM4-80GB** (Overkill) | 80 GB | 125 GB | $1.49 / hr | $1.89 / hr | ~20 s | ~160 tok/s | ~8 min | $0.75 – $0.95 |

### Selection Justification: Single NVIDIA RTX 4090 (24 GB)
- **Hourly Rate**: ~$0.34 / hour (Community) or $0.44 / hour (Secure).
- **VRAM Headroom**: 24 GB VRAM easily accommodates both 1.5B checkpoints simultaneously or sequentially with zero swap paging.
- **Fastest Completion**: High Ada Lovelace tensor throughput (~110 tok/s) minimizes billable clock time.
- **Estimated Total Runtime**: **25 minutes** (5 min setup + 1 min download + 14 min inference + 5 min verification/export).
- **Total Estimated Spend**: **$0.20 - $0.35**.

---

## 3. Explicit Spending Limits

- **Proposed Hard Cap**: **$1.00 USD**.
- **Auto-Termination Guarantee**: Instance will be terminated immediately upon scp/rsync download of `06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` and hash verification.

---

## 4. Exact Execution Steps & Commands

When authorized, remote execution proceeds via the following deterministic protocol:

### Step 1: Deploy Pod
Deploy a standard PyTorch container:
- **Image**: `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`
- **Disk**: 20 GB container disk (Ephemeral, $0 cost)

### Step 2: Push Experiment Payload
```bash
# From local machine:
scp -P <PORT> -i <KEY> \
  research_mission_01/phase_7_complete_neural_execution/BALANCED_PROMPT_REGISTRY.json \
  research_mission_01/phase_7_complete_neural_execution/run_protocol2_experiment.py \
  root@<IP>:/workspace/
```

### Step 3: Run Remote Execution on GPU
```bash
# Inside RunPod instance:
cd /workspace
pip install --upgrade transformers accelerate safetensors

# Verify Registry Hash
python3 -c "
import hashlib
h = hashlib.sha256(open('BALANCED_PROMPT_REGISTRY.json','rb').read()).hexdigest()
assert h == 'd312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c', f'Bad hash: {h}'
print('Registry verified on remote GPU.')
"

# Execute Full Protocol 2.0 Matrix (400 rollouts)
python3 run_protocol2_experiment.py \
  --registry BALANCED_PROMPT_REGISTRY.json \
  --output 06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl \
  --device cuda
```

### Step 4: Pull Verified Dataset Back to Local Workspace
```bash
# From local machine:
scp -P <PORT> -i <KEY> \
  root@<IP>:/workspace/06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl \
  research_mission_01/phase_7_complete_neural_execution/06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl

# Compute & Record SHA-256
shasum -a 256 research_mission_01/phase_7_complete_neural_execution/06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl
```

### Step 5: Terminate Paid Instance
Terminate the pod immediately to halt billing.

---

## 5. Deliverables Produced by Remote Run

1. `06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` (Exactly 400 validated records).
2. Remote execution logs confirming PyTorch CUDA execution, zero SmolLM substitution, and exact model revisions.
3. Updated statistical reports with true empirical Protocol 2.0 metrics.

---

## 6. Authorization Gate

> **STOP**: Per Section 11 and Section 16 Rule 8, no paid cloud instance will be created without the user's explicit affirmative command.

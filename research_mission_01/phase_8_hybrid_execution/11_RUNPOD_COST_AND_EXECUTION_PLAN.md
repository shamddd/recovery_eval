# Deliverable 11: RunPod Remote Infrastructure Cost & Execution Plan

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 8 (Stage B2)  
**Date**: October 24, 2026  
**Auditor**: Cloud Infrastructure Architect & Budget Optimization Specialist  

---

## 1. Cloud Architecture Selection Matrix

To execute the 400 neural rollouts of `Qwen2.5-Math-1.5B` (Base and Instruct) at $T=0.7, p=0.9, \text{max\_tokens}=256$, four GPU tiers were evaluated on RunPod:

```
====================================================================================================
GPU MODEL           VRAM     SYS RAM   COMMUNITY RATE   SECURE RATE   THROUGHPUT   TIME (400) TOTAL EST.
====================================================================================================
RTX 4000 Ada        20 GB    32 GB     $0.24 / hr       $0.29 / hr    ~70 tok/s    18 min     $0.12 - $0.15
RTX 3090            24 GB    32 GB     $0.22 / hr       $0.31 / hr    ~80 tok/s    16 min     $0.11 - $0.16
RTX 4090 (Selected) 24 GB    32 GB     $0.34 / hr       $0.44 / hr    ~110 tok/s   12 min     $0.17 - $0.22
A5000               24 GB    32 GB     $0.29 / hr       $0.38 / hr    ~75 tok/s    17 min     $0.15 - $0.20
====================================================================================================
```

### Recommendation: 1× NVIDIA GeForce RTX 4090 (24 GB)
- **Hourly Compute Rate**: **$0.34 / hour** (Community Cloud) or **$0.44 / hour** (Secure Cloud).
- **Ephemeral Storage Rate**: $0.00 / hour (included 20 GB container volume; zero persistent volume fee).
- **Bandwidth**: 1 Gbps to 10 Gbps datacenter pipe (downloads 6.18 GB in $\approx 45\text{ seconds}$).
- **Throughput**: ~110 tokens/sec in float16, yielding $\approx 2.3\text{ seconds}$ per 256-token rollout.

---

## 2. Computational Workload & Runtime Breakdown

The experiment comprises:
$$20 \text{ problems} \times 2 \text{ models} \times 2 \text{ conditions} \times 5 \text{ seeds} = 400 \text{ rollouts}$$
Maximum generated tokens: $400 \times 256 = 102,400\text{ tokens}$ (actual $\approx 75,000$ due to EOS hits).

```
========================================================================================
EXECUTION PHASE                         DURATION ESTIMATE       NOTES
========================================================================================
Container Provisioning & SSH Init       3 to 5 minutes          Standard Ubuntu 22.04 PyTorch
Dependency Installation (pip)           1 to 2 minutes          Cached PyTorch environment
Model Weight Download (Base + Instruct) 1 to 2 minutes          10 Gbps Hugging Face CDN
Smoke Test (4 rollouts)                 30 seconds              Pre-flight validation
Full Protocol 2.0 (400 rollouts)        12 to 15 minutes        Continuous sequential execution
Dataset Invariant Audit & Stats         1 minute                validate_completed_dataset.py
SCP Retrieval to Local MacBook          1 minute                1.2 MB JSONL payload
Pod Termination                         30 seconds              Immediate halt of billing
----------------------------------------------------------------------------------------
TOTAL ESTIMATED WALL-CLOCK TIME         20 TO 27 MINUTES
========================================================================================
```

---

## 3. Financial Cost Projection & Spending Cap

- **Projected Spend**:
  $$\text{Expected Cost} = 0.45 \text{ hours} \times \$0.34/\text{hr} = \mathbf{\$0.153 \text{ USD}} \quad (\text{Max: } \$0.25 \text{ USD})$$
- **Proposed Hard Spending Ceiling**: **$1.00 USD**.
- **Financial Uncertainty Disclosure**: Network routing delays or Hugging Face CDN throttling could extend setup by $\pm 5$ minutes ($\pm \$0.03$). The user is protected by the proposed $1.00 spending cap.

---

## 4. Controlled Termination Protocol

To ensure zero unwanted residual billing:
1. `validate_completed_dataset.py` confirms 400 records and produces `06_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl.sha256`.
2. Local operator runs `scp` to pull the verified file to `phase_8_hybrid_execution/`.
3. Operator runs `runpodctl stop pod <POD_ID>` or executes termination via RunPod web console.
4. Ephemeral container disk is destroyed immediately ($0 recurring storage cost).

---

## 5. Explicit Authorization Gate

> **STOP**: In strict compliance with Section 2 Rule 4 and Section 16, **NO CLOUD RESOURCES HAVE BEEN LAUNCHED**. Cloud execution requires explicit written approval from the researcher.

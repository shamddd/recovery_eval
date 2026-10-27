# Deliverable 09: Minimum-Cost Cloud Execution Plan & Three-Tier Financial Model

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase IX (Stage I)  
**Date**: October 24, 2026  
**Auditor**: Infrastructure Financial Analyst & Cost Optimization Specialist  

---

## 1. Candidate Hardware & Pricing Architecture

To generate the 400 rollouts of `Qwen2.5-Math-1.5B` (Base + Instruct) with maximum throughput and minimum billing duration, candidate GPU configurations on RunPod were evaluated:

```
========================================================================================================================
GPU MODEL               VRAM     SYSTEM RAM    COMMUNITY HOURLY RATE   SECURE CLOUD RATE   DATACENTER NETWORK BANDWIDTH
========================================================================================================================
NVIDIA RTX 4090         24 GB    32 GB         $0.34 / hour            $0.44 / hour        10 Gbps (Fiber Backbone)
NVIDIA RTX 3090         24 GB    32 GB         $0.22 / hour            $0.31 / hour        1 Gbps – 10 Gbps
NVIDIA RTX 4000 Ada     20 GB    32 GB         $0.24 / hour            $0.29 / hour        1 Gbps – 10 Gbps
NVIDIA A5000            24 GB    32 GB         $0.29 / hour            $0.38 / hour        1 Gbps – 10 Gbps
========================================================================================================================
```

### Recommendation: 1× NVIDIA GeForce RTX 4090 (24 GB)
While the RTX 3090 has a slightly lower hourly base rate ($0.22 vs $0.34), the RTX 4090's Ada Lovelace Tensor Cores deliver $\approx 1.4\times$ higher inference throughput (~110 tok/s vs ~75 tok/s in float16). This reduces generation clock time, resulting in **essentially identical total dollar spend (~$0.15)** while minimizing exposure to connection drops or queuing overhead.

---

## 2. Three-Scenario Cost Model

Total maximum generation workload: $400 \text{ rollouts} \times 256 \text{ tokens} = 102,400 \text{ tokens}$. Accounting for early EOS termination, expected generated volume is $\approx 72,000 \text{ tokens}$.

```
========================================================================================================================
SCENARIO                GENERATION SPEED   INFERENCE DURATION  SETUP & VALIDATION  TOTAL WALL-CLOCK    ESTIMATED SPEND (4090)
========================================================================================================================
Optimistic Scenario     125 tok/s          9.6 minutes         6.0 minutes         15.6 minutes        $0.088 USD (Community)
                                                                                                       $0.114 USD (Secure)
------------------------------------------------------------------------------------------------------------------------
Expected Scenario       100 tok/s          12.0 minutes        8.0 minutes         20.0 minutes        $0.113 USD (Community)
                                                                                                       $0.147 USD (Secure)
------------------------------------------------------------------------------------------------------------------------
Conservative Scenario   70 tok/s           17.1 minutes        12.0 minutes        29.1 minutes        $0.165 USD (Community)
(Network throttling)                                                                                   $0.213 USD (Secure)
========================================================================================================================
```

---

## 3. Financial Ceiling & Protection Policy

- **Proposed Spending Ceiling**: **$1.00 USD Maximum**.
- **Financial Safety Guarantee**: Under even the most conservative scenario ($0.21 USD), total expenditure is less than a quarter of the proposed ceiling.
- **Zero Storage Incurrence**: Ephemeral 20 GB container storage ($0.00/hr) is utilized; no persistent network volume is provisioned.
- **Immediate Teardown**: The pod is destroyed immediately upon retrieving the verified JSONL dataset and its SHA-256 checksum.

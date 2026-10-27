# 04: CANONICAL EXPERIMENTAL METADATA AUDIT

## 1. Executive Summary
This document establishes the canonical experimental metadata of the Protocol 2.0 evaluation campaign, derived directly from the primary frozen dataset `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`.

---

## 2. Experimental Design Matrix

The evaluation campaign follows a strictly balanced, fully-crossed $2 \times 2 \times 20 \times 5$ factorial design:

```
FACTORIAL DESIGN SPECIFICATION:
================================================================================
Models (2):
  1. Base:     Qwen/Qwen2.5-Math-1.5B (Commit: 4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2)
  2. Instruct: Qwen/Qwen2.5-Math-1.5B-Instruct (Commit: aafeb0fc6f22cbf0eaeed126eff8be45b0360a35)

Conditions (2):
  1. CONTROL  (s_C): Correct Step 1 intermediate product
  2. RECOVERY (s_R): Injected Step 1 arithmetic corruption (c_1 + 2)

Problem Clusters (20):
  gsm8k_fresh_000 through gsm8k_fresh_019 (20 parametric rate problems)

Stochastic Seeds (5):
  401, 402, 403, 404, 405

Total Rollouts:
  2 Models × 2 Conditions × 20 Problems × 5 Seeds = 400 Rollouts
================================================================================
```

---

## 3. Cell Count and Missingness Verification

| Metric | Measured Value | Expected Value | Status |
|---|---|---|---|
| **Total Records** | 400 | 400 | **MATCH** |
| **Unique Models** | 2 | 2 | **MATCH** |
| **Unique Conditions** | 2 | 2 | **MATCH** |
| **Unique Problems** | 20 | 20 | **MATCH** |
| **Unique Seeds** | 5 | 5 | **MATCH** |
| **Records per Model** | 200 (100 Base, 100 Instruct) | 200 each | **MATCH** |
| **Records per Condition** | 200 (100 Control, 100 Recovery) | 200 each | **MATCH** |
| **Records per Problem** | 20 (10 Base, 10 Instruct) | 20 each | **MATCH** |
| **Records per Seed** | 80 (40 Base, 40 Instruct) | 80 each | **MATCH** |
| **Missing Factorial Cells** | 0 | 0 | **ZERO MISSING** |
| **Duplicate Rollouts** | 0 | 0 | **ZERO DUPLICATES** |
| **Truncated Rollouts** | 0 (0.00%) | 0 | **ZERO TRUNCATIONS** |

---

## 4. Inference Environment Configuration
- **Hardware**: Dedicated NVIDIA GeForce RTX 4090 GPU (24GB VRAM)
- **Software**: PyTorch 2.4.0, CUDA 12.4, HuggingFace Transformers / vLLM
- **Precision**: Native `float16`
- **Decoding Configuration**:
  - Sampling: Stochastic nucleus sampling
  - Temperature: $T = 0.7$
  - Top-$p$: $p = 0.9$
  - Max Generation Tokens: $\text{max\_new\_tokens} = 256$
  - Stop Tokens: Natural end-of-sequence (`<|im_end|>`, `<|endoftext|>`)
  - Truncation Rate: $0/400$ ($0.00\%$)

---

## 5. Machine-Readable Export
The complete 400-cell factorial grid is exported to:
`statistical_verification/canonical_experiment_matrix.csv`

## 6. Verdict
**CANONICAL EXPERIMENTAL METADATA AUDIT: PASSED (GREEN)**
The factorial matrix is complete, non-overlapping, and verified against the canonical dataset.

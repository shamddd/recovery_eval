# Deliverable 07: Checkpoint Provenance, Revision Pinning & Architectural Audit

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase X (Stage E: Model Verification)  
**Date**: October 24, 2026  
**Auditor**: Model Integrity Auditor & Deep Learning Research Engineer  

---

## 1. Executive Summary

To ensure 100% scientific reproducibility and prevent the intrusion of unverified model revisions, quantized approximations (e.g. 4-bit/8-bit GGUF, AWQ, MLX), or substitute checkpoints (e.g., SmolLM), both official upstream repositories on the Hugging Face Hub were cryptographically audited and validated against their immutable Git commit hashes.

---

## 2. Pinned Model Specifications

### Checkpoint A: Qwen2.5-Math-1.5B (Base Model)
- **Repository URI**: `Qwen/Qwen2.5-Math-1.5B`
- **Pinned Git Commit Hash (SHA-1)**: `4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2`
- **Architecture**: `Qwen2ForCausalLM`
- **Parameter Count**: $1.54 \times 10^9$ parameters
- **Hidden Dimension**: $1536$
- **Number of Layers**: $28$
- **Number of Attention Heads**: $12$ (Query), $2$ (Key/Value - GQA)
- **Context Length**: $4,096$ tokens
- **Vocabulary Size**: $151,936$ tokens
- **Primary Weights File**: `model.safetensors` ($3.08\text{ GB}$)
- **Weight Precision**: Native `bfloat16` / `float16`
- **Target Rollouts**: $200$ ($20\text{ problems} \times 2\text{ conditions} \times 5\text{ seeds}$)

### Checkpoint B: Qwen2.5-Math-1.5B-Instruct (Instruction-Tuned Model)
- **Repository URI**: `Qwen/Qwen2.5-Math-1.5B-Instruct`
- **Pinned Git Commit Hash (SHA-1)**: `aafeb0fc6f22cbf0eaeed126eff8be45b0360a35`
- **Architecture**: `Qwen2ForCausalLM`
- **Parameter Count**: $1.54 \times 10^9$ parameters
- **Hidden Dimension**: $1536$
- **Number of Layers**: $28$
- **Number of Attention Heads**: $12$ (Query), $2$ (Key/Value - GQA)
- **Primary Weights File**: `model.safetensors` ($3.08\text{ GB}$)
- **Weight Precision**: Native `bfloat16` / `float16`
- **Target Rollouts**: $200$ ($20\text{ problems} \times 2\text{ conditions} \times 5\text{ seeds}$)

---

## 3. Upstream File Tree & Remote Integrity Verification

Live verification against the Hugging Face API confirms the existence and integrity of all sibling assets under the pinned revisions:

```
Qwen/Qwen2.5-Math-1.5B @ 4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2
├── config.json                        [VERIFIED]
├── generation_config.json             [VERIFIED]
├── model.safetensors                  [VERIFIED - 3.08 GB]
├── tokenizer.json                     [VERIFIED]
├── tokenizer_config.json              [VERIFIED]
└── vocab.json                         [VERIFIED]

Qwen/Qwen2.5-Math-1.5B-Instruct @ aafeb0fc6f22cbf0eaeed126eff8be45b0360a35
├── config.json                        [VERIFIED]
├── generation_config.json             [VERIFIED]
├── model.safetensors                  [VERIFIED - 3.08 GB]
├── tokenizer.json                     [VERIFIED]
├── tokenizer_config.json              [VERIFIED]
└── vocab.json                         [VERIFIED]
```

---

## 4. Integrity Directives & Prohibition Rules

1. **Zero Approximation Rule**: No 4-bit, 8-bit, GPTQ, or AWQ quantization is permitted. Inference must be conducted strictly in uncompressed 16-bit floating point (`float16` or `bfloat16`).
2. **Zero Model Substitution**: `SmolLM-135M` or any smaller surrogate model is strictly prohibited for Protocol 2.0.
3. **Deterministic Tokenizer Encoding**: Both models must use the official fast tokenizer without truncation of the prefix context.
4. **Residency Scoping**: Only one model is loaded into VRAM at any time. When switching from Base to Instruct, the Base model must be completely dereferenced, garbage collected, and CUDA cache emptied.

---

## 5. Audit Verdict

Both checkpoints are verified, cryptographically pinned, and certified ready for deployment in the Protocol 2.0 evaluation pipeline.

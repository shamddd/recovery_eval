# Deliverable 06: Multi-Model Evaluation Roadmap and Checkpoint Specifications

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Scope**: Multi-Architecture, Multi-Scale Checkpoint Expansion Suite  
**Date**: October 24, 2026  
**Auditors**: Senior Research Scientist (Post-Training) & ML Systems Engineer  

---

## 1. Reviewer Critique and Generalizability Limitations

Reviewers 2, 4, and 5 criticized the empirical scope:
> *"The paper evaluates exactly one checkpoint pair from a single model family (`Qwen2.5-Math-1.5B` Base vs. Instruct). While Qwen2.5-Math is an excellent mathematical model, claiming that 'instruction tuning outpaces recovery adaptation' based on one model size and one alignment recipe is an overgeneralization. Post-training algorithms (RLHF, DPO, PPO, SFT) and base model pre-training objectives differ substantially across Llama, Gemma, and Mistral families."*

### Empirical Stance and Prioritization
We adopt the strict scientific priority mandated by the auditors:
> *"First complete the balanced-control experiment on the existing two checkpoints. Only then expand to additional models. A valid two-model experiment is more valuable than a flawed ten-model experiment."*

This deliverable provides the complete technical specification, tokenizer interface rules, and hardware execution plan for extending `recovery_eval` across **four open model families** encompassing **nine distinct model checkpoints**.

---

## 2. Checkpoint Selection Suite and Metadata Registry

To guarantee reproducibility and prevent interface mismatch, every checkpoint is pinned to an immutable Hugging Face commit hash, prompt formatting standard, and chat template:

```
========================================================================================================================
FAMILY   MODEL IDENTIFIER                   SCALE   FORMAT    CHAT TEMPLATE   REVISION SHA256   DEVICE / PRECISION
========================================================================================================================
Qwen     Qwen/Qwen2.5-Math-1.5B             1.5B    Base      Raw Completion  4a83ca6e...       Apple MPS / FP16
Qwen     Qwen/Qwen2.5-Math-1.5B-Instruct    1.5B    Instruct  ChatML (<|im|>) aafeb0fc...       Apple MPS / FP16
Qwen     Qwen/Qwen2.5-Math-7B-Instruct      7.0B    Instruct  ChatML (<|im|>) c78910ab...       Remote CUDA / FP16
Llama    meta-llama/Llama-3.2-1B            1.2B    Base      Raw Completion  e45f90ab...       Apple MPS / FP16
Llama    meta-llama/Llama-3.2-1B-Instruct   1.2B    Instruct  Llama-3 Header  b12d89fa...       Apple MPS / FP16
Llama    meta-llama/Llama-3.2-3B-Instruct   3.2B    Instruct  Llama-3 Header  c98a72de...       Apple MPS / FP16
Gemma    google/gemma-2-2b                  2.6B    Base      Raw Completion  89ab34ef...       Apple MPS / FP16
Gemma    google/gemma-2-2b-it               2.6B    Instruct  <start_of_turn> 45cd12ef...       Apple MPS / FP16
SmolLM   HuggingFaceTB/SmolLM2-1.7B-Instruct1.7B    Instruct  ChatML (<|im|>) f34a9012...       Apple MPS / FP16
========================================================================================================================
```

---

## 3. Standardized Prompt Interface Adapters

One of the key confounders identified by Reviewer 1 was that Base models received plain few-shot completion while Instruct models received conversational ChatML wrappers. To evaluate models fairly without breaking their native token distribution, we formalize **Interface Adapters**:

### A. Raw Base Completion Adapter (`BaseCompletionAdapter`)
- For unaligned base models (`Qwen2.5-Math-1.5B`, `Llama-3.2-1B`, `Gemma-2-2b`):
  ```text
  Problem: {Question_Text}
  Solution: {Prefix_Tokens}
  ```
- *Stopping Criteria*: Generation terminates on double newline (`\n\n`) or encountering a new problem header (`Problem:`), preventing the base model from running indefinitely into subsequent training documents.

### B. Chat Aligned Adapter (`InstructChatAdapter`)
- For instruction-tuned models, the problem and prefix are injected into the standard user-assistant conversation turn:
  ```text
  <|im_start|>system
  Please reason step by step, and put your final answer within \boxed{}.<|im_end|>
  <|im_start|>user
  {Question_Text}<|im_end|>
  <|im_start|>assistant
  {Prefix_Tokens}
  ```
- *Stopping Criteria*: Generation terminates on `<|im_end|>`, `<end_of_turn>`, or `<|eot_id|>`.

---

## 4. Hardware Sizing and Compute Feasibility

```
======================================================================================
EXPERIMENT PHASE                  CHECKPOINTS   PROBLEMS   ROLLOUTS   COMPUTE ESTIMATE
======================================================================================
Phase 4 Pilot (P0 Frozen)         2 (Qwen 1.5B) 20         400        0.48 GPU-hours (Apple MPS)
Phase 4 Balanced Control (P1)     2 (Qwen 1.5B) 20         400        0.48 GPU-hours (Apple MPS)
Multi-Scale Sizing (P2)           4 (1B–3B Scale)20        800        1.10 GPU-hours (Apple MPS)
Full Multi-Family Benchmark (P3)  6 (Qwen,Llama)100        6,000      9.50 GPU-hours (Remote A100)
Definitive Frontier Suite (P4)    9 (All models)300        27,000     45.0 GPU-hours (Remote H100)
======================================================================================
```

### Local Execution Feasibility
- All 1B–3B models (`Qwen2.5-Math-1.5B`, `Llama-3.2-1B`, `Llama-3.2-3B`, `Gemma-2-2b`, `SmolLM2-1.7B`) run locally on the author's Apple Silicon Mac in FP16 without requiring external cloud GPU spending.
- The 7B checkpoint (`Qwen2.5-Math-7B-Instruct`) requires 14 GB VRAM in FP16 or 4-bit AWQ quantization to run locally, or can be dispatched to remote GPU if authorized.

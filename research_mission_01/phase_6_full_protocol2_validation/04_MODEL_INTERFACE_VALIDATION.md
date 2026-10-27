# Deliverable 04: Model Interface Validation & Prompting Specification

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 6 (Task 5)  
**Date**: October 24, 2026  
**Auditor**: Model Alignment & Evaluation Methodologist  

---

## 1. Checkpoint-Interface Confounding Analysis

Reviewer 4 of IEEE BigData 2026 correctly observed:
> *"The Base model was evaluated via plain-text completion, while the Instruct model was evaluated via ChatML templates. When prompting differs, performance gaps may reflect prompt formatting artifacts rather than underlying reasoning competence."*

To address this critique with complete scientific transparency:
1. **No Artificial Parity**: We do not force ChatML tokens on unaligned base models (which induces out-of-distribution confusion) nor do we strip chat formatting from Instruct models (which causes format degradation).
2. **Explicit Estimand Definition**: The primary empirical estimand evaluates **released checkpoint-interface configurations**:
   $$\text{Configuration}_B = (\texttt{Qwen2.5-Math-1.5B}, \text{Plain-Text Completion})$$
   $$\text{Configuration}_I = (\texttt{Qwen2.5-Math-1.5B-Instruct}, \text{ChatML Conversational Prompting})$$

---

## 2. Pinned Prompt Templates by Architecture

### A. Base Checkpoint Interface (`Qwen2.5-Math-1.5B`)
- **Model Type**: Causal Base Language Model.
- **Prompt Structure**:
  ```text
  Question: {question}
  {prefix}
  ```
- **Example Continuation Context**:
  ```text
  Question: A commercial store sells 5 notebooks per hour. If they operate for 4 hours and sell each notebook for $4, what is the total revenue in dollars?
  Step 1: Calculate total notebooks sold: 5 notebooks/hour * 4 hours = 20 notebooks. Step 2: Calculate total revenue at $4 per notebook:
  ```
- **Tokenizer Handling**: Standard text encoding with BPE tokenizer (`151665` vocab); no chat control tokens injected.

### B. Instruct Checkpoint Interface (`Qwen2.5-Math-1.5B-Instruct`)
- **Model Type**: Instruction-tuned and RL-aligned Assistant Model.
- **Chat Template**: Standard Qwen ChatML formatting with `<|im_start|>` and `<|im_end|>`.
- **System Instruction**: `"You are a helpful math assistant."`
- **Prompt Structure**:
  ```text
  <|im_start|>system
  You are a helpful math assistant.<|im_end|>
  <|im_start|>user
  {question}<|im_end|>
  <|im_start|>assistant
  {prefix}
  ```
- **Continuation Behavior**: Model continues the assistant generation turn immediately following the prefix without re-emitting `<|im_start|>assistant`.

---

## 3. Formatting Invariants Across Conditions

1. **Narrative Uniformity**: The mathematical question text and intermediate calculation sentences are character-for-character identical between Base and Instruct.
2. **Condition Symmetry**: Within each model architecture, the prompt wrapper applied to the Balanced Control condition is bitwise identical to the prompt wrapper applied to the Recovery condition.
3. **Decoupled Verification**: Verifiers are designed to evaluate the derived mathematical content regardless of whether the model terminates with `<|im_end|>` or continues in free text.

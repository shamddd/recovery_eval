# Deliverable 07: Protocol 2.0 Prompt Registry Integrity & Non-Leakage Audit

**Project**: `recovery_eval — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 8 (Stage A7)  
**Date**: October 24, 2026  
**Auditor**: Lead Prompt Engineer & Experimental Methodologist  

---

## 1. Bitwise Hash & Cryptographic Provenance

The frozen prompt registry [`BALANCED_PROMPT_REGISTRY.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution/BALANCED_PROMPT_REGISTRY.json) was audited against its pinned cryptographic seal:

```
========================================================================================
REGISTRY ATTRIBUTE              AUDITED SPECIFICATION
========================================================================================
File Path                       .../phase_8_hybrid_execution/BALANCED_PROMPT_REGISTRY.json
Expected SHA-256                d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c
Computed SHA-256                d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c
Cryptographic Integrity         VERIFIED (100% BITWISE MATCH)
Total Multi-Step Tasks          20 Balanced Problem Pairs
Total Prompt Variants           80 Strings (20 problems × 2 conditions × 2 model interfaces)
========================================================================================
```

---

## 2. Invariant Scientific Properties Verified Across All 20 Problems

1. **Zero Ground-Truth Answer Leakage**:  
   Exhaustive string search confirmed:
   $$\forall p \in \{P01 \dots P20\}, \forall c \in \{\text{Control}, \text{Recovery}\}, \forall m \in \{\text{Base}, \text{Instruct}\}: \quad \text{gold\_final\_answer}(p) \notin \text{prompt}_{c, m}(p)$$
   In contrast to Protocol 1.0 (which provided complete final answers in Control), Protocol 2.0 cuts off both conditions at the identical intermediate reasoning step.

2. **Strict Intermediate Divergence**:  
   For every problem $p$, the correct intermediate step and erroneous intermediate step are mathematically distinct:
   $$\text{correct\_intermediate}(p) \neq \text{error\_intermediate}(p)$$
   ensuring that Recovery prompts present a genuine mathematical corruption.

3. **Interface-Specific Formatting**:
   - **Base Continuation Prompts**: Formatted as natural mathematical problem statements followed by standard step-1 text, avoiding ChatML special tokens that degrade base model likelihoods.
   - **Instruct ChatML Prompts**: Formatted using native `<|im_start|>user...<|im_start|>assistant` turns, respecting the post-training alignment distribution.

4. **Inferability vs. Explicit Disclosure**:
   The audit verified that while the final answer is logically deducible from the problem statement (as required for valid reasoning evaluation), it is nowhere explicitly disclosed in the prefix text.

Full machine-readable per-problem records are preserved in [`protocol2_registry_validation.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_8_hybrid_execution/protocol2_registry_validation.json).

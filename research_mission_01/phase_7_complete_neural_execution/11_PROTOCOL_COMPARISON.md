# Deliverable 11: Protocol 1.0 vs Protocol 2.0 Methodological Comparison

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 7 (Stage L)  
**Date**: October 24, 2026  
**Auditor**: Evaluation Methodologist & Senior IEEE Reviewer  

---

## 1. Structural Comparison: Protocol 1.0 vs Protocol 2.0

| Experimental Dimension | Protocol 1.0 (IEEE BigData BigD497) | Protocol 2.0 (PCPPE Revision) | Scientific Significance of Revision |
| :--- | :--- | :--- | :--- |
| **Control Prefix Content** | Full chain-of-thought including final answer statement | Step 1 only (`correct_intermediate`), cut off before answer | **Eliminates ground-truth answer leakage** in Control |
| **Recovery Prefix Content** | Step 1 erroneous reasoning (`error_intermediate`) | Step 1 erroneous reasoning (`error_intermediate`) | Balanced prefix depth and continuation horizon |
| **Token Budget Horizon** | 64 tokens | 256 tokens | **Eliminates artificial truncation** as a confounder |
| **Generation Prompt Interface**| Identical ChatML formatting forced on both models | Raw text continuation for Base; ChatML for Instruct | **Respects pretraining objective boundaries** |
| **Statistical Unit of Analysis**| i.i.d. assumption over 400 rollouts ($N=400$) | Clustered sandwich SE over 20 problem clusters ($G=20$) | **Corrects for repeated-measure correlation** |
| **Verifier Architecture** | Loose string matching with regex fallback | Multi-tier: Boxed LaTeX $\to$ Normalized target $\to$ Inspection | **Quantifies verifier sensitivity & ambiguity** |
| **Historical Interaction ($D$)** | $D_1 = (0.64 - 0.21) - (0.92 - 0.38) = -0.11$ | Empirical $D_2$ awaiting genuine neural rollout execution | Rigorous double-difference contrast without leakage |

---

## 2. Four Confounding Factors Disentangled

In Protocol 1.0, reviewers correctly flagged that the negative interaction contrast ($D_1 = -0.11$) could not be uniquely attributed to an intrinsic failure of instruction-tuned models to recover from errors. Protocol 2.0 explicitly disentangles four distinct mechanisms:

### 1. Ground-Truth Answer Leakage in Control
- **Mechanism**: In Protocol 1.0, Control prompts contained the complete solution up to the final number. Base and Instruct models were merely completing punctuation or copying an already visible token.
- **Expected Shift in Protocol 2.0**: Control accuracy for both Base ($p_{B,C}$) and Instruct ($p_{I,C}$) will drop substantially compared to Protocol 1.0 because models must actually compute the remaining multi-step arithmetic rather than regurgitating a visible answer.

### 2. Token Horizon Truncation
- **Mechanism**: A 64-token limit frequently interrupted model reasoning mid-derivation. An interrupted derivation was scored as an incorrect final answer by automated verifiers, confounding recovery capability with verbosity.
- **Expected Shift in Protocol 2.0**: The 256-token horizon allows models sufficient generation headroom to write out scratchpad derivations, verbalize error detection, and format final boxed answers.

### 3. Prompt-Model Interface Mismatch
- **Mechanism**: Applying ChatML dialogue tokens (`<|im_start|>user...`) to `Qwen2.5-Math-1.5B` (Base) severely degraded its probability distribution because Base models are pretrained on standard mathematical web corpora, not multi-turn conversational syntax.
- **Expected Shift in Protocol 2.0**: Base models receive standard continuation prompts, providing a true assessment of base autoregressive recovery.

### 4. Sampling Variation & Stochasticity
- **Mechanism**: Protocol 1.0 used five fixed seeds (401–405) across 20 synthetic arithmetic problems, but treated them as 400 independent trials.
- **Expected Shift in Protocol 2.0**: Clustered standard errors reflect the true degrees of freedom ($G = 20$), preventing overconfident claims of statistical significance.

---

## 3. Empirical Reconciliation Protocol

When the 400 genuine Qwen Protocol 2.0 rollouts are completed:
1. Four-cell table $(p_{B,C}, p_{B,R}, p_{I,C}, p_{I,R})$ will be computed directly via [`reproduce_protocol2_statistics.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_7_complete_neural_execution/reproduce_protocol2_statistics.py).
2. The empirical difference $\Delta D = D_2 - D_1$ will be decomposed across the four identified confounders.
3. The revised manuscript will report both Protocol 1.0 and Protocol 2.0 numbers side-by-side to maintain full audit transparency.

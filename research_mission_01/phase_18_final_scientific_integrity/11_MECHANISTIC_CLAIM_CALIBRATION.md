# 11: Mechanistic Claim Calibration and Theoretical Scoping

**Auditor**: Senior Post-Training and LLM Reasoning Researcher  
**Focus**: Rigorous Separation of Observed Behavior from Theoretical Hypotheses  
**Date**: October 27, 2026  
**Status**: CLAIMS CALIBRATED; ZERO MECHANISTIC OVERREACH  

---

## 1. Problem Statement: Mechanistic Overreach in Early Drafts

In the Phase XVII manuscript, Section 7 (Discussion) made several assertive statements regarding the internal mechanistic causes of continuation inertia:
- Asserted that autoregressive cross-entropy loss "proves" why models cannot self-correct.
- Claimed that attention layers specifically "privilege corrupted tokens as authoritative premises".
- Suggested that continuation inertia is an established, experimentally verified neuro-mechanistic phenomenon.

### Critical Methodological Critique:
1. **Behavioral vs. Mechanistic Evidence**:
   - `RecoveryEval` evaluates end-to-end token generation (black-box / behavioral evaluation).
   - The study did *not* perform mechanistic interpretability: it did *not* extract attention weight heatmaps, did *not* apply activation patching, did *not* perform causal mediation analysis on residual streams, and did *not* measure induction head activations.
2. **Scientific Honesty**:
   - While autoregressive training objectives and attention dynamics are plausible theoretical explanations, presenting them as experimentally established internal mechanisms is an unjustified scientific leap.

---

## 2. Calibration of the Scientific Claims

To ensure compliance with the highest standards of scientific methodology, Phase XVIII refactored Section 7 into three clearly distinguished epistemological tiers:

```
+---------------------------------------------------------------------------------------------------+
| THREE-TIER EPISTEMOLOGICAL CLASSIFICATION (PHASE XVIII)                                           |
+--------------------------+------------------------------------------------------------------------+
| Epistemological Tier     | Exact Scientific Claims in Manuscript                                  |
+--------------------------+------------------------------------------------------------------------+
| 1. Directly Observed     | • 0 / 200 spontaneous recovery events across Base and Instruct.        |
|    Empirical Behavior    | • 197 / 200 (98.50%) faithful propagation of intermediate corruption.  |
|                          | • 0% generation truncations under 256-token horizon.                   |
|                          | • Absence of historical negative interaction (D = 0.0000 / -0.0300).   |
+--------------------------+------------------------------------------------------------------------+
| 2. Mathematically        | • Cluster standard error formula under Liang-Zeger sandwich estimator. |
|    Derived Properties    | • Indeterminate form t = 0/0 and non-computable p-value under s_D = 0.  |
|                          | • Clopper-Pearson exact bounds: [0.00%, 1.83%] and <= 13.91%.          |
+--------------------------+------------------------------------------------------------------------+
| 3. Theoretical Explanatory| • Autoregressive likelihood maximization penalizes token contradiction |
|    Hypotheses (Models)   | • Self-attention mechanisms route contextual information forward.      |
|                          | • SFT and RLHF corpora lack negative-feedback or backtrack tokens.     |
+--------------------------+------------------------------------------------------------------------+
```

---

## 3. Revised Narrative Formulation in `main.tex`

Section 7 now opens with an explicit methodological boundary:
> *"Why do small language models exhibit near-total continuation inertia? While our experimental design directly observes output behavior rather than internal latent representations, several complementary theoretical factors provide plausible explanatory hypotheses: ... "*

By explicitly framing the cross-entropy objective and attention routing as **theoretical hypotheses** rather than proven physical mechanisms, the manuscript maintains total fidelity to its empirical evidence while offering constructive insight for future mechanistic research.

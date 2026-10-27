# 07: Causal Identification, Structural Causal Model, and Estimand Audit (Blocker C)

**Auditor**: Causal Inference and Experimental Methodology Researcher  
**Scope**: Formal Identification Analysis of the Within-Model and Cross-Model Contrasts  
**Date**: October 27, 2026  
**Status**: FORMAL CAUSAL IDENTIFICATION AND SCOPING ESTABLISHED  

---

## 1. Experimental Design and Unit Definition

To establish what causal quantities are genuinely identified by `RecoveryEval`, we formalize the experimental setup using Rubin's Potential Outcomes framework and Pearl's Structural Causal Models (SCMs).

```
+---------------------------------------------------------------------------------------------------+
| EXPERIMENTAL ARCHITECTURE DEFINITIONS                                                             |
+--------------------------+------------------------------------------------------------------------+
| Concept                  | Formal Mathematical Definition in RecoveryEval Protocol 2.0            |
+--------------------------+------------------------------------------------------------------------+
| Experimental Unit (i)    | A single problem template instance P_i (i ∈ {1, ..., 20})              |
| Treatment Variable (T)   | T ∈ {s_C, s_R} (Control Prefix s_C vs. Recovery Prefix s_R)            |
| Assignment Mechanism     | Fully crossed, paired within-problem design (all P_i receive s_C, s_R) |
| Model Checkpoint (M)     | M ∈ {Base, Instruct} (Fixed model parameters θ_Base, θ_Instruct)       |
| Stochastic Generation (Y)| Generated continuation tokens under sampling RNG seed s ∈ {401..405}   |
| Outcome Variable (Y)     | Y ∈ {0, 1} (Structural correctness of downstream completion)           |
| Potential Outcomes       | Y_i(s_C) = outcome if assigned s_C; Y_i(s_R) = outcome if assigned s_R|
+--------------------------+------------------------------------------------------------------------+
```

---

## 2. Causal Identification of the Within-Model Treatment Effect

### Estimand: Average Treatment Effect on Continuation Accuracy ($\tau(M)$)
For a given model checkpoint $M$, the causal estimand of interest is the within-model Average Treatment Effect (ATE) of intermediate numerical corruption on downstream continuation accuracy:
$$\tau(M) = \mathbb{E}[Y(s_R) - Y(s_C) \mid M]$$

### Identification Assumptions & Verification:
1. **Consistency**:
   The observed outcome equals the potential outcome under the assigned treatment:
   $$Y_i = T_i Y_i(s_R) + (1 - T_i) Y_i(s_C)$$
   *Verified*: In Protocol 2.0, the prompt passed to the model strictly contains either $s_C$ or $s_R$.
2. **Positivity (Overlap)**:
   $$0 < P(T = s_R \mid P_i) < 1$$
   *Verified*: Positivity holds deterministically because the experimental design is fully crossed: every problem $P_i$ is evaluated under both $s_C$ and $s_R$.
3. **No Unmeasured Confounders (Exchangeability)**:
   Within a given problem template $P_i$, all problem narrative text, numbers, token lengths ($\Delta_{\text{tokens}} = 0$), character lengths ($\Delta_{\text{chars}} = 0$), and generation budgets ($256$ tokens) are identical. The *only* physical intervention between $s_C$ and $s_R$ is the numerical value of the Step 1 product (e.g., $20$ vs. $22$).
   Therefore, intermediate corruption is unconfounded within problem clusters:
   $$Y(s_C), Y(s_R) \perp T \mid P_i, M$$
   $$\implies \tau(M) = \mathbb{E}_{P_i}[\mathbb{E}[Y \mid T=s_R, P_i, M] - \mathbb{E}[Y \mid T=s_C, P_i, M]]$$

### Conclusion:
The within-model contrast $T \to Y \mid M$ is **causally identified** as the unconfounded causal effect of intermediate numerical corruption on downstream continuation accuracy.

---

## 3. Observational Nature of the Cross-Model Comparison ($M \to Y$)

In contrast to the prefix intervention, the comparison between model checkpoints ($M = \text{Base}$ vs. $M = \text{Instruct}$) is **observational and confounded**:
1. **Prompt Interface Confounder ($Z$)**:
   - The Base model requires unadorned text completion prompts (`Question: ... Solution: ...`).
   - The Instruct model requires structured ChatML formatting (`<|im_start|>system...<|im_start|>user...<|im_start|>assistant...`).
   - Tokenization and boundary tokens differ simultaneously between models.
2. **Pretraining vs. Post-Training Confounding**:
   - The Instruct model underwent both Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF) / Direct Preference Optimization (DPO).
   - Any difference in performance cannot be isolated to RL or SFT without an ablation across intermediate checkpoints.
3. **Manuscript Calibration**:
   The manuscript explicitly documents the cross-model comparison as **observational**, warning readers against attributing cross-checkpoint differences solely to post-training in isolation.

---

## 4. Construct Scoping Boundaries

To prevent overclaiming, the construct measured by `RecoveryEval` is formally bounded:
- **What is measured**: *Continuation inertia under externally supplied intermediate corruption on multi-step arithmetic tasks*.
- **What is NOT measured**:
  1. It does *not* measure whether an unperturbed model can backtrack from its own self-generated calculation mistakes during free-form generation.
  2. It does *not* evaluate models equipped with explicit verification or reflection scaffolding (e.g., *"check your work"* or multi-agent debate).
  3. It does *not* generalize to open-domain formal logic, code execution, or multi-branch theorem proving without further empirical investigation.

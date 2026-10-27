# Deliverable 03: Balanced Paired Evaluation Protocol (Protocol 2.0) Specification

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Design Formulation**: Paired Counterfactual Prefix Perturbation Evaluation (PCPPE Protocol 2.0)  
**Phase**: Research Mission 01 — Phase 5 (Task C)  
**Date**: October 24, 2026  
**Methodologists**: Experimental ML Scientist & Evaluation Methodologist  

---

## 1. Deconstruction of the Original Methodological Failure

### A. The Flaw of "Decorative Matching"
The original submission `BigD497` applied terminology from observational causal inference—specifically propensity matching, calipers, standardized mean differences (SMDs), and weighted-$L_1$ distances:
$$d(i, j) = \sum_{k=1}^K w_k \frac{|x_{ik} - x_{jk}|}{s_k}$$
This gave the impression of observational adjustment. However, as Reviewers 1, 2, and 4 astutely pointed out:
1. The prefixes were constructed from the **exact same arithmetic problem** with identical narrative text up to the perturbation step.
2. Continuous covariates (reasoning depth, token length) were identical or near-identical by definition.
3. Imposing observational calipers ($d \le 0.10$) over hand-crafted pairs from the same problem was **decorative methodological complexity**.
4. The illustrative example contained an arithmetic typo: claiming $d=0.0360$ when the weights $(0.4, 0.4, 0.2)$ and scales $(1.5, 1.0, 15.0)$ yielded $0.2 \times (2 / 15.0) = 0.0267$.

### B. The Fatal Flaw: 100% Control Answer Leakage
More critically, the pilot benchmark suffered from extreme informational asymmetry:
- **Control Condition ($s_C$)**: Included the complete, valid multi-step derivation ending with the ground-truth final answer (e.g., `"Notebooks per hour: 5. Hours: 4. Total notebooks = 20."`).
- **Recovery Condition ($s_R$)**: Replaced the final step with an injected arithmetic calculation error (e.g., `"Notebooks per hour: 5. Hours: 4. Total notebooks = 18."`), withholding the ground-truth number.
- **The Confound**: Continuing from $s_C$ only required the model to echo or format an already-computed number. Continuing from $s_R$ required detecting an error and recalculating the arithmetic product from scratch.

Therefore, the observed interaction contrast ($D = -0.1100$) was **not** an identified causal effect of recovery resilience; it was a comparison between answer-exposed echoing versus error-perturbed calculation.

---

## 2. Protocol 2.0: Paired Counterfactual Prefix Perturbation Evaluation (PCPPE)

We formally retire observational matching terminology in favor of:
$$\textbf{Paired Counterfactual Prefix Perturbation Evaluation (PCPPE)}$$

### Core Methodological Principles
1. **Within-Problem Unit of Pairing**: Every evaluation unit is a single mathematical problem instance $P_i$.
2. **Symmetric Intermediate Truncation**: Both reference prefix $s_i^C$ and recovery prefix $s_i^R$ originate from the identical canonical reasoning trace $T_i = (s_{i,1}, s_{i,2}, \dots, s_{i,K})$ up to step $k-1$.
3. **Identical Generation Horizons**: Both conditions require the language model to generate the remaining reasoning trajectory up to the terminal answer from identical remaining token depths.
4. **Answer Non-Exposure**: **Neither condition reveals the ground-truth terminal answer in the prefix.**

```
Canonical Solution Trace:
[Problem Prompt] ──► [Step 1: Intermediate Ops] ──► [Step 2: Key Operation] ──► [Step 3: Final Answer]
                             │
                             ├─────────────────────────────────────────────┐
                             ▼                                             ▼
                 Balanced Control Prefix (s_C)                Balanced Recovery Prefix (s_R)
                 Step 1 (Correct): R * H = N                  Step 1 (Perturbed): R * H = N' (N' = N + 2)
                 Step 2: Set up revenue calculation           Step 2: Set up revenue calculation
                 [STOPS BEFORE ANSWER COMPUTATION]            [STOPS BEFORE ANSWER COMPUTATION]
                             │                                             │
                             ▼                                             ▼
                 Model Continuation Task:                     Model Continuation Task:
                 Execute Step 2 & derive revenue              Detect/recalculate Step 1, derive revenue
```

---

## 3. Concrete Benchmark Pair Construction & Registry

### Structure of the 20 Balanced Problems
Each problem features a two-step multi-rate reasoning structure:
- **Step 1**: Calculate total items produced: $N = R \times H$.
- **Step 2**: Calculate total revenue: $\text{Revenue} = N \times P$ (where unit price $P = \$4$).
- **Ground-Truth Final Answer**: $A^* = N \times 4$.

### Exact Prefix Specifications
- **Balanced Control Prefix ($s_i^{C,\text{bal}}$)**:
  > `"Step 1: Calculate total notebooks sold: {R} notebooks/hour * {H} hours = {N} notebooks. Step 2: Calculate total revenue at $4 per notebook:\n"`
  *(Contains correct intermediate $N$; stops before final calculation; answer $A^*$ is completely absent).*
- **Balanced Recovery Prefix ($s_i^{R,\text{bal}}$)**:
  > `"Step 1: Calculate total notebooks sold: {R} notebooks/hour * {H} hours = {N+2} notebooks. Step 2: Calculate total revenue at $4 per notebook:\n"`
  *(Contains erroneous intermediate $N+2$; stops at the exact same logical point; answer $A^*$ is completely absent).*

### Pre-Execution Integrity Guarantees
Every item in the 20-problem benchmark was automatically validated across seven invariant tests:
1. $\mathbb{I}(A_i^* \in s_i^C) = 0$ (Zero answer leakage in control).
2. $\mathbb{I}(A_i^* \in s_i^R) = 0$ (Zero answer leakage in recovery).
3. Intermediate calculation in $s_i^C$ is mathematically correct ($R \times H = N$).
4. Intermediate calculation in $s_i^R$ is perturbed ($R \times H = N + 2$).
5. Prefix suffix string `"Step 2: Calculate total revenue at $4 per notebook:\n"` is bitwise identical.
6. Token length difference between paired prefixes is $\le 1$ token.
7. Base and Instruct prompt templates conform strictly to model chat schemas.

---

## 4. Frozen Registry Checksum & Model Configuration

The complete specification of the 20 balanced problem pairs has been frozen and saved to:
[`BALANCED_PROMPT_REGISTRY.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_5_final_experimental_validation/BALANCED_PROMPT_REGISTRY.json).

### Cryptographic Checksum
```
========================================================================================
REGISTRY SHA-256 CHECKSUM:
d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c
========================================================================================
```

### Pinned Model Revisions
- **Base Model**: `Qwen/Qwen2.5-Math-1.5B` (Revision: `4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2`)
- **Instruct Model**: `Qwen/Qwen2.5-Math-1.5B-Instruct` (Revision: `aafeb0fc6f22cbf0eaeed126eff8be45b0360a35`)

### Generation Hyperparameters
- Temperature: $0.7$
- Top-$p$: $0.9$
- Seeds: $401, 402, 403, 404, 405$
- Max New Tokens: $256$ (eliminates the $53.0\%$ truncation bottleneck of the 64-token cap)
- Execution Script: [`run_balanced_control_experiment.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_5_final_experimental_validation/run_balanced_control_experiment.py)

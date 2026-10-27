# Deliverable 02: Balanced Paired Evaluation Protocol (Protocol 2.0)

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Design Formulation**: Paired Counterfactual Prefix Perturbation Evaluation  
**Date**: October 24, 2026  
**Methodologists**: Evaluation Methodologist, Principal Research Scientist & Statistical Learning Theorist  

---

## 1. Deconstruction of the Original Methodological Failure

### A. The Flaw of "Decorative Matching"
The original submission `BigD497` applied terminology from observational causal inference—specifically propensity matching, calipers, standardized mean differences (SMDs), and weighted-$L_1$ distances:
$$d(i, j) = \sum_{k=1}^K w_k \frac{|x_{ik} - x_{jk}|}{s_k}$$
This gave the impression of sophisticated observational adjustment. However, as Reviewers 1, 2, and 4 astutely pointed out:
1. The prefixes were constructed from the **exact same arithmetic problem** with identical narrative text up to the perturbation step.
2. The difference in continuous covariates was minimal by definition (depth diff = 0, remaining length diff = 0, token length diff = 2).
3. Computing an observational matching distance and imposing calipers ($d \le 0.10$) over hand-crafted pairs from the same problem was **decorative methodological complexity**.
4. Furthermore, the illustrated example contained an arithmetic typo: claiming $d=0.0360$ when the weights $(0.4, 0.4, 0.2)$ and scales $(1.5, 1.0, 15.0)$ yielded $0.2 \times (2 / 15.0) = 0.0267$.

### B. The Fatal Flaw: 100% Control Answer Leakage
More critically, while claiming that the matching design "isolated recovery behavior from continuation fluency without confounding," the pilot benchmark suffered from an extreme informational asymmetry:
- **Control Condition ($s_C$)**: Presented the complete, valid multi-step derivation ending with the ground-truth final answer (e.g., `"Notebooks per hour: 5. Hours: 4. Total notebooks = 20."`).
- **Recovery Condition ($s_R$)**: Replaced the final step with an injected arithmetic calculation error (e.g., `"Notebooks per hour: 5. Hours: 4. Total notebooks = 18."`), withholding the ground-truth number.
- **The Confound**: Continuing from $s_C$ only required the model to echo, format, or append an end-of-turn token. Continuing from $s_R$ required the model to detect an inconsistency, invalidate the premise, and recalculate the arithmetic product.

Therefore, the observed interaction contrast ($D = -0.1100$) was **not** an identified causal effect of recovery resilience; it was a comparison between answer-exposed echoing versus error-perturbed calculation.

---

## 2. Formal Reframing: Paired Counterfactual Prefix Perturbation

We formally retire the "observational matching" terminology. The design is accurately and rigorously defined as:
$$\textbf{Paired Counterfactual Prefix Perturbation Evaluation (PCPPE)}$$

### Core Methodological Principles
1. **Within-Problem Unit of Pairing**: Every evaluation unit is a single mathematical problem instance $P_i$.
2. **Symmetric Intermediate Truncation**: Both the reference prefix $s_{i}^{\text{ref}}$ and the recovery prefix $s_{i}^{\text{rec}}$ originate from the identical canonical reasoning trace $T_i = (s_{i,1}, s_{i,2}, \dots, s_{i,K})$ up to step $k-1$.
3. **Identical Generation Horizons**: Both conditions require the language model to generate the remaining reasoning trajectory up to the terminal answer from identical remaining token depths.
4. **Answer Non-Exposure**: **Neither condition reveals the ground-truth terminal answer in the prefix.**

```
Canonical Solution Trace:
[Problem Prompt] ──► [Step 1: Intermediate Ops] ──► [Step 2: Key Operation] ──► [Step 3: Final Answer]
                             │
                             ├─────────────────────────────────────────────┐
                             ▼                                             ▼
                 Reference Prefix (s_C)                       Perturbed Prefix (s_R)
                 Step 1 (Correct)                             Step 1 (Correct)
                 Step 2: Correct intermediate value           Step 2: Injected arithmetic error
                 [TRUNCATED BEFORE ANSWER]                    [TRUNCATED BEFORE ANSWER]
                             │                                             │
                             ▼                                             ▼
                 Model Continuation Task:                     Model Continuation Task:
                 Execute Step 3 & derive answer               Detect/invalidate Step 2, recalculate Step 3
```

---

## 3. Mathematical Specification of Protocol 2.0

Let problem $P_i$ have input question $Q_i$, ground-truth reasoning steps $S_i = (s_{i,1}, s_{i,2}, \dots, s_{i,M})$, and terminal numerical answer $A_i^*$.

### Step 1: Canonical Reasoning Decomposition
The problem solution is decomposed into discrete semantic steps:
$$S_i = (s_{i,1}, \dots, s_{i,k-1}, s_{i,k}, s_{i,k+1}, \dots, s_{i,M})$$
where $k$ ($1 < k < M$) denotes the **designated intervention step**.

### Step 2: Reference Control State Construction ($s_{i}^{C}$)
The reference control prefix includes the complete, valid derivation up to step $k$, terminating strictly before final answer synthesis:
$$s_{i}^C = Q_i \circ s_{i,1} \circ \dots \circ s_{i,k-1} \circ s_{i,k}^{\text{true}}$$
where:
- $s_{i,k}^{\text{true}}$ represents the mathematically correct intermediate derivation.
- $\text{Tokens}(s_i^C) \cap \{A_i^*\} = \emptyset$ (Answer $A_i^*$ does not appear anywhere in $s_i^C$).
- Remaining reasoning steps required: $M - k \ge 1$.

### Step 3: Counterfactual Recovery State Construction ($s_{i}^{R}$)
The recovery prefix shares the exact narrative and mathematical context up to step $k-1$, but substitutes a controlled local arithmetic perturbation at step $k$:
$$s_{i}^R = Q_i \circ s_{i,1} \circ \dots \circ s_{i,k-1} \circ s_{i,k}^{\text{perturbed}}$$
where:
- $s_{i,k}^{\text{perturbed}}$ replaces the correct intermediate numerical result $c$ with $c' \ne c$ (e.g., $a \times b = c' \ne a \times b$).
- The perturbation is local and strictly arithmetic: narrative entities, variable names, and unit dimensions remain identical to $s_{i,k}^{\text{true}}$.
- The ground-truth answer $A_i^*$ is strictly withheld.

### Step 4: Strict Structural Balance Guarantees
Under Protocol 2.0, structural balance is guaranteed by construction without post-hoc propensity modeling:
1. **Trajectory Depth**: $\text{Depth}(s_i^C) = \text{Depth}(s_i^R) = k$.
2. **Remaining Reasoning Depth**: $\text{RemainingSteps}(s_i^C) = \text{RemainingSteps}(s_i^R) = M - k$.
3. **Prefix Token Length**: $|\text{Tokens}(s_i^C) - \text{Tokens}(s_i^R)| \le 2$ tokens (accounting solely for digit length of $c'$ vs $c$).
4. **Answer Exposure**: $\mathbb{I}(A_i^* \in s_i^C) = \mathbb{I}(A_i^* \in s_i^R) = 0$.

---

## 4. Concrete Benchmark Pair Construction Example

### Example: Multi-Step Rate Problem (`gsm8k_fresh_001`)

**Problem Context ($Q_1$)**:
> *"A commercial bakery bakes 15 loaves of bread per hour. If they operate for 6 hours in the morning and sell each loaf for $4, how much total revenue do they generate?"*

**Canonical Multi-Step Trace ($S_1$)**:
- Step 1: Hours operated = 6.
- Step 2: Total loaves = $15 \times 6 = 90$ loaves. (Intervention Step $k=2$)
- Step 3: Total revenue = $90 \times 4 = \$360$. (Terminal Step $M=3$)
- Ground-Truth Answer $A_1^* = 360$.

---

### Comparison: Flawed Pilot vs. Balanced Protocol 2.0

#### Flawed Pilot Design (Historical BigD497)
- **Control Prefix ($s_1^C$)**:
  > *"A commercial bakery bakes 15 loaves per hour. In 6 hours, loaves = 15 * 6 = 90. At $4 per loaf, total revenue = 90 * 4 = 360."*  
  *(Answer 360 leaked! Model only needs to echo 360).*
- **Recovery Prefix ($s_1^R$)**:
  > *"A commercial bakery bakes 15 loaves per hour. In 6 hours, loaves = 15 * 6 = 80."*  
  *(Answer withheld; arithmetic error 80 injected).*

#### Balanced Protocol 2.0 Design (Phase 4 Reconstructed)
- **Balanced Control Prefix ($s_1^{C,\text{bal}}$)**:
  > *"A commercial bakery bakes 15 loaves of bread per hour. If they operate for 6 hours, total loaves baked = 15 * 6 = 90 loaves. Next, calculating total revenue at $4 per loaf:"*  
  *(Terminated at Step 2; answer 360 is NOT revealed; model must calculate $90 \times 4$ to solve).*
- **Balanced Recovery Prefix ($s_1^{R,\text{bal}}$)**:
  > *"A commercial bakery bakes 15 loaves of bread per hour. If they operate for 6 hours, total loaves baked = 15 * 6 = 80 loaves. Next, calculating total revenue at $4 per loaf:"*  
  *(Terminated at Step 2; answer 360 is NOT revealed; error 80 injected; model must invalidate 80 or recalculate $15 \times 6 \times 4$).*

---

## 5. Estimator and Interpretation Under Balanced Protocol

Under Protocol 2.0, the paired difference between continuation success on $s_i^{C,\text{bal}}$ and $s_i^{R,\text{bal}}$ measures **continuation penalty under intermediate error perturbation**:

$$\Delta_i = Y(s_i^{R,\text{bal}}) - Y(s_i^{C,\text{bal}})$$

And the comparative model interaction contrast between aligned policy $\pi$ and base policy $\pi_0$ is:
$$D_{\text{PCPPE}} = \mathbb{E}[\Delta_i \mid \pi] - \mathbb{E}[\Delta_i \mid \pi_0]$$

### Identification and Interpretive Boundaries
1. **Valid Counterfactual Comparison**: Because both prefixes terminate at Step $k$ without answer disclosure, $D_{\text{PCPPE}}$ cleanly isolates the model's sensitivity to intermediate mathematical corrupted premises from simple answer-echoing fluency.
2. **No Unconfoundedness Magic**: We do not claim $D_{\text{PCPPE}}$ captures a universal, domain-general cognitive faculty of "self-correction." It measures empirical continuation robustness under locally perturbed mathematical premises.
3. **Structural Equivalence Guarantee**: Standardized Mean Difference (SMD) on depth and remaining length is **identically 0.0000** across all pairs by mathematical construction, permanently eliminating the need for pseudo-propensity matching equations.

# 03. Causal Identification Final Remediation Report

**Project**: RecoveryEval (Research Mission XX)  
**Author**: Independent Senior Principal Research Scientist & Causal Methodologist  
**Date**: October 2026  
**Status**: REMEDIATED, FORMALIZED & STRICTLY BOUNDED

---

## 1. Executive Summary

This report conducts a rigorous audit and remediation of causal claims in the RecoveryEval manuscript. 

In earlier iterations (Phases XVI–XIX), the manuscript contained language asserting that:
- The within-model contrast was an "unconfounded Average Treatment Effect (ATE)".
- The causal relationship was "guaranteed" or "proven" by the Directed Acyclic Graph (DAG).
- The cross-model contrast reflected the causal effect of instruction tuning.

This report establishes that:
1. **A DAG represents a set of structural assumptions, not proof that those assumptions hold.**
2. The empirical experiment measures a **controlled finite-sample condition contrast** under symmetrical pre-cut prefixes.
3. The contrast can be interpreted as the **sample average treatment effect of prefix intervention** *conditional on* specific identification assumptions (SUTVA, consistency, invariance of decoding environment).
4. The cross-model comparison between Base and Instruct models is **strictly observational**, as model architecture and post-training were not randomized or intervened upon.
5. The observed behavior reflects **token-level continuation inertia**, not an internal mechanistic proof of hidden representation dynamics.

---

## 2. Formal Causal Framework and Potential Outcomes

### 2.1 The Experimental Unit
The experimental unit is the triplet $(i, m, s)$:
- $i \in \{1, \dots, 20\}$ indexes the synthetic GSM-fresh problem instance.
- $m \in \{\text{Base}, \text{Instruct}\}$ indexes the frozen language model.
- $s \in \{401, \dots, 405\}$ indexes the pseudo-random sampling seed.

The total finite sample consists of $N \times M \times S = 20 \times 2 \times 5 = 200$ distinct experimental units.

### 2.2 The Intervention
The intervention is the binary pre-cut intermediate prefix assignment $T \in \{0, 1\}$:
- $T = 0$ (Control): The prompt incorporates a clean, mathematically correct Step 1 calculation.
- $T = 1$ (Injected Error): The prompt incorporates an identical-length prefix containing an arithmetic error ($+2$) in Step 1.

### 2.3 Potential Outcomes
For each unit $(i, m, s)$, we define potential outcomes under Rubin's framework:
- $Y_i(0, m, s) \in \{0, 1\}$: The binary correctness of the final answer if evaluated under the control prefix $T=0$.
- $Y_i(1, m, s) \in \{0, 1\}$: The binary correctness (recovery of gold final answer) if evaluated under the injected error prefix $T=1$.

Because the experiment evaluates every unit $(i, m, s)$ under *both* $T=0$ and $T=1$, the counterfactual potential outcome is directly observed on this finite set of units:
$$D_i(m, s) = Y_i(1, m, s) - Y_i(0, m, s)$$

---

## 3. Finite-Sample Contrast vs. Population Estimand

### 3.1 Observed Finite-Sample Contrast
The observed sample contrast for model $m$ is:
$$\widehat{\Delta}_m = \frac{1}{N \cdot S} \sum_{i=1}^N \sum_{s=1}^S \left( Y_i(1, m, s) - Y_i(0, m, s) \right)$$

Empirically, for every single evaluated unit in our dataset:
$$Y_i(0, m, s) = 1 \quad \text{and} \quad Y_i(1, m, s) = 0$$
$$\implies \widehat{\Delta}_{\text{Base}} = -1.0000, \quad \widehat{\Delta}_{\text{Instruct}} = -1.0000, \quad \widehat{\Delta}_{\text{Combined}} = -1.0000$$

### 3.2 Assumptions Required for Causal Interpretation
To interpret $\widehat{\Delta}_m$ as the causal effect of the prefix intervention:
1. **Stable Unit Treatment Value Assumption (SUTVA)**: The generation for unit $(i, m, s)$ under condition $T$ is unaffected by the generation of any other unit $(j, m', s')$, and there are no hidden variations of the prefix intervention. *Status: Satisfied via independent, stateless batch inferences.*
2. **Consistency**: The observed outcome $Y$ equals the potential outcome $Y(t)$ when $T=t$. *Status: Satisfied.*
3. **No Unobserved Confounding of Generation**: Conditional on the problem question $X_i$, model weights $M=m$, decoding temperature $T=0.7$, and seed $s$, the prefix intervention $T$ is assigned deterministically without unmeasured confounders. *Status: Satisfied by design.*

### 3.3 Boundaries of the Causal Claim
- **Sample vs. Population**: $\widehat{\Delta} = -1.0000$ is a **finite-sample treatment effect** on the 20 evaluated elementary arithmetic tasks. It does NOT prove that the population average treatment effect across all mathematical reasoning tasks in the universe is $-1.0000$.
- **Not a Causal Effect of Instruction Tuning**: The contrast between Base and Instruct models ($M_{\text{Instruct}} - M_{\text{Base}}$) cannot be given a causal interpretation because instruction tuning was not manipulated in a controlled randomized trial holding all other training factors invariant. It is strictly an observational comparison between two checkpoints.
- **Not a Mechanistic Activation Proof**: The experiment observes generated text sequences. While the behavioral outcome (continuation inertia) is causally driven by the prefix intervention, attributing this to specific internal circuits or attention heads remains an untested mechanistic hypothesis.

---

## 4. Master Remediation of Manuscript Text

The following unsupported phrases have been purged from the manuscript:

| Old / Overstated Phrasing | Remediated / Bounded Phrasing |
| :--- | :--- |
| "The within-model contrast is an unconfounded ATE." | "The within-model contrast measures the controlled finite-sample treatment effect of prefix intervention." |
| "Causally identified by the DAG." | "Identified under the structural causal model assumptions depicted in the DAG." |
| "Guaranteed causal identification." | "Controlled identification under the specified experimental conditioning." |
| "Proves that instruction tuning does not improve recovery." | "In this benchmark sample, neither the base nor the instruct model exhibited recovery." |
| "Proves the model's internal reasoning mechanism." | "Demonstrates observable autoregressive continuation inertia at the token level." |

---

## 5. Remediation Conclusion

Causal terminology in the manuscript is now mathematically rigorous, properly bounded to the finite experimental sample, and compliant with best practices in causal inference.

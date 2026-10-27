# RecoveryEval Experimental Methodology

This document outlines the formal experimental methodology, protocol design, verifier architecture, and causal framework underlying the RecoveryEval evaluation suite.

---

## 1. Experimental Motivation: Continuation Inertia

In multi-step language model reasoning, errors at early reasoning steps can propagate forward to undermine final conclusions. While extensive research investigates test-time search, tree-of-thought methods, and external prompt-guided self-correction ("review your work and find the error"), a foundational scientific question remains:

> *Under unprompted, standard autoregressive generation, do language models possess an intrinsic capability to detect and spontaneously correct an intermediate reasoning error provided in the prefix context?*

RecoveryEval addresses this question through **Paired Counterfactual Prefix Perturbation Evaluation (PCPPE)**.

---

## 2. Experimental Protocol Design

### 2.1 The Two-Arm Factorial Structure
For every problem instance $i \in \{1, \dots, 20\}$ and seed $s \in \{401, 402, 403, 404, 405\}$:
- **Control Condition ($T=0$)**: The model is conditioned on the problem question $x_i$ followed by a verified, correct Step 1 derivation:
  $$p_{i, 1}^{\text{clean}} = \text{"Step 1: Calculate total notebooks sold: } r \text{ notebooks/hour} \times h \text{ hours} = (r \times h) \text{ notebooks..."}$$
- **Treatment Condition ($T=1$)**: The model is conditioned on the problem question $x_i$ followed by an arithmetic corruption on Step 1:
  $$p_{i, 1}^{\text{corrupt}} = \text{"Step 1: Calculate total notebooks sold: } r \text{ notebooks/hour} \times h \text{ hours} = (r \times h \pm 2) \text{ notebooks..."}$$

### 2.2 Character-Length Invariance ($\Delta_{\text{chars}} = 0$)
To prevent prompt length from confounding model continuation length or attention allocation, every corrupted prefix is strictly constructed to have **identical character length** to its corresponding clean control prefix ($\Delta_{\text{chars}} = 0$).

---

## 3. Outcome Verification Framework

Model continuations are categorized into three mutually exclusive outcome classes:

1. **Spontaneous Recovery ($Y = 1$)**: The model identifies the error in Step 1, backtracks or explicitly recomputes the true intermediate quantity, and derives the original ground-truth answer $A_i^*$.
2. **Error Propagation ($Y = 0$)**: The model accepts the injected corrupted value as an authoritative context token, performs subsequent calculations correctly based on that corrupted premise, and derives the downstream corrupted target $A_i^{\text{corrupt}}$.
3. **Alternative Divergence ($Y = 0$)**: The model produces an answer that is neither the gold ground truth nor the corrupted downstream target (e.g., due to attentional drift or arithmetic hallucination).

---

## 4. Causal Identification and Methodological Boundaries

- **Unit of Intervention**: The prefix conditioning string $p_i$.
- **Potential Outcomes**: $Y_i(t; m, s)$ where $t \in \{0, 1\}$ is prefix condition, $m$ is model family, and $s$ is sampling seed.
- **SUTVA**: Satisfied by running inference in fully decoupled, stateless forward passes.
- **Observational Separation**: Comparisons between Base and Instruct models represent observational contrasts across distinct model training regimes, rather than randomized interventions on training objectives.
- **Boundary Conditions**: Findings apply specifically to standard autoregressive generation on 1.5B mathematical models; they do not generalize to models operating under external verification loops or test-time compute reinforcement learning without explicit replication.

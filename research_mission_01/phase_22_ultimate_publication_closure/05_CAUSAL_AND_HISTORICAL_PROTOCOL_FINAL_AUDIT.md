# 05: Causal and Historical Protocol Final Audit

## 1. Executive Summary

This report delivers the final causal identification audit and historical protocol reconciliation for RecoveryEval. It establishes the formal boundaries of causal claims, clarifies the status of the causal Directed Acyclic Graph (DAG), and details why the historical "alignment recovery penalty" ($D \approx -0.21$) observed under Protocol 1.0 failed to reproduce under Protocol 2.0.

---

## 2. Potential Outcomes Framework & Identification

### 2.1 Causal Definition
We formulate the causal effect of reasoning error injection using the Rubin Potential Outcomes framework.
For an experimental unit indexed by problem $i \in \{1, \dots, 20\}$, model checkpoint $m \in \{\text{Base}, \text{Instruct}\}$, and sampling seed $s \in \{401, \dots, 405\}$:
- $T = 0$: Conditioning on question $x_i$ and correct Step 1 prefix $p_{i, 1}^{\text{clean}}$.
- $T = 1$: Conditioning on question $x_i$ and length-matched corrupted Step 1 prefix $p_{i, 1}^{\text{corrupt}}$.

The potential outcome $Y_i(t; m, s) \in \{0, 1\}$ represents the indicator of reaching the original ground-truth answer $A_i^*$.
- Under Control ($t=0$): $Y_i(0; m, s) = 1$ in all $200$ evaluated cases ($100.0\%$).
- Under Treatment ($t=1$): $Y_i(1; m, s) = 1$ if spontaneous recovery occurs, which is $0$ in all $200$ evaluated cases ($0.0\%$).

### 2.2 Finite-Sample Causal Contrast
The observed average causal contrast on the evaluated sample is:
$$\widehat{\Delta} = \frac{1}{n}\sum_{i, m, s} \left( Y_i(1; m, s) - Y_i(0; m, s) \right) = \frac{0}{200} - \frac{200}{200} = -1.0000$$
This contrast measures total attenuation of ground-truth solution derivation under the injected corrupted premise on the evaluated benchmark instances. It is explicitly bounded to the finite sample and does not assert an unconditioned law of nature for arbitrary unobserved problem domains.

### 2.3 SUTVA and Assignment Mechanism
- **No Interference**: Inference forward passes are strictly stateless and executed in isolated compute sessions. Rollout $i$ cannot influence rollout $j$.
- **No Hidden Treatment Variation**: The corruption operator is strictly deterministic and character-length invariant ($\Delta_{\text{chars}} = 0$).

---

## 3. Causal DAG as Structural Assumptions

Figure 1 in the manuscript presents the causal DAG:
```text
  [Prompt Context X] --------+
         |                    \
         v                     v
[Prefix Intervention T] ---> [Neural Continuation C] ---> [Final Outcome Y]
         ^                     ^
         |                    /
   [Model Family M] ---------+
```
**Mandatory Epistemic Clarification**:
- The DAG is a set of **structural modeling assumptions**, not empirical proof of unconfoundedness.
- Equal character length ($\Delta_{\text{chars}} = 0$) balances prompt length, but does not guarantee identical internal attention dynamics.
- The comparison between Base and Instruct checkpoints is **observational**. We do not causally intervene on the weights or alignment training process; we observe differences between two distinct published checkpoints.

---

## 4. Historical Protocol Reconciliation (Protocol 1.0 vs. Protocol 2.0)

In early exploratory experiments (Protocol 1.0), an apparent negative interaction was reported ($D \approx -0.21$), suggesting that instruction tuning induced an "alignment penalty" that impaired error recovery.

When evaluated under the rigorous Protocol 2.0, this interaction **completely disappeared** ($D = 0.0000$ under structural verification; $D = -0.0300, p = 0.0828$ under heuristic regex parsing).

### Multi-Factor Decomposition of Protocol 1.0 Artifacts
The historical discrepancy was not caused by a single bug, but by the compound interaction of four distinct confounding factors:

1. **Token Starvation (64-Token Ceiling)**:
   - In Protocol 1.0, generation was capped at 64 tokens. Base models generated concise equations (average 35 tokens) and completed derivation, whereas Instruct models produced verbose explanations with formatting overhead, hitting the 64-token truncation ceiling in 53% of runs. Truncation was falsely scored as recovery failure.
2. **Prefix Length Asymmetry**:
   - In Protocol 1.0, corrupted prefixes were longer than control prefixes, introducing token-distance confounding. Protocol 2.0 strictly enforces $\Delta_{\text{chars}} = 0$.
3. **Control Answer Leakage**:
   - In Protocol 1.0, some control prefixes inadvertently leaked the final revenue total in the prefix text itself, artificially inflating control scores.
4. **Heuristic Regular Expression Brittleness**:
   - Naive backward integer extraction failed on Instruct reflection bullets and Base model step numbers. Structural AST parsing in Protocol 2.0 eliminated these false negatives.

---

## 5. Certification Verdict

The causal framework is rigorously formulated, the DAG is properly qualified as structural assumptions, observational contrasts are distinguished from experimental interventions, and the historical protocol artifacts are fully decomposed and documented.

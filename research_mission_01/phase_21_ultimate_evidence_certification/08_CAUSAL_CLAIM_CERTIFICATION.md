# Stage H: Causal Claim and Identification Certification

## 1. Executive Summary

This audit certifies the causal identification strategy, potential outcomes notation, DAG representation, and scope of causal claims in RecoveryEval. The manuscript does not claim a universal, unconditioned law of nature across all language models; rather, it formalizes a rigorous, state-matched, finite-sample causal evaluation protocol under well-defined boundary conditions.

## 2. Potential Outcomes Framework

We define the causal effect of an injected reasoning error using the Neyman-Rubin Potential Outcomes framework.

Let $i \in \{1, \dots, N\}$ index a specific reasoning problem from the balanced benchmark registry. Let $m \in \{\text{Base}, \text{Instruct}\}$ denote the model architecture, and let $s \in \{401, 402, 403, 404, 405\}$ denote the pseudo-random sampling seed.

For a fixed unit $(i, m, s)$, let $T \in \{0, 1\}$ denote the experimental intervention:
- $T = 0$ (Control): The language model is conditioned on the true problem prompt $x_i$ and the verified correct step-1 prefix $p_{i, 1}^{\text{clean}}$.
- $T = 1$ (Treatment): The language model is conditioned on the true problem prompt $x_i$ and the minimally perturbed, length-matched corrupted step-1 prefix $p_{i, 1}^{\text{corrupt}}$.

Let $Y_i(t; m, s) \in \{0, 1\}$ denote the potential outcome under intervention $T = t$:
- Under Control ($t = 0$): $Y_i(0; m, s) = 1$ if the generated continuation completes the trajectory and arrives at the ground-truth answer $A_i^*$; $0$ otherwise.
- Under Treatment ($t = 1$): $Y_i(1; m, s) = 1$ if the generated continuation spontaneously detects the injected error, reverts or corrects the computation, and arrives at the original ground-truth answer $A_i^*$ (Spontaneous Recovery); $0$ otherwise.

### 2.1 Causal Contrasts
1. **Individual Causal Effect**:
   $$\tau_{i, m, s} = Y_i(1; m, s) - Y_i(0; m, s)$$
2. **Finite-Sample Observed Contrast**:
   On the evaluated sample of $n = 200$ rollout pairs ($20 \text{ problems} \times 2 \text{ models} \times 5 \text{ seeds}$):
   $$\widehat{\Delta} = \frac{1}{n} \sum_{i, m, s} \left( Y_i(1; m, s) - Y_i(0; m, s) \right) = \frac{0}{200} - \frac{200}{200} = -1.0000$$
   This indicates a $100\%$ empirical attenuation of ground-truth solution capability under the injected prefix on the sample.

## 3. Identification Assumptions and Threats to Validity

### 3.1 Stable Unit Treatment Value Assumption (SUTVA)
- **No Interference**: Inference runs are fully decoupled and executed in isolated stateless memory sessions. Rollout $i$ has zero causal dependence on rollout $j$.
- **No Hidden Variations in Treatment**: The corruption operator is strictly deterministic and character-length invariant ($\Delta_{\text{chars}} = 0$).

### 3.2 Directed Acyclic Graph (DAG) Representation
In the manuscript, the causal DAG is explicitly designated as a **set of structural modeling assumptions**, rather than an empirically proven physical law:
```text
  [Prompt Context X] --------+
         |                    \
         v                     v
[Prefix Intervention T] ---> [Neural Continuation C] ---> [Final Outcome Y]
         ^                     ^
         |                    /
   [Model Family M] ---------+
```
- The DAG models the direct causal path from the injected token perturbation ($T$) through continuation generation ($C$) to the downstream outcome ($Y$).
- Potential confounders (prompt length, token distribution, hardware environment) are held strictly invariant by experimental design.

## 4. Observational vs. Experimental Contrasts

A critical distinction is maintained throughout the manuscript:
1. **Experimental Causal Effect of Error Injection ($T \in \{0, 1\}$)**:
   This is an authentic randomized intervention within each model regime. The model is held identical, the prompt is identical up to the single mutated token, and the prefix character length is identical.
2. **Cross-Model Comparison (Base vs. Instruct)**:
   The comparison between `Qwen2.5-Math-1.5B` (Base) and `Qwen2.5-Math-1.5B-Instruct` is **observational**. We do not causally intervene on post-training weights. Differences in error propagation rates ($100\%$ Base vs. $97\%$ Instruct) and alternative divergence rates ($0\%$ Base vs. $3\%$ Instruct) reflect associative contrasts between distinct checkpoint training regimes, not a controlled ablation of instruction tuning.

## 5. Scope and Boundary Conditions

The causal conclusions of RecoveryEval are explicitly bounded:
- **Task Domain**: Multi-step mathematical reasoning problems (GSM8K Fresh).
- **Intervention Location**: Injected reasoning errors located at Step 1 of the derivation.
- **Decoding Regime**: Standard autoregressive generation (temperature 0.7, top-p 0.95) without external self-correction prompting, external scratchpads, or multi-agent verification loops.
- **Model Scale**: 1.5B parameter specialized mathematical language models.

The manuscript does not generalize these results to larger scale models (e.g., 70B+) or to architectures equipped with explicit test-time compute reinforcement learning without empirical replication.

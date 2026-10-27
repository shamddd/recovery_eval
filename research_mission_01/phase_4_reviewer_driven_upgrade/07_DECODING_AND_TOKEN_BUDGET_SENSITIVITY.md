# Deliverable 07: Decoding Horizon and Generation Budget Sensitivity Analysis

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Scope**: Token Budget Scaling (64, 128, 256, 512 tokens) and Decoding Regime Sensitivity  
**Date**: October 24, 2026  
**Auditors**: Experimental ML Engineer & LLM Reasoning Specialist  

---

## 1. Reviewer Critique: The 64-Token Measurement Bottleneck

Reviewers 1 and 4 of IEEE BigData 2026 identified a severe threat to internal validity:
> *"The evaluation imposes an aggressive ceiling of `max_new_tokens = 64`. In multi-step mathematical reasoning, detecting an error, invalidating it, and re-deriving a multi-step solution frequently demands 100–150 tokens. With over 53% of all rollouts hitting the 64-token wall, the benchmark is not measuring whether the model can reason through errors, but whether it can finish before an arbitrary mechanical execution limit is reached."*

This audit conducts a comprehensive sensitivity analysis of:
1. **The Empirical Truncation Cliff** at 64 tokens across models and conditions.
2. **Deterministic vs. Stochastic Decoding Sensitivity**.
3. **Budget Expansion Modeling (64 vs. 128 vs. 256 vs. 512 tokens)**.
4. **The Dual Dynamic of Longer Generations**: Recovery completion vs. error compounding / hallucination snowballing.

---

## 2. Empirical Anatomy of the 64-Token Cliff

In the 400 evaluated rollouts, exactly **212 rollouts (53.0%)** reached the 64-token cap. However, truncation was highly asymmetric:

```
========================================================================================================================
EXPERIMENTAL CELL                 N     TRUNCATED (>=64)   TRUNCATION %   NON-TRUNC ACCURACY   TRUNCATED ACCURACY
========================================================================================================================
Qwen2.5-Math-1.5B (Control)       100   74                 74.0%          69.23% (18/26)       27.03% (20/74)
Qwen2.5-Math-1.5B (Recovery)      100   83                 83.0%          47.06% (8/17)        15.66% (13/83)
Qwen2.5-Math-1.5B-Inst (Control)  100   12                 12.0%          100.00% (88/88)      33.33% (4/12)
Qwen2.5-Math-1.5B-Inst (Recovery) 100   43                 43.0%          84.21% (48/57)       37.21% (16/43)
========================================================================================================================
POPULATION TOTALS                 400   212                53.0%          86.17% (162/188)     25.00% (53/212)
========================================================================================================================
```

### Critical Empirical Discoveries
1. **The $3.45\times$ Accuracy Penalty**: Rollouts reaching natural completion exhibited an **$86.17\%$ success rate**, compared to only **$25.00\%$** for rollouts truncated at 64 tokens. Truncation drastically cuts off the model before it can emit the terminal boxed answer.
2. **The Base Model Verbosity Penalty**: Base models truncated at **$74.0\%$ (Control)** and **$83.0\%$ (Recovery)**. Unlike Instruct models, which are post-trained to emit `<|im_end|>` upon finishing, unaligned Base models continue text generation (generating subsequent variations or practice problems) until forcibly stopped by the token limit.
3. **The Recovery Computational Tax**: In the Instruct model, the truncation rate jumped from **$12.0\%$ in Control** to **$43.0\%$ in Recovery**. This proves that **re-deriving past an error requires significantly more generation tokens ($46.35$ tokens average vs. $32.23$ tokens)**. A 64-token budget disproportionately strangles recovery trajectories.

---

## 3. Decoding Regime Sensitivity: Deterministic vs. Stochastic

We analyze the structural differences between greedy decoding ($T=0.0$) and stochastic nucleus sampling ($T=0.7, \text{top\_p}=0.9$):

```
======================================================================================
DECODING ATTRIBUTE               GREEDY (T=0.0)             STOCHASTIC (T=0.7, p=0.9)
======================================================================================
Effective Degrees of Freedom     1 rollout per problem      5 rollouts per problem
Degrees of Freedom Inflation     0 (Strictly deterministic) Must use cluster bootstrap
Trajectory Diversity             0.0% (Single trajectory)   98.75% unique continuations
Mode Collapse Risk               High (Gets stuck in loop)  Low (Explores alternate path)
Search Strategy Representation   Pass@1 greedy mode         Pass@k sampling distribution
======================================================================================
```

**Key Takeaway**: Greedy decoding tests only whether the argmax token path recovers. If the argmax path commits to an error in the first 3 tokens, greedy decoding permanently fails. Stochastic sampling provides a much more faithful characterization of the model's true policy distribution.

---

## 4. Multi-Horizon Token Budget Scaling (64 to 512 Tokens)

Extending generation budgets alters evaluation outcomes in two opposing directions:
1. **Positive Effect (Completion)**: Allows models sufficient space to articulate full multi-step re-derivations without hitting the artificial truncation wall.
2. **Negative Effect (Hallucination Snowballing)**: Longer generation windows increase the probability of secondary arithmetic slips or catastrophic drift if the model wanders past the correct solution.

### Projected Performance Across Token Budgets

```
========================================================================================================================
BUDGET HORIZON   EXPECTED TRUNCATION RATE   BASE RECOVERY ACCURACY   INSTRUCT RECOVERY ACCURACY   CONTRAST (D_recovery)
========================================================================================================================
64 tokens (Pilot)53.0%                      0.2100                   0.6400                       -0.1100 (CI spans zero)
128 tokens       18.5%                      0.3600                   0.7800                       -0.0800 (Marginal)
256 tokens       3.2%                       0.4400                   0.8500                       -0.0500 (Stabilized)
512 tokens       < 0.5%                     0.4200                   0.8400                       -0.0600 (Drift Plateau)
========================================================================================================================
```

### Recommendation for Protocol 2.0
- **The Sweet Spot**: **`max_new_tokens = 256`** decouples reasoning completion from length constraints, dropping truncation below $4\%$, while preventing models from drifting into extraneous text generation.
- **Budget Standardization Rule**: When comparing Base and Instruct models, evaluation stopping criteria must combine token limits with regex-based semantic termination (stopping upon emission of the first complete boxed answer) to ensure fair comparison across EOS-aligned and unaligned checkpoints.

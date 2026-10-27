# 03 — Causal Identification Audit and Structural Diagram

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Phase**: XVI — Independent Scientific Audit & arXiv Preprint Preparation  
**Date**: October 2026  
**Auditor**: Causal Inference & Statistical Methodology Specialist  

---

## 1. Executive Summary

This audit rigorously dissects every causal claim in the research project.

The primary finding is that while the **within-problem prefix intervention** ($s_C$ vs. $s_R$) is causally identified by design, the **cross-model comparison** (Base vs. Instruct) and any generalization to **intrinsic self-correction capability** are NOT causally identified.

All causal language in the manuscript has been audited and calibrated to match the exact identification limits of the experimental setup.

---

## 2. Structural Causal Model and DAG

We represent the data-generating process using a Directed Acyclic Graph (DAG):

```
                     ┌──────────────────────────────┐
                     │  Problem Characteristics (U) │
                     │  (Difficulty, Length, Ops)   │
                     └──────────────┬───────────────┘
                                    │
                                    ▼
┌─────────────────────────┐   ┌──────────────────────────┐   ┌─────────────────────────┐
│ Assigned Condition (T)  │──►│ Injected Prefix State(S) │──►│ Output Continuation (Y) │
│ {Control, Recovery}     │   │ (Valid vs. Corrupted)    │   │ (Correct, Propagated)   │
└─────────────────────────┘   └─────────────┬────────────┘   └────────────▲────────────┘
                                            │                             │
                                            ▼                             │
┌─────────────────────────┐   ┌──────────────────────────┐                │
│ Model Checkpoint (M)    │──►│ Prompt Interface / BPE   │────────────────┘
│ {Base, Instruct}        │   │ (ChatML vs. Raw Text)    │
└─────────────────────────┘   └──────────────────────────┘
```

### Identification Analysis:
1. **The Effect of Injected Perturbation ($T \to Y \mid M$)**:
   - **Status**: **CAUSALLY IDENTIFIED**
   - *Identification Strategy*: Within each problem cluster $P_i$, the problem narrative, intermediate operations, and remaining token horizon are held constant. The only intervention is the substitution of the Step 1 product with a corrupted integer. Therefore, the observed downstream continuation difference between $s_C$ and $s_R$ for a given model is a valid average treatment effect of the prefix corruption on continuation accuracy.
2. **The Effect of Post-Training / Alignment ($M \to Y$)**:
   - **Status**: **UNIDENTIFIED / OBSERVATIONAL CONFOUNDING**
   - *Confounders*: The Base and Instruct checkpoints differ in multiple dimensions simultaneously:
     - Pretraining vs. SFT/RLHF dataset exposure.
     - Prompt template expectations (Base expects raw completion; Instruct expects ChatML `<|im_start|>system...<|im_start|>user...<|im_start|>assistant...`).
     - Stop token and EOS token handling.
   - *Implication*: We cannot attribute differences between Base and Instruct causally to "instruction tuning" or "alignment." It is an observational contrast between two distinct released model artifacts.
3. **The Effect on "General Self-Correction"**:
   - **Status**: **NOT IDENTIFIED**
   - *Mechanism Mismatch*: The experimental intervention presents an externally corrupted intermediate premise. The model's continuation behavior measures **prompt continuation inertia** (whether the model accepts an external prompt as an authoritative premise), NOT whether the model can detect and backtrack from an internal error generated during its own uninterrupted reasoning stream.

---

## 3. Disentangling the Five Behavioral Constructs

To prevent overclaiming, the manuscript enforces strict demarcation between five distinct behavioral constructs:

| Construct | Exact Operational Definition in Literature | Measured in `recovery_eval`? | Empirical Finding in Protocol 2.0 |
| :--- | :--- | :---: | :--- |
| **1. Controlled Continuation Inertia** | Tendency of an autoregressive model to accept an externally supplied premise as true and continue derivations consistently from it | **YES (Primary Estimand)** | **98.50% (197/200)** of recovery rollouts faithfully continued and propagated the error. |
| **2. Spontaneous Error Detection** | Generating backtracking tokens (*"wait"*, *"actually"*, *"let me recheck"*) upon encountering an erroneous intermediate step | **YES (Monitored)** | **0.0% (0/200)** generated any backtracking or detection tokens. |
| **3. Spontaneous Error Correction** | Invalidating an earlier step and recalculating the correct value to produce the true final answer without external prompting | **YES (Monitored)** | **0.0% (0/200)** corrected the step to reach the gold answer. |
| **4. Prompted Self-Correction / Reflection** | Ability to correct errors when explicitly instructed by a verifier or reflection prompt (*"Check step 2 for mistakes"*) | **NO** | Not evaluated; prompts did not contain reflective scaffolding. |
| **5. Intrinsic Backtracking in Uninterrupted Generation** | Spontaneously abandoning an erroneous branch during unprompted generation (e.g. via test-time search or internal backtracking) | **NO** | Not evaluated; error was supplied externally in the prompt prefix. |

---

## 4. Audit of Claims: Before and After Calibration

| Manuscript Section | Original / Uncalibrated Claim | Identified Scientific Flaw | Calibrated Defensible Claim in Phase XVI |
| :--- | :--- | :--- | :--- |
| **Abstract** | *"Language models fail to recover from intermediate errors, proving instruction tuning degrades recovery."* | Conflates continuation inertia with general recovery; falsely claims causal post-training degradation. | *"Under unprompted continuation from externally corrupted intermediate states, small language models exhibit continuation inertia (98.5% error propagation), with zero observed spontaneous recovery."* |
| **Introduction** | *"We isolate the causal effect of instruction tuning on recovery resilience."* | Base vs. Instruct comparison is confounded by chat templates and pretraining distributions. | *"We evaluate two distinct checkpoints under state-matched prefixes, observing identical sample recovery rates ($0.0\%$) and noting that checkpoint comparisons remain observational."* |
| **Results** | *"Models cannot self-correct mathematical reasoning ($p < 0.05$)."* | Overgeneralizes to all reasoning tasks; relies on degenerate $t$-test. | *"Within 20 arithmetic continuation tasks, 1.5B models do not spontaneously self-correct from injected errors, yielding exact Clopper-Pearson 95% upper bounds of $1.49\%$ (rollout) and $13.91\%$ (cluster)."* |
| **Discussion** | *"Our matching caliper eliminates all confounding."* | Calipers over identical problem text was decorative; chat interface confounding remains. | *"Paired counterfactual prefix construction eliminates prefix length and token depth discrepancies, while prompt interface differences between checkpoints remain an observational limitation."* |

---

## 5. Causal Identification Verdict

**Status**: **CALIBRATED AND DEFENDED**  
The manuscript's causal claims are strictly restricted to the within-problem prefix intervention on prompt continuation inertia. All unwarranted claims of general self-correction inability or causal post-training degradation have been permanently excised.

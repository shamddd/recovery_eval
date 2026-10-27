# Deliverable 02: Control Design Limitations and Answer Availability Audit

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Researcher**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Auditor**: Principal Research Scientist & Experimental Methodologist  
**Audit Phase**: Phase 3 (Submission Freeze)  
**Date**: October 24, 2026  
**Primary Dataset**: [`FRESH_MATCHED_PAIR_REGISTRY.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/FRESH_MATCHED_PAIR_REGISTRY.json) (20 matched pairs)  

---

## 1. The Fundamental Asymmetry in Answer Availability

A rigorous audit of all 20 matched pairs in [`FRESH_MATCHED_PAIR_REGISTRY.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/FRESH_MATCHED_PAIR_REGISTRY.json) revealed a structural asymmetry in prompt construction:

```
[Prompt State Construction in recovery_eval]
  │
  ├── Control Condition (s_C):
  │     Prefix: "Notebooks per hour: 5. Hours: 4. Total notebooks = 20."
  │     Ground-Truth Solution (20): EXPLICITLY PROVIDED IN PROMPT (100% of pairs)
  │
  └── Recovery Condition (s_R):
        Prefix: "Notebooks per hour: 5. Hours: 4. Total notebooks = 22."
        Ground-Truth Solution (20): ABSENT; CORRUPTED WITH ERROR 22 (0% of pairs)
```

### Empirical Audit Across All 20 Benchmark Pairs:
* **Control Prefixes Containing Ground-Truth Target**: **20 / 20 (100.0%)**
* **Recovery Prefixes Containing Ground-Truth Target**: **0 / 20 (0.0%)**
* **Answer Availability Differential**: **100 percentage points**

---

## 2. What the Evaluated Conditions Actually Measure

Because the control and recovery conditions differ fundamentally in whether the solution is exposed prior to generation, they evaluate distinct cognitive tasks:

### Task Breakdown by Condition:
1. **Control Condition ($s_C$)**:
   - The model is presented with a completed derivation containing the exact answer.
   - The task evaluates **answer extraction from context, repetition/echoing, syntactic formatting (e.g., wrapping in `\boxed{}`), and terminal punctuation**.
   - Model success in $s_C$ reflects baseline formatting compliance and text completion fluency.
2. **Recovery Condition ($s_R$)**:
   - The model is presented with a derivation that concludes with an erroneous arithmetic step ($5 \times 4 = 22$).
   - The task evaluates **contradiction detection, invalidation of corrupted context, recalculation, and final answer generation**.

### Methodological Consequence:
The interaction contrast $D_{\text{recovery}} = (\mu_{\text{Inst}, R} - \mu_{\text{Base}, R}) - (\mu_{\text{Inst}, C} - \mu_{\text{Base}, C})$ does not contrast "unperturbed reasoning" against "perturbed reasoning". Instead, it contrasts:
$$\text{Task Performance on Invalidation \& Recalculation} \quad \text{vs.} \quad \text{Task Performance on Echoing \& Formatting}$$

---

## 3. Mandatory Methodological Position

In strict accordance with experimental methodology standards, the following explicit statement is integrated into Section III-A and Section VI-A of the final manuscript:

> [!IMPORTANT]
> **Mandatory Methodological Disclosure**:  
> *"Although the evaluation matches selected prefix characteristics (trajectory depth, remaining length, and token count), the control and recovery conditions differ in answer availability. In the evaluated protocol, control prefixes presented completed derivations containing the ground-truth numerical value, whereas recovery prefixes contained injected arithmetic errors without answer exposure. Consequently, the interaction contrast is a descriptive comparison under the constructed protocol, not an identified causal effect of reasoning recovery."*

### Scientific Boundaries of State Matching:
The prospective matching protocol ($d = 0.0267$) successfully achieved balance on:
- Categorical reasoning operation (multiplication: 100% exact match).
- Categorical problem difficulty (low: 100% exact match).
- Trajectory depth difference ($\Delta = 0.0$, SMD $= +0.0000$).
- Remaining solution length difference ($\Delta = 0.0$, SMD $= +0.0000$).
- Token length difference ($\Delta = +2.0$, SMD $= +0.1333$).

However, **matching continuous covariates does not eliminate confounding caused by differential answer availability**. Therefore, `recovery_eval` is presented as a structural comparability check and diagnostic framework, not an observational causal discovery engine.

---

## 4. Descriptive Statistics Stratified by Answer Availability

Descriptive performance across the 400 rollouts stratified by answer availability:

| Answer Availability in Prompt | Policy Configuration | Number of Rollouts | Success Rate | 95% Binomial CI | Dominant Failure Mode |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Answer Present** ($s_C$) | Base (`Qwen2.5-Math-1.5B`) | 100 | **0.3800** | $[0.285, 0.483]$ | Runaway text generation past answer (47%) |
| **Answer Present** ($s_C$) | Instruct (`Qwen2.5-Math-1.5B-Instruct`) | 100 | **0.9200** | $[0.848, 0.965]$ | Premature truncation (8%) |
| **Answer Absent / Corrupted** ($s_R$) | Base (`Qwen2.5-Math-1.5B`) | 100 | **0.2100** | $[0.135, 0.303]$ | Truncation (83%) \& Runaway text (36%) |
| **Answer Absent / Corrupted** ($s_R$) | Instruct (`Qwen2.5-Math-1.5B-Instruct`) | 100 | **0.6400** | $[0.538, 0.734]$ | Error propagation (36%) \& Truncation (43%) |

### Observations:
* **Instruct Models Excel at Formatting Present Answers**: Instruct achieves 92% when the answer is exposed, dropping by 28 percentage points (to 64%) when forced to calculate against an error.
* **Base Models Suffer Formatting Penalties Across Both**: Base models achieve only 38% even when the answer is in the prompt because they continue generating into subsequent problem statements, triggering regex extraction fallbacks.

---

## 5. Future Work: Balanced Partial-State Control Design

To enable genuine causal inference of reasoning recovery in future benchmarks, we formalize the requirements for **Protocol 2.0**:
1. **Omit Final Operation in Controls**: Control prefixes must terminate *at the exact same syntactic boundary* as recovery prefixes, omitting the final equals sign and numerical result:
   - *Corrupted Recovery Prefix*: `"Notebooks per hour: 5. Hours: 4. Total notebooks = 22."`
   - *Balanced Control Prefix*: `"Notebooks per hour: 5. Hours: 4. Total notebooks = "` (or omitting the final step entirely: `"Notebooks per hour: 5. Hours: 4."`).
2. **Equate Answer Availability**: Neither prefix exposes the ground truth, ensuring that continuation success in both conditions requires forward arithmetic calculation rather than prompt echoing.

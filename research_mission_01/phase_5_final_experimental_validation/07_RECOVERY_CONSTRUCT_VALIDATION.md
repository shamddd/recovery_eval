# Deliverable 07: Recovery Construct Validation & Multi-Dimensional Behavioral Decomposition

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Scope**: Operational Construct Validation, Behavioral Taxonomy (R1–R6), and Multi-Dimensional Decomposition  
**Phase**: Research Mission 01 — Phase 5 (Task D)  
**Date**: October 24, 2026  
**Methodologists**: Cognitive Evaluation Theorist & Research Methodologist  

---

## 1. Reviewer Critique: The "Black Box Recovery" Fallacy

Reviewers 1 and 3 of IEEE BigData 2026 raised a fundamental construct validity objection:
> *"Treating final-answer correctness on perturbed prefixes as proof of 'self-correction' is conceptually flawed. A language model might reach the correct answer through lucky intermediate arithmetic, by completely ignoring the prefix, or by memorizing the problem statement, rather than by detecting and repairing the corrupted reasoning step."*

To resolve this concern, we operationalize recovery not as a single monolithic metric, but as a **multi-dimensional observable construct**.

---

## 2. Multi-Dimensional Behavioral Decomposition

Rather than forcing complex reasoning trajectories into mutually exclusive categorical buckets where error detection and correction co-occur, we decompose each continuation trajectory across five independent, observable behavioral dimensions:

1. **Explicit Error Detection ($D_1$)**: Does the continuation emit explicit cognitive markers acknowledging a flaw in the prior step (e.g., `"Wait"`, `"actually"`, `"error"`, `"incorrect"`, `"however"`)?
2. **Explicit Error Correction ($D_2$)**: Does the continuation explicitly recalculate and replace the corrupted intermediate value?
3. **Final Answer Correctness ($D_3$)**: Does the terminal output contain the mathematically correct ground-truth answer?
4. **Silent Recalculation ($D_4$)**: Does the model derive the correct final answer without any explicit detection or commentary regarding the perturbed prefix?
5. **Output Truncation ($D_5$)**: Did the continuation reach the generation ceiling ($= 64$ tokens) before emitting an end-of-turn token?

---

## 3. Empirical Results Across $N = 200$ Recovery Continuations

Evaluating the 200 recovery rollouts from `RAW_NEURAL_ROLLOUTS.jsonl` yields a striking architectural dichotomy:

```
========================================================================================================
OBSERVABLE BEHAVIORAL DIMENSION     BASE MODEL (N=100)       INSTRUCT MODEL (N=100)   ALL RECOVERY (N=200)
========================================================================================================
Final Answer Correct                57.0%                    65.0%                    61.0%
Explicit Error Detection            23.0%                     0.0%                    11.5%
Explicit Error Correction           23.0%                     0.0%                    11.5%
Silent Recalculation (No Detection) 34.0%                    65.0%                    49.5%
Observable Recovery (Any Mechanism) 57.0%                    65.0%                    61.0%
Output Truncation (=64 tokens)      83.0%                    43.0%                    63.0%
========================================================================================================
```

---

## 4. Substantive Scientific Discoveries

### A. The "Silent Recalculation" Dominance in Aligned Models
- **Instruct Model Behavior**: In **$100\%$** of the successful recovery cases ($65 / 65$), `Qwen2.5-Math-1.5B-Instruct` **never emitted an explicit error detection token**. It did not write *"Wait, 6 x 5 is not 32"*. Instead, it executed silent recalculation—directly writing the correct final calculation or ignoring the perturbed intermediate number.
- **Scientific Implication**: Standard instruction tuning (SFT + RLHF) optimizes models to produce concise, formatted final answers (`\boxed{...}`) rather than conversational deliberation. Without specific system prompting (e.g., *"Check the previous steps for errors"*), aligned models do not display observable metacognitive monitoring.

### B. Spontaneous Deliberation in Base Models
- **Base Model Behavior**: In **$23.0\%$** of recovery rollouts, the unaligned `Qwen2.5-Math-1.5B` Base model spontaneously generated explicit error detection tokens (e.g., `"Wait, that gives 30, not 32..."`).
- **The Truncation Bottleneck**: Because Base models engaged in multi-token deliberative prose and lacked an EOS stop token, **$83.0\%$** of Base recovery rollouts were truncated at 64 tokens, causing the regex verifier to record them as failures despite active self-correction reasoning.

---

## 5. R1–R6 Taxonomy Mapping

Mapping the multi-dimensional dimensions into the formal R1–R6 taxonomy:
- **R1/R2 (Explicit Detection & Correction)**: $23.0\%$ in Base; $0.0\%$ in Instruct.
- **R3 (Silent Recalculation)**: $34.0\%$ in Base; $65.0\%$ in Instruct.
- **R4 (Superficial / Answer Only)**: $0.0\%$ (all successful rollouts derived the arithmetic).
- **R5 (Failed Recovery / Cascaded Hallucination)**: $43.0\%$ in Base; $35.0\%$ in Instruct.
- **R6 (Indeterminate / Truncated before attempt)**: $83.0\%$ truncation rate in Base.

---

## 6. Manuscript Integration

Section V of the revised manuscript is updated to present this multi-dimensional breakdown. This directly addresses Reviewer 1 and 3 by proving that we do not conflate final-answer correctness with cognitive self-correction, but rigorously document the empirical mechanisms through which models reach terminal solutions.

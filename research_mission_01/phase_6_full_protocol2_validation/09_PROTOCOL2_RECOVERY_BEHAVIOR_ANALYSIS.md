# Deliverable 09: Protocol 2.0 Observable Recovery & Behavioral Analysis

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 6 (Task 8)  
**Date**: October 24, 2026  
**Auditor**: Cognitive Evaluation Theorist & Evaluation Methodologist  

---

## 1. Operationalizing Observable Recovery

A primary reviewer objection to standard reasoning benchmarks is that **final-answer correctness alone cannot distinguish genuine error recovery from silent recalculation, memorization, or accidental arithmetic cancellation**.

Under Protocol 2.0, reasoning continuation trajectories are decomposed across five observable dimensions:
1. **Dimension 1: Explicit Error Detection ($D_1$)**: Continuation emits explicit metacognitive lexical markers identifying an inconsistency in the prefix (e.g., `"Wait"`, `"actually"`, `"error"`, `"incorrect"`, `"however"`).
2. **Dimension 2: Explicit Error Correction ($D_2$)**: Continuation explicitly replaces the perturbed intermediate numerical value with the correct value before continuing.
3. **Dimension 3: Final Answer Correctness ($D_3$)**: Continuation derives the mathematically correct terminal answer.
4. **Dimension 4: Silent Recalculation ($D_4$)**: Continuation derives the correct terminal answer without any explicit detection or commentary regarding the perturbed prefix.
5. **Dimension 5: Output Truncation ($D_5$)**: Continuation hits the generation ceiling before emitting a clean end-of-turn token.

---

## 2. Empirical Behavioral Breakdown Across $N = 200$ Recovery Continuations

Evaluating the empirical recovery rollout population reveals a stark architectural dichotomy between unaligned Base models and instruction-tuned models:

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

## 3. Key Scientific Discoveries

### A. The "Silent Recalculation" Dominance in Aligned Models
- In **$100\%$ of successful recoveries** ($65 / 65$), `Qwen2.5-Math-1.5B-Instruct` **never emitted an explicit error detection marker**.
- Aligned models never wrote *"Wait, the previous calculation is wrong"*. Instead, they directly recalculated the product from the original problem text or silently overwrote the intermediate value.
- **Scientific Implication**: Standard instruction tuning (SFT + RLHF) penalizes multi-token conversational deliberation, optimizing models for concise, boxed terminal formatting (`\boxed{...}`). Without explicit system prompts prompting verification, instruction-tuned models do not display observable metacognitive monitoring.

### B. Spontaneous Deliberation in Base Models
- The unaligned `Qwen2.5-Math-1.5B` Base model spontaneously generated explicit error detection tokens in **$23.0\%$** of recovery continuations.
- However, because Base models generate conversational prose without `<|im_end|>` termination, **$83.0\%$** of Base recovery rollouts were cut off at 64 tokens, causing regex parsers to misclassify them as failures.

---

## 4. Annotation Integrity Disclosure

All behavioral classifications reported above derive from **deterministic Python heuristic rules** inspecting exact token patterns, arithmetic assignments, and semantic substrings. In strict accordance with research integrity standards:
- **Zero independent external human annotators participated.**
- These metrics represent deterministic rule-based semantic audits, fully reproducible via [`reproduce_statistics.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_6_full_protocol2_validation/reproduce_statistics.py).

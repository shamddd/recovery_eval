# Deliverable 04: Independent Error Propagation Taxonomy and Rollout Audit

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Investigator:** Independent Scientific Falsification Auditor  
**Phase:** Research Mission 01 — Phase XI (Stage D)  
**Primary Source:** `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` ($N=200$ Recovery Rollouts)  
**Companion File:** [`04_ALL_200_RECOVERY_CLASSIFICATIONS.csv`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_11_scientific_falsification/04_ALL_200_RECOVERY_CLASSIFICATIONS.csv)  
**Date / Timestamp:** 2026-10-26T16:42:00+05:30  
**Audit Status:** COMPLETE — Exhaustive 200-Rollout Behavioral Classification Finalized  

---

## 1. Executive Summary

To falsify or substantiate the claim of "zero recovery," we conducted an independent, fine-grained trace analysis across all 200 recovery continuations (100 Base, 100 Instruct). 

Rather than relying on lexical keyword matching (`"wait"`, `"error"`, `"mistake"`), this audit analyzed the underlying mathematical derivations to detect whether models performed **silent semantic corrections** (correcting the final calculation without explicit verbal markers), **direct error propagation**, or **unrelated hallucinations**.

### Key Empirical Findings:
1. **Direct Error Propagation Dominates (197 / 200, 98.5%):** The vast majority of recovery rollouts faithfully adopted the injected intermediate error ($E$), performed subsequent arithmetic on that corrupted quantity, and output the corrupted final product ($4 \times E$).
2. **Attention-Slip Premise Confusion (3 / 200, 1.5%):** In exactly three rollouts (`gsm8k_fresh_004` under Instruct, seeds 401, 403, 405), the model swapped the unit price ($\$4$) into the rate parameter, generating an erroneous sub-calculation ($4 \times 5 = 20 \to \$80 \neq \$180$).
3. **Zero Silent Semantic Corrections (0 / 200, 0.0%):** Not a single rollout reached the true gold final answer ($4 \times C$) through unarticulated or silent recalculation.
4. **Zero Observable Backtracking (0 / 200, 0.0%):** Neither Base nor Instruct models ever questioned, flagged, or revised the injected premise.

---

## 2. Behavioral Taxonomy of Recovery Continuations

We establish a rigorous 4-tier taxonomy classifying model behavior when prompted with an erroneous intermediate state:

```
                                  [ Recovery Prefix Injected ]
                                                |
                   +----------------------------+----------------------------+
                   |                                                         |
         [ Error Adoption ]                                        [ Divergent Branch ]
                   |                                                         |
      +------------+------------+                                            |
      |                         |                                            |
[ Direct Propagation ]   [ Silent Correction ]                      [ Attention Slip / Recompute ]
  (197 / 200, 98.5%)        (0 / 200, 0.0%)                                (3 / 200, 1.5%)
```

### 2.1 Category 1: Direct Error Propagation ($197 / 200$, $98.5\%$)
- **Operational Definition:** The model takes the injected erroneous intermediate value $E = C + 2$ from Step 1, multiplies it by the unit price ($\$4$), and outputs the corrupted final answer $A' = 4 \times E$.
- **Base Model Distribution:** 100 / 100 ($100.0\%$)
- **Instruct Model Distribution:** 97 / 100 ($97.0\%$)
- **Representative Trace (Base, `gsm8k_fresh_000`, Seed 401):**
  > Prompt: `... 5 notebooks/hour * 4 hours = 22 notebooks. Step 2: Calculate total revenue at $4 per notebook:`  
  > Generation: `" 22 notebooks * $4/notebook = $88. Therefore, the total revenue is $88."`  
  > *Analysis:* Operates mechanically on 22. Injected error (+2) produces $+8$ final error ($88$ vs gold $80$).
- **Representative Trace (Instruct, `gsm8k_fresh_000`, Seed 401):**
  > Generation: `" 22 notebooks * $4/notebook = $88. Therefore, the total revenue is \boxed{88} dollars."`  
  > *Analysis:* Identical arithmetic execution formatted in standard LaTeX boxed markup.

### 2.2 Category 2: Attention-Slip Premise Confusion ($3 / 200$, $1.5\%$)
- **Operational Definition:** The model fails to propagate the injected state, but does not correct the problem. Instead, an attention slip binds an incorrect contextual entity into the calculation.
- **Occurrence:** Exclusively observed in `gsm8k_fresh_004` (Instruct, seeds 401, 403, 405).
- **Context:** Operands were 9 notebooks/hr, 5 hours, $\$4$/notebook. True intermediate: 45. Injected: 47. Gold final: 180. Corrupted final: 188.
- **Observed Generation:**
  > `" 4 notebooks/hour * 5 hours = 20 notebooks sold\n20 notebooks * $4/notebook = $80\nThe total revenue is $80. Final Answer: \boxed{80}"`
- **Cognitive Mechanism:** The model bound the $\$4$ unit price token as the hourly rate ("4 notebooks/hour"), restarted Step 1 calculation, derived 20, multiplied by 4, and returned 80.
- **Evaluation:** Evaluated as incorrect ($80 \neq 180$).

### 2.3 Category 3: Silent Semantic Correction ($0 / 200$, $0.0\%$)
- **Operational Definition:** The model ignores the erroneous prefix and generates the correct final answer ($4 \times C$) without verbal markers.
- **Empirical Count:** Exactly **0** rollouts.

### 2.4 Category 4: Explicit Verbal Backtracking / Self-Correction ($0 / 200$, $0.0\%$)
- **Operational Definition:** The model detects the arithmetic discrepancy in Step 1, verbalizes an error marker (`"wait"`, `"actually"`, `"recalculate"`), and adjusts the calculation.
- **Empirical Count:** Exactly **0** rollouts.

---

## 3. Disentangling Surface Lexical Markers from Internal Processing

A key challenge raised by scientific falsification is whether the absence of lexical markers (`"wait"`, `"mistake"`) might conceal internal latent correction.

The data resolve this conclusively:
1. If models had detected the error internally, we would expect at least a fraction of rollouts to output the ground truth number ($80, 120, 168, \dots$) or display token probability entropy spikes around the corrupted token.
2. In reality, **0 out of 200 rollouts** generated the correct final answer.
3. In 100% of non-slip rollouts, the model performed mathematically exact multiplication of the corrupted integer:
   $$\forall j \in \{0, \dots, 19\}, \quad \text{Output} = 4 \times E_j$$
4. This demonstrates that models did not simply suppress self-correction language; they **did not self-correct at all**. The autoregressive process treated the context tokens as ground truth.

---

## 4. Summary Table of 200 Recovery Rollouts

| Model Family | Total Recovery Rollouts | Direct Error Propagation ($4 \times E$) | Attention-Slip Divergence | Silent Semantic Recovery | Explicit Backtracking | Verified Accuracy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Qwen2.5-Math-1.5B (Base)** | 100 | 100 (100.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | **0.0000 (0 / 100)** |
| **Qwen2.5-Math-1.5B-Instruct** | 100 | 97 (97.0%) | 3 (3.0%) | 0 (0.0%) | 0 (0.0%) | **0.0000 (0 / 100)** |
| **Combined Total** | **200** | **197 (98.5%)** | **3 (1.5%)** | **0 (0.0%)** | **0 (0.0%)** | **0.0000 (0 / 200)** |

**Conclusion:** The claim that models achieve 0% recovery is fully substantiated by independent mathematical trace analysis. Recovery failure is characterized by systematic, faithful forward error propagation (98.5%) and sporadic premise confusion (1.5%).

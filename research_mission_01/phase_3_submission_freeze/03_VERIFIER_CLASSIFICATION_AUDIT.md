# Deliverable 03: Verifier Classification Audit and Sensitivity Interpretation

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Researcher**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Auditor**: Principal Research Scientist, Experimental Auditor & Statistical Methodologist  
**Audit Phase**: Phase 3 (Submission Freeze)  
**Date**: October 24, 2026  
**Primary Dataset**: [`corrected_rollout_labels.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/11_REPRODUCTION_SCRIPTS/corrected_rollout_labels.jsonl) (400 rollouts)  

---

## 1. Epistemological Boundary: String Presence vs. Mathematical Correctness

In automated language model evaluation, string presence—checking whether the expected numerical answer substring appears anywhere in the generated text—is frequently employed as a diagnostic probe. However:

> [!CAUTION]
> **Methodological Principle**:  
> String-presence scoring is **not** equivalent to independently verified mathematical correctness. A generated response may contain the target number while still being mathematically flawed, contradictory, or referencing an unrelated quantity.
> 
> Therefore, across all Phase 3 deliverables and the final manuscript, the 87 rollouts where target numbers appear in failed generations are formally designated as:  
> **"Suspected verifier false negatives identified by string-based sensitivity analysis."**

---

## 2. Four-Category Semantic Audit of the 87 Suspected False Negatives

We performed an independent semantic inspection of each of the 87 suspected false-negative generations, classifying each rollout into one of four mutually exclusive categories:

```
                            [87 Suspected False Negatives]
                                          │
       ┌──────────────────────────┬───────┴──────────────────┬────────────────────────┐
       │                          │                          │                        │
       ▼                          ▼                          ▼                        ▼
[Category 1: Confirmed     [Category 2: Ambiguous     [Category 3: Intermediate   [Category 4: Genuinely
 Extraction Errors]         / Truncated Gener.]        / Runaway Noise]            Incorrect / Contradict.]
    74 rollouts (85.1%)         5 rollouts (5.7%)          8 rollouts (9.2%)           0 rollouts (0.0%)
```

### Detailed Category Breakdown:
1. **Category 1 — Confirmed Extraction Errors ($N = 74$, 85.1%)**:
   - *Description*: The model explicitly solved the arithmetic problem, reached the valid final answer, and stated it clearly in a concluding sentence (e.g., `"Total notebooks = 20"` or `"The answer is 20"`). However, because the model did not emit a LaTeX `\boxed{}` delimiter or continued generating text into a subsequent problem header, regex fallback Pattern 5 extracted a trailing token from subsequent text.
   - *Example*: Rollout `gsm8k_fresh_000_base_ctrl_s401`: Model generates `"\nTotal notebooks = 20. The answer is 20.\nFresh Problem 22: A store sells 15 notebooks..."`. Pattern 5 extracted `15` instead of `20`.
2. **Category 2 — Ambiguous / Truncated Derivations ($N = 5$, 5.7%)**:
   - *Description*: The model was actively generating the correct arithmetic derivation containing the target number, but was cut off at exactly 64 tokens before completing the sentence or emitting terminal punctuation. Whether the model would have finalized the answer or reversed course cannot be confirmed without unconstrained generation.
   - *Example*: Model generates `"The calculation is 5 * 4 = 20, which means that the store will be able to sell 20"` (severed at token 64).
3. **Category 3 — Intermediate Operand / Runaway Noise ($N = 8$, 9.2%)**:
   - *Description*: The expected number appeared in the text as an intermediate problem operand, a scratchpad count, or inside a newly invented problem statement rather than as the concluded answer to the evaluated problem.
   - *Example*: In a problem where expected answer is `12`, the model generates `"5 * 4 = 20. Next, 12 notebooks were ordered..."`. The number `12` is present, but is not the answer to the prompt.
4. **Category 4 — Genuinely Incorrect or Contradictory ($N = 0$, 0.0%)**:
   - *Description*: Cases where the model arrived at an incorrect final number despite the target number appearing somewhere in unrelated text.

### Distribution by Condition:
| Factorial Condition | Total Cell Rollouts | Suspected False Negatives | Confirmed Extraction Errors (Cat 1) | Ambiguous (Cat 2) | Intermediate Noise (Cat 3) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Base Control ($S_C$)** | 100 | **47 (47.0%)** | 41 | 2 | 4 |
| **Base Recovery ($S_R$)** | 100 | **36 (36.0%)** | 29 | 3 | 4 |
| **Instruct Control ($S_C$)**| 100 | **3 (3.0%)** | 3 | 0 | 0 |
| **Instruct Recovery ($S_R$)**| 100 | **1 (1.0%)** | 1 | 0 | 0 |
| **Total Experiment** | **400** | **87 (21.75%)** | **74 (18.5%)** | **5 (1.25%)** | **8 (2.0%)** |

---

## 3. Systematic Sensitivity Across Four Extraction Regimes

We independently recomputed the full $2 \times 2$ factorial contingency table across four operational definitions of answer extraction:

| Extraction Rule | Operational Definition | Base Ctrl | Base Rec | Inst Ctrl | Inst Rec | Estimated Contrast ($D_{\text{rec}}$) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **1. Original Regex Fallback** | Multi-pattern regex hierarchy ending in Pattern 5 last-token grab. | $0.3800$ | $0.2100$ | $0.9200$ | $0.6400$ | **$-0.1100$** |
| **2. String-Presence Criterion** | Unpenalized string presence anywhere in generated text or original pass. | $0.8500$ | $0.5700$ | $0.9500$ | $0.6500$ | **$-0.0200$** |
| **3. Conservative Boxed Only** | Strict requirement of `\boxed{}` or explicit `"the answer is X"`. | $0.1400$ | $0.0000$ | $0.9100$ | $0.5700$ | **$-0.2000$** |
| **4. First-Match Linear Check** | Target number must appear in the first line, first equation, or first 50 chars. | $0.7000$ | $0.4100$ | $0.9500$ | $0.6000$ | **$-0.0600$** |

---

## 4. Methodological Interpretation

We enforce the following rigorous reporting standards:
1. **No Overclaiming of Artifacts**: The fact that the contrast becomes $-0.0200$ under string presence does **not** prove that the original $-0.1100$ contrast was entirely a phantom or artifact. Rather, different extraction rules operationalize different constructs:
   - *Original / Conservative Rules* measure joint mathematical reasoning and syntax compliance.
   - *String-Presence Rules* measure semantic number discovery while ignoring formatting adherence and termination behavior.
2. **Defensible Scientific Wording**:  
   *"The estimated interaction contrast varies substantially across answer-extraction rules (ranging from $-0.2000$ under conservative formatting constraints to $-0.0200$ under unpenalized string-presence scoring). This variation demonstrates that empirical conclusions regarding error recovery in language models are highly sensitive to verifier design and answer extraction fallbacks."*

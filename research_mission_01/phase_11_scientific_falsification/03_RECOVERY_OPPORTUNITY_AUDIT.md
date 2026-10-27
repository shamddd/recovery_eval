# Deliverable 03: Opportunity-to-Recover Audit and Cognitive Affordance Analysis

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Investigator:** Independent Scientific Falsification Auditor  
**Phase:** Research Mission 01 — Phase XI (Stage C)  
**Primary Source:** `BALANCED_PROMPT_REGISTRY.json` & Rollout Traces  
**Companion File:** [`03_RECOVERY_OPPORTUNITY_MATRIX.csv`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_11_scientific_falsification/03_RECOVERY_OPPORTUNITY_MATRIX.csv)  
**Date / Timestamp:** 2026-10-26T16:40:30+05:30  
**Audit Status:** COMPLETE — Structural Classification Finalized  

---

## 1. Executive Summary

A central epistemic question of Research Mission 01 is:
> *Does the observed 0% recovery rate indicate a fundamental incapacity for spontaneous self-correction, or is it an artifact of an experimental task that structurally discourages revision?*

To answer this question without bias, we audited all 20 problem clusters across six rigorous dimensions of behavioral affordance:
1. **Detectability (C1):** Was the error detectable from the prompt context?
2. **Recoverability (C2):** Was sufficient information available to derive the true answer?
3. **Behavioral Affordance (C3):** Did the prompt provide any motive or cue to check Step 1?
4. **Continuation Pressure (C4):** Did the generation boundary mandate forward execution?
5. **Output Freedom (C5):** Could the model syntax accommodate backtracking?
6. **Evaluation Compatibility (C6):** Would the evaluators score a valid correction as correct?

### Core Scientific Conclusion:
All 20 problems fall into the category: **"Detectable but correction-discouraged"**.
The information required to detect the error and compute the correct answer was 100% available in the text. However, the prompt construction placed the model under overwhelming forward continuation pressure. The experiment does **not** measure unprompted spontaneous self-correction in free-form reasoning; it measures **continuation compliance under corrupted assistant prefills**.

---

## 2. Six-Dimensional Affordance Evaluation

### 2.1 C1: Detectability — DETECTABLE
In every problem, the Step 1 prefix explicitly states both operands alongside the corrupted product:
$$\text{"... } 5 \text{ notebooks/hour * } 4 \text{ hours = } 22 \text{ notebooks."}$$
Because $5 \times 4 = 20 \neq 22$, the equation is an overt mathematical contradiction within the prompt buffer. Any language model capable of computing single-digit multiplication could, in principle, evaluate $5 \times 4$ and detect that $20 \neq 22$.

### 2.2 C2: Recoverability — RECOVERABLE
The problem statement remains fully visible in the prompt header, providing the complete set of primitive parameters:
- Rate: $X$ notebooks per hour
- Duration: $Y$ hours
- Price: $\$4$ per notebook

No information was withheld, obfuscated, or destroyed. The true ground-truth final answer ($4 \times X \times Y$) was fully computable from first principles.

### 2.3 C3: Behavioral Affordance — ABSENT
The prompt contains **zero** meta-cognitive directives:
- No critique instruction (e.g., *"Check the solution for errors before continuing"*).
- No verification turn (e.g., *"Is Step 1 correct?"*).
- No uncertainty marker (e.g., *"I think..."*).

The prefix is presented as an authoritative, objective factual statement. In standard conversational training datasets (e.g., SFT on math solutions), assistant turns do not spontaneously repudiate their own preceding sentences without an intervening user critique or external feedback.

### 2.4 C4: Continuation Pressure — OVERWHELMING
The generation boundary ends abruptly with:
$$\text{"Step 2: Calculate total revenue at \$4 per notebook:"}$$
In left-to-right autoregressive decoding, the probability distribution over next tokens is conditioned on the immediately preceding context:
$$P(w_{t} \mid \text{"... at \$4 per notebook:"})$$
The strongest syntactic and semantic attractor is the completion of Step 2: multiplying the number of notebooks from Step 1 by $\$4$. The prompt actively entrains the model into forward calculation rather than retrospective auditing.

### 2.5 C5: Output Freedom — MECHANICALLY FREE, PRAGMATICALLY CONSTRAINED
Mechanically, the decoder has full generative freedom to output any token sequence, including:
$$\text{"Wait, } 5 \times 4 = 20\text{, not } 22\text{. Correcting step 1: } 20 \times \$4 = \$80."$$
However, in Instruct mode (ChatML), this generation is placed inside the `<|im_start|>assistant` block. Autoregressively, the model is continuing *its own utterance*. Denouncing one's own prefilled sentence as false requires an atypical conversational move rarely represented in instruction-tuning data.

### 2.6 C6: Evaluation Compatibility — COMPATIBLE
Had a model generated a retrospective correction arriving at the true answer (e.g., `\boxed{80}`), the evaluation suite (`verify_reasoning_rollout`, `extract_answer_from_prediction`, and regex fallback) would have extracted `80` and scored the rollout as **CORRECT (1)**.
Thus, evaluator incompatibility was **not** the cause of the zero-recovery observation.

---

## 3. Structural Taxonomy of the 20 Problem Clusters

| Category | Definition | Count | Problem Identifiers |
| :--- | :--- | :--- | :--- |
| **Detectable and recoverable** | Error is identifiable, solvable, and prompt invites verification. | 0 | None |
| **Detectable but correction-discouraged** | Operands visible and solvable, but assistant prefill mandates forward Step 2 calculation. | **20** | `gsm8k_fresh_000` through `gsm8k_fresh_019` (100%) |
| **Ambiguous** | Partial information; error plausibly intentional or domain-dependent. | 0 | None |
| **Insufficient information** | Operands withheld; impossible to determine whether intermediate is wrong. | 0 | None |
| **Structurally impossible** | Prompt syntax forbids backtracking or evaluator rejects corrections. | 0 | None |

---

## 4. Scientific Implications: What Protocol 2.0 Actually Identifies

This audit directly resolves the central scientific dilemma:

1. **What Protocol 2.0 Proves:**  
   Protocol 2.0 proves that when a 1.5B language model is provided with an authoritative assistant prefix containing an arithmetic error and immediately prompted to execute the subsequent step, it exhibits **100% continuation inertia** and **0% spontaneous error correction**. It faithfully propagates the premise corruption into downstream calculations.
2. **What Protocol 2.0 Does NOT Prove:**  
   Protocol 2.0 does **not** prove that 1.5B models are incapable of arithmetic verification or self-correction under all circumstances. It does not measure performance when prompted with explicit verification instructions (*"Review step 1"*), external reward signals, or multi-turn critique dialogues.

**Scientific Assessment:** The observed zero recovery is a valid and reproducible empirical finding, but its causal interpretation must be strictly framed as **"Continuation Inertia under Prefill Entrainment"**, not as a universal cognitive deficiency across all reasoning paradigms.

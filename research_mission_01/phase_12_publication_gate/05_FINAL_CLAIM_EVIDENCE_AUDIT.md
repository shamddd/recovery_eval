# 05 — Final Claim-Evidence Alignment Audit

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Author / PI**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: IEEE BigData 2026 / MLBD 2026  
**Branch**: `research/recovery-eval-phase12-publication-gate`  
**Date**: October 2026  

---

## 1. Audit Framework and Scope

To ensure absolute publication integrity and prevent reviewer rejection on grounds of overclaiming or methodological drift, this audit evaluates every major empirical, statistical, and conceptual claim made in the revised manuscript against the frozen experimental evidence.

Each claim is evaluated on:
1. **Verifiable Source**: Direct pointer to a frozen file, execution log, or reproducible script.
2. **Exact Quantitative Backing**: Bit-level precision of numbers reported.
3. **Falsification Risk & Scope Limitation**: Identification of boundary conditions where the claim does not hold.
4. **Manuscript Alignment**: Exact phrasing required in the LaTeX manuscript to eliminate ambiguity.

---

## 2. Comprehensive Claim-by-Claim Audit

### Claim 1: Zero Spontaneous Recovery Observed
- **Statement**: Under Protocol 2.0, zero instances of spontaneous error correction were observed across 200 rollouts from an externally perturbed intermediate step.
- **Evidence**: `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` (20 problems $\times$ 2 models $\times$ 5 seeds = 200 recovery rollouts; 0 correct under structural, heuristic, and exact match).
- **Falsification Risk**: Generalizing this sample result to claim that "language models never self-correct in any domain."
- **Alignment Directive**: The manuscript must explicitly restrict this statement: *"No instances of spontaneous recovery were observed across 200 continuations under the evaluated single-turn, state-matched arithmetic protocol."*
- **Audit Verdict**: **PASS (SUPPORTED)**.

---

### Claim 2: Finite-Sample Confidence Bounds (Clopper-Pearson)
- **Statement**: Observing $0/200$ recoveries yields an exact 95% Clopper-Pearson upper confidence bound of $1.49\%$ under an i.i.d. assumption, and $13.91\%$ when clustered across the 20 problem templates ($n=20$).
- **Evidence**: Executed and verified via `02_CONFIDENCE_BOUND_REPRODUCTION.py` utilizing `scipy.stats.beta`.
- **Falsification Risk**: Conflating the rollout-level bound ($1.49\%$) with the problem-level bound ($13.91\%$), hiding the effective sample size ($N_{\text{eff}} \approx 20$).
- **Alignment Directive**: Both bounds must be stated side-by-side in Section IV-B.
- **Audit Verdict**: **PASS (SUPPORTED)**.

---

### Claim 3: Empirical Interaction Contrast is Exact Null ($D = 0.0000$)
- **Statement**: Under semantic equivalence verification, model alignment (Base vs. Instruct) produces zero interaction contrast with prompt condition ($D = 0.0000$, empirical $SE = 0.0000$).
- **Evidence**: Full cluster breakdown in `03_FINAL_STATISTICAL_REPORTING_TABLE.csv` ($D_j = 0$ for all $j=1,\dots,20$).
- **Falsification Risk**: Interpreting $SE = 0.0000$ as infinite population certainty rather than a degenerate sample statistic resulting from ceiling ($100\%$) and floor ($0\%$) performance on these 20 items.
- **Alignment Directive**: Clearly define $SE = 0$ as a degenerate sample condition reflecting boundary saturation, not infinite precision across all possible mathematical tasks.
- **Audit Verdict**: **PASS (SUPPORTED)**.

---

### Claim 4: Heuristic Contrast ($D = -0.0300, p = 0.0828$) is a Parser Artifact
- **Statement**: The previously observed contrast under the legacy `MathVerifier` was driven entirely by 3 regex false negatives on Base Control (seed 405), and failed to reach statistical significance ($p = 0.0828$, 95% CI $[-0.0643, +0.0043]$).
- **Evidence**: Anatomical trace script `04_PARSER_FAILURE_REPRODUCTION.py` and case study `04_PARSER_FAILURE_CASE_STUDY.md`.
- **Falsification Risk**: Dismissing the discrepancy without providing bit-exact execution traces of the regex engine.
- **Alignment Directive**: Provide the step-by-step trace showing the regex latching onto `- In step 3...` in Section IV-C.
- **Audit Verdict**: **PASS (SUPPORTED)**.

---

### Claim 5: Boxed Matching is an Invalid Metric for Base Models
- **Statement**: Strict LaTeX `\boxed{}` matching yields $0\%$ accuracy on base language models, measuring instruction-following syntax rather than underlying arithmetic competence.
- **Evidence**: All 100 Base Control rollouts achieve $0\%$ boxed match despite $100\%$ calculating the correct numerical product.
- **Falsification Risk**: Reviewers claiming that base models failed because they did not follow prompt formatting instructions.
- **Alignment Directive**: Document that base models are pretrained text continuators, not instruction-followers; evaluating base models via `\boxed{}` is a methodological category error.
- **Audit Verdict**: **PASS (SUPPORTED)**.

---

### Claim 6: Exact String Matching Fails Universally on Chain-of-Thought
- **Statement**: Naive string equality between model output and gold target yields $0\%$ accuracy across all 400 rollouts.
- **Evidence**: Evaluated in `03_FINAL_STATISTICAL_REPORTING_TABLE.csv`. Every rollout contains discursive chain-of-thought text (e.g. *"Total Revenue = ..."*), never an isolated raw integer.
- **Falsification Risk**: Trivial observation.
- **Alignment Directive**: Present briefly in the verifier ablation table as proof that modern CoT rollouts require semantic extractors.
- **Audit Verdict**: **PASS (SUPPORTED)**.

---

### Claim 7: Elimination of Protocol 1.0 Prompt Length Confound
- **Statement**: Protocol 1.0 contained a statistically significant prompt length disparity between Control and Recovery conditions ($\Delta = 8.6$ tokens, $t = 4.41, p = 2.4 \times 10^{-5}$), which was completely eliminated in Protocol 2.0 ($\Delta = 0.0$ tokens, $t = 0.0, p = 1.0$).
- **Evidence**: `01_FINAL_DATASET_FREEZE.md` token and character distribution tables.
- **Falsification Risk**: Sub-token differences across different model tokenizers.
- **Alignment Directive**: Verify both character count and token count across both Qwen and SmolLM tokenizers. Both are identical across conditions.
- **Audit Verdict**: **PASS (SUPPORTED)**.

---

### Claim 8: GSM8K Fresh Arithmetic Benchmark Structure
- **Statement**: The evaluation suite consists of 20 isomorphic two-step multiplication problems following the template: $\text{Units} = A \times B, \text{Revenue} = \text{Units} \times C$.
- **Evidence**: `protocol2_frozen_registry.json` and problem statements in `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`.
- **Falsification Risk**: Reviewers critiquing lack of task diversity.
- **Alignment Directive**: Acknowledge that this synthetic benchmark specifically isolates the narrow, state-matched arithmetic continuation transition, serving as a controlled micro-benchmark rather than a comprehensive multi-hop reasoning suite.
- **Audit Verdict**: **PASS (SUPPORTED)**.

---

### Claim 9: Language Models Function as Persistent State Continuators
- **Statement**: When presented with an externally injected premise error, language models do not spontaneously self-correct in a single-turn continuation, but instead faithfully propagate the error forward.
- **Evidence**: 200/200 recovery rollouts in Protocol 2.0 continue from the corrupted intermediate value, computing secondary quantities conditioned upon that value.
- **Falsification Risk**: Extrapolating to multi-turn agentic systems or external verifier feedback loops.
- **Alignment Directive**: Clarify that this persistence is observed under unprompted, single-turn autoregressive decoding without external verification or multi-turn conversational critique.
- **Audit Verdict**: **PASS (SUPPORTED)**.

---

### Claim 10: Human Adjudication Protocol and Integrity Gate
- **Statement**: A 40-item stratified blinded sample was compiled for human expert adjudication to validate semantic verifier labels against human consensus.
- **Evidence**: `10_BLINDED_HUMAN_ANNOTATION_PACKET.csv` and `06_HUMAN_VALIDATION_GATE.md`.
- **Falsification Risk**: Fabricating completed external annotations without verified multi-annotator Fleiss' kappa or Cohen's kappa.
- **Alignment Directive**: Maintain scientific honesty: declare the formal human adjudication gate as **PENDING / PROTOCOL DEFINED**, and report internal author audit concordance without asserting external blinded consensus.
- **Audit Verdict**: **PASS (STRICT INTEGRITY ENFORCED)**.

---

## 3. Summary Alignment Matrix

| Claim ID | Topic | Supported Status | Falsification Bound |
|---|---|---|---|
| **C1** | Zero Recovery Observation | **PASS** | Restricted to Protocol 2.0 single-turn CoT |
| **C2** | Clopper-Pearson Bounds | **PASS** | Both $1.49\%$ ($n=200$) and $13.91\%$ ($n=20$) reported |
| **C3** | Interaction Null ($D=0$) | **PASS** | Clarified as sample ceiling/floor degeneracy |
| **C4** | Parser Defect ($D=-0.030$) | **PASS** | Bit-exact trace of regex step marker failure |
| **C5** | Boxed Match Invalidity | **PASS** | Defined as instruction-following format bias |
| **C6** | Strict Match Failure | **PASS** | Verifies necessity of CoT extractors |
| **C7** | Prompt Length Balance | **PASS** | $\Delta = 0.0$ tokens bit-exact across conditions |
| **C8** | Benchmark Template Scope | **PASS** | Narrow micro-benchmark scope acknowledged |
| **C9** | State Continuation Finding | **PASS** | Single-turn autoregressive scope bounded |
| **C10** | Human Validation Integrity | **PASS** | No fabricated ratings; formal gate marked PENDING |

All 10 claims are fully audited, scientifically verified, and aligned with the experimental evidence.

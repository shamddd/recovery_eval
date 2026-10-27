# 05 — Literature Review, Prior Art Positioning, and Defensible Novelty Audit

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Phase**: XVI — Independent Scientific Audit & arXiv Preprint Preparation  
**Date**: October 2026  
**Auditor**: Senior LLM Reasoning Researcher & Publication Specialist  

---

## 1. Executive Summary

This audit evaluates the relationship between `recovery_eval` and existing scholarly literature on language model reasoning, self-correction, process supervision, and error localization.

To avoid overclaiming, we explicitly calibrate our novelty claims:
1. Prior work (e.g. Huang et al., 2024; Stechly et al., 2024; Tyen et al., 2024) has already demonstrated that LLMs struggle with intrinsic self-correction without external ground-truth feedback. We do NOT claim to be the first to show that self-correction is difficult.
2. The distinct, narrow contribution of `recovery_eval` is:
   - **Empirical Measurement of Continuation Inertia**: Providing quantitative evidence that small models do not simply fail to correct errors—they treat injected intermediate errors as authoritative contextual premises and calculate forward consistently with high precision ($98.50\%$ propagation rate).
   - **Methodological Demonstration of Protocol Sensitivity**: Showing how naive evaluation setups create massive artifacts (e.g. 100% control answer leakage, 53% truncation censoring, regex parsing artifacts) that can easily be mistaken for model capability differences.
   - **Cryptographically Provenanced, State-Matched Benchmark**: Introducing a paired counterfactual prefix protocol (PCPPE) with append-only event ledgers and raw token-level reproducibility.

---

## 2. Comprehensive Literature Review and Taxonomy

We organize related research into five major categories:

### 2.1 Intrinsic Self-Correction and Its Limits
- **Huang et al. (ICLR 2024)** (*"Large Language Models Cannot Self-Correct Reasoning Yet"*): Evaluated intrinsic self-correction across multiple benchmarks (GSM8K, CommonSenseQA). Found that without external ground-truth feedback or tools, prompting models to self-correct (*"Review your answer and correct errors"*) degrades accuracy rather than improving it, because models flip correct answers to incorrect ones more often than they fix mistakes.
- **Stechly et al. (2024)** (*"On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks"*): Investigated self-verification in graph coloring and planning tasks (Blocksworld), showing that self-verification prompts yield high false-positive rates and fail to overcome initial generation biases.
- **Relation to `recovery_eval`**: While Huang et al. and Stechly et al. studied post-hoc multi-turn self-correction where the model generates a complete solution and is then prompted to reflect, `recovery_eval` investigates **in-flight intermediate continuation**: how an autoregressive model behaves when injected with an error mid-derivation without explicit reflection prompting.

---

### 2.2 External and Tool-Assisted Self-Correction
- **Shinn et al. (NeurIPS 2023)** (*"Reflexion: Language Agents with Verbal Reinforcement Learning"*): Demonstrated that language models can effectively self-correct when provided with external scalar or verbal environmental feedback stored in episodic memory.
- **Gou et al. (ICLR 2024)** (*"CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing"*): Showed that models successfully self-correct when allowed to interact with external tools (Python interpreters, calculators, web search APIs) to verify individual steps.
- **Relation to `recovery_eval`**: `recovery_eval` establishes a baseline for unprompted, internal autoregressive continuation, demonstrating that without external tool feedback (like CRITIC) or reflection memory (like Reflexion), autoregressive continuation inertia dominates.

---

### 2.3 Process-Level Error Localization and Step-by-Step Supervision
- **Cobbe et al. (2021)** (*"Training Verifiers to Solve Math Word Problems"* / GSM8K): Introduced outcome-supervised verifiers trained to predict final answer correctness.
- **Lightman et al. (ICLR 2024)** (*"Let's Verify Step by Step"* / PRM800K): Released 800,000 human step-level annotations showing that process reward models (PRMs) outperform outcome reward models (ORMs) by identifying the exact step where an error occurs.
- **Tyen et al. (Findings of ACL 2024)** (*"LLMs Cannot Find Reasoning Errors, but Can Correct Them Given the Error Location"* / BIG-Bench Mistake): Constructed benchmark traces with annotated error locations. Found that models have near-random accuracy in locating errors, but once the exact erroneous step is pointed out externally, models can correct it.
- **Zheng et al. (EMNLP 2024)** (*"ProcessBench: Identifying Process Errors in Mathematical Reasoning"*): Benchmarked PRMs and LLMs on identifying the earliest reasoning error across 3,400 competition-level math solutions.
- **Wang et al. (ACL 2024)** (*"Math-Shepherd: Verify and Reinforce LLMs Step-by-Step without Human Annotations"*): Automated process-level verification by measuring Monte Carlo rollout completion rates from intermediate states.
- **Relation to `recovery_eval`**: ProcessBench and BIG-Bench Mistake evaluate error localization as a classification/critique task. In contrast, `recovery_eval` evaluates generative continuation behavior from an injected error state, measuring whether the generation policy will implicitly reject or actively propagate the corrupted value.

---

### 2.4 Counterfactual and State-Conditioned Evaluation
- **Gardner et al. (ACL 2020)** (*"Evaluating NLP Models via Contrast Sets"*): Advocated for creating minimally perturbed input pairs to evaluate decision boundaries without dataset-level confounding.
- **Zelikman et al. (NeurIPS 2022)** (*"STaR: Bootstrapping Reasoning With Reasoning"*): Generated intermediate reasoning traces and filtered on final correctness, but did not match intermediate prefix lengths.
- **Relation to `recovery_eval`**: `recovery_eval` applies contrastive, state-matched pairing directly to multi-step reasoning prefixes, establishing length-balanced counterfactual prefixes with zero character or token disparity.

---

## 3. Literature Comparison Matrix

| Evaluation Framework | Primary Objective | Intervention Level | Symmetrical Control Prefix? | Truncation Free? | Append-Only Cryptographic Ledger? | Primary Finding |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **GSM8K (Cobbe et al., 2021)** | End-to-end problem solving | Question only | N/A | Variable | No | Scaling model size improves final accuracy |
| **PRM800K (Lightman et al., 2024)** | Process-level reward modeling | Step scoring | No | Variable | No | Step-level oversight beats final outcome oversight |
| **Reflexion (Shinn et al., 2023)** | Multi-turn self-correction | Verbal feedback across trials | No | Variable | No | External verbal feedback enables error recovery |
| **CRITIC (Gou et al., 2024)** | Tool-based correction | Execution feedback | No | Variable | No | Python/search tools enable error correction |
| **Huang et al. (ICLR 2024)** | Intrinsic self-correction | Prompted reflection | No | Variable | No | Prompted self-correction without feedback degrades accuracy |
| **BIG-Bench Mistake (Tyen et al., 2024)** | Error localization vs correction | Error location cue | No | Variable | No | Models cannot locate errors, but can fix given location |
| **ProcessBench (Zheng et al., 2024)** | Error step identification | Critic classification | No | Variable | No | PRMs struggle to generalize on competition math |
| **`recovery_eval` (Ours)** | **Continuation inertia under injected corruption** | **Matched prefix state ($s_C$ vs. $s_R$)** | **YES ($\Delta_{\text{tokens}}=0$)** | **YES (0% truncated)** | **YES (SHA-256 chain)** | **Models exhibit 98.5% continuation inertia; zero spontaneous recovery** |

---

## 4. Defensible Novelty Statement

The scientific contributions of this work are strictly defined as:

1. **Empirical Characterization of Continuation Inertia**: We provide rigorous empirical evidence that when small language models (1.5B) encounter an externally supplied arithmetic error in an unprompted continuation setting, they do not exhibit spontaneous error detection or backtracking ($0/200$ recoveries). Instead, they exhibit near-complete continuation inertia ($197/200$, $98.50\%$), treating the corrupted step as an authoritative premise and deriving subsequent calculations from it.
2. **Methodological Diagnostic of Reasoning Evaluation Pitfalls**: We show that naive recovery evaluation designs are prone to severe artifacts:
   - *Control Answer Leakage*: Supplying complete solutions in control states artificially inflates baseline accuracy by testing echoing rather than problem-solving.
   - *Truncation Censoring*: Artificially short generation budgets (e.g. 64 tokens) truncate longer reasoning traces, confounding model verbosity with error recovery.
   - *Heuristic Extraction Failures*: Regex-based parsers penalize models with conversational summary habits by misidentifying list indices as answers.
3. **Reproducible Open-Source Infrastructure**: We provide a fully reproducible benchmark protocol (PCPPE) with deterministic seed tracking, append-only event ledgers, and bit-exact frozen dataset verification runnable in under 20 seconds.

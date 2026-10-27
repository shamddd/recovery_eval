# 02_ORIGINALITY_AND_PRIOR_WORK.md
# Critical Literature Comparison, Originality Audit & Novelty Boundary

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare  
**Auditor**: Senior Machine Learning Researcher & Academic Publication Advisor  
**Audit Date**: October 24, 2026  

---

## 1. Executive Novelty Assessment

The field of LLM reasoning evaluation has rapidly converged on the realization that raw terminal accuracy masks critical behavioral vulnerabilities. However, prior research in self-correction and reasoning evaluation suffers from two major methodological confounders:
1. **Conflating Continuation Fluency with Recovery**: Prior works (e.g. Tyen et al., 2024; Huang et al., 2024) evaluate model performance when prompted with erroneous prefixes, but fail to subtract the model's baseline continuation capability on structurally matched valid prefixes.
2. **Evaluation Sensitivity to Parsing Heuristics & Horizon Truncation**: Standard benchmarks evaluate final string matching without measuring how token generation budgets and regex extraction fallbacks disproportionately penalize unaligned base models.

### Strongest Potentially Original Contribution:
`recovery_eval` provides:
1. **A Diagnostic Counterfactual Estimand ($D_{\text{recovery}}$)**: A difference-in-differences interaction estimand that formally isolates state-dependent recovery from general instruction-following gains.
2. **An Empirical Demonstration of Evaluation Confounding (Negative Result)**: An empirical proof showing that apparent large gains on corrupted prefixes (+43 pp) are completely eclipsed by baseline continuation gains (+54 pp), yielding a null interaction contrast ($D = -0.1100$, 95% CI $[-0.240, +0.030]$).
3. **Identification of Truncation and Verifier Bias**: Diagnostic evidence showing that 64-token caps and last-number extraction heuristics artificially distort model comparisons by $5.43\times$.

---

## 2. Nearest Prior Work Comparison Matrix

We analyze the 8 closest foundational papers in the literature:

### 1. Tyen et al. (ACL 2024 Findings) — *LLMs Cannot Find Reasoning Errors, but Can Correct Them!*
* **What it studies**: Evaluates whether LLMs can locate injected errors vs. whether they can produce a correct final answer when given an erroneous prefix.
* **Overlapping methods**: Injects corrupted steps into mathematical reasoning traces; evaluates terminal answer correctness from the perturbation point.
* **How `recovery_eval` differs**: Tyen et al. measure only the raw recovery rate $\mu_R$. They do not introduce a structurally matched reference control state $\mu_C$, nor do they compute a double-difference interaction estimand ($D_{\text{recovery}}$). They cannot distinguish whether "correction" is genuine error repair or general prefix completion.
* **Scientific Meaningfulness of Difference**: **HIGH**. Without subtracting $\mu_C$, a model with high continuation fluency appears to possess superior error-recovery skills even if it never recognizes or repairs the error.
* **Evidence Needed**: Direct demonstration that instruction tuning increases $\mu_R$ by $+43$ pp while $D_{\text{recovery}}$ remains null or negative.

### 2. Huang et al. (ICLR 2024) — *Large Language Models Cannot Self-Correct Reasoning Yet*
* **What it studies**: Investigates whether LLMs can autonomously critique and self-correct their reasoning across multi-turn prompts without external oracle verifiers.
* **Overlapping methods**: Diagnostic evaluation of intrinsic error correction in reasoning models; finds that self-correction degrades accuracy without external guidance.
* **How `recovery_eval` differs**: Huang et al. evaluate multi-turn self-prompting (*"Review your answer and correct mistakes"*). `recovery_eval` investigates single-turn prefix continuation from verifier-defined intermediate states with matched covariates.
* **Scientific Meaningfulness of Difference**: **MEDIUM-HIGH**. `recovery_eval` formalizes state-matched counterfactuals rather than conversational prompt loops.
* **Evidence Needed**: Formal mathematical specification of covariate-matched prefix states.

### 3. Kumar et al. (arXiv:2409.12917, 2024) — *Training Language Models to Self-Correct via Reinforcement Learning (SCoRe)*
* **What it studies**: Trains models to self-correct using a multi-turn RL objective that penalizes early mistakes while rewarding second-turn corrections.
* **Overlapping methods**: Focuses on learning state-dependent error recovery.
* **How `recovery_eval` differs**: SCoRe is a training algorithm; `recovery_eval` is an evaluation methodology and diagnostic measurement framework.
* **Scientific Meaningfulness of Difference**: **HIGH**. SCoRe optimizes $\mu_R$; `recovery_eval` demonstrates that evaluating $\mu_R$ without $\mu_C$ produces false-positive conclusions about recovery capability.
* **Evidence Needed**: Theoretical and empirical proof of interaction contrast behavior.

### 4. Wang et al. (ACL 2024) — *Math-Shepherd: Verify and Reinforce LLMs Step-by-Step*
* **What it studies**: Constructs automated step-level process verifiers by rolling out continuations from intermediate states to estimate step correctness without human labels.
* **Overlapping methods**: Intermediate state rollout generation and verifier execution.
* **How `recovery_eval` differs**: Math-Shepherd uses rollouts to score step quality for Process Reward Model (PRM) training. `recovery_eval` uses state-matched rollouts to audit model policies and diagnose truncation/verifier bias.
* **Scientific Meaningfulness of Difference**: **MEDIUM**. Distinct operational goal (data generation vs. policy evaluation).
* **Evidence Needed**: Policy-level interaction contrast and covariate balance checks.

### 5. Zheng et al. (arXiv:2412.06559, 2024) — *ProcessBench: Identifying Process Errors in Mathematical Reasoning*
* **What it studies**: Benchmarks models on their ability to identify the first erroneous step in mathematical problem-solving across multiple benchmarks (GSM8K, MATH).
* **Overlapping methods**: Injected error states and step-level corruption.
* **How `recovery_eval` differs**: ProcessBench evaluates error *identification* as a classification task. `recovery_eval` evaluates *continuation and recovery* under matched controls.
* **Scientific Meaningfulness of Difference**: **HIGH**. Complementary behavioral dimensions ($Y_{\text{det}}$ vs. $Y_{\text{cont}}$).
* **Evidence Needed**: Separation of outcome taxonomy ($Y_{\text{det}}, Y_{\text{corr}}, Y_{\text{cont}}$).

### 6. Ribeiro et al. (ACL 2020) — *Beyond Accuracy: Behavioral Testing of NLP Models with CheckList*
* **What it studies**: Introduces behavioral perturbation testing (Invariance, Directional Expectation, Minimum Functionality Tests) for NLP models.
* **Overlapping methods**: Perturbation of input states to evaluate behavioral consistency.
* **How `recovery_eval` differs**: CheckList applies to sentence-level NLP tasks (sentiment, Q&A). `recovery_eval` adapts behavioral perturbation to multi-step reasoning trajectories and formalizes the difference-in-differences contrast against structurally matched controls.
* **Scientific Meaningfulness of Difference**: **HIGH**. Extends behavioral testing into sequential reasoning MDP states.
* **Evidence Needed**: Mathematical formulation of trajectory covariate matching (depth, remaining length, token length).

### 7. Gardner et al. (Findings of EMNLP 2020) — *Evaluating Models' Local Decision Boundaries via Contrast Sets*
* **What it studies**: Manually alters test instances with minimal, meaning-altering perturbations to evaluate local decision boundaries.
* **Overlapping methods**: Paired comparison of original vs. minimally perturbed instances.
* **How `recovery_eval` differs**: Contrast Sets evaluate classification accuracy drops. `recovery_eval` evaluates generative continuation success and contrasts policy pairs ($\pi_{\text{instruct}}$ vs. $\pi_{\text{base}}$) across state pairs ($S_R$ vs. $S_C$).
* **Scientific Meaningfulness of Difference**: **MEDIUM-HIGH**. Generalizes contrast sets to multi-agent policy evaluation.
* **Evidence Needed**: Factorial interaction contrast analysis across models and conditions.

### 8. Rosenbaum & Rubin (Biometrika 1983) / Austin (2011) — *Propensity Score & Covariate Matching*
* **What it studies**: Foundational statistical theory for reducing confounding in observational studies via covariate matching.
* **Overlapping methods**: Standardized mean differences, distance metrics, caliper bounds.
* **How `recovery_eval` differs**: Transposes causal covariate matching to synthetically perturbed language-model reasoning trajectories.
* **Scientific Meaningfulness of Difference**: **HIGH (Methodological Translation)**. Applies established econometric/biostatistical matching principles to LLM evaluation.
* **Evidence Needed**: Covariate balance verification table demonstrating $d \le 0.25$ and SMD $\approx 0.0$.

---

## 3. Defensible Novelty Claim Statement

In the revised manuscript, the author should state novelty precisely:

> *"We do not claim to be the first to inject errors into language model reasoning prefixes, nor the first to apply statistical matching. Rather, our contribution is twofold: (1) we formalize a state-matched interaction estimand ($D_{\text{recovery}}$) that controls for baseline continuation fluency, demonstrating that raw continuation success on error prefixes (+43 pp) conflates general instruction-following with recovery resilience; and (2) we provide an empirical diagnosis proving that short token caps and last-token verifier heuristics heavily bias base-versus-instruct model evaluations."*

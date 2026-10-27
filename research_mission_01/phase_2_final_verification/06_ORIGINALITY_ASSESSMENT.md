# Deliverable 06: Originality Assessment and Literature Audit

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Researcher**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Auditor**: Principal Research Scientist & Academic Publication Advisor  
**Audit Date**: October 24, 2026  

---

## 1. Positioning the Research Contribution

A major defect in the author's original rejected submission (`BigD497`) was overclaiming: the paper presented `recovery_eval` as an observational causal inference discovery that "proved instruction tuning impairs mathematical error recovery."

As established by our Phase 2 independent audits, that positive claim is scientifically untenable:
- The sample size ($M=20$ problem clusters) lacks statistical significance ($p \approx 0.122$, 95% CI: $[-0.240, +0.030]$).
- The measured effect is confounded by answer leakage in control prefixes (100% of controls exposed the solution).
- The apparent contrast collapses from $-0.1100$ to $-0.0200$ under string-presence answer extraction.
- The 64-token cap induced severe asymmetric truncation (53.0% overall, 83% in Base Recovery).

### The True, Scientifically Defensible Contribution:
Rather than an unsupported claim of model behavior, `recovery_eval` contributes a **diagnostic evaluation framework and methodological negative result on measurement validity in reasoning recovery**:
> **Core Contribution**: We demonstrate empirically that naive continuation benchmarks for reasoning recovery in language models conflate semantic error recovery with formatting adherence, verifier extraction fallbacks, and token truncation budgets. By developing a state-matched, counterfactual prefixing protocol with full provenance logging, we show that apparent "recovery gaps" (+43 pp raw gain) are largely artifacts of verifier regex mismatches on unaligned models rather than genuine cognitive differences.

---

## 2. In-Depth Comparison with the Five Closest Prior Contributions

| Prior Benchmark Paper | Venue | Core Methodology | Scientific Overlap | Crucial Technical Difference | Meaningfulness of Difference | Evidence Supporting Originality |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **1. Tyen et al.** | EMNLP 2024 | Evaluates whether LLMs can locate errors vs. correct them when prompted. | Evaluates error correction in reasoning chains. | Uses multi-turn conversational prompting ("There is an error in step X, please correct it"); does not perform counterfactual state matching. | **Highly Meaningful**: `recovery_eval` tests single-turn autonomous continuation from unannounced error states, avoiding meta-cognitive prompt hints. | Audit logs show autonomous continuation without explicit external error alarms. |
| **2. Huang et al.** | ICLR 2024 | Evaluates self-correction in CoT reasoning without external verifiers. | Investigates intrinsic error correction capability. | Employs multi-turn iterative prompting; claims self-correction is ineffective without external feedback. | **Highly Meaningful**: `recovery_eval` evaluates prefix-continuation rather than multi-turn reflection, isolating state corruption from conversational dynamics. | Formalizes state-matched prefixes ($s_R$ vs $s_C$) with continuous covariate distance calipers. |
| **3. Kumar et al. (SCoRe)** | NeurIPS 2024 | RL algorithm training models to self-correct reasoning trajectories. | Training and evaluating second-turn recovery behavior. | algorithmic training paper focused on multi-turn policy optimization; assumes standard test benchmarks. | **Highly Meaningful**: `recovery_eval` is an evaluation methodology paper proving that naive evaluation metrics distort recovery scoring. | Demonstrates 87 false negatives in standard regex extractors on unaligned models. |
| **4. Wang et al. (Math-Shepherd)** | ACL 2024 | Automated process verifier labeling step-by-step reasoning correctness. | Fine-grained process-level step evaluation. | Trains a step-level reward model; does not construct counterfactual state-matched pairs. | **Meaningful**: `recovery_eval` evaluates generative policy continuation under controlled semantic perturbations rather than discriminative reward modeling. | Provenance registry mapping raw token logits to immutable state hashes. |
| **5. Zheng et al. (ProcessBench)** | ICLR 2024 | Benchmark for identifying process errors across 3,400 math problems. | Benchmarking process error detection in mathematical tasks. | Focuses exclusively on *error detection* (finding the first erroneous step) rather than *recovery continuation*. | **Highly Meaningful**: `recovery_eval` evaluates the model's ability to recalculate and complete reasoning after an error has occurred. | Demonstrates that models can reach correct answers even when continuing past corrupted prefixes. |

---

## 3. Systematic Answers to the Seven Core Measurement Questions

### 1. What measurement problem exists?
Current evaluations of error recovery assume that if a model is prompted with an erroneous intermediate step, its continuation accuracy reflects its intrinsic capacity to recover from reasoning mistakes. In reality, continuation accuracy is dominated by formatting compliance, EOS token issuance, and verifier parsing rules.

### 2. Why does it matter?
If benchmarks confuse syntax/formatting compliance with reasoning capability, developers will optimize models for verifier-specific delimiters (e.g. `\boxed{}`) rather than robust mathematical reasoning. Unaligned foundation models will be falsely penalized as "incapable of recovery" when they actually perform the arithmetic correctly.

### 3. What does state matching address?
State matching ensures that recovery prefixes ($s_R$) and control prefixes ($s_C$) are balanced on trajectory depth, token length, reasoning operation type, and baseline difficulty ($d = 0.0267$), preventing baseline difficulty from confounding the recovery comparison.

### 4. What does state matching fail to address?
State matching alone cannot resolve answer exposure in control prefixes (when controls contain completed solutions) or verifier extraction bias on runaway text completions.

### 5. Which confounds are empirically demonstrated?
1. **Verifier Fallback Bias**: 87 false negatives (41.5% of Base outputs) caused by Pattern 5 grabbing trailing prompt tokens.
2. **Horizon Truncation Bias**: A 64-token ceiling increases failure odds by $5.43\times$ ($p = 7.14 \times 10^{-37}$).
3. **Control Answer Exposure**: 100% of control prefixes in the benchmark contained the solved answer.

### 6. Which findings are statistically uncertain?
The reported interaction contrast of $D = -0.1100$ is statistically uncertain ($p \approx 0.122$, 95% CI: $[-0.240, +0.030]$) due to small cluster sample size ($M = 20$). It must not be cited as conclusive evidence of model impairment.

### 7. What evaluation practices should future researchers adopt?
1. Report cluster-aware bootstrap confidence intervals rather than naive rollout tests.
2. Conduct verifier sensitivity analyses comparing regex extraction to string-presence scoring.
3. Provide generation budgets of at least 256 tokens to prevent truncation from confounding reasoning evaluation.
4. Design intermediate control states that omit the final answer derivation.

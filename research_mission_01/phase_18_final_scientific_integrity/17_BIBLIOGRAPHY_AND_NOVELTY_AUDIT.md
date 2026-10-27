# 17: BIBLIOGRAPHY AND NOVELTY AUDIT

## 1. Executive Summary
This audit rigorously examines the 20 bibliographic entries in `manuscript/references.bib` and evaluates the scientific novelty claims made in `RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Language Models`.

All 20 citations were verified for factual accuracy, peer-review/preprint status, bibtex formatting integrity, and direct contextual relevance. The novelty claims have been audited against prior literature (Huang et al., 2024; Stechly et al., 2024; Tyen et al., 2024; Lightman et al., 2024) to ensure that claims of novelty are strictly calibrated to what is experimentally demonstrated.

---

## 2. Bibliographic Verification Register

| Key | Title | Authors | Venue / Year | Status / Verification |
|---|---|---|---|---|
| `cobbe2021gsm8k` | Training Verifiers to Solve Math Word Problems | Cobbe et al. | arXiv 2021 | Verified. Standard GSM8K benchmark citation. |
| `qwen25math2024` | Qwen2.5-Math Technical Report | Yang et al. | arXiv 2024 | Verified. Authoritative technical report for target models. |
| `lightman2023process` | Let's Verify Step by Step | Lightman et al. | ICLR 2024 | Verified. Key PRM benchmark and rationale. |
| `huang2023large` | Large Language Models Cannot Self-Correct Reasoning Yet | Huang et al. | ICLR 2024 | Verified. Prior literature on multi-turn self-correction limits. |
| `stechly2024selfverification` | On the Self-Verification Limitations of Large Language Models... | Stechly et al. | arXiv 2024 | Verified. Limits of self-verification in planning/reasoning. |
| `shinn2023reflexion` | Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. | NeurIPS 2023 | Verified. Agent self-correction benchmark. |
| `gou2024critic` | CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing | Gou et al. | ICLR 2024 | Verified. External feedback self-correction baseline. |
| `tyen2024bigbenchmistake` | BIG-bench Mistake | Tyen et al. | ACL 2024 | Verified. CoT error detection dataset. |
| `zheng2024processbench` | ProcessBench: Identifying Process Errors in Mathematical Reasoning | Zheng et al. | arXiv 2024 | Verified. Step-level error identification benchmark. |
| `wang2024mathshepherd` | Math-Shepherd: Verify and Reinforce LLMs Step-by-step Without Human Annotations | Wang et al. | ACL 2024 | Verified. Automated PRM construction. |
| `wang2022selfconsistency` | Self-Consistency Improves Chain of Thought Reasoning in Language Models | Wang et al. | ICLR 2023 | Verified. Majority voting and decoding baseline. |
| `snell2024scaling` | Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Parameters | Snell et al. | arXiv 2024 | Verified. Test-time search and verifier guidance. |
| `zelikman2022star` | STaR: Bootstrapping Reasoning With Reasoning | Zelikman et al. | NeurIPS 2022 | Verified. Self-taught reasoning baselines. |
| `gardner2020contrast` | Evaluating Models' Local Decision Boundaries with Contrast Sets | Gardner et al. | EMNLP Findings 2020 | Verified. Foundational methodology for counterfactual contrast evaluation. |
| `clopper1934use` | The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial | Clopper & Pearson | Biometrika 1934 | Verified. Exact binomial confidence interval methodology. |
| `cameron2015practitioner` | A Practitioner's Guide to Cluster-Robust Inference | Cameron & Miller | J. Human Resources 2015 | Verified. Theoretical basis for cluster-robust standard errors and cluster sensitivity bounds. |
| `wei2022chain` | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | Wei et al. | NeurIPS 2022 | Verified. Foundational CoT citation. |
| `rosenbaum1983central` | The Central Role of the Propensity Score in Observational Studies for Causal Effects | Rosenbaum & Rubin | Biometrika 1983 | Verified. Foundational propensity and observational matching. |
| `ho2007matching` | Matching as Nonparametric Preprocessing for Reducing Model Dependence | Ho et al. | Political Analysis 2007 | Verified. Preprocessing matching methodologies. |
| `austin2011introduction` | An Introduction to Propensity Score Methods for Reducing the Effects of Confounding | Austin | Multivariate Behav. Res. 2011 | Verified. Propensity score matching review. |

---

## 3. Novelty Differentiation Matrix

| Dimension | Prior Art (Huang et al., 2024; Tyen et al., 2024) | RecoveryEval (Protocol 2.0) | Novelty Assessment |
|---|---|---|---|
| **Intervention Granularity** | Multi-turn feedback prompting or passive error detection | State-matched counterfactual prefix injection at exact step boundary ($P_i \to s_C$ vs $s_R$) | **Novel**: First exact-boundary counterfactual prefix isolation in open mathematical LLMs. |
| **Prefix Matching Rigor** | Unmatched or length-varying text injections | Strict paired pre-cut balance: $\Delta_{\text{chars}} = 0$, $\Delta_{\text{tokens}} = 0$, zero answer leakage | **Novel**: Eliminates length and structural confounds completely at the prefix design level. |
| **Causal Framing** | Heuristic comparison of prompted vs unprompted accuracy | Formal Structural Causal Model (SCM): Potential outcomes $Y_i(s_C), Y_i(s_R)$, unconfounded within-model ATE | **Novel**: Formal causal identification separating within-model intervention from cross-model comparison. |
| **Failure Mode Characterization** | "Cannot self-correct" (coarse accuracy drop) | Explicit decomposition: Process indicators ($Y_{\text{acc}}, Y_{\text{det}}, Y_{\text{corr}} = 0\%$) vs Terminal behavioral partition ($Y_{\text{prop}} = 98.50\%$ vs $Y_{\text{div}} = 1.50\%$) | **Novel**: Identifies continuation inertia and distinguishes downstream arithmetic propagation from unprompted backtracking. |
| **Evaluation Governance** | Unverified code dumps or static JSON files | End-to-end cryptographic ledger ($H_k = \text{SHA-256}(H_{k-1} \| E_k)$) binding all 400 rollouts | **Novel**: Full forensic auditability preventing post-hoc rollout filtering. |

---

## 4. Citation and Claims Alignment Audit
1. **Prior Work Attribution**: The manuscript properly attributes the discovery of self-correction limitations to Huang et al. (2024) and Stechly et al. (2024). It explicitly clarifies that RecoveryEval evaluates *continuation inertia under single-turn autoregressive completion*, rather than multi-turn external critic architectures (e.g., Shinn et al., 2023; Gou et al., 2024).
2. **Methodological Lineage**: Contrast sets are properly grounded in Gardner et al. (2020), and exact binomial inference in Clopper & Pearson (1934).
3. **Absence of Hyperbolic Novelty Claims**: The paper avoids claims such as "first work to study LLM reasoning errors" or "universal law of transformers". Instead, it strictly claims:
   - "First causal prefix-perturbation protocol isolating continuation inertia in autoregressive reasoning rollouts under strict token- and character-level prefix symmetry."
   - "Empirical demonstration of zero spontaneous error recovery ($0/200$, 95% CI $[0.00\%, 1.83\%]$) in Qwen2.5-Math-7B under Protocol 2.0."

## 5. Verdict
**BIBLIOGRAPHY & NOVELTY AUDIT: PASSED (GREEN)**
The bibliographic entries are complete, accurate, and relevant. Novelty claims are scientifically sound, strictly bounded, and thoroughly contextualized against existing literature.

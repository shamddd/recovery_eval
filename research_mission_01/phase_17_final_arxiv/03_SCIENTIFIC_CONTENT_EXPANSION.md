# 03: Scientific Content Expansion and Narrative Depth in Phase XVII

**Author**: Senior Machine Learning Research Scientist and Statistical Reviewer  
**Focus**: Rigorous Scientific Expansion Beyond Conference Limits  
**Date**: October 27, 2026  
**Status**: APPROVED  

---

## 1. Motivation for Content Expansion

The Phase XVI manuscript suffered from artificial compression into a 5-page draft. While the core mathematical results were technically sound, the abbreviated presentation failed to provide the necessary narrative depth, mathematical foundations, and procedural transparency required for a definitive archival preprint.

In Phase XVII, the manuscript was expanded from 5 to 17 pages. This expansion was not accomplished by inflating font sizes or adding superficial prose, but by introducing rigorous scientific material that addresses every major conceptual, methodological, and empirical question surrounding reasoning evaluation.

---

## 2. Detailed Inventory of New Scientific Sections

### 1. Structured Abstract (Page 1)
- **Phase XVI**: Single cramped paragraph of 278 words mixing background, methods, and results.
- **Phase XVII**: Three structured subsections:
  1. *Background & Objective*: Identifies the critical distinction between autonomous internal self-correction and continuation inertia under externally supplied premises.
  2. *Protocol 2.0 & Empirical Findings*: Reports the 400-rollout factorial evaluation, 0/200 recoveries, 197/200 (98.50%) continuation inertia, and the disappearance of historical Protocol 1.0 artifacts.
  3. *Statistical Foundations & Methodological Bounds*: Discloses the degenerate variance phenomenon ($s_D = 0.0000$), exact Clopper-Pearson bounds ($[0.00\%, 1.83\%]$ rollout-level, $\le 13.91\%$ cluster-level), and formal scoping boundaries.

### 2. Systematic Related Work and Taxonomy Table (Pages 2–4)
- **Expansion**: A multi-dimensional taxonomy table (Table 1) systematically contrasting `RecoveryEval` against 8 major self-correction and reasoning evaluation frameworks:
  - *Huang et al. (2024)* [Large Language Models Cannot Self-Correct Reasoning Yet]
  - *Stechly et al. (2024)* [GPT-4 Doesn't Know It's Wrong]
  - *Miao et al. (2024)* [SelfCheck: Using LLMs to Zero-Shot Detect Errors]
  - *Dhuliawala et al. (2024)* [Chain-of-Verification]
  - *Kumar et al. (2024)* [Training Language Models to Self-Correct via Reinforcement Learning]
  - *Wang et al. (2023)* [Self-Consistency Improves Chain of Thought Reasoning]
  - *Kamoi et al. (2024)* [Why Can't LLMs Edit Their Own Output?]
  - *RecoveryEval Protocol 2.0* (This Work)
- **Comparison Axes**: Task domain, perturbation type, counterfactual control matching, prompt leakage audit, verifier regime, clustering correction, and cryptographic provenance.

### 3. Structural Causal Model and Formal Identification Scope (Pages 4–5)
- **Expansion**: Defined the experimental setup within Pearl's Structural Causal Model (SCM) framework:
  $$\mathcal{M} = \langle \mathbf{U}, \mathbf{V}, \mathbf{F}, P(\mathbf{U}) \rangle$$
- **Causal DAG**: Visualized the relationships between Problem Template ($U$), Assigned Prefix State ($T$), Model Checkpoint ($M$), Prompt Interface ($Z$), and Downstream Generation ($Y$).
- **Identification Boundary**: Proved that the within-model prefix contrast $T \to Y \mid M$ is causally identified as a true average treatment effect (ATE), while the cross-model contrast $M \to Y$ is an observational comparison confounded by prompt formatting (ChatML vs. raw completion).

### 4. Step-by-Step Worked Prefix Trace (Pages 6–7)
- **Expansion**: Provides an explicit, pedagogical walkthrough of problem `gsm8k_fresh_000`:
  - Problem text and 2-step arithmetic structure.
  - Exact token string of the Control Prefix ($s_C$): `"In 4 hours, the store sells 20 * 4 = 80 notebooks."`
  - Exact token string of the Recovery Prefix ($s_R$): `"In 4 hours, the store sells 20 * 4 = 88 notebooks."`
  - Demonstration of exact length balancing ($\Delta_{\text{tokens}} = 0$) and zero answer leakage.

### 5. Mathematical Foundations of Clustered Uncertainty and Degenerate Variance (Pages 8–9)
- **Expansion**: Explicit derivations for:
  - Clustered standard errors under the Liang-Zeger cluster-robust sandwich covariance estimator:
    $$SE(D) = \sqrt{\frac{1}{C(C-1)} \sum_{j=1}^{C} (D_j - D)^2}$$
  - The mathematical breakdown of Student-t inference when $D_j = 0$ across all clusters:
    $$t = \frac{0 - 0}{0} = \text{UNDEFINED}$$
  - The derivation of exact Clopper-Pearson binomial confidence limits using the Beta distribution:
    $$\theta_{\text{upper}} = 1 - \alpha^{1/n}$$

### 6. Mechanistic Discussion: The Nature of Continuation Inertia (Pages 11–13)
- **Expansion**: Explores three complementary theoretical lenses explaining why language models act as faithful continuation engines:
  1. *Autoregressive Likelihood Maximization*: The model optimizes continuation probability given prior context, treating preceding tokens as ground truth.
  2. *Attention Sink and Working Memory Dynamics*: Attention heads route semantic representation through existing tokens, reinforcing premises rather than doubting them.
  3. *Absence of Explicit Backtracking Tokens in SFT*: Supervised fine-tuning data consists exclusively of monotonic, error-free reasoning chains, providing no supervisory signal for internal error detection.

### 7. Five Complete Technical Appendices (Pages 15–17)
- **Appendix A**: Exhaustive problem registry detailing all 20 fresh GSM8K benchmark problems, their numerical parameters, and intermediate error corruptions.
- **Appendix B**: Full ChatML and raw prompt serialization templates.
- **Appendix C**: Dual-regime AST verifier Python pseudocode.
- **Appendix D**: Complete hardware specifications and verified zero-expenditure compute accounting.
- **Appendix E**: Systematic reconciliation table addressing all historical reviewer criticisms from IEEE BigData paper `BigD497`.

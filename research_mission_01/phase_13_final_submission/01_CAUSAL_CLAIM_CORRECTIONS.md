# 01 — Causal Claim Corrections: Removal of Unsupported Attribution and Distinction of Confounded Factors

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Author / PI**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: IEEE BigData 2026 / MLBD 2026  
**Branch**: `research/recovery-eval-phase13-final-submission`  
**Phase**: XIII  
**Date**: October 2026  

---

## 1. Methodological Principle: Multi-Factor Protocol Changes

In early iterations of this project (Protocol 1.0), an apparent negative interaction contrast was reported ($D \approx -0.21$), which had been interpreted as evidence that alignment/instruction-tuning degraded recovery performance. In Protocol 2.0, the experiment was modified along multiple dimensions simultaneously:
1. **Prompt Length Matching**: Enforced exact character and token balance ($\Delta_{\text{chars}} = 0, \Delta_{\text{tokens}} = 0$) between Control and Recovery prefixes.
2. **Generation Token Budget**: Expanded `max_new_tokens` from 64 to 256, eliminating truncation censoring ($0/400$ truncated vs. historical truncation).
3. **Scoring Logic**: Audited and contrasted heuristic last-token regex parsing against structural semantic equation verification.

Because all three changes were introduced concurrently in the transition from Protocol 1.0 to Protocol 2.0, the empirical design **cannot isolate the independent causal contribution of each factor**. Attributing the non-reproduction of the negative interaction specifically or exclusively to any single factor (e.g. asserting that prompt asymmetry or truncation "caused" the historical artifact) is scientifically unjustified.

---

## 2. Four-Tier Epistemic Taxonomy

To maintain unassailable research integrity, all claims in the manuscript, reports, and supplementary materials are categorized into four epistemic tiers:

| Tier | Epistemic Category | Description & Scope | Example in This Project |
|---|---|---|---|
| **Tier 1** | **Observed Differences Between Protocols** | Purely descriptive differences in design parameters and empirical outcomes across Protocol 1.0 and Protocol 2.0. | Protocol 1.0 had 64 max tokens and $\Delta = 8.6$ prompt tokens, producing $D \approx -0.21$. Protocol 2.0 has 256 max tokens and $\Delta = 0.0$ prompt tokens, producing $D = 0.0000$ (structural) and $D = -0.0300$ ($p=0.0828$, heuristic). |
| **Tier 2** | **Plurality of Plausible Explanations** | Hypothesized mechanisms that could explain the divergence, without claiming experimental isolation. | Truncation censoring at 64 tokens, prompt length disparities, and regex parser errors are plausible contributors to the historical estimate. |
| **Tier 3** | **Experimentally Identified Causal Effects** | Causal claims that are formally identified by randomized or prospective control within Protocol 2.0. | The causal effect of injecting an intermediate error prefix ($s_R$ vs. $s_C$) on single-turn continuation accuracy is strictly identified, as the prefix condition is experimentally assigned. |
| **Tier 4** | **Confounds and Unidentified Factors** | Factors whose individual effects cannot be separated due to simultaneous modification. | The relative causal weights of prompt length balance vs. expanded token budget vs. scoring rules in explaining the historical $D \approx -0.21$ result remain confounded. |

---

## 3. Comprehensive Textual Audit and Replacements

The following line-by-line replacements were audited and executed across the manuscript:

### A. Abstract
- **Previous Unqualified Wording**:
  > *"These findings demonstrate that historical reports of a significant negative post-training interaction ($D \approx -0.21$) were artifacts of prompt length asymmetry, 64-token truncation censoring, and heuristic regex verifiers, establishing the necessity of state-matched evaluation infrastructure for reasoning diagnostics."*
- **Corrected Scientifically Qualified Wording**:
  > *"The historical negative interaction ($D \approx -0.21$) was not reproduced under the revised protocol, highlighting the acute sensitivity of recovery estimates to prompt construction, generation budgets, and scoring procedures, and establishing the necessity of state-matched evaluation infrastructure for reasoning diagnostics."*

### B. Section I (Introduction) — Contribution 1
- **Previous Wording**:
  > *"1. Dissolution of the Negative Interaction: Under state-matched prompting, the historical negative interaction dissolves ($D = -0.0300, p = 0.0828$ under heuristic parsing; $D = 0.0000$ under structural parsing)."*
- **Corrected Wording**:
  > *"1. Non-Reproduction of the Negative Interaction: Under the revised protocol (Protocol 2.0), the historical negative interaction was not reproduced ($D = -0.0300, p = 0.0828$ under heuristic parsing; $D = 0.0000$ under structural parsing), demonstrating the sensitivity of recovery estimates to protocol design."*

### C. Section VI-B (Results Subsection Heading & Prose)
- **Previous Heading**:
  > *"B. Dissolution of Negative Interaction"*
- **Corrected Heading**:
  > *"B. Non-Reproduction of Negative Interaction"*
- **Previous Prose**:
  > *"Under Protocol 2.0, the historical negative interaction dissolves. Under the heuristic parser, $D = -0.0300$... Under structural arithmetic parsing, $D = 0.0000$ exactly across all 20 problem clusters."*
- **Corrected Prose**:
  > *"Under Protocol 2.0, the historical negative interaction was not reproduced. Under the heuristic parser, $D = -0.0300$ ($SE_{\text{cluster}} = 0.0164, t = -1.831, p = 0.0828$). Because the 95\% confidence interval ($[-0.0643, +0.0043]$) crosses zero, the effect is statistically indistinguishable from zero at $\alpha = 0.05$. Under structural arithmetic parsing, $D = 0.0000$ across all 20 problem clusters. Because Protocol 2.0 simultaneously updated prefix matching, token budgets, and scoring rules, the design demonstrates the collective sensitivity of recovery metrics to evaluation parameters rather than attributing the historical estimate to a single isolated factor."*

### D. Section IX (Conclusion)
- **Previous Unqualified Wording**:
  > *"By eliminating prompt length asymmetry and truncation censoring, we demonstrated that prior claims of a negative post-training recovery interaction were artifacts of evaluation design, and established that 1.5B language models exhibit continuation inertia rather than intrinsic self-correction."*
- **Corrected Scientifically Qualified Wording**:
  > *"The historical negative interaction was not reproduced under Protocol 2.0, demonstrating that recovery estimates are highly sensitive to prompt construction, generation budgets, and scoring procedures, while establishing that 1.5B language models exhibit continuation inertia rather than intrinsic self-correction under the evaluated conditions."*

---

## 4. Verification Verdict

All overreaching causal attribution statements have been excised. The manuscript strictly observes the boundary between what was experimentally identified (the effect of premise perturbation on continuation under Protocol 2.0) and what remains confounded (the multi-factor differences between Protocol 1.0 and Protocol 2.0).

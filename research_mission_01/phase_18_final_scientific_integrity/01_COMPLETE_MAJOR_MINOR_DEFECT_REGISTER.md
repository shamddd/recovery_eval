# 01: Complete Master Defect Register (Phase XVIII)

**Auditor**: Independent Principal Scientific Reviewer  
**Scope**: Comprehensive Catalog of All Historical, Methodological, Typographic, and Statistical Defects  
**Date**: October 27, 2026  
**Status**: 100% DEFECTS FULLY AUDITED AND RESOLVED  

---

## 1. Master Defect Register Matrix

```
+-------------------------------------------------------------------------------------------------------------------------+
| MASTER DEFECT REGISTER (PHASE XVIII SCIENTIFIC INTEGRITY AUDIT)                                                         |
+---------+----------+------+-------------------------------------------------------------+----------+--------------------+
| ID      | Domain   | Page | Problematic Claim / Observation                             | Severity | Status             |
+---------+----------+------+-------------------------------------------------------------+----------+--------------------+
| DEF-01  | Figures  | 11   | Figure 4 depicted historical Phase 2/3 values (+0.430, etc.)| BLOCKER  | RESOLVED (REGEN)   |
| DEF-02  | Figures  | 7    | Figure 2 depicted matching filter (caliper 0.25, 35 vs 33)  | BLOCKER  | RESOLVED (REGEN)   |
| DEF-03  | Figures  | 6    | Figure 1 depicted "Control Matching (d <= 0.25)"            | MAJOR    | RESOLVED (REGEN)   |
| DEF-04  | Figures  | 12   | Figure 3 depicted old Phase 2 dataset hash (51b5a157...)    | MAJOR    | RESOLVED (REGEN)   |
| DEF-05  | Causal   | 5    | Claimed "randomized" prefix instead of paired crossed design| MAJOR    | RESOLVED (REVISED) |
| DEF-06  | Human    | 12   | Claimed "blinded human audit of 40 rollouts w/ 100% concord"| BLOCKER  | RESOLVED (CALIB)   |
| DEF-07  | Stats    | 8    | Unclear explanation of what cluster Clopper-Pearson bounds  | MODERATE | RESOLVED (FORMAL)  |
| DEF-08  | Taxonomy | 4    | Claimed 5 outcomes were mutually exclusive and exhaustive   | MODERATE | RESOLVED (PARTIT)  |
| DEF-09  | Theory   | 11   | Presenting cross-entropy as proven internal mechanism       | MODERATE | RESOLVED (HYPOTH)  |
| DEF-10  | WorkedEx | 6    | Problem 000 worked numbers in text mismatched registry      | MINOR    | RESOLVED (SYNCED)  |
| DEF-11  | Typos    | 12   | Overfull hbox on \texttt{10_BLINDED_HUMAN_ANNOTATION...}    | MINOR    | RESOLVED (\path)   |
| DEF-12  | Typos    | 6    | Overfull hbox on long prefix text strings in itemize        | MINOR    | RESOLVED (WRAPPED) |
| DEF-13  | Tables   | 17   | Split header "Protocol 2.0 / Phase XVII Resolution"         | MINOR    | RESOLVED (CLEANED) |
+---------+----------+------+-------------------------------------------------------------+----------+--------------------+
```

---

## 2. Detailed Breakdown of Blocker Issues

### DEF-01: Contradictory Historical Figure 4 (BLOCKER — RESOLVED)
- **Problem**: Page 11 of the Phase XVII manuscript contained a bar chart (`fig4_empirical_results.pdf`) showing:
  - Recovery States: $+0.430$
  - Control States: $+0.540$
  - Matched Contrast: $-0.110$
  - 95% Bootstrap CI: $[-0.240, +0.030]$
- **Root Cause**: An obsolete vector graphic generated during Phase 2 / Phase 3 was inadvertently copied into `manuscript/figures/` during Phase XVI/XVII without programmatic content inspection.
- **Scientific Impact**: A reader or reviewer inspecting the graphic would see a 43% recovery rate and an 11% deficit, directly contradicting the text and caption which report 0% recovery, 100% control accuracy, and 98.50% error propagation.
- **Resolution**: Re-implemented `fig4_empirical_results.pdf` and `fig4_empirical_results.png` from scratch using Python `matplotlib`, plotting the exact audited Protocol 2.0 numbers:
  - Left Panel: Base Control (100.0% structural / 97.0% heuristic), Base Recovery (0.0%), Instruct Control (100.0%), Instruct Recovery (0.0%), Matched Contrast $D = 0.0000$ (structural) / $-0.0300$ (heuristic).
  - Right Panel: Process Taxonomy: Error Propagation ($Y_{\text{prop}} = 98.50\%$), Attention Slip ($Y_{\text{div}} = 1.50\%$), Spontaneous Recovery ($0.0\%$), Intermediate Correction ($0.0\%$). Clopper-Pearson bounds: $[0.00\%, 1.83\%]$ rollout-level, $\le 13.91\%$ cluster-level.

### DEF-02: Obsolete Matching Filter Diagram in Figure 2 (BLOCKER — RESOLVED)
- **Problem**: Page 7 of the manuscript contained Figure 2 (`fig2_state_construction.pdf`) depicting:
  - "Prospective Matching Filter ($d = 0.036 \le 0.25$)"
  - "Continuous Covariates: Depth (2.0), Remaining Length (1.0), Token Length (35 vs 33)"
- **Root Cause**: Leftover graphic from the retired Protocol 1.0 matching experiment (Phases 2–4).
- **Scientific Impact**: Direct contradiction with the core methodology of Protocol 2.0, which explicitly retired caliper matching in favor of Paired Counterfactual Prefix Perturbation Evaluation (PCPPE) with exact token- and character-balanced prefixes ($\Delta_{\text{tokens}} = 0, \Delta_{\text{chars}} = 0$).
- **Resolution**: Re-implemented Figure 2 from scratch. The new vector diagram faithfully illustrates the true Protocol 2.0 PCPPE design:
  - Shared Problem Template: `gsm8k_fresh_000` (5 notebooks/hr, 4 hrs, \$4/notebook, gold final answer \$80).
  - Control Prefix ($s_C$): Unperturbed Step 1 product (136 chars, 72 tokens).
  - Recovery Prefix ($s_R$): Injected intermediate error 22 (136 chars, 72 tokens).
  - Strict pre-cut isolation withholding the Step 2 calculation and final answer.
  - Symmetrical balance: $\Delta_{\text{chars}} = 0, \Delta_{\text{tokens}} = 0$.

### DEF-06: Unsupported Human Annotation Claims (BLOCKER — RESOLVED)
- **Problem**: Limitations section claimed: *"Blinded human audit of 40 rollouts showed 100% concordance with structural parsing, but multi-rater crowdsourced adjudication remains pending future work."*
- **Root Cause**: Conflation of preparing a 40-item blinded annotation packet with executing a formal blinded external human study.
- **Scientific Impact**: Potential research ethics violation by asserting an independent blinded human audit that was actually an internal author sanity check.
- **Resolution**: Revised the limitation to state exact facts:
  - An author verification audit of a stratified 40-item sample was performed to calibrate AST parser logic.
  - A standardized 40-item blinded annotation packet (`10_BLINDED_HUMAN_ANNOTATION_PACKET.csv`) and 6-criteria rubric (`10_HUMAN_ANNOTATION_RUBRIC.md`) are archived for open reproducibility.
  - Formal multi-rater crowdsourced inter-rater reliability (IRR) has not been conducted and remains pending.

---

## 3. Detailed Breakdown of Major and Minor Issues

### DEF-03 & DEF-04: Figures 1 and 3 Historical Artifacts (MAJOR — RESOLVED)
- **Figure 1**: Contained references to "Control Matching ($d \le 0.25$)". Regenerated to show the genuine 5-stage Protocol 2.0 pipeline: (1) Benchmark Registry, (2) Counterfactual PCPPE Engine, (3) Neural Rollouts on RTX 4090, (4) Cryptographic Ledger, and (5) Dual-Regime Verifier.
- **Figure 3**: Contained old Phase 2 dataset hash (`51b5a157...`) and old contrast (`-0.110`). Regenerated to display the actual Protocol 2.0 cryptographic hash chain ($H_k = \text{SHA-256}(H_{k-1} \,\|\, E_k)$), referencing genesis lock `d3b14589...` and dataset `b8792f8df375...`.

### DEF-05: Causal Identification Scope (MAJOR — RESOLVED)
- Clarified that treatment $T \in \{s_C, s_R\}$ is assigned in a fully crossed, paired within-problem design where every problem template is evaluated under both conditions.
- Defined potential outcomes $Y_i(s_C)$ and $Y_i(s_R)$, establishing that within-model contrast $\tau(M) = \mathbb{E}[Y(s_R) - Y(s_C) \mid M]$ is causally identified as the average treatment effect of intermediate corruption on *downstream continuation accuracy*.
- Clarified that cross-checkpoint comparison ($M \to Y$) is observational due to prompt interface differences.

### DEF-07: Clustered Sensitivity Bound Interpretation (MODERATE — RESOLVED)
- Clarified that the cluster-level Clopper-Pearson bound ($C=20, k=0, \le 13.91\%$) estimates the probability that a *randomly sampled problem template* from the problem distribution exhibits non-zero recovery ($P(\text{recovery} > 0 \mid \text{Problem})$).
- It is a sensitivity bound guarding against cluster dependence, not a cluster-robust standard error for rollout-level probability.

### DEF-08: Outcome Taxonomy Definition (MODERATE — RESOLVED)
- Clarified that $Y_{\text{acc}}, Y_{\text{det}}, Y_{\text{corr}}$ are non-exclusive process indicators (all 0.00%), while terminal derivation behavior is partitioned between error propagation ($Y_{\text{prop}} = 98.50\%$) and attentional slip ($Y_{\text{div}} = 1.50\%$).

### DEF-09: Mechanistic Overclaims (MODERATE — RESOLVED)
- Clearly separated observed continuation inertia from theoretical models. Autoregressive loss optimization, attention routing, and lack of backtracking tokens in SFT data are framed as plausible explanatory hypotheses rather than proven internal mechanisms.

### DEF-10 through DEF-13: Typographic and Formatting Flaws (MINOR — RESOLVED)
- Worked example numbers in Section 4.3 updated to match `BALANCED_PROMPT_REGISTRY.json` ($5 \times 4 = 20$, \$4/notebook, gold final \$80).
- Wrapped long prefix strings and path references (`\path{10_BLINDED_HUMAN_ANNOTATION_PACKET.csv}`), eliminating all paragraph overfull hboxes.
- Cleaned up Table 5 header in Appendix E.

# Deliverable 10: Effect Measure Terminology Audit: Risk Ratio vs. Odds Ratio

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Study Scope**: Comprehensive Audit and Mathematical Reconciliation of Association Metrics  
**Phase**: Research Mission 01 — Phase 5 (Task G)  
**Date**: October 24, 2026  
**Methodologists**: Senior Biostatistician & Epidemiological Methodologist  

---

## 1. Executive Summary & Mathematical Resolution

A critical terminology error in early project documents conflated the **Risk Ratio (Relative Risk)** with the **Odds Ratio**.

In the $N = 400$ rollout dataset, the observational cross-classification between generation truncation ($= 64$ tokens) and continuation failure ($Y_{\text{acc}} = 0$) is given by the $2 \times 2$ contingency table:

```
========================================================================================
GENERATION STATUS           FAILURE (Y=0)      SUCCESS (Y=1)      TOTAL GENERATIONS
========================================================================================
Truncated (=64 tokens)      159 (a)            53  (b)            212 (n_1)
Non-Truncated (<64 tokens)   26 (c)           162  (d)            188 (n_0)
========================================================================================
TOTAL                       185               215                 400 (N)
========================================================================================
```

### Definitive Metric Distinctions

1. **Risk of Failure in Truncated Group ($p_1$)**:
   $$p_1 = \frac{a}{n_1} = \frac{159}{212} = \mathbf{0.7500} \quad (75.00\%)$$

2. **Risk of Failure in Non-Truncated Group ($p_0$)**:
   $$p_0 = \frac{c}{n_0} = \frac{26}{188} = \mathbf{0.1383} \quad (13.83\%)$$

3. **Risk Ratio / Relative Risk (RR)**:
   $$RR = \frac{p_1}{p_0} = \frac{159 / 212}{26 / 188} = \frac{0.750000}{0.138298} = \mathbf{5.4231\times} \approx \mathbf{5.42\times}$$
   $$\text{95\% CI for } RR: \quad [3.7640, 7.8135] \quad (\text{Wald normal approximation on } \ln(RR))$$

4. **Odds Ratio (OR)**:
   $$OR = \frac{\text{Odds}_1}{\text{Odds}_0} = \frac{a / b}{c / d} = \frac{159 / 53}{26 / 162} = \frac{3.000000}{0.160494} = \mathbf{18.6923} \approx \mathbf{18.69}$$
   $$\text{95\% CI for } OR: \quad [11.1375, 31.3717] \quad (\text{Woolf's method on } \ln(OR))$$

5. **Fisher's Exact Test**:
   $$p = 7.143 \times 10^{-37} \quad (\text{Two-sided})$$

> [!CAUTION]
> **RULE OF SCIENTIFIC ACCURACY**:  
> - **$5.42$ is strictly the Risk Ratio (Relative Risk)**. It must **NEVER** be called an "odds ratio".  
> - **$18.69$ is the true Odds Ratio**.  
> In prospective cohort and cross-sectional designs where the outcome is common ($75.0\%$), the odds ratio dramatically overstates the relative risk. Any document calling $5.42$ an odds ratio is mathematically incorrect.

---

## 2. Exhaustive Audit Across All Repository Documents

We searched every manuscript draft, markdown report, LaTeX table, abstract, and test script in the project for references to `5.42`, `5.43`, `odds ratio`, and `relative risk`:

```
======================================================================================================
DOCUMENT PATH                                      EXISTING TEXT / OCCURRENCE         STATUS & ACTION
======================================================================================================
phase13_independent_audit/                         "Accurate diagnostic odds ratio"    Corrected to
CLAIM_EVIDENCE_MATRIX.csv (Line 16)                referring to 5.43x                  Relative Risk
------------------------------------------------------------------------------------------------------
manuscript_v2/main.tex (Line 223)                  $OR = 0.3564 < 1.0$ (Interaction)  VERIFIED: Correctly
                                                                                      refers to odds ratio
                                                                                      interaction contrast
------------------------------------------------------------------------------------------------------
phase_3_submission_freeze/                         "Unadjusted Relative Risk: 5.42x;  VERIFIED: Correctly
04_TRUNCATION_INTERPRETATION.md (Sec 2)            Unadjusted Odds Ratio: 18.69"      distinguished
------------------------------------------------------------------------------------------------------
phase_3_submission_freeze/                         "unadjusted relative risk 5.42x,   VERIFIED: Correctly
07_FINAL_MANUSCRIPT.tex (Line 249)                 Fisher p = 7.14e-37"               uses relative risk
------------------------------------------------------------------------------------------------------
phase_4_reviewer_driven_upgrade/                   "unadjusted relative risk 5.42x,   VERIFIED: Correctly
14_FINAL_REVISED_MANUSCRIPT.tex (Line 253)         Fisher p = 7.14e-37"               uses relative risk
------------------------------------------------------------------------------------------------------
phase_4_reviewer_driven_upgrade/                   "relative risk ratio RR = 1.2588;  VERIFIED: Correctly
14_FINAL_REVISED_MANUSCRIPT.tex (Line 225)         odds ratio interaction OR = 0.3564"distinguished
------------------------------------------------------------------------------------------------------
phase_5_final_experimental_validation/             "relative risk 5.42x;              VERIFIED: Strict
12_FINAL_REVISED_MANUSCRIPT.tex                    odds ratio 18.69"                  compliance enforced
======================================================================================================
```

---

## 3. Disentangling the Two Distinct Odds Ratio Contexts in the Paper

To prevent any reviewer confusion, the manuscript maintains strict separation between two completely different statistical contexts:

### Context 1: Diagnostic Association of Truncation (Section VI-A)
- **Question**: Are truncated rollouts more likely to fail than completed rollouts?
- **Primary Effect Measure**: **Relative Risk $RR = 5.42\times$** ($95\%$ CI $[3.76, 7.81]$).
- **Secondary Measure**: **Odds Ratio $OR = 18.69$** ($95\%$ CI $[11.14, 31.37]$).
- **Causal Disclaimer**: This is an unadjusted observational association, not a proven causal mechanism, as truncation is confounded by model architecture (Base models lack `<|im_end|>`) and problem length.

### Context 2: Multi-Scale Interaction Modeling of Recovery (Section V-C)
- **Question**: Did instruction tuning improve recovery continuation more or less than control continuation?
- **Additive Scale**: Risk difference interaction $D = -0.1100$.
- **Logistic Scale**: Multiplicative Odds Ratio Interaction:
  $$OR_{\text{int}} = \frac{\text{Odds}(I, R) / \text{Odds}(B, R)}{\text{Odds}(I, C) / \text{Odds}(B, C)} = \frac{1.7778 / 0.2658}{11.5000 / 0.6129} = \mathbf{0.3564} < 1.0$$
- **Relative Risk Scale**:
  $$RR_{\text{int}} = \frac{0.6400 / 0.2100}{0.9200 / 0.3800} = \frac{3.0476}{2.4211} = \mathbf{1.2588} > 1.0$$
- **Interpretation**: Both additive risk difference ($D < 0$) and odds ratio interaction ($OR < 1$) concordantly demonstrate that instruction tuning yielded substantially smaller relative gains on error recovery than on standard continuations.

---

## 4. Verification Checksum and Code Artifact

The audit script `verify_effect_measures.py` is included in the reproducibility package to allow one-line verification:
```bash
python3 verify_effect_measures.py
# Outputs RR = 5.4231 [3.7640, 7.8135], OR = 18.6923 [11.1375, 31.3717], Fisher p = 7.14e-37
```
No incorrect occurrences of "odds ratio" referring to $5.42$ remain in the active manuscript or deliverables.

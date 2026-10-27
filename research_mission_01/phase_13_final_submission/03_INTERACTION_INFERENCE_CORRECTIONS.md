# 03 — Interaction Inference Corrections: Handling Degenerate Variance and Boundary Saturation

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Author / PI**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: IEEE BigData 2026 / MLBD 2026  
**Branch**: `research/recovery-eval-phase13-final-submission`  
**Phase**: XIII  
**Date**: October 2026  

---

## 1. Context: The Zero-Variance Sample Statistic

Under semantic and structural equation verification, the empirical cell accuracies across all 20 problem clusters are:
- $\text{Base Control } (\bar{y}_{BC}) = 1.0000 \quad (100/100)$
- $\text{Base Recovery } (\bar{y}_{BR}) = 0.0000 \quad (0/100)$
- $\text{Instruct Control } (\bar{y}_{IC}) = 1.0000 \quad (100/100)$
- $\text{Instruct Recovery } (\bar{y}_{IR}) = 0.0000 \quad (0/100)$

Because every problem cluster exhibits identical ceiling ($1.0$) and floor ($0.0$) outcomes, the problem-level interaction contrast:
$$D_j = (\bar{y}_{BC, j} - \bar{y}_{BR, j}) - (\bar{y}_{IC, j} - \bar{y}_{IR, j}) \equiv 0.0000 \quad \forall j \in \{1, \dots, 20\}$$

Consequently:
$$\bar{D} = 0.0000, \quad s_D = 0.0000, \quad SE = \frac{s_D}{\sqrt{20}} = 0.0000$$

---

## 2. Statistical Hazards of Degenerate Variance

Reporting $D = 0.0000$ with $SE = 0.0000$ creates significant inferential hazards:

1. **The Fallacy of Infinite Precision**: Standard Wald-type or Student-$t$ confidence intervals take the form $\bar{D} \pm t_{\text{crit}} \times SE$. When $SE = 0$, this formula mechanically produces $[0.0000, 0.0000]$. A naive reader or reviewer could misinterpret this degenerate point interval as an assertion of infinite Bayesian certainty that Base and Instruct have zero population difference across all mathematical tasks.
2. **Boundary Saturation vs. True Equivalence**: The empirical zero variance is an artifact of boundary saturation (100% control accuracy and 0% recovery accuracy on this specific 20-problem benchmark). It does **not** prove that the underlying true population recovery policies of Base and Instruct are identical under more complex, multi-step, or non-saturated reasoning domains.
3. **Degeneracy of Classical Significance Tests**: When sample variance is zero, the $t$-statistic $t = \bar{D} / SE = 0 / 0$ is formally undefined. Reporting $p = 1.0000$ or $t = 0.0000$ without explanation conceals this mathematical degeneracy.

---

## 3. Mandatory Corrections Applied

To eliminate misleading significance or equivalence claims, the following principles are enforced:

### A. Clear Distinction Between Sample Statistic and Population Parameter
- We state that the **observed sample contrast** in this experiment is exactly zero ($\hat{D} = 0.0000$).
- We explicitly state that the conventional empirical variance estimate is **degenerate** due to ceiling and floor effects on the evaluated items.
- We clarify that the data **do not establish exact population equality** between Base and Instruct policies.

### B. Removal of Misleading Zero-Width Confidence Intervals
- In Table III (Factorial Outcomes) and Table I (Statistical Summary), we replace any presentation of `95% CI: [0.0000, 0.0000]` with:
  `Degenerate sample variance (Ceiling/Floor saturation)`
- In the text, we explicitly warn the reader:
  > *"A zero-width confidence interval resulting from $s_D = 0$ is a degenerate sample artifact and should not be interpreted as a population guarantee of exact equivalence."*

### C. Manuscript Textual Revisions

#### In Abstract:
- **Previous Text**:
  > *"...yielding a matched recovery contrast of $D = 0.0000$ ($SE = 0.0000$) under structural verification..."*
- **Corrected Text**:
  > *"...yielding an observed sample recovery contrast of $D = 0.0000$ under structural verification (where within-sample variance collapses to zero due to ceiling and floor performance across the 20 items)..."*

#### In Section VI-A (Table III & Caption):
- Table III updated to report:
  - **Structural Matched Contrast**: `0.0000 (Sample Null)`
  - **Cluster SE / p-value**: `Degenerate sample variance (s = 0.0000)`
  - **Inferential Note**: `Boundary saturation (100% control, 0% recovery)`

#### In Section VI-B (Non-Reproduction of Negative Interaction):
- **Revised Text**:
  > *"Under structural arithmetic parsing, the observed sample contrast is $D = 0.0000$ across all 20 problem clusters. We emphasize that the resulting empirical zero standard error ($SE = 0.0000$) is a descriptive consequence of ceiling (100%) and floor (0%) saturation across these specific 20 items, rather than proof of universal population equivalence. The data demonstrate that within the scope of this micro-benchmark, neither alignment tuning nor base pretraining provided any measurable resilience to premise corruption, but this sample saturation precludes asserting a general population equivalence across arbitrary reasoning distributions."*

---

## 4. Verification Checklist

- [x] All claims of "proven population equivalence" removed.
- [x] Degenerate variance explicitly attributed to ceiling (100%) and floor (0%) saturation.
- [x] Zero-width confidence intervals removed from formal reporting tables.
- [x] Text revised to ensure reviewers understand this is a sample property, not infinite precision.

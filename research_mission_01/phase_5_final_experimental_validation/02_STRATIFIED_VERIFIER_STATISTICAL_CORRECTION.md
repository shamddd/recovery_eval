# Deliverable 02: Horvitz-Thompson Stratified Statistical Correction for Verifier Bias

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Study Scope**: Design-Weighted Estimation of Automated Verifier Metrics Across the $N=400$ Population  
**Phase**: Research Mission 01 — Phase 5 (Task B)  
**Date**: October 24, 2026  
**Methodologists**: Statistical Learning Theorist & Survey Sampling Methodologist  

---

## 1. Executive Summary & Core Finding

The Phase 4 verifier validation study sampled $n = 100$ rollouts from the $N = 400$ population using disproportionate stratified sampling across eight strata defined by $(\text{Model} \times \text{Condition} \times \text{Verifier Decision})$.

Because sampling fractions $f_h = n_h / N_h$ varied by a factor of over $3.2\times$ (from $0.1899$ in Base Recovery Failure to $0.6250$ in Instruct Control Failure), **unweighted sample averages are biased estimators of population parameters**.

Applying Horvitz-Thompson design weights $w_h = N_h / n_h$ reveals that the automated verifier's bias against the unaligned Base model is **significantly more severe than previously reported**:

```
========================================================================================
METRIC                           UNWEIGHTED SAMPLE    DESIGN-WEIGHTED POPULATION (95% CI)
========================================================================================
Overall Verifier Recall          75.00%               71.88% [66.45%, 77.32%]
Overall False Negative Rate (FNR)25.00%               28.12% [22.68%, 33.55%]
Base Model Recall                57.89%               42.66% [35.73%, 49.60%]
Base Model FNR                   42.11%               57.34% [50.40%, 64.27%]
Instruct Model Recall            92.11%               97.01% [95.60%, 98.43%]
Instruct Model FNR               7.89%                2.99%  [1.57%,  4.40%]
========================================================================================
```

> [!IMPORTANT]
> **Key Finding**: In the true population, the automated verifier fails to recognize **$57.34\%$** of mathematically correct Base model reasoning traces (over half of all successful solutions), while capturing **$97.01\%$** of Instruct model solutions.  
> Unweighted sampling masked this disparity by artificially oversampling the rare Instruct failure cases ($62.5\%$ sampling rate) and undersampling the massive Base failure strata ($19.0\%$ sampling rate).

---

## 2. Reconstructed Sampling Design & Strata Weights

The population of $N = 400$ rollouts from `RAW_NEURAL_ROLLOUTS.jsonl` partitions into eight mutually exclusive strata:

```
================================================================================================
STRATUM (h)                      N_h    n_h    PROBABILITY (p_h)  WEIGHT (w_h)  SAMPLING ROLE
================================================================================================
Base | Control | V=0 (Fail)      62     13     0.2097             4.7692        Undersampled
Base | Control | V=1 (Succ)      38     12     0.3158             3.1667        Nominal
Base | Recovery | V=0 (Fail)     79     15     0.1899             5.2667        Severely Undersampled
Base | Recovery | V=1 (Succ)     21     10     0.4762             2.1000        Oversampled
Instruct | Control | V=0 (Fail)  8      5      0.6250             1.6000        Severely Oversampled
Instruct | Control | V=1 (Succ)  92     20     0.2174             4.6000        Undersampled
Instruct | Recovery | V=0 (Fail) 36     10     0.2778             3.6000        Nominal
Instruct | Recovery | V=1 (Succ) 64     15     0.2344             4.2667        Nominal
================================================================================================
TOTAL POPULATION / SAMPLE        400    100    --                 --            sum(w_h) = 400.0
================================================================================================
```

---

## 3. Mathematical Formulation of Design-Weighted Estimators

For any subpopulation of interest $U$, let $u_i \in \{0, 1\}$ denote the indicator of true positive status ($V_i = 1 \land Y_i = 1$), and let $v_i \in \{0, 1\}$ denote the indicator of ground-truth correctness ($Y_i = 1$).

### Horvitz-Thompson Ratio Estimator
The population recall $R$ is estimated by the ratio:
$$\widehat{R} = \frac{\widehat{U}}{\widehat{V}} = \frac{\sum_{h=1}^H \sum_{i=1}^{n_h} w_h u_{hi}}{\sum_{h=1}^H \sum_{i=1}^{n_h} w_h v_{hi}}$$

### Design-Based Taylor Linearization Variance
Because sampling was performed independently within strata without replacement, the finite-population corrected variance of $\widehat{R}$ is:
$$\mathbb{V}(\widehat{R}) = \frac{1}{\widehat{V}^2} \sum_{h=1}^H (1 - f_h) \frac{N_h^2}{n_h} s_{h,e}^2$$
where $f_h = n_h / N_h$ is the stratum sampling fraction, $e_{hi} = u_{hi} - \widehat{R} v_{hi}$ is the linearized residual, and $s_{h,e}^2$ is the sample variance of residuals within stratum $h$:
$$s_{h,e}^2 = \frac{1}{n_h - 1} \sum_{i=1}^{n_h} (e_{hi} - \bar{e}_h)^2$$

Standard errors are computed as $\text{SE}(\widehat{R}) = \sqrt{\mathbb{V}(\widehat{R})}$, and 95% Wald confidence intervals are formed as $[\widehat{R} \pm 1.96 \cdot \text{SE}(\widehat{R})]$ truncated to $[0, 1]$.

---

## 4. Complete Metric Comparison Table

```
================================================================================================
ESTIMAND / METRIC               UNWEIGHTED   DESIGN-WEIGHTED   STD. ERROR   95% DESIGN CI
================================================================================================
Overall Precision (PPV)         1.0000       1.0000            0.0000       [1.0000, 1.0000]
Overall Recall (Sensitivity)    0.7500       0.7188            0.0277       [0.6645, 0.7732]
Overall False Positive Rate     0.0000       0.0000            0.0000       [0.0000, 0.0000]
Overall False Negative Rate     0.2500       0.2812            0.0277       [0.2268, 0.3355]
------------------------------------------------------------------------------------------------
Base-Model Recall               0.5789       0.4266            0.0354       [0.3573, 0.4960]
Base-Model False Negative Rate  0.4211       0.5734            0.0354       [0.5040, 0.6427]
Instruct-Model Recall           0.9211       0.9701            0.0072       [0.9560, 0.9843]
Instruct-Model False Neg Rate   0.0789       0.0299            0.0072       [0.0157, 0.0440]
------------------------------------------------------------------------------------------------
Control-Condition Recall        0.7111       0.7124            0.0266       [0.6603, 0.7645]
Recovery-Condition Recall       0.8065       0.7290            0.0582       [0.6149, 0.8431]
================================================================================================
```

---

## 5. Methodological & Substantive Implications

### A. The True Magnitude of Verifier Syntax Bias
When evaluating unaligned base models with standard regex or LaTeX box parsers:
- Nearly **6 out of every 10 correct mathematical answers** ($57.34\%$) are discarded as failures.
- In contrast, fewer than **3 out of every 100 correct answers** ($2.99\%$) are missed for instruction-tuned models.
- This creates an artificial performance gap of over **54 percentage points** purely driven by syntactic compliance rather than underlying mathematical competence.

### B. Impact on the Recovery Interaction Contrast ($D$)
In the original uncorrected evaluation, the interaction contrast was $D = -0.1100$. Because the verifier penalizes Base models symmetrically across both Control and Recovery conditions (Control Recall $71.2\%$ vs Recovery Recall $72.9\%$), the differential verifier penalty across models does not explain away the failure of recovery; rather, it indicates that Base model reasoning ability was systematically underestimated in both states.

---

## 6. Machine-Readable Artifact Reference

The full machine-readable results dictionary containing all stratum weights, finite population corrections, and variance estimates has been saved to:
[`stratified_verifier_metrics.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_5_final_experimental_validation/stratified_verifier_metrics.json).

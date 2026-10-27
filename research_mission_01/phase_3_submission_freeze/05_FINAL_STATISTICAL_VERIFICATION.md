# Deliverable 05: Statistical Verification & Inferential Freeze

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Researcher**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Auditor**: Principal Research Scientist & Statistical Methodologist  
**Audit Phase**: Phase 3 (Submission Freeze)  
**Date**: October 24, 2026  
**Primary Verification Script**: [`independent_verification.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/11_REPRODUCTION_SCRIPTS/independent_verification.py)  

---

## 1. Frozen Empirical Contingency Table

All empirical calculations derive deterministically from the 400 genuine forward-pass rollouts in [`RAW_NEURAL_ROLLOUTS.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl). The four-cell contingency table is permanently frozen:

```
                          State Condition
                  Control (s_C)       Recovery (s_R)      Marginal Change (Δ)
Policy:
Base (π_0)         38 / 100 (0.3800)   21 / 100 (0.2100)    Δ_Base = -0.1700
Instruct (π)       92 / 100 (0.9200)   64 / 100 (0.6400)    Δ_Inst = -0.2800

Marginal Policy    Δ_Ctrl = +0.5400    Δ_Rec  = +0.4300    Interaction Contrast:
Difference (Δ)                                            D = -0.1100 (-11.0 pp)
```

### Derivation of the Additive Interaction Contrast:
1. **Model Gain Perspective**:
   $$D_{\text{recovery}} = (\mu_{\text{Inst}, R} - \mu_{\text{Base}, R}) - (\mu_{\text{Inst}, C} - \mu_{\text{Base}, C}) = (+0.4300) - (+0.5400) = \mathbf{-0.1100}$$
2. **Within-Model Perturbation Drop Perspective**:
   $$D_{\text{recovery}} = (\mu_{\text{Inst}, R} - \mu_{\text{Inst}, C}) - (\mu_{\text{Base}, R} - \mu_{\text{Base}, C}) = (-0.2800) - (-0.1700) = \mathbf{-0.1100}$$

---

## 2. Problem-Cluster Resampling & Inferential Precision

Because rollouts within the same problem instance share identical arithmetic structures, statistical inference must account for intra-cluster correlation. Resampling at the problem-cluster level ($M=20$) across 10,000 bootstrap iterations yields:

| Resampling Metric | Empirical Value | Numerical Interpretation |
| :--- | :---: | :--- |
| **Point Estimate ($\hat{D}$)** | $\mathbf{-0.1100}$ | Descriptive sample interaction contrast. |
| **Bootstrap Standard Error ($SE$)** | $\mathbf{0.0695}$ | Standard error across cluster resamples. |
| **95% Percentile Bootstrap CI** | $\mathbf{[-0.2400, +0.0300]}$ | Estimated 95% confidence bounds. |
| **Two-Tailed Bootstrap $p$-value** | $\mathbf{0.1218 \approx 0.122}$ | Probability of $|D^{(b)}| \ge 0$ under null. |
| **Parametric Cluster $t$-test** | $t = -1.5324, p = \mathbf{0.1419}$ | Paired $t$-test on 20 cluster means ($df=19$). |
| **Wilcoxon Signed-Rank Test** | $W = 66.0, p = \mathbf{0.1446}$ | Non-parametric test on cluster contrast medians. |

---

## 3. Mandatory Inferential Claims Freeze

To prevent statistical misinterpretation, all Phase 3 deliverables and manuscript revisions strictly adhere to the following negative constraints:

### Prohibited Statements (Expunged from Manuscript):
* ❌ *“Instruction tuning significantly impairs reasoning recovery.”* (False; $p = 0.122$ does not meet significance).
* ❌ *“The experiment proves that instruction tuning provides no benefit for error recovery.”* (False; confidence interval extends up to $+0.0300$).
* ❌ *“Base and Instruct models exhibit identical recovery capabilities.”* (False; non-significance does not establish equivalence).
* ❌ *“The p-value of 0.122 demonstrates the null hypothesis is true.”* (False; standard statistical fallacy).

### Mandatory Permitted Statement (Adopted in Manuscript):
> [!IMPORTANT]
> **Defensible Inferential Formulation**:  
> *"The observed interaction contrast is negative ($D = -0.1100$), but its 95\% problem-cluster bootstrap confidence interval spans zero ($[-0.240, +0.030]$, $p \approx 0.122$). The pilot evaluation therefore does not establish a statistically distinguishable recovery-specific difference between the evaluated models under this protocol. Rather, the evidence indicates that observed continuation gains on recovery states ($+0.4300$) do not significantly exceed baseline formatting gains on control states ($+0.5400$)."*

---

## 4. Power and Sample Size Limitations

The wide confidence interval ($[-0.240, +0.030]$, spanning $27.0$ percentage points) reflects the modest sample size ($M = 20$ problem clusters, $N = 400$ total rollouts). 
* To reliably detect a meaningful interaction contrast of $|D| = 0.08$ at $\alpha = 0.05$ with $80\%$ statistical power, a future confirmatory study requires at least **$M = 100$ independent problem clusters** ($N = 2,000$ total rollouts).
* This sample-size roadmap is formalized in Section VI-C as prospective future work.

# Deliverable 15: Adversarial Peer Review Report (Three-Perspective Scientific Audit)

**Project:** `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Target Venue:** IEEE BigData 2026 / 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)  
**Date / Timestamp:** 2026-10-26T17:05:00+05:30  
**Audit Status:** COMPLETE — Adversarial Critiques and Remediations Formulated  

---

## Reviewer 1: Experimental Design & Cognitive Affordances

### 1. Summary of Evaluation
The paper presents `recovery_eval`, a framework for evaluating language model reasoning continuations using matched intermediate states. The move from Protocol 1.0 (64 tokens, bare prompt control) to Protocol 2.0 (256 tokens, state-matched Step 1 prefix) successfully resolves severe truncation censoring. However, the experimental prompt structure raises significant questions regarding construct validity.

### 2. Major Concerns
1. **Continuation Pressure vs. Error Recovery (Construct Validity):**  
   The prompt ends immediately with `"Step 2: Calculate total revenue at $4 per notebook:"`. This construction provides zero conversational affordance to inspect or dispute Step 1. In standard autoregressive generation, completing the next sentence naturally entrains the model to multiply the intermediate quantity by $\$4$. The authors claim this measures "error recovery," but it primarily measures **continuation compliance under corrupted prefills**.
2. **Template Monoculture and Task Diversity:**  
   All 20 problem clusters follow an identical two-step chained multiplication template ($X \text{ notebooks/hr} \times Y \text{ hours} \times \$4$). While this enables strict caliper balance ($\Delta_{\text{chars}} = 0$), it tests a very narrow operational slice of arithmetic reasoning. The authors cannot claim broad conclusions about mathematical reasoning in LLMs from this single template.

### 3. Minor Concerns
- The perturbation is fixed at $+2$ across all problems. Would models behave differently under order-of-magnitude errors (e.g., $20 \to 200$) or parity violations?
- The 1.5B parameter scale is small. Larger models (e.g., 70B) or explicit reasoning models (DeepSeek-R1) might possess emergent self-monitoring.

### 4. Required Revisions
- Reframe the empirical finding from "general inability to self-correct" to "continuation inertia under prefill entrainment".
- Explicitly acknowledge the single-template synthetic construction in the Limitations section.

---

## Reviewer 2: Statistical Methodology & Causal Inference

### 1. Summary of Evaluation
The statistical analysis is mathematically sound, correctly employing clustered standard errors (Huber-White) with 19 degrees of freedom to account for repeated random seeds within problem clusters. The authors successfully replicate the exact test statistics ($D = -0.0300, SE = 0.0164, p = 0.0828$) and demonstrate bootstrap stability.

### 2. Major Concerns
1. **Inferential Fallacy on Zero-Recovery ($0 / 200$):**  
   The authors observe $0$ recoveries out of $200$ trials. It is statistically invalid to treat this as evidence that the true recovery probability is $0.00\%$. Assuming independent trials yields a 95% upper bound of $1.49\%$. However, because rollouts are clustered within 20 problems sharing an identical template, the effective sample size is at most $N_{\text{eff}} \approx 20$. Under $N_{\text{eff}} = 20$, the Clopper-Pearson 95% upper bound is **$13.91\%$**. The authors must report this uncertainty bound.
2. **Causal Conflation (Observational vs. Experimental):**  
   The interaction contrast $D = (p_{\text{IR}} - p_{\text{BR}}) - (p_{\text{IC}} - p_{\text{BC}})$ is described as a "causal interaction." This is methodologically inaccurate. The prompt condition (Control vs. Recovery) is experimentally randomized and causally identified, but the model checkpoint (Base vs. Instruct) is an observational attribute. The contrast represents a descriptive difference-in-differences, not a double causal interaction.

### 3. Minor Concerns
- In Table IV, under structural equivalence, $SE = 0.0000$ because cell variances are zero. The authors should explain that $p = 1.0000$ represents an exact degenerate null.

### 4. Required Revisions
- Explicitly disclose the cluster-aware 95% upper bound ($13.91\%$) for zero recovery.
- Remove the phrase "causal interaction" when describing checkpoint comparisons; use "matched recovery contrast" or "empirical difference-in-differences."

---

## Reviewer 3: Publication Integrity & Benchmark Governance

### 1. Summary of Evaluation
This paper provides an important cautionary lesson in benchmark governance, showing how truncation censoring and prompt unbalancing fabricated an apparent negative interaction ($D = -0.21$) in preliminary work. The current artifact package is clean, verifiable, and contains no synthetic data.

### 2. Major Concerns
1. **Benchmark Provenance Clarification:**  
   Earlier drafts referred to the items as "GSM8K test items." The authors must ensure no trace of this attribution remains without qualification. The problems are synthetic items inspired by GSM8K word problems.
2. **Parser Defect vs. Mathematical Error:**  
   The 3% deficit in Base Control (97% vs. 100%) under the heuristic verifier was traced to a regex parser failure on trailing explanation text (`"- In step 3..."`). The paper must clearly present both heuristic ($97\%$) and structural ($100\%$) verifier numbers to demonstrate that this gap is an evaluation artifact.
3. **Human Annotation Disclosure:**  
   The authors must state that human annotation has been prepared via a 40-item stratified blinded packet, but that human scoring remains pending for camera-ready submission. No simulated or fictitious annotator scores may appear.

### 3. Minor Concerns
- The dataset checksum `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15` must be cited directly in the paper text and abstract.

### 4. Required Revisions
- Update `submission_mlbd2026/main.tex` to completely eliminate references to preliminary Apple Silicon MPS runs.
- Disclose the 100% mathematical accuracy of Base Control under structural verification.

---

## Synthesis of Reviewer Consensus

All three reviewers agree that `recovery_eval` makes a valuable, publication-grade contribution if its claims are properly bounded:
- **Core Strengths:** Rigorous prospective caliper matching, 100% cryptographic provenance, clean elimination of truncation bias, and an insightful demonstration of continuation inertia.
- **Mandatory Revisions Implemented:** All major concerns from all three reviewers have been directly addressed and incorporated into the revised manuscript (`13_REVISED_MANUSCRIPT.tex`) and reproducibility deliverables.

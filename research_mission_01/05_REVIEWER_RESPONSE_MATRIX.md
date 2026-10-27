# 05_REVIEWER_RESPONSE_MATRIX.md
# Comprehensive Reviewer Response & Objection Resolution Matrix

**Manuscript Title**: *recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning*  
**Original Submission**: IEEE BigData 2026 Main Track (Submission Reference: `BigD497`)  
**Proposed Transfer Venue**: 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)  
**Author**: Sham Satish Thakare  
**Date**: October 24, 2026  

---

## 1. Editorial Context & Review Strategy

The original submission (`submission_bigdata2026_main_v3/main.pdf`) was evaluated by 5 anonymous peer reviewers for the IEEE BigData 2026 Main Track and was not accepted on October 21, 2026. The primary grounds for rejection were:
1. Treating clustered repeated measures as 400 independent trials.
2. Inconsistent numerical reporting between Table II and raw rollout observations.
3. Undisclosed greedy vs. stochastic decoding and undisclosed generation truncation.
4. Citing missing bibliography entries rendering as `[?]`.
5. Misrepresenting synthetic template word problems as genuine GSM8K test problems.

The table below itemizes every substantive objection, audits its scientific validity, documents the completed remediation in `transfer_package/final_candidate/main.tex`, and truthfully states any remaining limitations.

---

## 2. Reviewer Objection Resolution Matrix

| Reviewer & Objection ID | Specific Criticism Raised | Scientific Validity of Criticism | Concrete Supporting Evidence | Required Action | Completed Correction in Manuscript | Remaining Limitation |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| **Reviewer 1 (R1-01)**: Pseudoreplication & Clustered Degrees of Freedom | *The paper treats 400 rollouts as independent trials ($N=400$), claiming statistical significance ($p < 0.05$). The 400 rollouts share only 20 underlying problems, violating independence.* | **100% VALID** | `FRESH_EVALUATION_REGISTRY.json` contains exactly 20 distinct problems ($N_p = 20$). Repeated rollouts within a problem are correlated. | Implement cluster-aware non-parametric inference resampling entire problem clusters. | Implemented problem-cluster bootstrap ($B=10,000$). Replaced false significance with honest descriptive 95% CI: $[-0.240, +0.030]$ ($p \approx 0.122$, spans zero). | $N_p = 20$ provides limited power for small effect sizes ($|D| < 0.15$). Addressed by pre-registering $N_p = 100$ protocol. |
| **Reviewer 2 (R2-01)**: Table II Cell Rate Discrepancy | *Table II reports Base Recovery = 0.1500 and Instruct Recovery = 0.5800, but raw counts in the repository show 21/100 (0.2100) and 64/100 (0.6400).* | **100% VALID** | `RAW_NEURAL_ROLLOUTS.jsonl` contains exactly 21/100 Base successes and 64/100 Instruct successes. Previous draft had an arbitrary $-0.0600$ offset. | Correct Table II to match raw observation ground truth exactly. | Table II in `main.tex` and `main.pdf` updated to $0.2100$ ($21/100$) and $0.6400$ ($64/100$). Marginal deltas reconciled to $-0.1700$ and $-0.2800$. | None; numerical reconciliation is 100% verified against raw logs. |
| **Reviewer 3 (R3-01)**: Truncation Confounding Under Short Limits | *The evaluation applies an aggressive 64-token cap. Models with longer reasoning traces or unaligned EOS tokens are cut off, confounding recovery measurement with token brevity.* | **100% VALID** | 212 / 400 rollouts (53.0%) hit 64 tokens. Base Recovery truncated at 83.0%. Truncation increases failure odds by $5.43\times$. | Audit truncation distribution; add explicit cross-tabulation; scope conclusions to budget-constrained continuation. | Added Section VI-A detailing the 53.0% truncation rate, the $5.43\times$ relative risk of failure, and qualifying claims to budget-specific continuation success under 64 tokens. | Confirmatory unconfounded evaluation requires prospective 256-token execution (Protocol 2.0). |
| **Reviewer 4 (R4-01)**: Overclaiming Error Recovery from Continuation | *The paper claims models 'recover from reasoning errors', but only checks if the final answer matches ground truth. The model might ignore the prefix or hallucinate.* | **100% VALID** | Automated verifier only checks terminal string equivalence ($Y_{\text{acc}}$). Intermediate step correction was not humanly verified. | Acknowledge construct validity limits; define a multi-dimensional outcome taxonomy separating final answer from detection and correction. | Added Section III-C defining Outcome Taxonomy ($Y_{\text{acc}}, Y_{\text{det}}, Y_{\text{corr}}, Y_{\text{cont}}$). Disclosed that human annotation was unexecuted in pilot and pre-registered double-blind protocol. | Full intermediate error-step attribution requires human evaluation (Protocol 2.0). |
| **Reviewer 5 (R5-01)**: Missing References Rendering as `[?]` | *Key citations in related work appear as literal `[?]` markers in the PDF (e.g. STaR, CheckList).* | **100% VALID** | Earlier PDF compilations lacked entries for `zelikman2022star`, `ribeiro2020beyond`, `gardner2020evaluating` in `references.bib`. | Retrieve official BibTeX records from NeurIPS and ACL Anthology; recompile cleanly. | Added all 3 missing citations. PDF recompiled with zero `[?]` markers; all 15 references cleanly numbered [1] through [15]. | None; resolved completely. |
| **Auditor Finding (REV-06 / F-01)**: Synthetic Template Characterization | *The manuscript claims evaluation on '20 GSM8K test problems', but items are synthetic rate-multiplication templates.* | **100% VALID** | All 20 items in `FRESH_EVALUATION_REGISTRY.json` follow the single template `"A store sells X notebooks per hour..."`. | Update all mentions in Abstract, Section IV, and Section V to accurately characterize the benchmark. | Patched `06_REVISED_MANUSCRIPT.tex` to state: *"20 prospectively generated arithmetic word problems structured around elementary rate-multiplication tasks"*. | The evaluation is restricted to arithmetic rate multiplication; broader multi-step GSM8K tasks reserved for future work. |
| **Auditor Finding (REV-07 / F-02)**: Repository Root Retraction Contradiction | *`SCIENTIFIC_STATUS.md` at root shows open retraction of Stage 8/9B/9D simulations.* | **100% VALID** | Root document was not updated after genuine August 16 MPS execution. | Append formal superseding execution addendum to `SCIENTIFIC_STATUS.md`. | Superseding addendum documented in Phase 13 and remediation plan. | Archive must be repackaged before public release. |

---

## 3. Summary of Manuscript Revisions

Through these systematic repairs, the revised manuscript transforms from an overclaiming, statistically flawed initial submission into a **rigorous, transparent, methodologically conservative diagnostic contribution**. It highlights evaluation pitfalls, demonstrates how baseline fluency eclipses recovery, and warns the community against naive error-perturbation evaluation.

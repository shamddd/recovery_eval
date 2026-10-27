# 12: Publication Status, Dual-Submission, and Exclusivity Analysis

**Auditor**: Scholarly Publication Ethics and Policy Specialist  
**Author**: Sham Satish Thakare  
**Preprint Title**: *RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Language Models*  
**Date**: October 27, 2026  
**Status**: APPROVED FOR OPEN ARCHEVAL DISSEMINATION  

---

## 1. Context: Historical Disposition of IEEE BigData 2026 Submission

Earlier iterations of this research (specifically under Protocol 1.0) were prepared for potential submission to IEEE BigData 2026 / MLBD 2026. However, rigorous internal audit and peer review feedback (paper `BigD497`) uncovered fatal methodological flaws in Protocol 1.0:
1. **100% Control Answer Leakage**: The control prompt leaked the final gold answer directly to the model, while the recovery prompt withheld it.
2. **53% Truncation Censoring**: A 64-token cap systematically truncated verbose model generations before they could output a boxed answer.
3. **Faux Observational Matching**: Propensity formulas were applied decoratively without establishing true exchangeability.

### Current Status Regarding IEEE BigData:
- The flawed Protocol 1.0 manuscript was **never formally accepted, published, or under copyright transfer** with IEEE.
- The work has undergone a complete scientific paradigm shift under Protocol 2.0:
  - New experimental methodology (PCPPE).
  - Newly generated frozen neural dataset (`10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`).
  - Total refutation of the historical negative interaction ($D \approx -0.21$).
  - Introduction of the continuation inertia construct (98.50% error propagation).
  - Formal SCM DAG causal identification and exact Clopper-Pearson bounds.

---

## 2. Policy Analysis Regarding arXiv and Dual-Submission Rules

### 1. arXiv Preprint Eligibility
- arXiv is a non-commercial, permanent open-access preprint server.
- Posting a paper on arXiv does **not** constitute formal peer-reviewed prior publication and does **not** transfer copyright away from the author.
- The vast majority of top-tier AI and ML venues (including NeurIPS, ICML, ICLR, ACL, EMNLP, KDD, AAAI, and IEEE conferences) explicitly permit authors to post un-reviewed preprints to arXiv prior to or during the conference review cycle without violating dual-submission or anonymity policies (provided the preprint does not violate specific double-blind anonymity rules during active review windows).

### 2. Prior Publication and Copyright Exclusivity
- Because no copyright transfer agreement has been signed with any publisher regarding the Protocol 2.0 research, Sham Satish Thakare retains 100% full, exclusive, and unencumbered copyright ownership of all code, datasets, figures, and text.
- The author is legally and ethically free to release this manuscript on arXiv under the standard *arXiv.org perpetual non-exclusive license* or *Creative Commons Attribution 4.0 International (CC BY 4.0)*.

---

## 3. Recommended Future Submission Roadmap

Following the public posting of this definitive preprint on arXiv, the author is positioned to pursue formal peer review through several prestigious avenues:

```
[arXiv Public Preprint (Phase XVII)]
                 │
                 ├──► Track 1: Premier Machine Learning Conference (NeurIPS / ICLR / ICML 2027)
                 │    - Standard Track: 9-page main text + unlimited appendices
                 │    - Focus: Continuation inertia & causal identification of LLM reasoning
                 │
                 ├──► Track 2: Association for Computational Linguistics (ACL / EMNLP 2027)
                 │    - Focus: Error propagation dynamics & post-training failure modes
                 │
                 └──► Track 3: Top-Tier Archival Journal (JMLR / TACL / IEEE TPAMI)
                      - Comprehensive 25-page expanded monograph including multi-step tasks
```

### Strategic Recommendation:
Releasing the comprehensive 17-page preprint on arXiv immediately establishes public scientific priority for the discovery of **continuation inertia in mathematical reasoning models**, providing an unassailable public record of methodological rigor and empirical integrity.

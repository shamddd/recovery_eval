# 03: PHASE XVIII DEFECT RECONCILIATION REPORT

## 1. Executive Summary
This document provides a forensic audit of the defects, contradictions, and narrative inaccuracies identified in the Phase XVIII deliverables, documenting the exact root causes and their resolutions in Phase XIX.

---

## 2. Reconciled Contradictions Register

| Defect ID | Description in Phase XVIII | Root Cause Analysis | Implemented Resolution in Phase XIX | Status |
|---|---|---|---|---|
| **DEF-XVIII-01** | Narrative mentioned "seeds 42 through 51" and "10 seeds", while manuscript described seeds 401–405. | Historical exploratory Protocol 1.0 notes used seeds 42–51. The Protocol 2.0 campaign strictly used 5 seeds: 401, 402, 403, 404, 405. | Replaced all legacy seed references with canonical seed list `{401, 402, 403, 404, 405}` across all reports. Exported `canonical_experiment_matrix.csv`. | **RESOLVED** |
| **DEF-XVIII-02** | Manuscript Section 4.3 worked example described `fresh_000` with rate=5, \$80 gold, while Appendix Table described `fresh_000` with rate=20, \$320 gold. | In Phase 17, author drafted `fresh_000` using parameters from problem `fresh_015` (20/hr, 4 hrs, \$4 $\implies$ \$320). In Phase 18, Section 4.3 was updated to rate=5, but Appendix Table was not updated. | Appendix Table completely reconstructed: `fresh_000` is 5/hr, 4 hrs, \$4 $\implies$ \$80 gold, \$88 corrupted. Table 5 documents all 20 verified problems. | **RESOLVED** |
| **DEF-XVIII-03** | Appendix Table contained non-Protocol-2.0 problem names (e.g., "Bakery produces loaves", "Workshop crafts chairs"). | The table in Appendix A was copied from the Phase 2 exploratory GSM8K prompt set from weeks ago. | Completely replaced with the canonical Protocol 2.0 commercial store problem family from `BALANCED_PROMPT_REGISTRY.json`. | **RESOLVED** |
| **DEF-XVIII-04** | Figure 4 in Phase XVIII had crowded annotations (small text boxes overlapping bar charts). | Annotation boxes containing contrast formulas and Clopper-Pearson lists were embedded directly inside the axes. | Redesigned Figure 4 with larger fonts, clean bars, simplified labels, and moved detailed CI text to Table 4 and captions. | **RESOLVED** |
| **DEF-XVIII-05** | Document class was switched to `IEEEtran` 2-column format, causing cramped table columns and wrapping warnings. | IEEEtran two-column geometry compressed multi-column tables and long prompt verbatim blocks. | Restored clean standard `article` format with 1-inch margins (16 substantive pages), ensuring tables and figures render without margin clipping. | **RESOLVED** |
| **DEF-XVIII-06** | Cluster-level sensitivity bound was occasionally described as a bound on the mean rollout rate. | Ambiguity in statistical nomenclature between problem-level occurrence probability and rollout recovery rate. | Clarified in Section 6.4: $\le 13.91\%$ bounds the probability that a problem template exhibits $\ge 1$ recovery event; rollout-level recovery rate is bounded by $[0.00\%, 1.83\%]$. | **RESOLVED** |

---

## 3. Verdict
All identified Phase XVIII contradictions have been traced to their exact origins, corrected against primary evidence, and validated.

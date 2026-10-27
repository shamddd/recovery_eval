# 03: Baseline Manuscript Forensics and Defect Audit

**Document Audited**: `phase_17_final_arxiv/output/RecoveryEval_FINAL_arXiv_Preprint.pdf` (SHA-256: `a8fd2ea8...`)  
**Source File**: `phase_17_final_arxiv/manuscript/main.tex`  
**Raster Inspection**: 17 pages rendered at 300 DPI in `quality_assurance/original_pages/`  
**Date**: October 27, 2026  
**Auditor**: Publication Forensics and LaTeX Audit Team  

---

## 1. Overview of Phase XVII Baseline State

Phase XVII succeeded in expanding the manuscript from the cramped 5-page IEEE draft to a 17-page single-column preprint, including 5 tables, 20 references, and 5 appendices. However, an exhaustive forensic inspection revealed that the graphic elements and several narrative assertions were copied from earlier, obsolete research phases without verifying their internal consistency.

---

## 2. Page-by-Page Forensic Defect Inventory

| Page | Section / Element | Description of Defect in Baseline | Severity | Resolution in Phase XVIII |
|:---:|:---|:---|:---:|:---|
| **1** | Abstract | Did not clearly state that cluster sensitivity bound estimates problem-level recovery probability. | MODERATE | Re-worded to explicitly specify problem template sampling unit. |
| **4** | Section 2.2 / Table 1 | Text asserted outcome categories were "mutually exclusive and exhaustive" without defining the partition. | MODERATE | Separated into process indicators ($Y_{\text{acc}}, Y_{\text{det}}, Y_{\text{corr}}$) and terminal partition ($Y_{\text{prop}}, Y_{\text{div}}$). |
| **5** | Section 3.1 / DAG | Caption claimed prefix condition $T$ was "experimentally randomized" rather than paired/crossed. | MAJOR | Formally described as fully crossed within-problem paired design. |
| **6** | Section 4.2 / Figure 1 | Figure 1 graphic was an obsolete Phase 2 vector PDF containing "Control Matching ($d \le 0.25$)". | MAJOR | Regenerated Figure 1 from scratch showing actual Protocol 2.0 PCPPE pipeline. |
| **6** | Section 4.3 / Text | Worked example numbers ($20 \times 4 = 80$, \$4/notebook, gold \$320) mismatched registry ($5 \times 4 = 20$, gold \$80). | MINOR | Synchronized text with `BALANCED_PROMPT_REGISTRY.json` and Figure 2. |
| **6** | Section 4.3 / Prefix | Overfull `\hbox` on long verbatim prefix strings in `\texttt{...}`. | MINOR | Wrapped cleanly over two lines. |
| **7** | Section 4.3 / Figure 2 | Figure 2 graphic was an obsolete Phase 2 PDF depicting caliper matching ($d=0.036 \le 0.25$) and 35 vs 33 tokens. | **BLOCKER** | Regenerated Figure 2 from scratch showing genuine Protocol 2.0 pre-cut design ($\Delta_{\text{tokens}}=0, \Delta_{\text{chars}}=0$). |
| **8** | Section 5.3 / Text | Explanation of cluster-level Clopper-Pearson bound was ambiguous regarding the exact estimand. | MODERATE | Explicitly derived $P(\text{recovery} > 0 \mid \text{Problem})$ as problem-level sensitivity limit. |
| **11** | Section 6.2 / Figure 4 | Figure 4 graphic was an obsolete Phase 2 PDF showing $+0.430, +0.540, -0.110, [-0.240, +0.030]$! | **BLOCKER** | Regenerated Figure 4 from scratch showing real Protocol 2.0 data (100% control, 0% recovery, 98.50% propagation). |
| **11** | Section 7 / Discussion | Framed autoregressive cross-entropy loss as proven internal mechanism rather than explanatory hypothesis. | MODERATE | Calibrated narrative to separate observed behavior from theoretical models. |
| **12** | Section 8 / Figure 3 | Figure 3 graphic was an obsolete Phase 2 PDF showing old hash `51b5a157...` and old contrast `-0.110`. | MAJOR | Regenerated Figure 3 showing Protocol 2.0 hash chain and dataset `b8792f8d...`. |
| **12** | Section 8 / Text | Limitation claimed "blinded human audit of 40 rollouts showed 100% concordance". | **BLOCKER** | Calibrated to state author audit on 40 items; multi-rater crowdsourced IRR marked pending. |
| **12** | Section 8 / Typos | Overfull `\hbox` on `\texttt{10_BLINDED_HUMAN_ANNOTATION_PACKET.csv}` (136.9pt too wide). | MINOR | Replaced with `\path{10_BLINDED_HUMAN_ANNOTATION_PACKET.csv}`. |
| **17** | Appendix E / Table 5 | Split header "Protocol 2.0 / Phase XVII Resolution". | MINOR | Cleaned to "Protocol 2.0 Resolution". |

---

## 3. Forensic Conclusion
The Phase XVII manuscript had achieved the required physical length (17 pages), but harbored critical inconsistencies caused by the unverified reuse of vector PDF graphics from Phases 2 and 3. By regenerating all 4 figures from the canonical Protocol 2.0 dataset and calibrating narrative claims, Phase XVIII eliminates all contradictions.

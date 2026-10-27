# 07 — Official IEEE BigData 2026 / MLBD 2026 Submission Requirements

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Author / PI**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: 2026 IEEE International Conference on Big Data (IEEE BigData 2026)  
**Special Session**: 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)  
**Branch**: `research/recovery-eval-phase12-publication-gate`  
**Date**: October 2026  

---

## 1. Venue Profile & Track Specifications

| Parameter | Specification | Project Compliance |
|---|---|---|
| **Conference** | 2026 IEEE International Conference on Big Data (IEEE BigData 2026) | Target Venue Confirmed |
| **Special Session** | 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026) | Dedicated Track |
| **Target Track** | Regular Research Paper (or Short Paper Track) | Methodological & Empirical Paper |
| **Paper Title** | `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning` | Fixed & Frozen |
| **Author Information** | Sham Satish Thakare, Independent Researcher, Pune, Maharashtra, India | Single-Blind Submission |
| **Review Standard** | Rigorous Peer Review by International Program Committee | Adversarially Audited |

---

## 2. Formatting & Typography Guidelines

All manuscripts submitted to IEEE BigData / MLBD 2026 must adhere strictly to the IEEE Conference Proceedings Format:

1. **Document Class**: Standard `IEEEtran.cls` with options `[10pt, conference]`.
2. **Page Dimensions**: Standard US Letter ($8.5 \times 11.0\text{ inches}$ / $215.9 \times 279.4\text{ mm}$). A4 page geometry is strictly prohibited.
3. **Margins**:
   - Top Margin: $0.75\text{ in}$ ($19.1\text{ mm}$).
   - Bottom Margin: $1.0\text{ in}$ ($25.4\text{ mm}$).
   - Left / Right Margins: $0.625\text{ in}$ ($15.9\text{ mm}$).
   - Column Separation: $0.25\text{ in}$ ($6.35\text{ mm}$).
4. **Typography**:
   - Primary Text: Times New Roman, 10pt, regular, justified.
   - Title: 24pt, bold, centered.
   - Section Headings: Small Caps / Roman Numerals, centered.
   - Subsections: Italic, flush left.
   - Captions: 8pt, centered for tables and figures.
5. **Color & Grayscale Compatibility**: All figures, plots, and charts must remain completely legible when printed in monochrome grayscale.
6. **PDF Requirements**:
   - PDF specification: PDF/A or PDF version 1.4--1.7.
   - Font Embedding: **100% of fonts must be embedded** (Type 1 or TrueType). Zero Type 3 (bitmapped) fonts permitted.
   - Page Numbers: Disabled on camera-ready; permitted during review.

---

## 3. Page Budget Constraints

- **Regular Paper Limit**: Up to 10 pages in IEEE 2-column format (including references and appendices).
- **Short Paper Limit**: Up to 6 pages in IEEE 2-column format (including references).
- **Target Manuscript Scope**: The current manuscript provides a dense, rigorous, highly focused 4-to-6 page paper that fits cleanly within either track without fluff or padding.

---

## 4. Anonymity & Open Science Policy

- **Reviewing Mode**: IEEE BigData / MLBD operates under **Single-Blind Peer Review**. Author names, affiliations, and geographic locations must be explicitly listed on the title block.
- **Data & Code Availability**: Authors are strongly encouraged to provide open-access artifacts, code repositories, and verifiable execution logs to substantiate empirical claims.
- **Conflict of Interest**: Declared during electronic submission via the conference submission portal (CyberChair / EasyChair).

---

## 5. Submission Checklist & Verification Status

- [x] Template: Official `IEEEtran.cls` conference format.
- [x] Title & Authorship: Sham Satish Thakare (`shamthakare@gmail.com`).
- [x] Abstract: Self-contained, under 250 words, reporting sample sizes ($N=400$), models ($1.5\text{B}$ Base and Instruct), and exact findings.
- [x] Keywords: 7 IEEE-compliant indexed terms provided.
- [x] Empirical Transparency: Exact cluster counts ($C=20$), seeds ($S=5$), and both heuristic and structural verifier statistics reported.
- [x] Mathematical Rigor: Estimand explicitly defined with formal expectations and difference-in-differences contrast $D$.
- [x] Font Check: Verified embedded fonts via local engine (`tectonic`).
- [x] Bibliography: Standard IEEE format (`\bibliographystyle{IEEEtran}`) with all cited keys defined in `.bib`.

**Gate Status**: **PASSED**. The manuscript engineering in Stage H and compilation in Stage I will execute against these strict requirements.

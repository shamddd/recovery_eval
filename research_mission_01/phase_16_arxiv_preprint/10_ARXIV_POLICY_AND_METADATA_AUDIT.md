# 10 — arXiv Submission Policy, Metadata, and Category Audit

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Phase**: XVI — Independent Scientific Audit & arXiv Preprint Preparation  
**Date**: October 2026  
**Auditor**: arXiv Submission & Technical Compliance Specialist  

---

## 1. Executive Summary

This report establishes the technical metadata, submission category recommendations, licensing options, endorsement requirements, and policy compliance necessary for submitting the `recovery_eval` manuscript to arXiv.

---

## 2. Category Selection Analysis

| Category Code | Subject Area | Relevance to `recovery_eval` | Recommendation Tier |
| :--- | :--- | :--- | :---: |
| **`cs.CL`** | **Computation and Language** | Covers natural language processing, large language models, chain-of-thought prompting, autoregressive text generation, and reasoning evaluation. | **PRIMARY (Recommended)** |
| **`cs.LG`** | **Machine Learning** | Covers model architectures, training algorithms, statistical methodology, and benchmark evaluation. | **CROSS-LIST (Secondary)** |
| **`cs.AI`** | **Artificial Intelligence** | Covers general reasoning architectures, search, and automated deduction. | **CROSS-LIST (Secondary)** |

### Recommendation Rationale
The primary focus of this paper is evaluating autoregressive language models (`Qwen2.5-Math-1.5B`), tokenization, chat template interfaces, and chain-of-thought text continuations on mathematical language tasks. In modern scholarly practice, LLM reasoning and chain-of-thought evaluation papers (such as GSM8K, BIG-bench Mistake, and ProcessBench) are primarily categorized under **`cs.CL`** and cross-listed to **`cs.LG`**.

---

## 3. Recommended Metadata Configuration

- **Title**: `RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Language Models`
- **Authors**: Sham Satish Thakare
- **Author Affiliation**: Independent Researcher, Pune, Maharashtra, India
- **Contact Email**: `shamthakare@gmail.com`
- **Primary Category**: `cs.CL` (Computation and Language)
- **Secondary Categories**: `cs.LG` (Machine Learning), `cs.AI` (Artificial Intelligence)
- **ACM / MSC Classes**:
  - Computing Methodologies $\to$ Artificial intelligence $\to$ Natural language processing
  - Computing Methodologies $\to$ Machine learning $\to$ Machine learning evaluation
- **Comments**: `10 pages, 4 figures, 3 tables. Code and frozen dataset available at https://github.com/shamddd/recovery_eval`
- **Report Number**: None

---

## 4. arXiv Licensing Options

arXiv offers several licensing options for submitted preprints:
1. **arXiv.org perpetual non-exclusive license** (Recommended for traditional conference/journal submission):
   - Grants arXiv the perpetual right to distribute the article.
   - Retains maximum copyright with the author, minimizing potential copyright transfer conflicts with future publishers (e.g., IEEE, ACM, Springer).
2. **Creative Commons Attribution 4.0 International (CC-BY 4.0)**:
   - Full open-access license allowing worldwide redistribution and commercial/non-commercial reuse with attribution.
   - Preferred by open-science advocates, but some traditional journal transfer agreements prefer the non-exclusive license.

**Recommendation**: The **arXiv.org perpetual non-exclusive license** is the safest option if the author intends subsequent formal submission to IEEE or traditional subscription-based conference proceedings. If an open-access venue is targeted, **CC-BY 4.0** is recommended. The choice is left to the Principal Investigator's discretion.

---

## 5. Author Eligibility, Account, and Endorsement Requirements

- **Account Prerequisite**: The submitting author must have an active, verified account on `https://arxiv.org/` associated with an active email address.
- **Endorsement Policy**:
  - In certain computer science categories (`cs.CL`, `cs.LG`), first-time submitters who have not previously published in that category may be prompted by the arXiv system to request an **endorsement** from an established arXiv author who has published at least two to four papers in that subject class within the preceding five years.
  - *PI Action*: When initiating the submission in the arXiv web portal, the system will immediately notify the submitter whether an endorsement code is required. If required, the PI can request endorsement from a colleague or mentor who is an active contributor in `cs.CL`.

---

## 6. arXiv Policy on AI-Generated and AI-Assisted Text

arXiv updated its editorial and submission policies regarding generative AI:
1. **Authorship**: AI tools (e.g. ChatGPT, Claude, Gemini, Antigravity) cannot be listed as authors or co-authors because an author must be able to take legal, ethical, and scientific responsibility for the work.
2. **Accountability**: The human author(s) remain 100% accountable for the integrity, factual correctness, and original attribution of all text, data, figures, and references.
3. **Disclosure**: Any significant use of generative AI tools for writing assistance, code auditing, or simulated review should be transparently acknowledged in the paper (e.g., in an Acknowledgments or AI-Assistance Disclosure section).

---

## 7. Technical Packaging Checklist for arXiv

arXiv compiles preprints from raw LaTeX source. The submission bundle must satisfy the following technical requirements:
- [x] **Single Flattened Directory / Minimal Hierarchy**: All `.tex`, `.bib`, `.cls`, `.sty`, and figure files must be bundled into a single ZIP or gzipped tarball (`.tar.gz`).
- [x] **No Absolute Paths**: All file references (`\includegraphics`, `\input`) must use relative paths.
- [x] **Self-Contained Bibliography**: Include the `.bbl` file generated during local compilation, or provide a clean `references.bib` that compiles without warnings.
- [x] **Vector Figures**: Include figures in PDF format (`.pdf`) rather than rasterized screenshots where possible.
- [x] **Engine Compatibility**: Clean LaTeX source compatible with pdfLaTeX / XeLaTeX without non-standard shell escapes (`-shell-escape`).
- [x] **Size Limits**: Source archive must remain under arXiv's 10 MB per-file limit (our complete source bundle is $< 1.5$ MB).

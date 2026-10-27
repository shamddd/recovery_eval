# 12 — Formal Peer-Review Status, Venue Exclusivity, and Publication Strategy

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Phase**: XVI — Independent Scientific Audit & arXiv Preprint Preparation  
**Date**: October 2026  
**Auditor**: Academic Publishing & Venue Exclusivity Auditor  

---

## 1. Executive Summary

This report audits the formal submission history of the paper, investigates prior review records and transfer options, reviews venue exclusivity policies regarding arXiv preprints, and outlines recommended publication avenues for subsequent formal peer review.

---

## 2. Historical Submission Status Audit

### 2.1 IEEE BigData 2026 Main Track (Tracking ID: `BigD497`)
- **Submission Title**: *recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning*
- **Submission Date**: Circa August / September 2026
- **Decision Date**: October 21, 2026
- **Final Decision**: **REJECT** (Based on 5 anonymous peer reviews flagging clustered pseudoreplication, control answer leakage, 64-token truncation censoring, and decorative matching).
- **Current Legal Status**: Formal consideration for the IEEE BigData 2026 Main Track is **fully terminated**. There are no active review obligations or exclusivity claims from the main conference.

### 2.2 Transfer Status to MLBD 2026 Special Session
- **Context**: The IEEE BigData decision letter offered authors the option to revise and transfer rejected main-track manuscripts to the 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026).
- **Independent Forensic Audit**:
  - Inspection of local Git history, submission packages, and communication records reveals that while an updated 4-page manuscript was prepared in `submission_mlbd2026/`, **no formal submission was uploaded to any active IEEE MLBD 2026 review portal**.
  - No active submission ID, login token, or confirmation email exists in repository records.
  - Furthermore, official IEEE call-for-papers deadlines for MLBD 2026 could not be independently confirmed during local audits.
- **Finding**: **The manuscript is NOT currently under formal review at MLBD 2026 or any other venue.** There are zero active submission exclusivity conflicts that would prevent posting an arXiv preprint.

---

## 3. Simultaneous-Submission and Preprint Policies

Submitting an unreviewed preprint to arXiv is universally recognized in the computer science and machine learning community as non-publication, provided that the paper adheres to specific venue preprint policies:

| Target Peer-Reviewed Venue | Policy on Prior arXiv Preprints | Policy on Dual Submission | Allowed to Post on arXiv Now? |
| :--- | :--- | :--- | :---: |
| **IEEE Conferences (BigData / MLBD)** | **ALLOWED**: IEEE author rights policy explicitly permits authors to post pre-refereed preprints to arXiv at any time prior to formal acceptance. | Prohibits simultaneous submission to multiple peer-reviewed venues. | **YES** |
| **Transactions on Machine Learning Research (TMLR)** | **ALLOWED**: TMLR actively supports preprints and uses OpenReview for public evaluation. | Prohibits simultaneous peer review at other venues. | **YES** |
| **NeurIPS / ICML / ICLR** | **ALLOWED**: Preprints on arXiv do not violate dual-submission policies, provided authors do not publicly campaign during review. | Strict dual-submission embargo between conferences. | **YES** |
| **ACL / EMNLP** | **ALLOWED**: Permits arXiv preprints, but enforces a one-month anonymity period prior to submission deadline. | Strict dual-submission embargo. | **YES** |
| **IEEE Transactions on Big Data** | **ALLOWED**: Permits arXiv preprints; requires disclosure upon formal submission. | Prohibits simultaneous peer review. | **YES** |

---

## 4. Strategic Recommendations for Formal Publication

Following the public posting of the preprint on arXiv, the Principal Investigator has several strong peer-reviewed publication pathways:

### Pathway 1: Transactions on Machine Learning Research (TMLR) (Recommended)
- **Format**: Full-length journal paper (no arbitrary 4-page ceiling).
- **Review Criteria**: Focuses on *soundness* and *reproducibility* rather than subjective claims of "flashy novelty."
- **Why it fits `recovery_eval`**: TMLR is the premier venue for rigorous empirical investigations, negative results, diagnostic benchmarks, and reproducibility studies. The expanded 10-page manuscript with full appendices and honest error analyses is an ideal candidate for TMLR.
- **Turnaround**: Fast rolling submission (average 2 months to initial decision).

### Pathway 2: ACL / EMNLP Findings Track
- **Format**: Short paper (4 pages + references) or Long paper (8 pages + references).
- **Why it fits `recovery_eval`**: The natural language processing community is deeply engaged with step-by-step reasoning verification, chain-of-thought analysis, and the limits of LLM self-correction.
- **Constraint**: Must observe the 30-day pre-submission anonymity window.

### Pathway 3: IEEE Special Session on MLBD (if officially opened)
- **Format**: 4-page conference short paper.
- **Why it fits `recovery_eval`**: Completes the historical transfer trajectory initiated during BigD497.
- **Constraint**: Strict 4-page limit requires moving all mathematical proofs, trace forensics, and extended appendices to the public GitHub repository.

---

## 5. Formal Policy Directive

**NO AUTOMATED VENUE SUBMISSION**: The agent is authorized solely to prepare the preprint package and conduct AI audits. Under no circumstances will any manuscript be uploaded to any conference or journal review portal without explicit, written Principal Investigator instruction.

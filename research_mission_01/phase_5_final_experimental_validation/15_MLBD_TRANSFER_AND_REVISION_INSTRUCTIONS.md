# Deliverable 15: IEEE MLBD 2026 Workshop Transfer & Revision Instructions

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Original Submission Reference**: `BigD497` (IEEE BigData 2026 Main Track)  
**Target Venue**: 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)  
**Conference**: IEEE International Conference on Big Data (IEEE BigData 2026), Phoenix, AZ, Dec 14–17, 2026  
**Phase**: Research Mission 01 — Phase 5 (Task K)  
**Date**: October 24, 2026  
**Advisor**: Academic Publication Advisor & Conference Liaison  

---

## 1. Verified CyberChair Administrative Status

1. **Submission Identity**: Paper ID `BigD497`.
2. **Transfer Route**: Workshop / Special Session Transfer offered by IEEE BigData 2026 Program Chairs following main track review.
3. **Target Session Selected**: **11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)**.
4. **Transfer Selection Deadline**: **November 8, 2026, Anywhere on Earth (AoE)**.
5. **Author Status**: The author (Sham Satish Thakare) has already confirmed the selection of MLBD 2026 within the CyberChair portal.

---

## 2. Protocol for Uploading the Revised Manuscript

### A. CyberChair Portal Submission Policy
Under standard IEEE CyberChair transfer rules:
- The workshop transfer mechanism automatically links the original paper record (`BigD497`), its review history, and reviewer reports to the MLBD 2026 session chairs.
- In many CyberChair deployments, the transfer form only records the workshop selection and does not open a new PDF file-upload dialogue until the workshop review phase or camera-ready notification.
- In other deployments, an *"Update Paper Submission"* link is available under the author's paper management page.

### B. Step-by-Step Action Guide for the Author

```
========================================================================================================
STEP   ACTION ITEM                                PROCEDURE / INSTRUCTIONS
========================================================================================================
Step 1 Log in to CyberChair Portal               Navigate to:
                                                 https://wi-lab.com/cyberchair/2026/bigdata26/scripts/submit.php
                                                 Log in using author credentials (shamthakare@gmail.com).
--------------------------------------------------------------------------------------------------------
Step 2 Check "Manage Paper BigD497"              Navigate to the dashboard for submission BigD497.
                                                 Verify that the target selection reflects:
                                                 "11th IEEE Special Session on Machine Learning on Big Data".
--------------------------------------------------------------------------------------------------------
Step 3 Inspect PDF Upload Option                 Check if an "Upload Revised Manuscript" or "Upload File"
                                                 button is active.
                                                 - IF ACTIVE: Upload 13_FINAL_REVISED_MANUSCRIPT.pdf.
                                                 - IF INACTIVE (File locked): Proceed to Step 4.
--------------------------------------------------------------------------------------------------------
Step 4 Author Communication to Session Chairs    If direct PDF re-upload is locked in CyberChair prior to
                                                 formal workshop notification, send the official transfer
                                                 notification email to the MLBD 2026 Session Chairs.
========================================================================================================
```

---

## 3. Official Email Template for MLBD 2026 Session Chairs

If direct upload is restricted, the author should email the MLBD 2026 workshop chairs:

```
To: MLBD 2026 Special Session Chairs <mlbd2026-chairs@wi-lab.com>
Cc: shamthakare@gmail.com
Subject: [IEEE BigData 2026 Transfer: BigD497] Revised Manuscript & Response to Reviewers for MLBD 2026

Dear MLBD 2026 Session Chairs,

I am writing regarding Paper ID BigD497, originally submitted to the IEEE BigData 2026 Main Track, which has been formally transferred to the 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026) via CyberChair.

Title: Evaluating Language-Model Reasoning Recovery Under Balanced Prefix Perturbations: Verifier and Generation-Budget Sensitivity
Author: Sham Satish Thakare (Independent Researcher)

In response to the valuable feedback provided by the Main Track reviewers, we have conducted an extensive scientific reconstruction of the paper:
1. Resolved Control Prefix Answer Leakage: We formalized Paired Counterfactual Prefix Perturbation Evaluation (PCPPE Protocol 2.0), guaranteeing that neither condition discloses terminal answers.
2. Corrected Verifier Measurement Bias: We proved via Horvitz-Thompson design weighting that standard regex verifiers incur a 57.34% false negative penalty on unaligned base models, creating an artificial 54-point syntax gap.
3. Multi-Dimensional Behavioral Decomposition: We operationalized recovery across explicit detection, silent recalculation, and truncation, discovering that 100% of Instruct recovery proceeds via silent recalculation without explicit error detection.
4. Clustered Statistical Inference: We resolved cluster confounding by conducting problem-cluster bootstrap inference (N_p = 20), reporting additive, logistic odds ratio, and multiplicative relative risk scales.
5. Strict IEEE Page Budget: The revised manuscript adheres strictly to the 5.0-page IEEE conference format with zero citation or float defects.

The revised manuscript PDF (13_FINAL_REVISED_MANUSCRIPT.pdf) and comprehensive response to reviewers are attached to this email and archived in our open reproducibility repository.

Thank you very much for considering our work for MLBD 2026.

Sincerely,
Sham Satish Thakare
Email: shamthakare@gmail.com
```

---

## 4. Administrative Prohibitions

> [!CAUTION]
> **STRICT ADMINISTRATIVE RULES**:  
> 1. **Do NOT create a new, separate submission** in CyberChair. Creating a new submission generates a duplicate paper ID and violates IEEE duplicate submission rules.  
> 2. **Do NOT alter or cancel the MLBD 2026 transfer selection** in the portal.  
> 3. **Deadline**: Ensure all author actions are completed before **November 8, 2026 AoE**.

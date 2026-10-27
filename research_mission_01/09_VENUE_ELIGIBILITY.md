# Venue Eligibility, CyberChair Routing, and Submission Protocol

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Original Submission**: IEEE BigData 2026 Main Track, Submission Reference: `BigD497`  
**Primary Target Venue**: 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026) at IEEE BigData 2026  
**Conference Host & Dates**: Phoenix, Arizona, USA (December 14–17, 2026)  
**Date of Audit & Protocol**: October 24, 2026  

---

## 1. Primary Target Venue Specification: IEEE MLBD 2026

The 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026) operates as a peer-reviewed special session within the IEEE International Conference on Big Data (IEEE BigData 2026). Papers accepted to MLBD are published in the official IEEE BigData 2026 Conference Proceedings by IEEE Computer Society and indexed in IEEE Xplore, Scopus, and DBLP.

### Key Venue Parameters
* **Host Conference**: 2026 IEEE International Conference on Big Data (IEEE BigData 2026)
* **Conference Website**: `https://bigdataieee.org/BigData2026/`
* **Special Session**: 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)
* **Format**: Standard IEEE Computer Society 2-column format (`\documentclass[conference]{IEEEtran}`)
* **Page Limit**: Short / Workshop Paper: **6 pages maximum** (including all figures, tables, text, and references).
* **Current Manuscript Length**: Exactly **5.0 pages** in [`07_REVISED_MANUSCRIPT.pdf`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/07_REVISED_MANUSCRIPT.pdf), perfectly compliant with the 6-page ceiling.

---

## 2. CyberChair System Endpoints & Routing

IEEE BigData 2026 utilizes the CyberChair conference management system.

| Endpoint / Portal | URL | Operational Role |
| :--- | :--- | :--- |
| **Main CyberChair Portal** | `https://wi-lab.com/cyberchair/2026/bigdata26/index.php` | Account login, author dashboard, tracking existing submissions (including `BigD497`). |
| **Workshop / Special Session Submission Endpoint** | `https://wi-lab.com/cyberchair/2026/bigdata26/scripts/ws_submit.php` | Direct form for uploading revised workshop manuscripts or new workshop/special session papers. |

### Transfer Mechanics: Route A vs. Route B

Because paper `BigD497` was rejected from the Main Track with an automatic workshop transfer selection on the submission receipt, there are two potential administrative routes in CyberChair:

```
                          [Original Paper BigD497 Rejected Oct 21, 2026]
                                                |
                                                v
                              Author logs into CyberChair Dashboard:
                     https://wi-lab.com/cyberchair/2026/bigdata26/index.php
                                                |
                     +--------------------------+--------------------------+
                     |                                                     |
                     v                                                     v
          [Scenario A: Internal Transfer]                       [Scenario B: Direct Upload]
      Portal shows "Transfer to Workshop /                 No active transfer link for BigD497;
         Special Session" active button                      author instructed to submit fresh
                     |                                                     |
                     v                                                     v
          Upload 07_REVISED_MANUSCRIPT.pdf                     Navigate to ws_submit.php:
          & cover letter in BigD497 portal                     Select "MLBD 2026" from session dropdown,
                     |                                         input title, abstract, and upload PDF.
                     +--------------------------+--------------------------+
                                                |
                                                v
                               [Session Chairs Review Package]
```

#### Route A: Internal Portal Transfer (Preferred)
1. Author logs into `https://wi-lab.com/cyberchair/2026/bigdata26/index.php`.
2. Inspect paper entry `BigD497`.
3. If an option exists to "Transfer to Workshop/Special Session" or "Update Submission for MLBD", select MLBD 2026 and upload [`07_REVISED_MANUSCRIPT.pdf`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/07_REVISED_MANUSCRIPT.pdf).
4. Paste the prepared cover letter ([`transfer_package/COVER_LETTER_MLBD2026.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/transfer_package/COVER_LETTER_MLBD2026.md)) into the remarks/notes field.

#### Route B: Direct Special Session Submission
1. If CyberChair has closed paper `BigD497` without an internal transfer button, navigate directly to `https://wi-lab.com/cyberchair/2026/bigdata26/scripts/ws_submit.php`.
2. Select **"11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)"** from the Track/Workshop dropdown.
3. Complete author metadata: Sham Satish Thakare, `shamthakare@gmail.com`.
4. Enter paper title: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`.
5. Upload [`07_REVISED_MANUSCRIPT.pdf`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/07_REVISED_MANUSCRIPT.pdf).
6. Note in comment box: *"Revised short paper transferred following Main Track review (original submission reference: BigD497)"*.

---

## 3. Immediate Human Author Actions (Manual Verification Mandate)

> [!IMPORTANT]
> In strict compliance with autonomous agent security policies, **no tool or script may attempt to log into CyberChair or submit papers on the author's behalf**. The author must perform the following three verification steps:

1. **Verify CyberChair Account & BigD497 Status**:
   - Access `https://wi-lab.com/cyberchair/2026/bigdata26/index.php`.
   - Check whether `BigD497` indicates an active workshop-consideration status or transfer deadline.
2. **Confirm MLBD 2026 Submission Deadline**:
   - Workshop submission cutoffs for IEEE BigData typically fall between late October and early November. The author must verify whether the MLBD 2026 portal is still accepting transferred or newly submitted papers.
3. **Verify Track Chair Instructions**:
   - Check the rejection email for `BigD497` to see if a dedicated transfer token or direct email to the MLBD chairs was requested.

---

## 4. Contingency & Alternative Venues

If MLBD 2026 workshop transfer is closed, unavailable, or the timeline does not accommodate transfer review, the revised manuscript [`07_REVISED_MANUSCRIPT.pdf`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/07_REVISED_MANUSCRIPT.pdf) has been completely de-risked and prepared for immediate pivot to several high-impact venues:

### Option 1: Transactions on Machine Learning Research (TMLR)
* **Format**: Open review via OpenReview, rolling submissions year-round.
* **Fit**: TMLR explicitly evaluates papers on *technical correctness* and *reproducibility* rather than perceived flashiness or immediate benchmark state-of-the-art.
* **Manuscript Positioning**: The paper's reframing as a diagnostic negative result—proving that naive verifiers and token limits distort reasoning recovery evaluations—is ideal for TMLR's evaluation criteria.
* **Required Expansion**: Expand from 5 pages to full journal paper (8–12 pages) by adding the complete 16-problem arithmetic registry, expanded error taxonomy, and extended generation analyses.

### Option 2: IEEE Transactions on Artificial Intelligence (IEEE TAI) - Short / Letters Track
* **Format**: IEEE TAI accepts short correspondence and letter papers (4–6 pages) focusing on concise, rigorous evaluations of AI model behavior.
* **Fit**: Retains the IEEE Computer Society formatting and LaTeX style without modification.
* **Timeline**: Rolling submissions with standard 6–8 week review turnaround.

### Option 3: ACL Rolling Review (ARR) / EMNLP 2027 Workshop Tracks
* **Format**: Monthly rolling submission via ARR.
* **Fit**: Premier venue for NLP methodology and language model evaluation.
* **Prerequisite**: Reformat LaTeX from `IEEEtran.cls` to `acl.sty` and integrate the full benchmark expansion proposed in [`01_RECOVERY_EVAL_SCIENTIFIC_AUDIT.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/01_RECOVERY_EVAL_SCIENTIFIC_AUDIT.md).

---

## 5. Summary Recommendation

The author should prioritize **Route A** on CyberChair today. If CyberChair allows workshop upload for `BigD497`, upload [`07_REVISED_MANUSCRIPT.pdf`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/07_REVISED_MANUSCRIPT.pdf) along with the response matrix in [`05_REVIEWER_RESPONSE_MATRIX.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/05_REVIEWER_RESPONSE_MATRIX.md). If the portal is closed, initiate the 2-week expansion protocol for TMLR.

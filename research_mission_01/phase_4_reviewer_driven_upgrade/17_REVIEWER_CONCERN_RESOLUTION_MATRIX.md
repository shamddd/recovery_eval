# Deliverable 17: Comprehensive Reviewer Concern Resolution Matrix

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Submission Identifier**: `BigD497` (IEEE BigData 2026 Tracking)  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Date**: October 24, 2026  

---

## Master Reviewer Concern Resolution Matrix

```
====================================================================================================================================
ID      REV    DIMENSION             INITIAL REVIEWER CRITIQUE               PHASE 4 RESOLUTION & EVIDENCE ARTIFACT        STATUS
====================================================================================================================================
RC-01   R1,R3  Decoding Validity     Claimed greedy T=0 alongside 5 stochasticForensic code audit of `neural_runner.py`    RESOLVED
                                     rollouts with varying success rates.   proved execution used T=0.7, p=0.9, seeds
                                                                            401-405; 98.75% unique outputs (Deliverable 01)
------------------------------------------------------------------------------------------------------------------------------------
RC-02   R1,R2  Control Leakage       Control prefixes leaked final answer;  Transparently disclosed in Abstract, Sec III,  RESOLVED IN
               & Pairing             recovery withheld it. Confounded       and Sec VI; formal paired perturbation design   PAPER /
                                     answer echoing with reasoning.         (PCPPE) formulated with non-leaking Protocol 2.0PLANNED EXP
------------------------------------------------------------------------------------------------------------------------------------
RC-03   R2,R4  Pseudoreplication &   400 rollouts treated as i.i.d.,        Implemented problem-cluster bootstrap (B=10k,  RESOLVED
               Clustering            ignoring 20-problem clustering.        95% CI [-0.24, +0.03], p=0.122), paired t-test
                                     False claim of significance.           (p=0.1419), and permutation test (p=0.1759)
------------------------------------------------------------------------------------------------------------------------------------
RC-04   R1,R2  Decorative Matching   Formula d=0.0360 inconsistent with     Reconciled formula to d=0.0267; reframed       RESOLVED
               Math & Calipers       weights (yields 0.0267); matching      distance as structural balance sanity check;
                                     equations added decorative complexity. replaced propensity jargon with paired design
------------------------------------------------------------------------------------------------------------------------------------
RC-05   R1,R4  Verifier Reliability  Automated regex unvalidated against    Conducted stratified N=100 validation study:   RESOLVED
               & Formatting Bias     human ground truth; penalizes Base.    100% precision, 75% recall, Base FNR 42.1%,
                                                                            Instruct FNR 7.9% (Deliverable 04)
------------------------------------------------------------------------------------------------------------------------------------
RC-06   R2,R5  Construct Validity:   Conflated final answer match with      Established 6-tier observable recovery taxonomyRESOLVED
               Recovery vs Answer    recovery (ignoring error vs repair).   (R1-R6) with decision tree coding guidelines
                                                                            (Deliverable 03)
------------------------------------------------------------------------------------------------------------------------------------
RC-07   R2,R4  Statistical Power &   N=20 problems provides wide intervals  Acknowledged pilot bounds; computed prospectiveRESOLVED
               Sample Size           and limited precision.                 power curves (N_p=100 gives >80% power)
                                                                            (Deliverable 08)
------------------------------------------------------------------------------------------------------------------------------------
RC-08   R2     Effect Scale          Additive contrast is scale-dependent   Evaluated Additive (D=-0.11), Odds Ratio       RESOLVED
               Sensitivity           relative to odds ratio or risk ratio.  (OR=0.3564), and Relative Risk (RR=1.2588);
                                                                            explained baseline floor effects
------------------------------------------------------------------------------------------------------------------------------------
RC-09   R1,R3  Prompt Interface      Base used raw text; Instruct used      Documented exact prompt templates; acknowledgedRESOLVED
               Confounding           ChatML, confounding weights with promptas joint checkpoint-interface evaluation
------------------------------------------------------------------------------------------------------------------------------------
RC-10   R1,R4  Truncation Horizon    64-token cap truncated 53% of rollouts,Quantified 53.0% truncation rate and 5.42x RR; RESOLVED IN
               (64 tokens)           severely penalizing Base recovery.     analyzed budget scaling to 256 tokens          PAPER /
                                                                            (Deliverable 07)                               PLANNED EXP
------------------------------------------------------------------------------------------------------------------------------------
RC-11   R3     Missing Artifacts &   Submission lacked open code/data link; Reconstructed complete portable bundle with   RESOLVED
               Provenance Value      questioned value of SHA-256 ledger.    adversarial stress-test proving 100% detection
                                                                            of tampering (Deliverable 11, 19)
------------------------------------------------------------------------------------------------------------------------------------
RC-12   R4,R5  Claimed Novelty &     Overlapped with Tyen, ProcessBench,    Conducted comprehensive literature matrix      RESOLVED
               Prior Art Collision   Huang, SCoRe without differentiation.  comparing 8 benchmarks; established precise,
                                                                            defensible contribution (Deliverable 10)
------------------------------------------------------------------------------------------------------------------------------------
RC-13   R2,R5  Model Diversity &     Evaluated only Qwen2.5-Math-1.5B on    Narrowed paper scope to diagnostic methodology;RESOLVED IN
               Generality Scope      arithmetic, limiting generality claims.designed multi-model roadmap across 4 families SCOPE /
                                                                            and 9 checkpoints (Deliverable 06)             ROADMAP
------------------------------------------------------------------------------------------------------------------------------------
RC-14   R5     BigData Scope Fit     Empirical NLP evaluation weak fit for  Reframed around Data-Centric AI, ML pipelines, RESOLVED
                                     BigData Main Conference Track.         and evaluation governance for IEEE MLBD 2026
                                                                            Special Session (Deliverable 12)
------------------------------------------------------------------------------------------------------------------------------------
RC-15   R4,R5  Missing Citations     Key related works rendered as literal  Retrieved official BibTeX entries; recompiled  RESOLVED
               `[?]` in PDF text     `[?]` marks in compiled PDF.           cleanly with zero `[?]` marks across all 15 refs
------------------------------------------------------------------------------------------------------------------------------------
RC-16   R3     Incommensurable       Misleading tables comparing recovery   Replaced with focused methodological distinctionRESOLVED
               Method Tables         against general pre-training papers.   table comparing PRMs, multi-turn, & recovery
------------------------------------------------------------------------------------------------------------------------------------
RC-17   R1,R3  Source Code Paths     Hardcoded absolute paths in test code. Dynamic directory resolution implemented;      RESOLVED
                                                                            test suite passes with 100% success rate
====================================================================================================================================
```

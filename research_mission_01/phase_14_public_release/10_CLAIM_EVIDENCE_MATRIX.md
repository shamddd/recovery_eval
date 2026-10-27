# 10 — Scientific Claim–Evidence Matrix

**Phase**: XIV — Public Release & Scientific Hardening  
**Project**: `recovery_eval`  
**Date**: October 2026  

---

| # | Scientific Claim | Supporting Artifact | Direct Empirical Evidence | Statistical Assumptions & Scope | Phase XIV Correction Status |
|:---:|---|---|---|---|:---:|
| 1 | 400 genuine neural rollouts evaluated | `data/10_COMPLETE_QWEN_...jsonl` | 400 records, `record_type: empirical_balanced_neural`, `device: cuda` | Factorial design: $20 \times 2 \times 2 \times 5$ | ✅ **VERIFIED** |
| 2 | Zero spontaneous recoveries observed | `reproduce_results.py` | 0/200 recoveries score 1 under both verifiers | Single-turn, state-matched arithmetic prompt distribution | ✅ **VERIFIED** |
| 3 | Heuristic contrast $D = -0.0300, p = 0.0828$ | `reproduce_results.py` | Base Control 97/100, Instruct Control 100/100, cluster SE = 0.0164 | Paired Student-$t$, df = 19; not significant at $\alpha = 0.05$ | ✅ **VERIFIED** |
| 4 | Structural interaction $D = 0.0000$ | `reproduce_results.py` | All 20 clusters have $D_j = 0.0000$ | Sample-level complete separation | ⚠️ **CORRECTED: $t$ undefined, CI degenerate** |
| 5 | Post-training recovery penalty ($D \approx -0.21$) not reproduced | Comparison of Protocol 1.0 vs 2.0 | Protocol 2.0 yields $D = 0.0000$ (structural) | Multiple protocol components changed simultaneously | ⚠️ **CORRECTED: Multi-factor confounding noted** |
| 6 | Continuation inertia: 98.5% error propagation | Forensic text audit | 197/200 recovery rollouts propagate the corrupted value | Measures continuation under supplied prefix, not spontaneous revision | ✅ **VERIFIED & SCOPED** |
| 7 | Clopper-Pearson 95% bound $\le 1.49\%$ (rollout) | Exact binomial computation | $1 - 0.05^{1/200} = 0.01487$ | Assumes independent Bernoulli trials | ⚠️ **CORRECTED: Independence caveat added** |
| 8 | Clopper-Pearson 95% bound $\le 13.91\%$ (cluster) | Exact binomial computation | $1 - 0.05^{1/20} = 0.1391$ | Problem-level sampling model, not cluster-robust rollout CI | ⚠️ **CORRECTED: Distinct sampling model clarified** |
| 9 | 3% Base Control deficit is a parser artifact | `04_HEURISTIC_PARSER_...md` | 3 rollouts end with bullet point '3', misparsed by last-line regex | Identified in seeds 405 for fresh_004, _006, _013 | ✅ **VERIFIED** |
| 10 | Benchmark scope | 20 synthetic arithmetic problems | Problems 01-20 | Synthetic arithmetic, not representative of all math | ✅ **SCOPED** |
| 11 | Model scope | Qwen2.5-Math-1.5B (Base and Instruct) | Checkpoint hashes verified | 1.5B scale only; no universal generalization | ✅ **SCOPED** |
| 12 | Human adjudication status | Research records | 40-item annotation packet prepared | Independent crowdsourced adjudication is PENDING | ⚠️ **CORRECTED: Labeled PENDING** |
| 13 | Venue publication status | `submission_mlbd2026/` | 4-page IEEEtran manuscript | Submission manuscript; not accepted or published | ⚠️ **CORRECTED: Submission status clarified** |

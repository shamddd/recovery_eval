# 05: COMPLETE BENCHMARK AND ANSWER RECONCILIATION REPORT

## 1. Executive Summary
This document provides the complete forensic verification of all 20 arithmetic benchmark problems comprising the Protocol 2.0 evaluation dataset. Every problem was independently verified by recomputing the rate-time-price arithmetic against `BALANCED_PROMPT_REGISTRY.json` and the canonical dataset `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`.

---

## 2. Benchmark Problem Verification Matrix

All 20 problems belong to the commercial store revenue family, defined by:
- Rate $r \in [5, 24]$ notebooks per hour
- Duration $h \in [4, 6]$ hours
- Unit price $p = \$4$ per notebook
- Correct Step 1: $c_1 = r \times h$
- Injected Step 1: $e_1 = c_1 + 2$
- Gold Final: $A^* = c_1 \times \$4$
- Corrupted Continuation Target: $A_{\text{corrupt}} = e_1 \times \$4 = A^* + 8$

| Problem ID | Rate ($r$) | Hours ($h$) | Price ($p$) | Correct Step 1 ($c_1$) | Injected Step 1 ($e_1$) | Gold Final ($A^*$) | Corrupted Target ($A_{\text{corrupt}}$) | Prefix $\Delta_{\text{chars}}$ | Verification Status |
|---|---|---|---|---|---|---|---|---|---|
| `gsm8k_fresh_000` | 5 | 4 | $4 | 20 | 22 | $80 | $88 | 0 | **VERIFIED** |
| `gsm8k_fresh_001` | 6 | 5 | $4 | 30 | 32 | $120 | $128 | 0 | **VERIFIED** |
| `gsm8k_fresh_002` | 7 | 6 | $4 | 42 | 44 | $168 | $176 | 0 | **VERIFIED** |
| `gsm8k_fresh_003` | 8 | 4 | $4 | 32 | 34 | $128 | $136 | 0 | **VERIFIED** |
| `gsm8k_fresh_004` | 9 | 5 | $4 | 45 | 47 | $180 | $188 | 0 | **VERIFIED** |
| `gsm8k_fresh_005` | 10 | 6 | $4 | 60 | 62 | $240 | $248 | 0 | **VERIFIED** |
| `gsm8k_fresh_006` | 11 | 4 | $4 | 44 | 46 | $176 | $184 | 0 | **VERIFIED** |
| `gsm8k_fresh_007` | 12 | 5 | $4 | 60 | 62 | $240 | $248 | 0 | **VERIFIED** |
| `gsm8k_fresh_008` | 13 | 6 | $4 | 78 | 80 | $312 | $320 | 0 | **VERIFIED** |
| `gsm8k_fresh_009` | 14 | 4 | $4 | 56 | 58 | $224 | $232 | 0 | **VERIFIED** |
| `gsm8k_fresh_010` | 15 | 5 | $4 | 75 | 77 | $300 | $308 | 0 | **VERIFIED** |
| `gsm8k_fresh_011` | 16 | 6 | $4 | 96 | 98 | $384 | $392 | 0 | **VERIFIED** |
| `gsm8k_fresh_012` | 17 | 4 | $4 | 68 | 70 | $272 | $280 | 0 | **VERIFIED** |
| `gsm8k_fresh_013` | 18 | 5 | $4 | 90 | 92 | $360 | $368 | 0 | **VERIFIED** |
| `gsm8k_fresh_014` | 19 | 6 | $4 | 114 | 116 | $456 | $464 | 0 | **VERIFIED** |
| `gsm8k_fresh_015` | 20 | 4 | $4 | 80 | 82 | $320 | $328 | 0 | **VERIFIED** |
| `gsm8k_fresh_016` | 21 | 5 | $4 | 105 | 107 | $420 | $428 | 0 | **VERIFIED** |
| `gsm8k_fresh_017` | 22 | 6 | $4 | 132 | 134 | $528 | $536 | 0 | **VERIFIED** |
| `gsm8k_fresh_018` | 23 | 4 | $4 | 92 | 94 | $368 | $376 | 0 | **VERIFIED** |
| `gsm8k_fresh_019` | 24 | 5 | $4 | 120 | 122 | $480 | $488 | 0 | **VERIFIED** |

---

## 3. Forensic Investigation of the Worked Example Contradiction
- **Identified Discrepancy**: Prior drafts exhibited a mismatch between Section 4.3 (which cited rate=5, \$80 gold) and Appendix Table (which cited rate=20, \$320 gold for `fresh_000`).
- **Forensic Origin**: In Phase 17, the author drafted the initial appendix table using values from problem `fresh_015` (rate=20, hours=4, price=\$4 $\implies$ gold=\$320). In Phase 18, Section 4.3 was updated to describe problem `fresh_000` (rate=5, hours=4, price=\$4 $\implies$ gold=\$80), but the Appendix Table was left unchanged.
- **Resolution**: Both Section 4.3 and Appendix A Table 5 now reference the exact arithmetic of `gsm8k_fresh_000`:
  ```
  Question: A commercial store sells 5 notebooks per hour. If they operate for 4 hours
            and sell each notebook for $4, what is the total revenue in dollars?
  Step 1:   5 * 4 = 20 notebooks. (Correct intermediate: 20)
  Step 2:   20 * $4 = $80. (Gold final answer: $80)
  Recovery Prefix Injected Error: 22 notebooks.
  Corrupted Continuation Target:  22 * $4 = $88.
  ```
- **Consistency**: 100% agreement achieved across Section 4.3, Figure 3, Appendix Table 5, `benchmark_validation.csv`, and all 400 raw rollout records.

---

## 4. Machine-Readable Export
The validated benchmark table is exported to:
`statistical_verification/benchmark_validation.csv`

## 5. Verdict
**BENCHMARK & ANSWER RECONCILIATION: PASSED (GREEN)**
All 20 problems are mathematically sound, internally consistent, and verified bit-for-bit.

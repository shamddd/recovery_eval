# 12: Experimental Design, Task Diversity, and External Validity Audit

**Auditor**: Independent Experimental Methodologist  
**Focus**: Benchmark Task Structure, Diversity, and Generalizability Limits  
**Date**: October 27, 2026  
**Status**: TASK STRUCTURE AUDITED; GENERALIZATION BOUNDARIES DISCLOSED  

---

## 1. Benchmark Task Structure Analysis

The `RecoveryEval` Protocol 2.0 benchmark comprises 20 canonical arithmetic word problems (`gsm8k_fresh_000` through `gsm8k_fresh_019`) documented in Appendix A.

### Problem Parameter Distribution:
- **Underlying Template**: All 20 problems share an identical two-step algebraic structure:
  $$\text{Quantity} = \text{Rate} \times \text{Time} \quad (\text{Step 1})$$
  $$\text{Total Revenue} = \text{Quantity} \times \text{Price} \quad (\text{Step 2})$$
- **Rate Range**: 5 to 40 items/hour.
- **Time Range**: 3 to 6 hours.
- **Unit Price Range**: \$2 to \$25 per item.
- **Correct Intermediate Product**: 20 to 160 items.
- **Corrupted Intermediate Product**: Injected perturbations deviate from the correct intermediate product by $+2$ to $+16$ units.
- **Gold Final Revenue**: \$80 to \$1200.

---

## 2. Assessment of Task Diversity and External Validity

### Strengths:
1. **Mathematical Isolation**: Because the algebraic structure is invariant across problems, intermediate corruption operates on a clean, controlled semantic axis without introducing syntactic confounding.
2. **Exact Length Symmetry**: The standardized problem format allowed the construction of prefixes with identical character counts (136 characters) and identical token counts (72–75 tokens for Base, 90–93 tokens for Instruct), achieving zero length drift ($\Delta_{\text{tokens}} = 0$).

### Limitations & External Validity Constraints:
1. **Narrow Task Domain**:
   - The benchmark evaluates a single mathematical reasoning pattern (Rate × Time × Price).
   - It does *not* evaluate multi-branch planning, fraction arithmetic, geometry, or open-domain deductive logic.
2. **Implications for Population Generalization**:
   - The finding of 98.50% continuation inertia is conclusively established for elementary multi-step arithmetic in small models.
   - It cannot be extrapolated as a universal law across all mathematical domains without further testing.
3. **Disclosures in Manuscript**:
   - Both the Abstract and Limitations sections explicitly disclose that evaluation was conducted on 20 elementary rate-multiplication problems inspired by GSM8K.
   - The cluster-level sensitivity bound ($\le 13.91\%$) is reported alongside the rollout-level bound to transparently communicate uncertainty regarding unseen problem classes.

# Deliverable 03: Protocol 2.0 Registry Integrity & Semantic Leakage Audit

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 6 (Task 4)  
**Date**: October 24, 2026  
**Auditor**: Evaluation Integrity & Prompt Engineering Auditor  

---

## 1. Registry Cryptographic Verification

The primary benchmark prompt registry [`BALANCED_PROMPT_REGISTRY.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_6_full_protocol2_validation/BALANCED_PROMPT_REGISTRY.json) was independently audited for bitwise cryptographic integrity:

```
========================================================================================================
PROPERTY                         SPECIFICATION / VERIFIED VALUE
========================================================================================================
File Path                        research_mission_01/phase_6_full_protocol2_validation/BALANCED_PROMPT_REGISTRY.json
Total Problem Instances          20 Paired Reasoning Problems (40 Unique Condition Prefixes)
Expected Checksum (Phase 5)      d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c
Computed Checksum (Phase 6)      d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c
Integrity Status                 BITWISE VERIFIED (Exact Match)
========================================================================================================
```

---

## 2. Exhaustive Semantic Leakage & Boundary Audit

To eliminate the critique that simple string absence might overlook subtle answer exposure, all 20 paired benchmark items were programmatically tested against four strict semantic leakage vectors:

```
========================================================================================================
PROBLEM ID       GOLD ANSWER  INTERMEDIATE (C)  INTERMEDIATE (R)  LEAKAGE STATUS  STRUCTURAL SYMMETRY
========================================================================================================
gsm8k_fresh_000  80           20                22                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_001  120          30                32                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_002  168          42                44                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_003  128          32                34                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_004  180          45                47                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_005  240          60                62                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_006  176          44                46                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_007  240          60                62                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_008  312          78                80                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_009  224          56                58                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_010  300          75                77                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_011  384          96                98                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_012  272          68                70                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_013  360          90                92                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_014  456          114               116               ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_015  320          80                82                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_016  420          105               107               ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_017  528          132               134               ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_018  368          92                94                ZERO LEAKAGE    EXACT SYMMETRY
gsm8k_fresh_019  480          120               122               ZERO LEAKAGE    EXACT SYMMETRY
========================================================================================================
```

### Specific Semantic Leakage Invariant Tests
1. **Numerical Absence**: The gold answer integer string $A_i^*$ does not appear anywhere in either prefix.
2. **Derivation Non-Exposure**: Neither prefix contains expressions of the form `* 4 = A*` or `= A*`.
3. **Step 2 Termination**: Both Control and Recovery prefixes terminate with the identical prompt string:
   `"Step 2: Calculate total revenue at $4 per notebook:\n"`
4. **Task Parity**: In both conditions, the language model is required to perform multi-step arithmetic continuation from an intermediate premise. In Control, the premise is valid ($N$). In Recovery, the premise is perturbed ($N + 2$).

---

## 3. Structural Equivalence Guarantees

Under Protocol 2.0:
- **Reasoning Depth**: Identical ($k=2$).
- **Remaining Steps Required**: Identical ($M - k = 1$).
- **Covariate SMD**: Standardized Mean Difference on continuous properties is identically **$0.0000$**.
- **Observational Matching Calipers**: Completely retired.

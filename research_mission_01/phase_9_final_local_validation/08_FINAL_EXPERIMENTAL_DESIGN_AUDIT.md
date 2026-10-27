# Deliverable 08: Protocol 2.0 Experimental Design & Full Matrix Verification Audit

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase IX (Stage H)  
**Date**: October 24, 2026  
**Auditor**: Lead Experimental Methodologist & Protocol Compliance Auditor  

---

## 1. Experimental Matrix Specification

The Protocol 2.0 experimental campaign is locked to a balanced factorial design across four experimental dimensions:

$$\mathcal{M} = 20 \text{ Problems} \times 2 \text{ Checkpoints} \times 2 \text{ Conditions} \times 5 \text{ Seeds} = \mathbf{400 \text{ Rollouts}}$$

```
========================================================================================================================
DIMENSION               SPECIFICATION                                       VALIDATION STATUS
========================================================================================================================
Problem Set             20 Balanced Multi-Step Problems (P01 – P20)         Verified in BALANCED_PROMPT_REGISTRY.json
Base Model              Qwen/Qwen2.5-Math-1.5B                              Pinned: 4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2
Instruct Model          Qwen/Qwen2.5-Math-1.5B-Instruct                     Pinned: aafeb0fc6f22cbf0eaeed126eff8be45b0360a35
Evaluated Conditions    CONTROL (Balanced Step 1) vs. RECOVERY (Corrupted)  Verified (Zero final-answer leakage)
Stochastic Seeds        401, 402, 403, 404, 405                             Locked in SEEDS constant
Generation Budget       max_new_tokens = 256                                Hard-locked in runner
Sampling Controls       temperature = 0.7, top_p = 0.9, do_sample = True    Hard-locked in runner
Registry Cryptoseal     d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c (100% Match)
========================================================================================================================
```

---

## 2. Invariant Methodological Protections

1. **Elimination of Control Answer Leakage**:  
   In Protocol 1.0, Control prompts contained the complete solution including the final answer. In Protocol 2.0, both Control and Recovery prompts terminate at the exact same step-1 milestone. Neither condition contains the ground-truth answer.
2. **Expansion of Token Ceiling to 256 Tokens**:  
   The historical 64-token ceiling artificially truncated 83% of Base recovery rollouts. The 256-token ceiling provides sufficient headroom for chain-of-thought scratchpad derivations and explicit verification checks.
3. **Distribution-Aligned Prompt Formatting**:  
   Base models receive raw mathematical continuation prompts; Instruct models receive formatted ChatML `<|im_start|>user...<|im_start|>assistant` turns. Neither model is evaluated outside its training distribution.
4. **Pre-Registered Estimand**:  
   The primary estimand is the double-difference interaction contrast:
   $$\Delta = (p_{I,R} - p_{B,R}) - (p_{I,C} - p_{B,C})$$
   evaluated with problem-level clustered standard errors ($G = 20$). The statistical analysis script is frozen prior to neural inference.

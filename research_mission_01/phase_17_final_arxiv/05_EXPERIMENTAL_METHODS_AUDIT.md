# 05: Experimental Methods and Reproducibility Protocol Audit

**Auditor**: Experimental Reproducibility Engineer  
**Focus**: Protocol 2.0 Methodological Soundness and Integrity  
**Date**: October 27, 2026  
**Status**: FULLY COMPLIANT AND AUDITED  

---

## 1. Experimental Protocol Architecture: Protocol 2.0

Protocol 2.0 was designed to completely replace the flawed, artifact-prone Protocol 1.0 setup that generated spurious results in early research iterations.

```
+---------------------------------------------------------------------------------------------------+
| COMPARATIVE AUDIT: PROTOCOL 1.0 (RETIRED) VS. PROTOCOL 2.0 (CANONICAL)                            |
+---------------------------------------------------------------------------------------------------+
| Feature                      | Protocol 1.0 (Flawed Baseline)    | Protocol 2.0 (Reconstructed)   |
+------------------------------+-----------------------------------+--------------------------------+
| Gold Answer Leakage          | 100% leaked into control prefix   | 0% leaked; strict pre-cut      |
| Generation Horizon Cap       | 64 tokens (induced 53% truncation)| 256 tokens (0% truncation)     |
| Prefix Token Balancing       | Uncontrolled character drift      | Exact token/character match    |
| Evaluation Design            | Post-hoc observational matching   | Paired Counterfactual (PCPPE)  |
| Verification Framework       | Brittle regex matching last digit | Dual-Regime (Regex + AST)      |
| Provenance Enforcement       | None                              | Cryptographic Hash Chaining    |
| Statistical Model            | Naive i.i.d. Student-t            | Clustered SE + Clopper-Pearson |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Key Methodological Components Audited

### 1. Counterfactual Prefix Construction (PCPPE)
- **Design**: For each of the 20 benchmark arithmetic problems ($P_i$), two length-matched prefixes were generated:
  - *Control Prefix ($s_C$)*: Contains valid Step 1 arithmetic calculation.
  - *Recovery Prefix ($s_R$)*: Contains corrupted Step 1 product calculation.
- **Answer Pre-Cut**: Both prefixes truncate immediately after the Step 1 conclusion, prior to Step 2. Neither prefix contains or implies the final gold answer.
- **Length Balance**: $\Delta_{\text{tokens}} = 0$, ensuring no token length confounders influence generation dynamics.

### 2. Checkpoint and Generation Configuration
- **Models Evaluated**:
  - `Qwen2.5-Math-1.5B` (Base): Commit revision `4a83ca6e45` (`4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2`).
  - `Qwen2.5-Math-1.5B-Instruct` (Instruct): Commit revision `aafeb0fc8b` (`aafeb0fc8b8981d3f5454fa67d1db0e99876`).
- **Inference Precision**: Native `torch.float16` on NVIDIA GeForce RTX 4090 GPU (24GB VRAM).
- **Sampling Parameters**: Stochastic nucleus sampling with $T=0.7$, $\text{top-}p=0.9$, $\text{max\_new\_tokens}=256$.
- **RNG Seeds**: Fixed seed schedule $\{401, 402, 403, 404, 405\}$.
- **Prompt Interfaces**: Base model uses raw completion prompts; Instruct model uses official ChatML format.

### 3. Censoring and Truncation Audit
- In Protocol 1.0, 53% of rollouts were truncated due to a 64-token cap, artificially creating a negative interaction because verbose models were truncated before stating their final answers.
- Under Protocol 2.0 with a 256-token horizon, **zero rollouts (0/400, 0.00%) were truncated**. Every rollout reached natural End-Of-Sequence (`<|endoftext|>` or `<|im_end|>`).

### 4. Dual-Regime Verification Logic
- **Heuristic Verifier**: Employs legacy regular expressions (`r"(?:final answer|revenue is|\$)\s*(\d+)"`). As documented in Section 6.3 of the manuscript, this verifier introduces 3 false negatives on base model control rollouts due to trailing commentary digits (`- In step 3...`).
- **Structural AST Verifier**: Parses mathematical AST expressions and verifies equality between extracted mathematical statements and gold targets. Confirms 100/100 control completions for both base and instruct models.

---

## 3. Cryptographic Event Ledger and Ledger Governance

Every experimental event—from dataset registration to prompt generation, GPU rollout execution, and verifier scoring—is cryptographically recorded in an append-only ledger:
$$H_k = \text{SHA-256}(H_{k-1} \,\|\, E_k)$$
- Initial Genesis Root: `d3b145890e0350d757f0f46df35b4430f81d830c25d886dd7519ff7f9ff3a976`
- Immutable Dataset SHA-256: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- Ledger tamper tests (`tests/test_exposure_append_only.py`) confirm that any retroactive modification or status downgrade raises an immediate cryptographic exception.

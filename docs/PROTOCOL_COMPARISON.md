# Protocol 1.0 versus Protocol 2.0 Comparison

**Project**: `recovery_eval`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: IEEE BigData 2026 / MLBD 2026  

---

## 1. Architectural Differences

The transition from historical Protocol 1.0 to Protocol 2.0 eliminated critical experimental confounders that originally generated spurious negative post-training penalty findings ($D \approx -0.21$).

| Parameter / Dimension | Protocol 1.0 (Historical) | Protocol 2.0 (Verified Standard) | Methodological Rationale |
|---|---|---|---|
| **Max New Tokens** | 64 tokens | **256 tokens** | Prevents premature truncation of multi-step reasoning traces. |
| **Prompt Structure** | Unbalanced prefix lengths | **State-Matched Prefix** | Both Control and Recovery have identical token lengths and step boundaries prior to perturbation. |
| **Perturbation Method** | Injected free-form corruption | **Controlled Intermediate Value Perturbation** | Isolates the specific step-1 calculation error while preserving syntax. |
| **Scoring Regimes** | Regex-only `MathVerifier` | **Dual Regime**: Heuristic Regex + Structural / Semantic | Detects parser-induced artifacts vs true mathematical reasoning failures. |
| **Statistical Unit** | Naive rollout-level pooling | **Paired Problem Clusters ($C = 20, \mathrm{df} = 19$)** | Controls for problem-specific difficulty and intra-cluster correlation. |
| **Execution Hardware** | Apple Silicon M1 (Swapping) | **NVIDIA RTX 4090 (24 GB VRAM)** | Eliminates memory constraints and non-deterministic CPU quantization. |

---

## 2. Experimental Results Under Both Protocols

```
Protocol 1.0 (Confounded):
  - Base Recovery:     ~25%
  - Instruct Recovery: ~4%
  - Interaction D:     ~ -0.21  (Spurious post-training penalty caused by token starvation)

Protocol 2.0 (State-Matched, 256 tokens):
  - Base Control:      97.00% (Heuristic) / 100.00% (Structural)
  - Base Recovery:      0.00% (Heuristic) /   0.00% (Structural)
  - Instruct Control: 100.00% (Heuristic) / 100.00% (Structural)
  - Instruct Recovery:  0.00% (Heuristic) /   0.00% (Structural)
  - Interaction D:     -0.0300 (p = 0.0828, Heuristic) / 0.0000 (Structural)
```

### Scientific Conclusion:
The reported "post-training recovery penalty" in Protocol 1.0 was an experimental artifact resulting from token budget starvation (64 tokens) where verbose Instruct completions were prematurely truncated, while terse Base completions occasionally emitted numbers before hitting the budget. Under state-matched prompting with adequate token budgets (256 tokens), both models exhibit identical 0.00% recovery rates due to continuation inertia.

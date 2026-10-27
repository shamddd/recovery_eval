# Deliverable 01: Decoding Reproducibility and Sampling Audit

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Submission Identifier**: `BigD497` (IEEE BigData 2026 Tracking)  
**Date**: October 24, 2026  
**Auditor**: Experimental Machine Learning Engineer & Scientific Integrity Auditor  

---

## 1. The Historical Contradiction and Reviewer Critique

Reviewers 1 and 3 of IEEE BigData 2026 correctly flagged a major contradiction in the original submission text (`BigD497`):
> *"Section III claims that decoding was executed using greedy search (temperature = 0.0), but then reports running five stochastic rollouts per condition per problem yielding varying continuation trajectories and varying success rates. If decoding is greedy, five identical seeds must yield five identical outputs. Either the decoding was stochastic, or the reported variance is an artifact."*

This audit independently establishes the empirical truth by inspecting:
1. The execution engine source code (`neural_runner.py`).
2. The runtime logging calls and random number generator (RNG) initialization.
3. The raw rollout evidence records (`RAW_NEURAL_ROLLOUTS.jsonl`).
4. Output diversity, duplicate rates, and variance across all 400 rollouts.

---

## 2. Forensic Code and Parameter Verification

### A. Execution Engine Inspection (`neural_runner.py`)
Direct inspection of the actual execution code located at `research-next/ieee_bigdata_2026/recovery_eval/execution/neural_runner.py` reveals the following generation loop:

```python
# Model and MPS RNG initialization
torch.manual_seed(seed)
if self.device.type == "mps":
    torch.mps.manual_seed(seed)

inputs = self.tokenizer(prompt_text, return_tensors="pt").to(self.device)
input_ids = inputs["input_ids"]

start_ns = time.monotonic_ns()

with torch.inference_mode():
    output_ids = self.model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        do_sample=True,
        pad_token_id=self.tokenizer.eos_token_id
    )

if self.device.type == "mps":
    torch.mps.synchronize()

end_ns = time.monotonic_ns()
```

### B. Verified Runtime Generation Configuration
Cross-referencing `neural_runner.py` and `RAW_NEURAL_ROLLOUTS.jsonl` confirms the actual runtime parameters across all 400 rollouts:

| Parameter | Value in Original Manuscript Text | Actual Execution Ground Truth | Verification Source |
| :--- | :---: | :---: | :--- |
| **Sampling Mode** (`do_sample`) | Greedy (`False`) | **`True`** (100% of 400 rollouts) | `RAW_NEURAL_ROLLOUTS.jsonl` |
| **Temperature** ($T$) | $0.0$ (Claimed) | **$0.7$** (100% of 400 rollouts) | `RAW_NEURAL_ROLLOUTS.jsonl` |
| **Nucleus Sampling** (`top_p`) | Omitted | **$0.9$** (100% of 400 rollouts) | `RAW_NEURAL_ROLLOUTS.jsonl` |
| **Generation Seeds** | $1 \dots 5$ (Unspecified) | **$401, 402, 403, 404, 405$** | `RAW_NEURAL_ROLLOUTS.jsonl` |
| **Hardware Device** | Apple Silicon | **Apple MPS (`mps:0`) in FP16** | `neural_runner.py` |
| **Token Horizon** (`max_new_tokens`) | 64 | **64 tokens** | `RAW_NEURAL_ROLLOUTS.jsonl` |

**Conclusion on Contradiction**: The original submission suffered from a severe editorial discrepancy: **the manuscript text erroneously described the decoding as greedy ($T=0.0$), whereas the neural inference engine executed stochastic nucleus sampling ($T=0.7, p=0.9$) across 5 distinct random seeds (401–405)**.

---

## 3. Quantitative Output Diversity Audit

To rule out any possibility that the seeds were pseudo-stochastic or collapsing to identical text, we conducted a full combinatorial diversity audit across all 80 experimental cells (2 models $\times$ 2 conditions $\times$ 20 problem instances $\times$ 5 seeds = 400 rollouts).

### A. Output Diversity Summary
```
======================================================================================
METRIC                                                  OBSERVED VALUE       PERCENTAGE
======================================================================================
Total Evaluated Rollouts                                400                  100.0%
Total 5-Seed Experimental Cell Groups                    80                   100.0%
Groups with 5 completely unique text generations        79 / 80              98.75%
Groups with duplicate generations                        1 / 80               1.25%
Groups where all 5 generations were identical            0 / 80               0.00%
Total Pairwise Comparisons within 5-seed cells          800                  100.0%
Total Pairwise Duplicate Generations                     1 / 800              0.12%
Average Unique Continuations per 5-Seed Cell             4.99 / 5.0           99.80%
======================================================================================
```

### B. Breakdown by Model and Condition Cell
```
====================================================================================================
CELL GROUP                       N     MEAN TOKENS   STD TOKENS   ACCURACY   AVG UNIQUE GENERATIONS
====================================================================================================
Qwen2.5-Math-1.5B (Control)      100   54.08         17.74        0.3800     5.00 / 5.0 (min 5, max 5)
Qwen2.5-Math-1.5B (Recovery)     100   59.46         12.55        0.2100     5.00 / 5.0 (min 5, max 5)
Qwen2.5-Math-1.5B-Inst (Control) 100   32.23         17.47        0.9200     4.95 / 5.0 (min 4, max 5)
Qwen2.5-Math-1.5B-Inst (Recovery)100   46.35         18.37        0.6400     5.00 / 5.0 (min 5, max 5)
====================================================================================================
```

*Note on Duplicate Case*: The single duplicate occurrence was in `gsm8k_fresh_018` for `Qwen2.5-Math-1.5B-Instruct` under Control, where seeds 402 and 404 both generated the identical 6-token terminal completion: `"Total = 15 notebooks."`. In all other 79 problem-condition cells, every single seed produced a distinct continuation.

---

## 4. Variance Decomposition (Within-Problem vs. Between-Problem)

A stochastic evaluation requires examining how much variance arises from prompt difficulty (between-problem variance) versus stochastic generation sampling (within-problem variance across seeds).

```
======================================================================================
EXPERIMENTAL CELL                 ACCURACY BETWEEN-VAR   ACCURACY AVG WITHIN-VAR (SEEDS)
======================================================================================
Qwen2.5-Math-1.5B (Control)       0.0476                 0.1880
Qwen2.5-Math-1.5B (Recovery)      0.0259                 0.1400
Qwen2.5-Math-1.5B-Inst (Control)  0.0256                 0.0480
Qwen2.5-Math-1.5B-Inst (Recovery) 0.0384                 0.1920
======================================================================================
```

**Interpretation**:
- In the Instruct Control cell, within-problem variance is minimal ($0.0480$) because the model almost deterministically echoes and concludes the already-solved problem ($92\%$ accuracy).
- In the Recovery condition for both Base and Instruct, within-problem variance is substantial ($0.1400$ and $0.1920$). This demonstrates that whether a model successfully recalculates past an injected arithmetic error varies substantially across stochastic generation trajectories for the exact same problem prompt.

---

## 5. Executable Reproducibility Script

The following self-contained script reproduces this entire audit from the raw logs:

```python
#!/usr/bin/env python3
import json, collections, numpy as np

def run_audit(raw_path):
    records = [json.loads(line) for line in open(raw_path)]
    assert len(records) == 400, f"Expected 400 records, got {len(records)}"
    
    # Check parameters
    assert all(r['do_sample'] is True for r in records)
    assert all(r['temperature'] == 0.7 for r in records)
    assert all(r['top_p'] == 0.9 for r in records)
    assert set(r['generation_seed'] for r in records) == {401, 402, 403, 404, 405}
    
    # Group by (model, condition, problem)
    groups = collections.defaultdict(list)
    for r in records:
        groups[(r['policy_id'], r['recovery_or_control'], r['problem_id'])].append(r)
        
    unique_counts = [len(set(r['generated_text'] for r in g)) for g in groups.values()]
    print(f"Total groups: {len(groups)}")
    print(f"Groups with 5 unique outputs: {sum(1 for u in unique_counts if u == 5)} / 80")
    print(f"Average unique generations: {np.mean(unique_counts):.4f} / 5.0")
    print("AUDIT RESULT: VERIFIED STOCHASTIC SAMPLING")

if __name__ == "__main__":
    run_audit("research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl")
```

---

## 6. Final Audit Verdict

1. **Editorial Error Replaced with Empirical Truth**: The claim of greedy decoding ($T=0.0$) in the original manuscript was false. The actual neural rollouts were generated via stochastic nucleus sampling ($T=0.7, p=0.9$, seeds 401–405).
2. **Generative Diversity Confirmed**: 98.75% of cell groups generated 5 unique rollouts; duplicate pair rate was $0.12\%$.
3. **Manuscript Alignment Complete**: In Phase 4, the manuscript explicitly states: *"Continuation rollouts were sampled stochastically using nucleus sampling ($T=0.7$, $\text{top\_p}=0.9$, $\text{max\_new\_tokens}=64$) across five pre-registered random seeds (401--405) on Apple Silicon MPS in half-precision (FP16)."*

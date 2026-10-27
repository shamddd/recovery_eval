# Deliverable 04: Token Truncation Analysis and Observational Interpretation

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Researcher**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Auditor**: Principal Research Scientist, Experimental Auditor & Statistical Methodologist  
**Audit Phase**: Phase 3 (Submission Freeze)  
**Date**: October 24, 2026  
**Primary Dataset**: [`RAW_NEURAL_ROLLOUTS.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl) (400 rollouts)  

---

## 1. Truncation Empirical Distribution (64-Token Ceiling)

All 400 neural rollouts were evaluated under a fixed maximum generation limit of 64 new tokens (`max_new_tokens = 64`).

### Cross-Condition Truncation Rates:
| Experimental Cell | Total Rollouts ($N$) | Truncated Rollouts ($=64$ tokens) | Truncation Rate | Mean Generated Tokens | Standard Deviation |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Base Control ($S_C$)** | 100 | 74 | **74.0%** | 54.08 tokens | 14.82 |
| **Base Recovery ($S_R$)** | 100 | 83 | **83.0%** | 59.46 tokens | 10.63 |
| **Instruct Control ($S_C$)** | 100 | 12 | **12.0%** | 32.23 tokens | 15.71 |
| **Instruct Recovery ($S_R$)** | 100 | 43 | **43.0%** | 46.35 tokens | 17.54 |
| **Total Experiment** | **400** | **212** | **53.0%** | **48.03 tokens** | **18.78** |

---

## 2. Observational Association Between Truncation and Failure

Generations that reached the 64-token cap exhibited substantially higher failure rates:
* **Failure Rate Among Truncated Generations ($=64$ tokens)**: $159 / 212 = \mathbf{75.00\%}$
* **Failure Rate Among Completed Generations ($<64$ tokens)**: $26 / 188 = \mathbf{13.83\%}$
* **Unadjusted Relative Risk**:
  $$RR_{\text{obs}} = \frac{0.7500}{0.1383} = \mathbf{5.4231\times} \approx \mathbf{5.42\times}$$
* **Unadjusted Odds Ratio**:
  $$OR_{\text{obs}} = \frac{159 \times 162}{53 \times 26} = \mathbf{18.6923} \quad (p = 7.14 \times 10^{-37}, \text{Fisher's Exact Test})$$

---

## 3. Strict Elimination of Causal Language

In previous drafts, this empirical association was occasionally described with causal framing (e.g., *"truncation caused a 5.43x surge in model failures"*). That language is methodologically flawed because the study design is observational with respect to generation length.

### Required Observational Framing:
> [!IMPORTANT]
> **Defensible Scientific Wording**:  
> *"Generations reaching the 64-token limit exhibited substantially higher measured failure rates ($75.0\%$ vs. $13.8\%$, relative risk $5.42\times$). However, this observational association does not establish that truncation independently caused those failures. Truncation is jointly associated with model architecture, prompt condition, problem difficulty, and termination behavior."*

### Competing Plausible Mechanisms for Truncation:
1. **Architectural Stop-Token Suppression**:
   - `Qwen2.5-Math-1.5B-Instruct` is supervised on conversational turn templates and trained to emit terminal `<|im_end|>` tokens upon concluding a solution (mean length: 32.2 tokens in Control).
   - `Qwen2.5-Math-1.5B` (Base) is an unaligned base model that lacks end-of-turn supervision. Even after reaching the correct answer, it continues generating until stopped by the hard token budget (mean length: 54.1 to 59.5 tokens).
2. **Cognitive Overhead in Error Recovery**:
   - In Recovery states, models that struggle to resolve arithmetic contradictions often repeat steps, explain errors, or re-derive intermediate quantities.
   - For Instruct models, mean generation length expanded by $+43.8\%$ (from 32.2 to 46.4 tokens), increasing truncation from 12% to 43%.
3. **Unequal Truncation as a Confounder**:
   - Because Base models truncate at 74–83% while Instruct Control truncates at only 12%, **raw performance comparisons between Base and Instruct models under a 64-token budget are heavily confounded by the generation limit**.

---

## 4. Methodological Recommendation

Rather than attempting to statistically adjust for truncation post-hoc (which introduces collider-stratification bias), valid evaluation of reasoning recovery requires:
1. **Budget Expansion**: Increasing `max_new_tokens` to at least **256 tokens** to decouple reasoning completion from length constraints.
2. **Explicit Stop Criteria**: Allowing models to emit standard natural stop sequences while evaluating unaligned models under linear answer-extraction windows.

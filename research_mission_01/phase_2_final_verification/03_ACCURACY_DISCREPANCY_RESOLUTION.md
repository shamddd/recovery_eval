# Deliverable 03: Condition-Level Accuracy Discrepancy Resolution

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Auditor**: Principal Research Scientist, Experimental Auditor & Statistical Methodologist  
**Audit Date**: October 24, 2026  
**Primary Dataset**: `RAW_NEURAL_ROLLOUTS.jsonl` (400 records, SHA-256: `51b5a157d9e44102caeb86d0b356f558aa7499f6bad3634f668f0dd1ed76b1b4`)  
**Status**: **PUBLICATION-BLOCKER FULLY RESOLVED & DE-RISKED**  

---

## 1. The Discrepancy Statement

During the initial review of previous research mission documentation, a critical inconsistency was flagged between two competing summaries of condition-level accuracy:

* **Description A (Corrupted / Transposed Summary)**:
  - Base Control ($S_C$) = $21\%$
  - Base Recovery ($S_R$) = $64\%$
  - Instruct Control ($S_C$) = $92\%$
  - Instruct Recovery ($S_R$) = $94\%$
* **Description B (Verified Ground-Truth Summary)**:
  - Base Control ($S_C$) = $38\%$
  - Base Recovery ($S_R$) = $21\%$
  - Instruct Control ($S_C$) = $92\%$
  - Instruct Recovery ($S_R$) = $64\%$

Because both sets of four numbers cannot simultaneously describe the same four experimental cells of 100 rollouts each, this discrepancy constitutes a publication-blocking issue that required absolute resolution before manuscript preparation could proceed.

---

## 2. Independent Forensic Query on `RAW_NEURAL_ROLLOUTS.jsonl`

We parsed all 400 raw JSONL records in [`RAW_NEURAL_ROLLOUTS.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl) using [`phase_2_final_verification/11_REPRODUCTION_SCRIPTS/independent_verification.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_2_final_verification/11_REPRODUCTION_SCRIPTS/independent_verification.py).

The exact distribution of records by policy ID (`policy_id`), state condition (`recovery_or_control`), and evaluation reward (`primitive_success`) is:

```python
# Raw JSONL query result across 400 records:
{
    ("Qwen/Qwen2.5-Math-1.5B", "CONTROL"):  {"total": 100, "success": 38, "failure": 62},
    ("Qwen/Qwen2.5-Math-1.5B", "RECOVERY"): {"total": 100, "success": 21, "failure": 79},
    ("Qwen/Qwen2.5-Math-1.5B-Instruct", "CONTROL"):  {"total": 100, "success": 92, "failure": 8},
    ("Qwen/Qwen2.5-Math-1.5B-Instruct", "RECOVERY"): {"total": 100, "success": 64, "failure": 36}
}
```

### The Definitive Empirical Truth:
| Factorial Cell Index | Model Architecture | Evaluated State Condition | Total Rollouts ($N$) | Ground-Truth Successes | Measured Empirical Accuracy |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **Cell 1** | Base (`Qwen2.5-Math-1.5B`) | **Control ($S_C$)** | 100 | 38 | **0.3800 (38.0%)** |
| **Cell 2** | Base (`Qwen2.5-Math-1.5B`) | **Recovery ($S_R$)** | 100 | 21 | **0.2100 (21.0%)** |
| **Cell 3** | Instruct (`Qwen2.5-Math-1.5B-Instruct`) | **Control ($S_C$)** | 100 | 92 | **0.9200 (92.0%)** |
| **Cell 4** | Instruct (`Qwen2.5-Math-1.5B-Instruct`) | **Recovery ($S_R$)** | 100 | 64 | **0.6400 (64.0%)** |

---

## 3. Forensic Root-Cause Analysis: Origin of the Inconsistency

Where did the corrupted numbers in **Description A** ($21\%, 64\%, 92\%, 94\%$) originate?

A comprehensive audit of the conversation history and intermediate summary text revealed the exact mechanism:
1. In the text response concluding Research Mission 01 Phase 1, the agent was instructed to answer the 5 initial requirements of Section 14.
2. In drafting Requirement 5 (*"The first reproducible analysis to perform"*), an accidental **transposition and typographical copy-paste error** occurred in the prose summary:
   - The value `0.2100` (which is actually **Base Recovery**, Cell 2) was inadvertently typed under the label `Base Control`.
   - The value `0.6400` (which is actually **Instruct Recovery**, Cell 4) was inadvertently typed under the label `Base Recovery`.
   - The value `0.9200` (which is **Instruct Control**, Cell 3) was correctly labeled.
   - The value `0.9400` was a hallucinated typographical slip (likely combining `92` and the recovery `64`, or a transposition of `64`).
3. **Crucially, this error existed ONLY in the informal chat prose summary**.
   - The underlying dataset [`RAW_NEURAL_ROLLOUTS.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl) has always contained $38, 21, 92, 64$.
   - The verified validation script [`final_validation/reconstruct_empirical_data.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/final_validation/reconstruct_empirical_data.py) lines 73–91 explicitly asserts:
     ```python
     assert cells[("Base", "CONTROL")]["success"] == 38
     assert cells[("Base", "RECOVERY")]["success"] == 21
     assert cells[("Instruct", "CONTROL")]["success"] == 92
     assert cells[("Instruct", "RECOVERY")]["success"] == 64
     ```
   - The revised manuscript source [`research_mission_01/06_REVISED_MANUSCRIPT.tex`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/06_REVISED_MANUSCRIPT.tex) lines 183–197 (Table \ref{tab:outcomes}) correctly displays:
     - Base Recovery: $0.2100$ (21/100)
     - Base Control: $0.3800$ (38/100)
     - Instruct Recovery: $0.6400$ (64/100)
     - Instruct Control: $0.9200$ (92/100)

---

## 4. Mathematical Proof of Incompatibility for Description A

To definitively establish why Description A is mathematically impossible, consider the reported interaction contrast $D = -0.1100$:

### Under Description B (The True Empirical Data):
1. **Model Differences Across Conditions**:
   - Recovery Difference: $\Delta_{\text{rec}} = 0.6400 - 0.2100 = \mathbf{+0.4300}$
   - Control Difference: $\Delta_{\text{ctrl}} = 0.9200 - 0.3800 = \mathbf{+0.5400}$
   - Contrast:
     $$D = \Delta_{\text{rec}} - \Delta_{\text{ctrl}} = (+0.4300) - (+0.5400) = \mathbf{-0.1100}$$
2. **Within-Model Perturbation Penalties**:
   - Base Penalty: $\Delta_{\text{Base}} = 0.2100 - 0.3800 = \mathbf{-0.1700}$
   - Instruct Penalty: $\Delta_{\text{Instruct}} = 0.6400 - 0.9200 = \mathbf{-0.2800}$
   - Contrast:
     $$D = \Delta_{\text{Instruct}} - \Delta_{\text{Base}} = (-0.2800) - (-0.1700) = \mathbf{-0.1100}$$

Both derivations yield **exactly $-0.1100$**.

### Under Description A (The Corrupted Transcription):
If one attempts to compute the contrast using the numbers $21\%, 64\%, 92\%, 94\%$:
- Recovery Difference: $\Delta_{\text{rec}} = 0.9400 - 0.6400 = \mathbf{+0.3000}$
- Control Difference: $\Delta_{\text{ctrl}} = 0.9200 - 0.2100 = \mathbf{+0.7100}$
- Resulting Contrast:
  $$D_{\text{corrupt}} = (+0.3000) - (+0.7100) = \mathbf{-0.4100} \neq -0.1100$$

A contrast of $-0.4100$ is completely at odds with all statistical code, bootstrap distributions, and manuscript tables.

---

## 5. Resolution Verdict

1. **The True Four-Cell Distribution is Confirmed**:
   $$\text{Base Control} = \mathbf{38.0\%}, \quad \text{Base Recovery} = \mathbf{21.0\%}, \quad \text{Instruct Control} = \mathbf{92.0\%}, \quad \text{Instruct Recovery} = \mathbf{64.0\%}$$
2. **The Reported Interaction Contrast is Confirmed**:
   $$D_{\text{rec}} = \mathbf{-0.1100} \quad (-11.0\text{ percentage points})$$
3. **The Discrepancy is Permanently Resolved**: Description A was an isolated clerical transposition in conversational prose, while all codebase records, unit tests, and LaTeX sources strictly adhere to Description B.

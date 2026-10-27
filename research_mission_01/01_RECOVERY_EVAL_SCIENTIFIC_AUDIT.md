# 01_RECOVERY_EVAL_SCIENTIFIC_AUDIT.md
# Comprehensive Scientific Audit & Evidence Ledger: recovery_eval

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (github.com/shamddd)  
**Submission Reference**: IEEE BigData 2026 Main Track (`BigD497`, Not Accepted Oct 21, 2026)  
**Candidate Target**: 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)  
**Lead Auditor**: Principal Research Scientist & Senior Experimental Methodologist  
**Audit Date**: October 24, 2026  
**Primary Directory**: `/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/`  

---

## 1. Executive Forensic Summary

This audit establishes the rigorous, objective truth regarding the `recovery_eval` codebase, empirical records, research design, and manuscript claims:

1. **Empirical Ground Truth Verified**:
   - The primary empirical dataset [`research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl) (SHA-256: `51b5a157d9e44102caeb86d0b356f558aa7499f6bad3634f668f0dd1ed76b1b4`, 1,081,024 bytes) contains **400 genuine forward-pass neural rollouts** generated on Apple Silicon MPS (`mps:0`) using released `Qwen2.5-Math-1.5B` checkpoints on August 16, 2026 between 18:39:01 and 19:40:01 IST.
   - Zero empirical numbers in the current manuscript descend from the retracted simulation files of historical Stages 8, 9B, and 9D.
2. **Critical Scientific Defect Identified (F-01)**:
   - The manuscript asserts in the Abstract and Section IV that it evaluates *"20 prospectively isolated GSM8K test problems"* \cite{cobbe2021gsm8k}.
   - In fact, all 20 evaluated items in `FRESH_EVALUATION_REGISTRY.json` are **synthetic, single-operation rate-multiplication templates** (*"A store sells X notebooks per hour. How many in Y hours?"*). Citing Cobbe et al. while evaluating synthetic templates is a material benchmark misrepresentation that must be corrected immediately.
3. **Control State Leakage Discovered (F-05)**:
   - Control state prefixes in `FRESH_MATCHED_PAIR_REGISTRY.json` already contain the full solution and the final ground-truth answer (e.g. `Notebooks per hour: 5. Hours: 4. Total notebooks = 20.`). The control condition evaluates trivial completion/formatting adherence, driving Instruct control performance to a 92% ceiling.
4. **Verifier Parsing Artifact Quantified (F-04)**:
   - `math_verifier.py` fallback Pattern 5 extracts the last numerical token in the text. For unaligned base models that continue generating text beyond the initial answer, this heuristic extracted numbers from subsequent text, causing **87 false negatives (41.5% of all Base outputs)**.
5. **Severe Generation Truncation Quantified**:
   - The 64-token generation cap truncated **53.0% of all rollouts** (and 83.0% of Base Recovery rollouts). Truncation increased the odds of measured failure by **$5.43\times$** (75.0% vs. 13.8%).

---

## 2. Research Design & Methodological Audit

### 2.1 The Core Research Question
> *When an instruction-tuned model succeeds after an intermediate reasoning error, does this reflect an autonomous error-recovery capability specific to invalid intermediate states, or is it an artifact of general continuation fluency?*

### 2.2 The Estimand Formulation
The study proposes the policy-by-state interaction contrast:
$$D_{\text{recovery}} = (\mu_{R, \text{instruct}} - \mu_{R, \text{base}}) - (\mu_{C, \text{instruct}} - \mu_{C, \text{base}})$$
where:
* $\mu_{R, \pi}$: Probability that policy $\pi$ reaches the correct answer from an invalid (recovery) intermediate state $S_R$.
* $\mu_{C, \pi}$: Probability that policy $\pi$ reaches the correct answer from a structurally matched valid (control) intermediate state $S_C$.

### 2.3 Methodological Soundness of the Estimand:
* **The Concept**: Subtracting the control delta $(\mu_{C, \text{instruct}} - \mu_{C, \text{base}})$ from the recovery delta $(\mu_{R, \text{instruct}} - \mu_{R, \text{base}})$ is mathematically sound and conceptually valuable. It prevents researchers from mistaking general instruction-following gains for recovery-specific mechanisms.
* **The Empirical Finding**: The empirical estimate is $D_{\text{recovery}} = (+0.4300) - (+0.5400) = \mathbf{-0.1100}$, with a 95% problem-cluster bootstrap interval of $\mathbf{[-0.2400, +0.0300]}$ ($p \approx 0.1220$, spanning zero).
* **The Substantive Interpretation**: Instruction tuning produced a massive $+43$ pp gain on recovery states, but this was outpaced by a $+54$ pp gain on control states. Thus, there is **no evidence of a recovery-specific advantage**; the observed recovery successes are completely explained by baseline continuation fluency and formatting compliance.

---

## 3. Evidence Traceability Ledger

| Claim / Manuscript Table Element | Source File & Location | Cryptographic Hash | Verification Script & Output | Status |
| :--- | :--- | :--- | :--- | :---: |
| **400 Rollout Total** | `09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl` | `51b5a157...` | `validate_empirical_results.py`: 400 lines | **VERIFIED** |
| **Base Model Revision** | `09_genuine_execution_v1/BASE_LOCAL_WEIGHT_MANIFEST.json` | `708b00dd...` | Revision: `4a83ca6e4526a4f2da3aa259ec36c259f66b2ab2` | **VERIFIED** |
| **Instruct Model Revision** | `09_genuine_execution_v1/INSTRUCT_LOCAL_WEIGHT_MANIFEST.json` | `ae182f0a...` | Revision: `aafeb0fc6f22cbf0eaeed126eff8be45b0360a35` | **VERIFIED** |
| **Base Control (0.3800)** | `RAW_NEURAL_ROLLOUTS.jsonl` | `51b5a157...` | $38 / 100 = 0.3800$ exact match | **VERIFIED** |
| **Base Recovery (0.2100)** | `RAW_NEURAL_ROLLOUTS.jsonl` | `51b5a157...` | $21 / 100 = 0.2100$ exact match | **VERIFIED** |
| **Instruct Control (0.9200)**| `RAW_NEURAL_ROLLOUTS.jsonl` | `51b5a157...` | $92 / 100 = 0.9200$ exact match | **VERIFIED** |
| **Instruct Recovery (0.6400)**| `RAW_NEURAL_ROLLOUTS.jsonl` | `51b5a157...` | $64 / 100 = 0.6400$ exact match | **VERIFIED** |
| **Contrast ($D = -0.1100$)**| `Table II`, `main.tex` (L201) | `aa91e06b...` | $(0.64 - 0.21) - (0.92 - 0.38) = -0.1100$ | **VERIFIED** |
| **Cluster Bootstrap CI** | `STATISTICAL_RESULTS.json` | `810dd3ce...` | $B=10,000$ resamples: $[-0.2400, +0.0300]$ | **VERIFIED** |
| **Truncation Rate (53.0%)** | `RAW_NEURAL_ROLLOUTS.jsonl` | `51b5a157...` | 212 / 400 rollouts = 53.0% | **VERIFIED** |
| **GSM8K Benchmark Claim** | `main.tex` (L32, L141) | `aa91e06b...` | `FRESH_EVALUATION_REGISTRY.json`: 20 synthetic templates | **CONTRADICTED (F-01)** |
| **Open Retraction Notice** | `SCIENTIFIC_STATUS.md` | `62b977ed...` | Root file states all model results are retracted | **CONTRADICTED (F-02)** |

---

## 4. Root Cause of Main Conference Rejection (Paper BigD497)

The author’s original submission (`submission_bigdata2026_main_v3/main.pdf`) was rejected primarily because:
1. **Unclustered Statistical Tests**: It treated 400 repeated rollouts across 20 problems as $N=400$ independent trials, claiming statistical significance ($p < 0.05$). When properly clustered at the problem level ($N_p = 20$), the confidence interval spans zero ($p \approx 0.122$).
2. **Table II Value Discrepancies**: Base Recovery was misreported as $0.1500$ and Instruct Recovery as $0.5800$ (an offset of $-0.0600$).
3. **Undisclosed Decoding Parameters**: The submission reported greedy decoding ($T=0.0$), whereas generation was actually nucleus sampled ($T=0.7, p=0.9$).
4. **Undisclosed Truncation**: The severe 64-token truncation ceiling (53.0% overall; 83.0% on Base Recovery) was completely omitted from the text.
5. **Three Missing Bibliography Keys**: Citations to STaR, CheckList, and Contrast Sets appeared as literal `[?]` markers.

All of these initial defects were resolved in `manuscript_v2` and `transfer_package/final_candidate/`. However, Phase 13 revealed that the **synthetic benchmark mischaracterization (F-01)** remained uncorrected in the manuscript text. Fixing F-01 is the final scientific prerequisite for publication readiness.

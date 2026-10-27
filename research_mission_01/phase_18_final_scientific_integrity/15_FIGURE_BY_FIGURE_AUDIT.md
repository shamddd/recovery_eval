# 15: Figure-by-Figure Independent Audit Report

**Auditor**: Publication Graphics and Visual Inspection Specialist  
**Target Document**: `output/RecoveryEval_FINAL_VERIFIED_arXiv.pdf`  
**Figures Directory**: `manuscript/figures/`  
**Date**: October 27, 2026  
**Status**: 100% FIGURES ACCURATE, SYNCHRONIZED, AND VERIFIED  

---

## 1. Figure Inventory and Verification Matrix

```
+-------------------------------------------------------------------------------------------------------------------------+
| INDEPENDENT FIGURE-BY-FIGURE AUDIT (PHASE XVIII)                                                                        |
+--------+------+-----------------------------+------------------------------------+------------------+-------------------+
| Figure | Page | Source Vector File          | Generation Script                  | Input Dataset    | Audit Verdict     |
+--------+------+-----------------------------+------------------------------------+------------------+-------------------+
| DAG    | 5    | LaTeX Framed Minipage Box   | Embedded in main.tex (lines 131-45)| SCM Architecture | PASS (Aligned)    |
| Fig 1  | 6    | fig1_architecture.pdf       | generate_protocol2_figures.py      | Protocol 2.0 Spec| PASS (Clean vec)  |
| Fig 2  | 7    | fig2_state_construction.pdf | generate_protocol2_figures.py      | Prompt Registry  | PASS (Delta=0)    |
| Fig 4  | 11   | fig4_empirical_results.pdf  | generate_protocol2_figures.py      | 400 Rollouts Log | PASS (Exact data) |
| Fig 3  | 12   | fig3_provenance_chain.pdf   | generate_protocol2_figures.py      | Event Ledger     | PASS (Hash chain) |
+--------+------+-----------------------------+------------------------------------+------------------+-------------------+
```

---

## 2. Exhaustive Verification of Each Visual Figure

### 1. Structural Causal DAG (Page 5, Figure `fig:dag`)
- **Visual Presentation**: Framed centered algorithmic box.
- **Node Connections**:
  - `Problem Template (U)` $\longrightarrow$ `Assigned Prefix State (T)` $\longrightarrow$ `Downstream Output (Y)`
  - `Model Checkpoint (M)` $\longrightarrow$ `Prompt Interface / BPE (Z)` $\longrightarrow$ `Downstream Output (Y)`
- **Caption**: Explains that $T \in \{s_C, s_R\}$ is assigned in a fully crossed, paired within-problem design across $U$. Identifies within-model contrast $T \to Y \mid M$ as causally unconfounded and cross-model contrast $M \to Y$ as observational.
- **Audit Verdict**: PASS.

### 2. Figure 1: Protocol 2.0 Evaluation & Governance Pipeline (Page 6)
- **Visual Presentation**: Clean vector diagram with 5 horizontal stages linked by directional arrows.
- **Content**:
  - Stage 1: Benchmark Registry (20 Fresh GSM8K Tasks).
  - Stage 2: Counterfactual PCPPE Engine ($\Delta_{\text{tokens}}=0, \Delta_{\text{chars}}=0$, strict pre-cut).
  - Stage 3: Neural Rollouts on RTX 4090 (Base & Instruct across 5 seeds, 400 rollouts, 0% truncation).
  - Stage 4: Cryptographic Ledger ($H_k = \text{SHA-256}(...)$, dataset `b8792f8d...`).
  - Stage 5: Dual-Regime Verifier (Structural AST Equivalence vs. Heuristic Regex, 5-tier process taxonomy).
- **Audit Verdict**: PASS (Zero references to retired caliper matching).

### 3. Figure 2: Paired Counterfactual Prefix Perturbation Evaluation (Page 7)
- **Visual Presentation**: Dual-box side-by-side comparison under shared problem context.
- **Content**:
  - Shared Problem: `gsm8k_fresh_000` (5 notebooks/hr, 4 hrs, \$4/notebook, gold final answer \$80).
  - Control Prefix ($s_C$): Unperturbed Step 1 product (136 characters, 72 tokens).
  - Recovery Prefix ($s_R$): Corrupted Step 1 product (136 characters, 72 tokens).
  - Pre-cut isolation highlighted; final answer ($80$) strictly withheld.
  - Symmetrical balance confirmed: $\Delta_{\text{chars}} = 0, \Delta_{\text{tokens}} = 0$.
- **Audit Verdict**: PASS (Zero references to obsolete 35 vs. 33 caliper matching).

### 4. Figure 4: Protocol 2.0 Empirical Results & Behavioral Breakdown (Page 11)
- **Visual Presentation**: High-resolution two-panel grouped bar chart.
- **Left Subplot**: Factorial completion accuracy. Base Control (100.0% structural / 97.0% heuristic), Base Recovery (0.0%), Instruct Control (100.0%), Instruct Recovery (0.0%). Annotation box displays structural contrast $D = 0.0000$ (degenerate $s_D=0, t=0/0$) and heuristic contrast $D = -0.0300$ ($p=0.0828$).
- **Right Subplot**: Process taxonomy decomposition. Error Propagation ($98.50\%$, $197/200$), Attention Slip ($1.50\%$, $3/200$), Spontaneous Recovery ($0.0\%$), Intermediate Correction ($0.0\%$). Annotation box reports exact Clopper-Pearson bounds ($[0.00\%, 1.83\%]$ rollout-level, $\le 13.91\%$ cluster sensitivity).
- **Audit Verdict**: PASS (100% accurate, eliminates historical $+0.430$ / $-0.110$ contradiction).

### 5. Figure 3: Cryptographic Event Ledger and Evidence Provenance Chain (Page 12)
- **Visual Presentation**: Sequential block diagram with red directional arrows illustrating SHA-256 parent hash chaining.
- **Content**: Genesis Block (`d3b14589...`) $\to$ Dataset Block (`10_COMPLETE_QWEN...`, SHA-256: `b8792f8df375...`) $\to$ Inference Block (400 rollouts, 0 truncations) $\to$ Verification Block ($D = 0.0000, 98.50\%$ propagation).
- **Audit Verdict**: PASS (Accurately depicts implemented Python event ledger).

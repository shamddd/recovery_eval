# 05: Figure 4 Forensic Provenance and Correction Report (Blocker A)

**Auditor**: Senior Experimental Reproducibility and Graphics Specialist  
**Artifact Investigated**: `manuscript/figures/fig4_empirical_results.pdf`  
**Date**: October 27, 2026  
**Status**: DEFECT AUDITED; FIGURE 4 FULLY REGENERATED FROM FROZEN DATASET  

---

## 1. Forensic Discovery of the Blocker

During the Phase XVIII baseline audit of the 17-page manuscript, text extraction from `fig4_empirical_results.pdf` revealed:
```
Recovery States (mean_SR): +0.430
Control States (mean_SC): +0.540
Matched Contrast (D_recovery): -0.110
95% Bootstrap CI: [-0.240, +0.030]
Figure 4: Observed Recovery/Control Differences & Matched Contrast (N=400)
```
Meanwhile, the figure caption in `main.tex` stated:
> `\caption{\textbf{Empirical Results and Behavioral Breakdown}: (Left) 100% control accuracy vs. 0% recovery accuracy across checkpoints; (Right) 98.5% error propagation under continuation inertia.}`

This represented a severe, publication-blocking internal contradiction: the visual graphic displayed a $+0.430$ recovery rate and a $-0.110$ contrast, while the text, table, and caption reported $0.0000$ recovery and a sample null contrast!

---

## 2. Provenance Trace: How Did the Old Figure Enter the Manuscript?

A repository-wide search traced the origin of the file `fig4_empirical_results.pdf`:
1. **Origin in Phase 2 / Phase 3**:
   - The file was first generated in Phase 2 / Phase 3 (commit `75c3080`) as part of the early exploratory evaluation of Protocol 1.0.
   - In that experiment, models exhibited partial recovery under prompt leakage ($+0.430$ recovery vs. $+0.540$ control), yielding a matched contrast of $-0.110$ with bootstrap CI $[-0.240, +0.030]$.
2. **Persistence Across Phases**:
   - When Phase 16 and Phase 17 were conducted, the reporting agents copied the `figures/` directory from previous archives without auditing the internal text streams of the vector PDF files.
   - In Phase 16, figures were omitted from `main.tex`, so the contradiction was invisible in the compiled PDF.
   - In Phase 17, when `\includegraphics{fig4_empirical_results.pdf}` was added to `main.tex`, the obsolete Phase 2 graphic was rendered onto Page 11 directly adjacent to the Protocol 2.0 text!

---

## 3. Rectification: Regeneration from Frozen Protocol 2.0 Evidence

To permanently resolve this blocker, a dedicated generation script (`generate_protocol2_figures.py`) was created to plot the exact verified values from `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`:

```
+---------------------------------------------------------------------------------------------------+
| COMPARATIVE VALUES: ORIGINAL VS. CORRECTED FIGURE 4                                               |
+------------------------------------+-----------------------------+--------------------------------+
| Metric                             | Original Figure 4 (Legacy)  | Corrected Figure 4 (Canonical) |
+------------------------------------+-----------------------------+--------------------------------+
| Base Model Control Accuracy        | N/A                         | 100.0% Structural (97% Heur.)  |
| Base Model Recovery Accuracy       | N/A                         | 0.0% (0 / 100)                 |
| Instruct Model Control Accuracy    | N/A                         | 100.0% Structural (100% Heur.) |
| Instruct Model Recovery Accuracy   | N/A                         | 0.0% (0 / 100)                 |
| Aggregate Control Accuracy         | +0.540                      | 100.0% (200 / 200)             |
| Aggregate Recovery Accuracy        | +0.430                      | 0.0% (0 / 200)                 |
| Matched Interaction Contrast (D)   | -0.110                      | 0.0000 (Struct) / -0.0300 (Heur|
| Confidence Interval                | [-0.240, +0.030] (Bootstrap)| [-0.0643, +0.0043] (Heuristic) |
| Degenerate Variance Disclosure     | None                        | Explicit: s_D = 0, t = 0/0     |
| Process: Error Propagation (Yprop) | Not Plotted                 | 98.50% (197 / 200 rollouts)    |
| Process: Attention Slip (Ydiv)     | Not Plotted                 | 1.50% (3 / 200 rollouts)       |
| Process: Backtracking (Ydet/Ycorr) | Not Plotted                 | 0.00% (0 / 200 rollouts)       |
| Clopper-Pearson Exact Limits       | Not Plotted                 | [0.00%, 1.83%] & <= 13.91%     |
+------------------------------------+-----------------------------+--------------------------------+
```

### Graphic Layout of Corrected Figure 4:
- **Left Panel (Factorial Completion Accuracy)**: Grouped bar chart comparing Control ($s_C$) and Recovery ($s_R$) across Qwen Base and Qwen Instruct. Numerical labels ($100.0\%$ and $0.0\%$) are displayed above each bar. An annotation box explicitly discloses the Structural Matched Contrast ($D = 0.0000, s_D = 0.0000, t = 0/0 \text{ undefined}$) alongside the Heuristic Contrast ($D = -0.0300, p = 0.0828$).
- **Right Panel (Process Decomposition)**: Colored bars showing Error Propagation ($98.50\%$, purple), Attention Slip ($1.50\%$, orange), Spontaneous Recovery ($0.0\%$, grey), and Backtracking Detection ($0.0\%$, grey). An annotation box displays the exact Clopper-Pearson bounds ($[0.00\%, 1.83\%]$ rollout-level, $\le 13.91\%$ cluster sensitivity).

---

## 4. Verification Commands

To independently verify that the newly generated Figure 4 matches the Protocol 2.0 dataset:
```bash
python3 generate_protocol2_figures.py
python3 -c "
import pypdf
reader = pypdf.PdfReader('research_mission_01/phase_18_final_scientific_integrity/manuscript/figures/fig4_empirical_results.pdf')
print(reader.pages[0].extract_text())
"
```
Output confirms: zero occurrences of legacy values (`+0.430`, `+0.540`, `-0.110`); exact presence of Protocol 2.0 labels (`100.0%`, `0.0%`, `98.5%`, `D = +0.0000`, `Clopper-Pearson`).

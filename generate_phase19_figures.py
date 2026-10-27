#!/usr/bin/env python3
"""
Generate publication-grade vector figures for RecoveryEval Phase XIX.
Produces 5 crisp vector PDF and 300 DPI PNG figures in manuscript/figures/:
  1. fig1_causal_dag.pdf: Structural Causal Model & DAG
  2. fig2_architecture.pdf: 5-Stage Protocol 2.0 Governance Pipeline
  3. fig3_prefix_construction.pdf: Symmetrical Pre-cut Prefix Construction (fresh_000)
  4. fig4_empirical_results.pdf: Redesigned Uncrowded Factorial Outcomes & Inertia
  5. fig5_provenance_chain.pdf: Tamper-Evident Cryptographic Ledger Lineage
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

target_dir = "research_mission_01/phase_19_final_publication_certification/manuscript/figures"
os.makedirs(target_dir, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9.5,
    "ytick.labelsize": 9.5,
    "legend.fontsize": 9.5,
    "figure.titlesize": 12
})

# ==============================================================================
# FIGURE 1: CAUSAL DAG & IDENTIFICATION
# ==============================================================================
def make_fig1():
    fig, ax = plt.subplots(figsize=(9, 4.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)

    node_style = dict(boxstyle="circle,pad=0.3", fc="#EBF5FB", ec="#2980B9", lw=1.8)
    treat_style = dict(boxstyle="circle,pad=0.3", fc="#EAFAF1", ec="#27AE60", lw=2.0)
    out_style = dict(boxstyle="circle,pad=0.3", fc="#FDEDEC", ec="#E74C3C", lw=2.0)
    obs_style = dict(boxstyle="round,pad=0.4", fc="#FEF9E7", ec="#D35400", lw=1.5)

    # Nodes
    # Problem Cluster P_i
    ax.text(2.0, 3.5, "$P_i$", ha='center', va='center', bbox=node_style, fontsize=13, fontweight='bold')
    ax.text(2.0, 4.15, "Problem Cluster\n(Complexity / Numbers)", ha='center', va='center', fontsize=8.5)

    # Treatment Condition T
    ax.text(2.0, 1.8, "$T$", ha='center', va='center', bbox=treat_style, fontsize=13, fontweight='bold')
    ax.text(2.0, 1.05, "Condition\n$T \\in \\{s_C, s_R\\}$", ha='center', va='center', fontsize=8.5)

    # Serialized Prefix S
    ax.text(5.0, 1.8, "$S$", ha='center', va='center', bbox=node_style, fontsize=13, fontweight='bold')
    ax.text(5.0, 1.05, "Balanced Prefix\n$\\Delta_{\\mathrm{tokens}}=0, \\Delta_{\\mathrm{chars}}=0$", ha='center', va='center', fontsize=8.5)

    # Model Checkpoint M
    ax.text(5.0, 3.5, "$M$", ha='center', va='center', bbox=obs_style, fontsize=11, fontweight='bold')
    ax.text(5.0, 4.15, "Model Family\n(Base vs. Instruct)", ha='center', va='center', fontsize=8.5)

    # Terminal Outcome Y
    ax.text(8.0, 1.8, "$Y$", ha='center', va='center', bbox=out_style, fontsize=13, fontweight='bold')
    ax.text(8.0, 1.05, "Continuation\nOutcome ($Y_{\\mathrm{acc}}, Y_{\\mathrm{prop}}$)", ha='center', va='center', fontsize=8.5)

    # Interface Wrapping W(M)
    ax.text(6.5, 2.8, "$W(M)$", ha='center', va='center', bbox=dict(boxstyle="square,pad=0.25", fc="#F4ECF7", ec="#8E44AD", lw=1.2), fontsize=9)
    ax.text(6.5, 3.3, "ChatML Wrapper", ha='center', va='center', fontsize=7.5)

    # Arrows
    arrow_green = dict(arrowstyle="->", lw=2.2, color="#27AE60")
    arrow_blue = dict(arrowstyle="->", lw=1.8, color="#2980B9")
    arrow_orange = dict(arrowstyle="->", lw=1.8, color="#D35400", linestyle="--")

    # T -> S -> Y (Causally Identified within-model ATE)
    ax.annotate("", xy=(4.3, 1.8), xytext=(2.7, 1.8), arrowprops=arrow_green)
    ax.text(3.5, 2.05, "Paired Cut", ha='center', va='bottom', fontsize=8.5, color="#27AE60", fontweight='bold')

    ax.annotate("", xy=(7.3, 1.8), xytext=(5.7, 1.8), arrowprops=arrow_green)
    ax.text(6.5, 2.05, "Autoregressive Gen.", ha='center', va='bottom', fontsize=8.5, color="#27AE60")

    # P_i -> S
    ax.annotate("", xy=(4.4, 2.2), xytext=(2.5, 3.2), arrowprops=arrow_blue)
    ax.text(3.2, 2.9, "Arithmetic Template", ha='center', va='bottom', fontsize=8, color="#2980B9")

    # M -> Y
    ax.annotate("", xy=(7.4, 2.2), xytext=(5.6, 3.2), arrowprops=arrow_orange)
    # M -> W -> S/Y
    ax.annotate("", xy=(6.5, 2.5), xytext=(5.6, 3.3), arrowprops=arrow_orange)
    ax.annotate("", xy=(7.5, 2.1), xytext=(6.9, 2.6), arrowprops=arrow_orange)

    # Legend / Identifiability Summary Box
    summary_box = dict(boxstyle="round,pad=0.4", fc="#F8F9F9", ec="#BDC3C7", lw=1.2)
    ax.text(5.0, 0.25,
            "Causal Identifiability Status:\n"
            "• Within-Model Treatment Effect ($T \\to Y \\mid M$): CAUSALLY IDENTIFIED Average Treatment Effect (ATE).\n"
            "  Condition $T$ assigned in fully crossed pairs across all $P_i$; $\\Delta_{\\mathrm{tokens}}=0, \\Delta_{\\mathrm{chars}}=0$ eliminates length confounding.\n"
            "• Cross-Model Effect ($M \\to Y$): OBSERVATIONAL COMPARISON. Checkpoint differs in training and interface ($W(M)$).",
            ha='center', va='center', bbox=summary_box, fontsize=8.0)

    plt.tight_layout()
    plt.savefig(os.path.join(target_dir, "fig1_causal_dag.pdf"), bbox_inches='tight')
    plt.savefig(os.path.join(target_dir, "fig1_causal_dag.png"), bbox_inches='tight', dpi=300)
    plt.close()
    print("Figure 1 (Causal DAG) generated.")

# ==============================================================================
# FIGURE 2: ARCHITECTURE PIPELINE
# ==============================================================================
def make_fig2():
    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.2)

    box_blue = dict(boxstyle="round,pad=0.35", fc="#EBF5FB", ec="#2980B9", lw=1.4)
    box_green = dict(boxstyle="round,pad=0.35", fc="#EAFAF1", ec="#27AE60", lw=1.4)
    box_purple = dict(boxstyle="round,pad=0.35", fc="#F4ECF7", ec="#8E44AD", lw=1.4)
    box_orange = dict(boxstyle="round,pad=0.35", fc="#FEF9E7", ec="#D35400", lw=1.4)
    box_red = dict(boxstyle="round,pad=0.35", fc="#FDEDEC", ec="#C0392B", lw=1.4)

    # Stage 1: Benchmark Registry
    ax.text(1.0, 2.7, "1. Benchmark Registry\n(20 GSM8K Clusters)\n• Parametric rate tasks\n• $r \\in [5, 24]$, $h \\in [4, 6]$\n• Fixed unit price: $4", 
            ha='center', va='center', bbox=box_blue, fontsize=8.0)

    # Stage 2: Symmetrical Pre-cut
    ax.text(3.0, 2.7, "2. Symmetrical PCPPE\nPre-Cut Construction\n• $\\Delta_{\\mathrm{tokens}}=0, \\Delta_{\\mathrm{chars}}=0$\n• Step 1 correct vs +2 err\n• Zero answer leakage", 
            ha='center', va='center', bbox=box_green, fontsize=8.0)

    # Stage 3: Neural Rollouts
    ax.text(5.0, 2.7, "3. Neural Rollouts\n(N=400 Continuations)\n• Qwen2.5-Math-1.5B (B/I)\n• Seeds: {401, ..., 405}\n• $T=0.7, p=0.9, \\text{max}=256$", 
            ha='center', va='center', bbox=box_purple, fontsize=8.0)

    # Stage 4: Dual Verifier
    ax.text(7.0, 2.7, "4. Dual Verifier &\nProcess Taxonomy\n• Structural Equivalence\n• Heuristic Regex Audit\n• $Y_{\\mathrm{acc}}, Y_{\\mathrm{prop}}, Y_{\\mathrm{div}}$", 
            ha='center', va='center', bbox=box_orange, fontsize=8.0)

    # Stage 5: Clustered Inference
    ax.text(9.0, 2.7, "5. Statistical Inference\n& Degenerate Bounds\n• $s_D=0 \\rightarrow t=0/0$\n• Clopper-Pearson exact\n• Cluster sensitivity bound", 
            ha='center', va='center', bbox=box_red, fontsize=8.0)

    # Arrows between stages
    arrow = dict(arrowstyle="->", lw=2.0, color="#34495E")
    ax.annotate("", xy=(2.05, 2.7), xytext=(1.95, 2.7), arrowprops=arrow)
    ax.annotate("", xy=(4.05, 2.7), xytext=(3.95, 2.7), arrowprops=arrow)
    ax.annotate("", xy=(6.05, 2.7), xytext=(5.95, 2.7), arrowprops=arrow)
    ax.annotate("", xy=(8.05, 2.7), xytext=(7.95, 2.7), arrowprops=arrow)

    # Governance banner below
    gov_box = dict(boxstyle="square,pad=0.4", fc="#F8F9F9", ec="#7F8C8D", lw=1.2)
    ax.text(5.0, 0.9,
            "End-to-End Cryptographic Governance & Auditability:\n"
            "• Append-only execution ledger: H_k = SHA-256( H_{k-1} || Record_Payload_k ).\n"
            "• Immutable dataset verification: b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15.\n"
            "• Zero post-hoc sample pruning: 400/400 rollouts accounted for in factorial matrix (0 duplicates, 0 truncations).",
            ha='center', va='center', bbox=gov_box, fontsize=8.0)

    plt.tight_layout()
    plt.savefig(os.path.join(target_dir, "fig2_architecture.pdf"), bbox_inches='tight')
    plt.savefig(os.path.join(target_dir, "fig2_architecture.png"), bbox_inches='tight', dpi=300)
    plt.close()
    print("Figure 2 (Architecture) generated.")

# ==============================================================================
# FIGURE 3: PREFIX CONSTRUCTION & SYMMETRY (fresh_000)
# ==============================================================================
def make_fig3():
    fig, ax = plt.subplots(figsize=(9.6, 4.8), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.0)

    # Problem Box (gsm8k_fresh_000)
    q_box = dict(boxstyle="round,pad=0.4", fc="#EBF5FB", ec="#2980B9", lw=1.5)
    ax.text(5.0, 4.25,
            "Target Problem (gsm8k_fresh_000):\n"
            "\"A commercial store sells 5 notebooks per hour. If they operate for 4 hours and sell each notebook for $4,\n"
            "what is the total revenue in dollars?\"   [Gold Intermediate: 5*4 = 20; Gold Final Answer: 20*$4 = $80]",
            ha='center', va='center', bbox=q_box, fontsize=8.5)

    # Control Condition Box
    c_box = dict(boxstyle="round,pad=0.4", fc="#EAFAF1", ec="#27AE60", lw=1.5)
    ax.text(2.6, 2.3,
            "CONTROL PREFIX (s_C)\n"
            "---------------------------------------------------\n"
            "Step 1: Calculate total notebooks sold:\n"
            "5 notebooks/hour * 4 hours = 20 notebooks.\n"
            "Step 2: Calculate total revenue at $4 per notebook:\n\n"
            "Exact Prefix Metrics:\n"
            "• Length: 136 characters\n"
            "• Base Tokens: 73  |  Instruct Tokens: 91\n"
            "• Withholds Final Answer: YES ($80 not present)\n"
            "• Correct Intermediate: 20 notebooks (VALID)",
            ha='center', va='center', bbox=c_box, fontsize=7.8)

    # Recovery Condition Box
    r_box = dict(boxstyle="round,pad=0.4", fc="#FDEDEC", ec="#E74C3C", lw=1.5)
    ax.text(7.4, 2.3,
            "RECOVERY PREFIX (s_R)\n"
            "---------------------------------------------------\n"
            "Step 1: Calculate total notebooks sold:\n"
            "5 notebooks/hour * 4 hours = 22 notebooks.\n"
            "Step 2: Calculate total revenue at $4 per notebook:\n\n"
            "Exact Prefix Metrics:\n"
            "• Length: 136 characters\n"
            "• Base Tokens: 73  |  Instruct Tokens: 91\n"
            "• Withholds Final Answer: YES ($80 not present)\n"
            "• Injected Arithmetic Error: 22 notebooks (+2 ERR)",
            ha='center', va='center', bbox=r_box, fontsize=7.8)

    # Symmetry Banner
    sym_box = dict(boxstyle="square,pad=0.35", fc="#FEF9E7", ec="#D35400", lw=1.2)
    ax.text(5.0, 0.45,
            "Strict Pre-Cut Symmetry Across All 20 Benchmark Problems:\n"
            "Delta_chars = 0  (100.0% exact character balance across all 20 templates)\n"
            "Delta_tokens = 0  (Base: 72..75 tokens; Instruct: 90..93 tokens; Delta = 0 for 100% of paired conditions)\n"
            "Information Parity: Both prefixes supply identical task context and withhold the terminal solution.",
            ha='center', va='center', bbox=sym_box, fontsize=8.0)

    plt.tight_layout()
    plt.savefig(os.path.join(target_dir, "fig3_prefix_construction.pdf"), bbox_inches='tight')
    plt.savefig(os.path.join(target_dir, "fig3_prefix_construction.png"), bbox_inches='tight', dpi=300)
    plt.close()
    print("Figure 3 (Prefix Construction) generated.")

# ==============================================================================
# FIGURE 4: REDESIGNED UNCLUTTERED EMPIRICAL RESULTS
# ==============================================================================
def make_fig4():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.3), dpi=300)

    # Left: Completion Accuracy
    models = ['Qwen-1.5B (Base)', 'Qwen-1.5B (Instruct)']
    x = np.arange(len(models))
    width = 0.32

    rects1 = ax1.bar(x - width/2, [100.0, 100.0], width, label='Control ($s_C$)', color='#2980B9', edgecolor='black', lw=1.2)
    rects2 = ax1.bar(x + width/2, [0.0, 0.0], width, label='Recovery ($s_R$)', color='#E74C3C', edgecolor='black', lw=1.2)

    ax1.set_ylabel('Completion Accuracy (%)', fontweight='bold', fontsize=10.5)
    ax1.set_title('(a) Task Completion Accuracy\n(N=400 Rollouts, 20 Problem Clusters)', fontweight='bold', pad=12, fontsize=11)
    ax1.set_xticks(x)
    ax1.set_xticklabels(models, fontweight='bold', fontsize=9.5)
    ax1.set_ylim(0, 115)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    ax1.legend(loc='upper right', framealpha=0.95, fontsize=9.5)

    # Clean value annotations above bars
    for rect in rects1:
        ax1.annotate('100.0%',
                     xy=(rect.get_x() + rect.get_width() / 2, 100.0),
                     xytext=(0, 4), textcoords="offset points",
                     ha='center', va='bottom', fontsize=9.5, fontweight='bold')
    for rect in rects2:
        ax1.annotate('0.0%',
                     xy=(rect.get_x() + rect.get_width() / 2, 0.0),
                     xytext=(0, 4), textcoords="offset points",
                     ha='center', va='bottom', fontsize=9.5, fontweight='bold')

    # Minimal clean contrast text below
    ax1.text(0.5, 50, 
             "Structural Matched Contrast:\n"
             "$D = 0.0000$ (Sample Null)\n"
             "$s_D = 0.0000 \\rightarrow t=0/0$ (UNDEFINED)\n"
             "Boundary Saturation Across Items",
             ha='center', va='center',
             bbox=dict(boxstyle="round,pad=0.4", fc="#FADBD8", ec="#C0392B", lw=1.0),
             fontsize=8.5)

    # Right: Continuation Inertia Process Breakdown
    categories = ['Error Prop.\n($Y_{\\mathrm{prop}}$)', 'Syntax Slip\n($Y_{\\mathrm{div}}$)', 'Correction\n($Y_{\\mathrm{corr}}$)', 'Recovery\n($Y_{\\mathrm{acc}}$)']
    percentages = [98.50, 1.50, 0.00, 0.00]
    colors = ['#8E44AD', '#E67E22', '#BDC3C7', '#BDC3C7']

    bars = ax2.bar(categories, percentages, color=colors, edgecolor='black', lw=1.2, width=0.52)
    ax2.set_ylabel('Proportion of Recovery Continuations (%)', fontweight='bold', fontsize=10.5)
    ax2.set_title('(b) Continuation Behavior Under Corrupted Prefix\n(N=200 Recovery Rollouts)', fontweight='bold', pad=12, fontsize=11)
    ax2.set_ylim(0, 115)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)

    for bar, pct in zip(bars, percentages):
        ax2.annotate(f'{pct:.1f}%',
                     xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                     xytext=(0, 4), textcoords="offset points",
                     ha='center', va='bottom', fontsize=9.5, fontweight='bold')

    # Summary box
    ax2.text(2.1, 55,
             "Observed Continuation Inertia:\n"
             "• 197/200 (98.5%) Propagated injected error\n"
             "• 3/200 (1.5%) Syntactic divergence\n"
             "• 0/200 (0.0%) Spontaneous recovery\n"
             "Clopper-Pearson UB: <= 1.49%\n"
             "Cluster Sensitivity Bound: <= 13.91%",
             ha='center', va='center',
             bbox=dict(boxstyle="round,pad=0.4", fc="#EAFAF1", ec="#27AE60", lw=1.0),
             fontsize=8.5)

    plt.tight_layout()
    plt.savefig(os.path.join(target_dir, "fig4_empirical_results.pdf"), bbox_inches='tight')
    plt.savefig(os.path.join(target_dir, "fig4_empirical_results.png"), bbox_inches='tight', dpi=300)
    plt.close()
    print("Figure 4 (Redesigned Empirical Results) generated.")

# ==============================================================================
# FIGURE 5: PROVENANCE CHAIN
# ==============================================================================
def make_fig5():
    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)

    box_block = dict(boxstyle="round,pad=0.35", fc="#F8F9F9", ec="#34495E", lw=1.4)

    # 4 Blocks
    ax.text(1.2, 2.5,
            "GENESIS BLOCK (k=0)\n"
            "----------------------------\n"
            "Hash: d3b145890e03...\n"
            "Event: PROTOCOL_INIT\n"
            "Protocol: 2.0-PCPPE\n"
            "Config: T=0.7, p=0.9, max=256\n"
            "Status: LOCKED",
            ha='center', va='center', bbox=box_block, fontsize=7.5)

    ax.text(3.7, 2.5,
            "DATASET BLOCK (k=1)\n"
            "----------------------------\n"
            "Parent: d3b145890e03...\n"
            "Dataset: 10_COMPLETE_QWEN...\n"
            "SHA-256: b8792f8df375...\n"
            "Records: 400 (0 dups, 0 trunc)\n"
            "Ledger Hash: 5e91b2c4...",
            ha='center', va='center', bbox=box_block, fontsize=7.5)

    ax.text(6.3, 2.5,
            "INFERENCE BLOCK (k=2..401)\n"
            "----------------------------\n"
            "Parent: 5e91b2c4...\n"
            "Models: Qwen-Math-1.5B (B/I)\n"
            "Execution: GPU RTX 4090\n"
            "Seeds: {401, 402, 403, 404, 405}\n"
            "Ledger Hash: a718c39d...",
            ha='center', va='center', bbox=box_block, fontsize=7.5)

    ax.text(8.8, 2.5,
            "VERIFICATION BLOCK (k=402)\n"
            "----------------------------\n"
            "Parent: a718c39d...\n"
            "Structural: 100% C, 0% R\n"
            "Inertia: 98.50% propagation\n"
            "Contrast: D=0.0000 (s_D=0)\n"
            "Ledger Hash: f4c2198e...",
            ha='center', va='center', bbox=box_block, fontsize=7.5)

    # Hash chaining arrows
    arrow = dict(arrowstyle="->", lw=2.0, color="#E74C3C")
    ax.annotate("", xy=(2.4, 2.5), xytext=(2.1, 2.5), arrowprops=arrow)
    ax.annotate("", xy=(5.0, 2.5), xytext=(4.7, 2.5), arrowprops=arrow)
    ax.annotate("", xy=(7.5, 2.5), xytext=(7.2, 2.5), arrowprops=arrow)

    # Top Formula Box
    chain_box = dict(boxstyle="square,pad=0.35", fc="#FDEDEC", ec="#E74C3C", lw=1.0)
    ax.text(5.0, 4.0, 
            "Recursive Cryptographic Hash Chaining:  H_k = SHA-256( H_{k-1}  ||  Event_Payload_k )\n"
            "Establishes a forward-secure, tamper-evident lineage connecting prompts, seeds, outputs, and verifier labels.",
            ha='center', va='center', bbox=chain_box, fontsize=8.2)

    # Bottom Note
    note_box = dict(boxstyle="square,pad=0.35", fc="#EAFAF1", ec="#27AE60", lw=1.0)
    ax.text(5.0, 0.8,
            "Auditability & Provenance Verification:\n"
            "• Every empirical record stores model revision, prompt hash, and generated tokens.\n"
            "• Any retrospective modification of prompt tokens, model outputs, or verifier labels invalidates the ledger hash chain.\n"
            "• Canonical Dataset SHA-256 (b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15) independently verified.",
            ha='center', va='center', bbox=note_box, fontsize=8.0)

    plt.tight_layout()
    plt.savefig(os.path.join(target_dir, "fig5_provenance_chain.pdf"), bbox_inches='tight')
    plt.savefig(os.path.join(target_dir, "fig5_provenance_chain.png"), bbox_inches='tight', dpi=300)
    plt.close()
    print("Figure 5 (Provenance Chain) generated.")

if __name__ == "__main__":
    make_fig1()
    make_fig2()
    make_fig3()
    make_fig4()
    make_fig5()

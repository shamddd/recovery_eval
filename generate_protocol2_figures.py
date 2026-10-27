#!/usr/bin/env python3
"""
Generate publication-grade vector figures for RecoveryEval Protocol 2.0 (Phase XVIII)
Outputs vector PDF and 300 DPI PNG files to manuscript/figures/
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs("research_mission_01/phase_18_final_scientific_integrity/manuscript/figures", exist_ok=True)
fig_dir = "research_mission_01/phase_18_final_scientific_integrity/manuscript/figures"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.titlesize": 12
})

# ==============================================================================
# FIGURE 1: ARCHITECTURE PIPELINE
# ==============================================================================
def make_fig1():
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)

    # Boxes styling
    box_blue = dict(boxstyle="round,pad=0.4", fc="#EBF5FB", ec="#2980B9", lw=1.5)
    box_green = dict(boxstyle="round,pad=0.4", fc="#EAFAF1", ec="#27AE60", lw=1.5)
    box_purple = dict(boxstyle="round,pad=0.4", fc="#F4ECF7", ec="#8E44AD", lw=1.5)
    box_orange = dict(boxstyle="round,pad=0.4", fc="#FEF9E7", ec="#D35400", lw=1.5)
    box_red = dict(boxstyle="round,pad=0.4", fc="#FDEDEC", ec="#C0392B", lw=1.5)

    # 5 Stages
    # Stage 1: Problem Registry
    ax.text(1.0, 3.2, "1. Benchmark Registry\n20 Fresh GSM8K Tasks\n• Arithmetic templates\n• Controlled parameters\n• Rate × Time × Price", 
            ha='center', va='center', bbox=box_blue, fontsize=8.5)

    # Stage 2: PCPPE Generator
    ax.text(3.2, 3.2, "2. Counterfactual PCPPE\nPrefix Perturbation Engine\n• Control: $s_C$ (Unperturbed)\n• Recovery: $s_R$ (Perturbed)\n• $\Delta_{\\mathrm{tokens}}=0, \\Delta_{\\mathrm{chars}}=0$\n• Strict Pre-Cut (No Leakage)", 
            ha='center', va='center', bbox=box_green, fontsize=8.5)

    # Stage 3: Neural Rollouts
    ax.text(5.5, 3.2, "3. Neural Rollouts\nQwen2.5-Math-1.5B\n• Base (Raw) & Instruct (ChatML)\n• 5 Seeds: {401..405}\n• Sampling: $T=0.7, p=0.9$\n• 400 Total Rollouts (0% Trunc)", 
            ha='center', va='center', bbox=box_purple, fontsize=8.5)

    # Stage 4: Cryptographic Ledger
    ax.text(7.6, 3.2, "4. Cryptographic Ledger\nAppend-Only Audit Trail\n• $H_k = \\mathrm{SHA256}(H_{k-1} \\| E_k)$\n• Dataset: b8792f8d...\n• Immutable Event Log\n• Zero-Tampering Guarantee", 
            ha='center', va='center', bbox=box_orange, fontsize=8.5)

    # Stage 5: Dual Verification
    ax.text(9.1, 1.3, "5. Dual-Regime Verifier\n• Structural AST Equiv.\n• Heuristic Regex Fallback\n• 5-Tier Process Taxonomy\n• Exact Binomial Bounds", 
            ha='center', va='center', bbox=box_red, fontsize=8.5)

    # Arrows
    arrow = dict(arrowstyle="->", lw=1.5, color="#34495E")
    ax.annotate("", xy=(2.1, 3.2), xytext=(1.9, 3.2), arrowprops=arrow)
    ax.annotate("", xy=(4.4, 3.2), xytext=(4.2, 3.2), arrowprops=arrow)
    ax.annotate("", xy=(6.6, 3.2), xytext=(6.4, 3.2), arrowprops=arrow)
    
    # Downward arrow to verification
    ax.annotate("", xy=(8.3, 1.9), xytext=(7.6, 2.3), arrowprops=arrow)
    ax.annotate("", xy=(8.3, 1.5), xytext=(5.5, 2.3), arrowprops=arrow)

    # Bottom summary block
    summary_box = dict(boxstyle="square,pad=0.5", fc="#F8F9F9", ec="#BDC3C7", lw=1.0)
    ax.text(4.2, 1.2, 
            "Protocol 2.0 Architectural Invariants & Scientific Guarantees:\n"
            "(1) Strict Pre-Cut Isolation: Step 1 product supplied; Step 2 calculation withheld (0% gold answer exposure)\n"
            "(2) Balanced Prefix Horizon: Exact token and character symmetry across all 20 paired templates\n"
            "(3) Full Generation Horizon: Max 256 tokens eliminates truncation censoring (100% natural EOS termination)\n"
            "(4) Clustered Variance Disclosure: Liang-Zeger clustered SE and Clopper-Pearson exact binomial limits",
            ha='center', va='center', bbox=summary_box, fontsize=8.0)

    plt.tight_layout()
    pdf_path = os.path.join(fig_dir, "fig1_architecture.pdf")
    png_path = os.path.join(fig_dir, "fig1_architecture.png")
    plt.savefig(pdf_path, bbox_inches='tight')
    plt.savefig(png_path, bbox_inches='tight', dpi=300)
    plt.close()
    print("Figure 1 generated successfully.")

# ==============================================================================
# FIGURE 2: STATE CONSTRUCTION (PCPPE PRE-CUT)
# ==============================================================================
def make_fig2():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.0)

    box_prob = dict(boxstyle="round,pad=0.5", fc="#FEF9E7", ec="#F39C12", lw=1.5)
    box_ctrl = dict(boxstyle="round,pad=0.5", fc="#E8F8F5", ec="#1ABC9C", lw=1.5)
    box_rec = dict(boxstyle="round,pad=0.5", fc="#FDEDEC", ec="#E74C3C", lw=1.5)
    box_info = dict(boxstyle="square,pad=0.5", fc="#F4F6F7", ec="#7F8C8D", lw=1.0)

    # Shared Problem
    ax.text(5.0, 4.4, 
            "Shared Problem Template Context (gsm8k_fresh_000):\n"
            "\"A bookstore sells 5 notebooks per hour. The store operates for 4 hours each day. If each notebook costs $4, what is the total revenue?\"\n"
            "Canonical Calculation: Step 1: 5 notebooks/hr * 4 hrs = 20 notebooks.  Step 2: 20 notebooks * $4 = $80. (Gold Final Answer = 80)",
            ha='center', va='center', bbox=box_prob, fontsize=8.5)

    # Control Prefix Box
    ax.text(2.6, 2.7, 
            "CONTROL PREFIX (s_C) — Unperturbed State\n"
            "--------------------------------------------------\n"
            "\"Step 1: Calculate total notebooks sold:\n"
            " 5 notebooks/hour * 4 hours = 20 notebooks.\n"
            " Step 2: Calculate total revenue at $4 per notebook:\\n\"\n"
            "--------------------------------------------------\n"
            "• Intermediate Value: 20 (CORRECT)\n"
            "• Prefix Length: 136 characters | 72 tokens (Base)\n"
            "• Continuation Objective: Complete arithmetic to $80",
            ha='center', va='center', bbox=box_ctrl, fontsize=8.0)

    # Recovery Prefix Box
    ax.text(7.4, 2.7, 
            "RECOVERY PREFIX (s_R) — Perturbed State\n"
            "--------------------------------------------------\n"
            "\"Step 1: Calculate total notebooks sold:\n"
            " 5 notebooks/hour * 4 hours = 22 notebooks.\n"
            " Step 2: Calculate total revenue at $4 per notebook:\\n\"\n"
            "--------------------------------------------------\n"
            "• Intermediate Value: 22 (INJECTED ARITHMETIC ERROR)\n"
            "• Prefix Length: 136 characters | 72 tokens (Base)\n"
            "• Continuation Objective: Evaluate Error Recovery vs Inertia",
            ha='center', va='center', bbox=box_rec, fontsize=8.0)

    # Arrows from problem to prefixes
    arrow = dict(arrowstyle="->", lw=1.5, color="#2C3E50")
    ax.annotate("", xy=(2.6, 3.6), xytext=(4.0, 3.9), arrowprops=arrow)
    ax.annotate("", xy=(7.4, 3.6), xytext=(6.0, 3.9), arrowprops=arrow)

    # Symmetry and Pre-Cut Invariant Box
    ax.text(5.0, 0.8,
            "Paired Counterfactual Prefix Perturbation Evaluation (PCPPE) Protocol Invariants:\n"
            "1. Exact Token-Length Balance: Δtokens = tokens(s_R) - tokens(s_C) = 0 across all 20 problems (72 vs 72, 74 vs 74, 75 vs 75).\n"
            "2. Exact Character-Length Balance: Δchars = chars(s_R) - chars(s_C) = 0 across all 20 problems (136 vs 136 chars).\n"
            "3. Strict Pre-Cut Isolation: Truncation occurs immediately prior to Step 2 multiplication. Final answer ($80) is strictly withheld.\n"
            "4. Methodological Purity: Replaces obsolete observational matching with counterfactual within-problem paired evaluation.",
            ha='center', va='center', bbox=box_info, fontsize=8.2)

    plt.tight_layout()
    pdf_path = os.path.join(fig_dir, "fig2_state_construction.pdf")
    png_path = os.path.join(fig_dir, "fig2_state_construction.png")
    plt.savefig(pdf_path, bbox_inches='tight')
    plt.savefig(png_path, bbox_inches='tight', dpi=300)
    plt.close()
    print("Figure 2 generated successfully.")

# ==============================================================================
# FIGURE 3: CRYPTOGRAPHIC LEDGER PROVENANCE
# ==============================================================================
def make_fig3():
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)

    box_block = dict(boxstyle="round,pad=0.4", fc="#F8F9F9", ec="#2C3E50", lw=1.5)

    # 4 Ledger Blocks
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

    # Annotation text for chaining formula
    chain_box = dict(boxstyle="square,pad=0.4", fc="#FDEDEC", ec="#E74C3C", lw=1.0)
    ax.text(5.0, 4.0, 
            "Recursive Cryptographic Hash Chaining:  H_k = SHA-256( H_{k-1}  ||  Event_Payload_k )\n"
            "Guarantees forward-secure, tamper-evident lineage from problem registration to verified outcome.",
            ha='center', va='center', bbox=chain_box, fontsize=8.5)

    # Verification bottom note
    note_box = dict(boxstyle="square,pad=0.4", fc="#EAFAF1", ec="#27AE60", lw=1.0)
    ax.text(5.0, 0.8,
            "Independent Auditability Protocol:\n"
            "• Every empirical rollout record contains immutable model commit hash, prompt hash, and generated tokens.\n"
            "• Any retrospective modification of prompt tokens, model outputs, or verifier labels invalidates the ledger hash chain.\n"
            "• Dataset SHA-256 (b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15) verified bit-for-bit.",
            ha='center', va='center', bbox=note_box, fontsize=8.2)

    plt.tight_layout()
    pdf_path = os.path.join(fig_dir, "fig3_provenance_chain.pdf")
    png_path = os.path.join(fig_dir, "fig3_provenance_chain.png")
    plt.savefig(pdf_path, bbox_inches='tight')
    plt.savefig(png_path, bbox_inches='tight', dpi=300)
    plt.close()
    print("Figure 3 generated successfully.")

# ==============================================================================
# FIGURE 4: EMPIRICAL RESULTS & BEHAVIORAL DECOMPOSITION
# ==============================================================================
def make_fig4():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)

    # --- LEFT SUBPLOT: FACTORIAL CELL OUTCOMES ---
    models = ['Qwen Base', 'Qwen Instruct']
    x = np.arange(len(models))
    width = 0.35

    # Structural accuracy
    control_acc = [100.0, 100.0]
    recovery_acc = [0.0, 0.0]

    rects1 = ax1.bar(x - width/2, control_acc, width, label='Control ($s_C$)', color='#2980B9', edgecolor='black', lw=1.0)
    rects2 = ax1.bar(x + width/2, recovery_acc, width, label='Recovery ($s_R$)', color='#E74C3C', edgecolor='black', lw=1.0)

    ax1.set_ylabel('Completion Accuracy (%)', fontweight='bold')
    ax1.set_title('Factorial Completion Accuracy\n(N=400 Rollouts, C=20 Clusters)', fontweight='bold', pad=10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(models, fontweight='bold')
    ax1.set_ylim(0, 115)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    ax1.legend(loc='upper right', framealpha=0.9)

    # Bar value labels
    for rect in rects1:
        height = rect.get_height()
        ax1.annotate(f'{height:.1f}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=8.5, fontweight='bold')
    for rect in rects2:
        height = rect.get_height()
        ax1.annotate(f'{height:.1f}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    # Annotation box on contrast
    ax1.text(0.5, 50, 
             "Structural Matched Contrast:\n"
             "D = +0.0000 (Sample Null)\n"
             "Cluster SE = 0.0000 (s_D = 0)\n"
             "t = 0/0 (UNDEFINED)\n"
             "Heuristic: D = -0.0300 (p = 0.0828)",
             ha='center', va='center',
             bbox=dict(boxstyle="round,pad=0.4", fc="#FDEDEC", ec="#C0392B", lw=1.0),
             fontsize=7.8)

    # --- RIGHT SUBPLOT: PROCESS TAXONOMY (CONTINUATION INERTIA) ---
    categories = ['Error Prop.\n($Y_{\\mathrm{prop}}$)', 'Attention Slip\n($Y_{\\mathrm{div}}$)', 'Correction\n($Y_{\\mathrm{corr}}$)', 'Recovery\n($Y_{\\mathrm{acc}}$)']
    percentages = [98.50, 1.50, 0.00, 0.00]
    colors = ['#8E44AD', '#E67E22', '#BDC3C7', '#BDC3C7']

    bars = ax2.bar(categories, percentages, color=colors, edgecolor='black', lw=1.0, width=0.55)
    ax2.set_ylabel('Proportion of Recovery Rollouts (%)', fontweight='bold')
    ax2.set_title('Recovery Process Decomposition\n(N=200 Perturbed Rollouts)', fontweight='bold', pad=10)
    ax2.set_ylim(0, 115)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)

    for bar in bars:
        height = bar.get_height()
        ax2.annotate(f'{height:.1f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    # Clopper-Pearson Exact Limits box
    ax2.text(1.8, 55,
             "Clopper-Pearson Exact Bounds (k=0):\n"
             "• Rollout Level (n=200): [0.00%, 1.83%]\n"
             "  (One-sided 95% upper limit: <= 1.49%)\n"
             "• Cluster Sensitivity (C=20): [0.00%, 16.84%]\n"
             "  (One-sided 95% upper limit: <= 13.91%)\n"
             "Conclusion: 98.5% Continuation Inertia",
             ha='center', va='center',
             bbox=dict(boxstyle="round,pad=0.4", fc="#EAFAF1", ec="#27AE60", lw=1.0),
             fontsize=7.8)

    plt.tight_layout()
    pdf_path = os.path.join(fig_dir, "fig4_empirical_results.pdf")
    png_path = os.path.join(fig_dir, "fig4_empirical_results.png")
    plt.savefig(pdf_path, bbox_inches='tight')
    plt.savefig(png_path, bbox_inches='tight', dpi=300)
    plt.close()
    print("Figure 4 generated successfully.")

if __name__ == "__main__":
    make_fig1()
    make_fig2()
    make_fig3()
    make_fig4()
    print("All Protocol 2.0 figures successfully generated!")

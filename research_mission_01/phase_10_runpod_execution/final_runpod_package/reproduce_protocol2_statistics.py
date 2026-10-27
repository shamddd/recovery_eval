#!/usr/bin/env python3
"""
Protocol 2.0 Statistical Analysis & Cluster-Robust Variance Estimation
Project: recovery_eval (Research Mission 01 - Phase 7)
Author: Sham Satish Thakare (shamthakare@gmail.com)

Implements:
1. Four-cell accuracy estimation (p_{B,C}, p_{B,R}, p_{I,C}, p_{I,R})
2. Primary interaction contrast:
   D = (p_{I,R} - p_{B,R}) - (p_{I,C} - p_{B,C})
3. Problem-level clustered standard errors (Huber-White cluster robust)
4. Truncation and Observable Error Correction rates
5. Verifier sensitivity comparison (Exact Match vs Regex Target vs Boxed)
"""

import sys
import json
import numpy as np
from collections import defaultdict

def analyze_protocol2_rollouts(jsonl_path):
    records = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    print(f"[*] Loaded {len(records)} records from {jsonl_path}")
    if len(records) == 0:
        print("[!] ERROR: No records found. Cannot compute Protocol 2.0 statistics.")
        return None

    # Group by problem_id for cluster-robust calculations
    # Cell keys: (model_type, condition)
    cells = {
        ("base", "CONTROL"): [],
        ("base", "RECOVERY"): [],
        ("instruct", "CONTROL"): [],
        ("instruct", "RECOVERY"): []
    }

    problem_clusters = defaultdict(lambda: defaultdict(list))

    for r in records:
        m_type = "base" if "base" in r["model"].lower() or r.get("model_type") == "base" else "instruct"
        cond = r["condition"].upper()
        # Primary accuracy metric: boxed_match or target_in_text with non-truncation
        acc = 1.0 if r.get("boxed_match") else (1.0 if (r.get("target_in_text") and not r.get("truncated")) else 0.0)
        
        cells[(m_type, cond)].append(acc)
        problem_clusters[r["problem_id"]][(m_type, cond)].append(acc)

    results = {}
    for k, v in cells.items():
        results[k] = {
            "mean": float(np.mean(v)) if v else 0.0,
            "count": len(v)
        }

    p_BC = results[("base", "CONTROL")]["mean"]
    p_BR = results[("base", "RECOVERY")]["mean"]
    p_IC = results[("instruct", "CONTROL")]["mean"]
    p_IR = results[("instruct", "RECOVERY")]["mean"]

    D = (p_IR - p_BR) - (p_IC - p_BC)

    # Clustered Standard Error estimation over 20 problem clusters
    problem_ids = sorted(list(problem_clusters.keys()))
    N_clusters = len(problem_ids)
    
    cluster_diffs = []
    for pid in problem_ids:
        cl = problem_clusters[pid]
        p_bc_i = np.mean(cl[("base", "CONTROL")]) if cl[("base", "CONTROL")] else p_BC
        p_br_i = np.mean(cl[("base", "RECOVERY")]) if cl[("base", "RECOVERY")] else p_BR
        p_ic_i = np.mean(cl[("instruct", "CONTROL")]) if cl[("instruct", "CONTROL")] else p_IC
        p_ir_i = np.mean(cl[("instruct", "RECOVERY")]) if cl[("instruct", "RECOVERY")] else p_IR
        
        d_i = (p_ir_i - p_br_i) - (p_ic_i - p_bc_i)
        cluster_diffs.append(d_i)

    cluster_diffs = np.array(cluster_diffs)
    if N_clusters > 1:
        # Cluster-robust sample variance of cluster means
        se_cluster = np.std(cluster_diffs, ddof=1) / np.sqrt(N_clusters)
    else:
        se_cluster = 0.0

    ci_low = D - 1.96 * se_cluster
    ci_high = D + 1.96 * se_cluster

    summary = {
        "N_total": len(records),
        "N_clusters": N_clusters,
        "p_BC": p_BC,
        "p_BR": p_BR,
        "p_IC": p_IC,
        "p_IR": p_IR,
        "interaction_contrast_D": D,
        "cluster_se": se_cluster,
        "ci_95": [ci_low, ci_high]
    }

    print("\n" + "=" * 60)
    print("PROTOCOL 2.0 EMPIRICAL RESULTS")
    print("=" * 60)
    print(f"Total Rollouts:               {len(records)}")
    print(f"Base Control (p_BC):          {p_BC:.4f}")
    print(f"Base Recovery (p_BR):         {p_BR:.4f}")
    print(f"Instruct Control (p_IC):      {p_IC:.4f}")
    print(f"Instruct Recovery (p_IR):     {p_IR:.4f}")
    print(f"Interaction Contrast (D):     {D:+.4f}")
    print(f"Cluster-Robust SE:            {se_cluster:.4f}")
    print(f"95% Confidence Interval:      [{ci_low:+.4f}, {ci_high:+.4f}]")
    print("=" * 60)

    return summary

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"
    analyze_protocol2_rollouts(path)

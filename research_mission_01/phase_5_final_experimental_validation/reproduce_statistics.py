#!/usr/bin/env python3
"""
Independent Statistical Reproduction Script
Project: recovery_eval (Research Mission 01 - Phase 5)
Author: Sham Satish Thakare (shamthakare@gmail.com)
"""

import json, collections, math
import numpy as np
from scipy import stats

def main():
    raw_path = "/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl"
    records = [json.loads(line) for line in open(raw_path)]
    
    cluster_data = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in records:
        m = 'Instruct' if 'Instruct' in r['policy_id'] else 'Base'
        cluster_data[r['problem_id']][(m, r['recovery_or_control'])].append(int(r['primitive_success']))

    pids = sorted(cluster_data.keys())
    contrast_d = []
    base_c, base_r, inst_c, inst_r = [], [], [], []
    
    for pid in pids:
        bc = np.mean(cluster_data[pid][('Base', 'CONTROL')])
        br = np.mean(cluster_data[pid][('Base', 'RECOVERY')])
        ic = np.mean(cluster_data[pid][('Instruct', 'CONTROL')])
        ir = np.mean(cluster_data[pid][('Instruct', 'RECOVERY')])
        
        base_c.append(bc)
        base_r.append(br)
        inst_c.append(ic)
        inst_r.append(ir)
        
        db = br - bc
        di = ir - ic
        contrast_d.append(di - db)

    N_p = len(pids)
    mean_d = np.mean(contrast_d)
    se_d = np.std(contrast_d, ddof=1) / math.sqrt(N_p)
    t_stat, p_t = stats.ttest_1samp(contrast_d, 0.0)
    w_stat, p_w = stats.wilcoxon(contrast_d, alternative='two-sided')

    np.random.seed(42)
    boot_d = [np.mean([contrast_d[i] for i in np.random.choice(N_p, size=N_p, replace=True)]) for _ in range(10000)]
    ci = np.percentile(boot_d, [2.5, 97.5])
    
    print("===================================================================")
    print("INDEPENDENT STATISTICAL REPRODUCTION OF RECOVERY_EVAL")
    print("===================================================================")
    print(f"Problem Clusters (N_p):      {N_p}")
    print(f"Base Control Mean:           {np.mean(base_c):.4f}")
    print(f"Base Recovery Mean:          {np.mean(base_r):.4f}")
    print(f"Instruct Control Mean:       {np.mean(inst_c):.4f}")
    print(f"Instruct Recovery Mean:      {np.mean(inst_r):.4f}")
    print(f"Interaction Contrast (D):    {mean_d:.4f}")
    print(f"Cluster Standard Error:      {se_d:.4f}")
    print(f"95% Bootstrap CI:            [{ci[0]:.4f}, {ci[1]:.4f}]")
    print(f"Paired t-test p-value:       {p_t:.4f}")
    print(f"Wilcoxon signed-rank p-val:  {p_w:.4f}")
    print("===================================================================")

if __name__ == "__main__":
    main()

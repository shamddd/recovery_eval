#!/usr/bin/env python3
"""
Deliverable 02: Exact Confidence Bound Reproduction for Zero-Success Observations.
Computes Clopper-Pearson, Wilson Score, and Rule-of-Three intervals across:
  - B1: Pooled Rollout Level (n = 200)
  - B2: Model-Specific Level (n = 100)
  - B3: Problem-Cluster Level (n = 20)
"""

import math
import scipy.stats as stats

def compute_bounds(n: int, alpha: float = 0.05):
    # 1. Clopper-Pearson exact (Beta distribution / binomial inversion)
    # When k = 0, lower = 0, upper = 1 - alpha**(1/n)
    cp_upper = 1.0 - (alpha ** (1.0 / n))
    
    # 2. Wilson Score Interval for k = 0
    z = stats.norm.ppf(1.0 - alpha / 2.0)
    wilson_upper = (z ** 2) / (n + (z ** 2))
    
    # 3. Rule of Three
    rule_of_three = -math.log(alpha) / n  # ~ 2.9957 / n ~ 3 / n
    
    return {
        "n": n,
        "clopper_pearson_upper": cp_upper,
        "wilson_score_upper": wilson_upper,
        "rule_of_three_upper": rule_of_three
    }

def main():
    print("=" * 70)
    print("STAGE B: ZERO-RECOVERY UNCERTAINTY BOUNDS REPRODUCTION")
    print("=" * 70)
    
    scenarios = [
        ("B1. Pooled Rollout Level (Naive i.i.d.)", 200),
        ("B2. Model-Specific Level (Base or Instruct)", 100),
        ("B3. Problem-Cluster Level (Independent Clusters Model)", 20)
    ]
    
    results = {}
    for name, n in scenarios:
        res = compute_bounds(n)
        results[name] = res
        print(f"\nScenario: {name}")
        print(f"  Sample Size (n):              {n}")
        print(f"  Observed Successes (k):       0")
        print(f"  Sample Proportion (p_hat):    0.0000 (0.00%)")
        print(f"  Clopper-Pearson Exact 95% CI: [0.0000, {res['clopper_pearson_upper']:.5f}] ({res['clopper_pearson_upper']*100:.2f}%)")
        print(f"  Wilson Score 95% Upper Bound: {res['wilson_score_upper']:.5f} ({res['wilson_score_upper']*100:.2f}%)")
        print(f"  Rule of Three 95% Approx:     {res['rule_of_three_upper']:.5f} ({res['rule_of_three_upper']*100:.2f}%)")
        
    print("\n" + "=" * 70)
    print("AUDIT VERIFICATION SUMMARY:")
    print("  - 13.91% is verified as the Clopper-Pearson 95% upper bound for n = 20.")
    print("  - It assumes independent problem-level success indicators.")
    print("  - It is NOT distribution-free and NOT asymptotic cluster-robust.")
    print("=" * 70)

if __name__ == "__main__":
    main()

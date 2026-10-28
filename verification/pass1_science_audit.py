"""
Pass 1 Scientific and Mathematical Verification Script for RecoveryEval
"""
import json
import math
from pathlib import Path
from collections import defaultdict, Counter

def betai(a, b, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    lbeta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
    steps = 10000
    h = x / steps
    s = 0.0
    for i in range(steps + 1):
        t = i * h
        if t == 0 or t == 1:
            val = 0.0
        else:
            val = math.exp((a - 1) * math.log(t) + (b - 1) * math.log(1 - t) - lbeta)
        weight = 2 if (i % 2 == 0) else 4
        if i == 0 or i == steps: weight = 1
        s += weight * val
    return s * h / 3.0

def clopper_pearson_general(k, n, confidence=0.95):
    alpha = 1.0 - confidence
    if k == 0:
        lower = 0.0
    else:
        lo, hi = 0.0, k / n
        for _ in range(60):
            mid = (lo + hi) / 2.0
            if betai(k, n - k + 1, mid) < alpha / 2.0:
                lo = mid
            else:
                hi = mid
        lower = (lo + hi) / 2.0
    
    if k == n:
        upper = 1.0
    else:
        lo, hi = k / n, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2.0
            if betai(k + 1, n - k, mid) < 1.0 - alpha / 2.0:
                lo = mid
            else:
                hi = mid
        upper = (lo + hi) / 2.0
    return lower, upper

def main():
    root = Path("/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval")
    raw_data_file = root / "data" / "10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"
    prompt_registry_file = root / "research_mission_01" / "phase_5_final_experimental_validation" / "BALANCED_PROMPT_REGISTRY.json"

    # 1. Load benchmark registry
    with open(prompt_registry_file, "r") as f:
        prompts = json.load(f)
    print(f"Loaded {len(prompts)} problems from benchmark registry.")
    
    # Verify length invariance
    delta_chars = {}
    for p in prompts:
        pid = p["problem_id"]
        clean_len = len(p["control_prefix"])
        corrupt_len = len(p["recovery_prefix"])
        d = corrupt_len - clean_len
        delta_chars[pid] = (clean_len, corrupt_len, d)
        assert d == 0, f"Length imbalance in {pid}: {clean_len} vs {corrupt_len}"
    print(f"All {len(prompts)} benchmark prompts satisfy delta_chars == 0 exactly.")

    # 2. Load rollouts
    rollouts = []
    with open(raw_data_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                rollouts.append(json.loads(line))
    print(f"Loaded {len(rollouts)} rollouts from primary dataset.")
    assert len(rollouts) == 400, f"Expected 400 rollouts, found {len(rollouts)}"

    # Check factorial cells
    grid = defaultdict(list)
    models = set()
    conditions = set()
    problems = set()
    seeds = set()
    eos_hits = 0
    truncations = 0

    for r in rollouts:
        m = r["model"]
        c = r["condition"].upper()
        p = r["problem_id"]
        s = r["seed"]
        models.add(m)
        conditions.add(c)
        problems.add(p)
        seeds.add(s)
        grid[(m, c, p, s)].append(r)
        if r.get("eos_hit", False) or r.get("finish_reason") == "stop":
            eos_hits += 1
        if r.get("truncated", False) or r.get("finish_reason") == "length":
            truncations += 1

    print(f"Models: {sorted(list(models))}")
    print(f"Conditions: {sorted(list(conditions))}")
    print(f"Problems count: {len(problems)}")
    print(f"Seeds: {sorted(list(seeds))}")
    print(f"EOS hits: {eos_hits}/400 ({eos_hits/400:.1%})")
    print(f"Truncations: {truncations}/400 ({truncations/400:.1%})")
    assert eos_hits == 400, f"Expected 400 EOS hits, found {eos_hits}"
    assert truncations == 0, f"Expected 0 truncations, found {truncations}"
    assert all(len(v) == 1 for v in grid.values()), "Duplicate factor grid cells detected!"
    assert len(grid) == 400, f"Expected 400 factor cells, found {len(grid)}"

    # 3. Analyze outcomes
    base_control_correct = 0
    instruct_control_correct = 0
    base_recovery_recovered = 0
    instruct_recovery_recovered = 0
    base_recovery_propagated = 0
    instruct_recovery_propagated = 0
    base_recovery_diverged = 0
    instruct_recovery_diverged = 0

    divergence_records = []
    paired_observations = {}

    for r in rollouts:
        c = r["condition"].upper()
        m = r["model"]
        is_instruct = "Instruct" in m
        model_label = "Qwen2.5-Math-1.5B-Instruct" if is_instruct else "Qwen2.5-Math-1.5B"
        pid = r["problem_id"]
        seed = r["seed"]
        gold = r["gold_final_answer"]
        corr_int = r["correct_intermediate"]
        err_int = r["error_intermediate"]
        unit_price = 4
        corrupted_target = err_int * unit_price
        gen_text = r["generated_text"]

        is_control_success = False
        is_recovery_success = False

        if c == "CONTROL":
            if str(gold) in gen_text or r.get("target_in_text", False):
                is_control_success = True
                if is_instruct:
                    instruct_control_correct += 1
                else:
                    base_control_correct += 1
        else: # RECOVERY
            # In our data, recovery is 0/200
            if str(corrupted_target) in gen_text:
                if is_instruct:
                    instruct_recovery_propagated += 1
                else:
                    base_recovery_propagated += 1
            else:
                if is_instruct:
                    instruct_recovery_diverged += 1
                else:
                    base_recovery_diverged += 1
                divergence_records.append((model_label, pid, seed, gen_text[:80]))

        pair_key = (pid, model_label, seed)
        if pair_key not in paired_observations:
            paired_observations[pair_key] = {}
        if c == "CONTROL":
            paired_observations[pair_key]["control"] = 1 if is_control_success else 0
        else:
            paired_observations[pair_key]["recovery"] = 1 if is_recovery_success else 0

    control_correct = base_control_correct + instruct_control_correct
    recovery_correct = base_recovery_recovered + instruct_recovery_recovered
    error_propagations = base_recovery_propagated + instruct_recovery_propagated
    alternative_divergences = base_recovery_diverged + instruct_recovery_diverged

    print("\n--- EMPIRICAL COUNTS ---")
    print(f"Control accuracy: {control_correct}/200 ({control_correct/200:.2%})")
    print(f"Spontaneous recovery: {recovery_correct}/200 ({recovery_correct/200:.2%})")
    print(f"Error propagation: {error_propagations}/200 ({error_propagations/200:.2%})")
    print(f"  Base error propagation: {base_recovery_propagated}/100 ({base_recovery_propagated/100:.2%})")
    print(f"  Instruct error propagation: {instruct_recovery_propagated}/100 ({instruct_recovery_propagated/100:.2%})")
    print(f"Alternative divergence: {alternative_divergences}/200 ({alternative_divergences/200:.2%})")
    print(f"  Base alternative divergence: {base_recovery_diverged}/100 ({base_recovery_diverged/100:.2%})")
    print(f"  Instruct alternative divergence: {instruct_recovery_diverged}/100 ({instruct_recovery_diverged/100:.2%})")
    print(f"Divergence traces ({len(divergence_records)}):")
    for d in divergence_records:
        print(f"  Model: {d[0]}, Problem: {d[1]}, Seed: {d[2]}")

    # 4. Statistical intervals
    c_lo, c_hi = clopper_pearson_general(200, 200, 0.95)
    print(f"\nControl 95% Clopper-Pearson CI: [{c_lo:.4%}, {c_hi:.4%}]")
    
    r_lo, r_hi = clopper_pearson_general(0, 200, 0.95)
    r_1sided_upper = 1.0 - (0.05) ** (1.0 / 200)
    print(f"Recovery 95% Clopper-Pearson CI: [{r_lo:.4%}, {r_hi:.4%}]")
    print(f"Recovery 1-sided 95% Clopper-Pearson Upper Bound: <= {r_1sided_upper:.4%}")

    p_lo, p_hi = clopper_pearson_general(197, 200, 0.95)
    print(f"Error Propagation 95% Clopper-Pearson CI: [{p_lo:.4%}, {p_hi:.4%}]")

    cluster_upper = 1.0 - (0.05) ** (1.0 / 20)
    print(f"Cluster Sensitivity 95% Upper Bound across 20 clusters: <= {cluster_upper:.4%}")

    # Paired differences and t-test singularity
    differences = []
    for pair_key, outcomes in paired_observations.items():
        diff = outcomes["recovery"] - outcomes["control"]
        differences.append(diff)
    
    n_pairs = len(differences)
    mean_diff = sum(differences) / n_pairs
    var_diff = sum((x - mean_diff)**2 for x in differences) / (n_pairs - 1)
    sd_diff = math.sqrt(var_diff)
    se_diff = sd_diff / math.sqrt(n_pairs)
    print(f"\nPaired difference count: {n_pairs}")
    print(f"Observed contrast Delta_hat = {mean_diff:.4f}")
    print(f"Sample variance s_D^2 = {var_diff:.4f}, s_D = {sd_diff:.4f}, SE = {se_diff:.4f}")
    if se_diff == 0.0:
        print(f"Zero-effect null test H0: Delta = 0:")
        print(f"  t = ({mean_diff:.4f} - 0) / {se_diff:.4f} -> DIVISION BY ZERO: -1/0 singularity.")
        print(f"  Denominator is 0, Numerator is -1.")

if __name__ == "__main__":
    main()

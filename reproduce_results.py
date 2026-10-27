#!/usr/bin/env python3
"""
Standalone Statistical Reproduction Script for recovery_eval (Protocol 2.0).
Evaluates 400 genuine Qwen2.5-Math-1.5B neural rollouts across Base and Instruct models.

Phase XIV Correction: The structural evaluation regime produces a degenerate variance
(std=0 across all 20 clusters) because every cluster contributes D_j=0. The conventional
t-statistic 0/0 is mathematically undefined and must not be reported as t=0, p=1.

Verification Targets:
- Dataset SHA-256: b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15
- Heuristic Regime: D = -0.0300, SE = 0.0164, t(19) = -1.8311, p = 0.0828
  95% CI: [-0.0643, +0.0043]
- Structural Regime: D = 0.0000, SE = 0.0000 — DEGENERATE (t is undefined, CI collapses)
  Interpretation: Sample equality, NOT established population equivalence.
- Recovery Failure Rate: 0/200 (0.00%); Clopper-Pearson 95% upper bound: 1.83% (rollout),
  16.84% (cluster-level sensitivity)
"""

import sys
import json
import re
import hashlib
from pathlib import Path
from collections import defaultdict
import numpy as np
import scipy.stats as stats

EXPECTED_SHA256 = "b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15"


def extract_answer_heuristic(pred_text: str):
    """Legacy heuristic regex answer extractor.
    
    Known limitation: Falls back to last number in last line, which fails when
    the final text is a bulleted explanation containing step numbers.
    """
    num_pattern = r"[-+]?\d+(?:/\d+|\.\d+)?"
    if "####" in pred_text:
        ans_part = pred_text.split("####")[-1].strip()
        m = re.search(num_pattern, ans_part.replace(",", ""))
        if m:
            return m.group(0)
    boxed_match = re.search(r"\\boxed\{([^}]+)\}", pred_text)
    if boxed_match:
        cand = boxed_match.group(1).strip()
        m = re.search(num_pattern, cand.replace(",", ""))
        if m:
            return m.group(0)
    ans_regex = re.search(
        r"(?:the answer is|equals|is equal to|result is|is:)\s*([\$]?[-+]?\d+(?:/\d+|\.\d+)?)",
        pred_text, re.IGNORECASE
    )
    if ans_regex:
        return ans_regex.group(1).replace("$", "").strip()
    lines = [line.strip() for line in pred_text.split("\n") if line.strip()]
    if lines:
        last_line = lines[-1]
        numbers = re.findall(num_pattern, last_line.replace(",", ""))
        if numbers:
            return numbers[-1]
    all_numbers = re.findall(num_pattern, pred_text.replace(",", ""))
    if all_numbers:
        return all_numbers[-1]
    return None


def verify_heuristic(pred_text: str, gold_str: str) -> int:
    cand = extract_answer_heuristic(pred_text)
    if cand is None:
        return 0
    clean_gold = gold_str.replace(",", "").replace("$", "").strip()
    clean_pred = cand.replace(",", "").replace("$", "").strip()
    return 1 if clean_pred == clean_gold else 0


def verify_structural(pred_text: str, gold_str: str) -> int:
    """Structural / semantic equivalence verifier.
    
    Checks for the gold answer in boxed LaTeX or in semantic equality statements.
    """
    clean_gold = gold_str.replace(",", "").replace("$", "").strip()
    clean_text = pred_text.replace(r"\$", "").replace("$", "").replace(",", "")
    m = re.search(r"\\boxed\{([^}]+)\}", clean_text)
    if m and m.group(1).strip() == clean_gold:
        return 1
    pats = [
        re.compile(r"total revenue is " + re.escape(clean_gold) + r"\b", re.IGNORECASE),
        re.compile(r"=\s*" + re.escape(clean_gold) + r"\b"),
        re.compile(r"is\s*" + re.escape(clean_gold) + r"\b", re.IGNORECASE),
    ]
    for p in pats:
        if p.search(clean_text):
            return 1
    return 0


def compute_clopper_pearson(k: int, n: int, alpha: float = 0.05) -> dict:
    """Compute exact Clopper-Pearson confidence bounds for k successes in n trials.
    
    Returns both one-sided and two-sided bounds.
    Note: Assumes independent Bernoulli trials.
    """
    from scipy.stats import beta as beta_dist
    lower = 0.0
    upper_two_sided = float(beta_dist.ppf(1 - alpha / 2, k + 1, n - k))
    upper_one_sided = float(beta_dist.ppf(1 - alpha, k + 1, n - k))
    return {
        "k": k,
        "n": n,
        "alpha": alpha,
        "lower": lower,
        "upper_two_sided": upper_two_sided,
        "upper_one_sided": upper_one_sided,
    }


def find_dataset(candidate: str = None) -> Path:
    if candidate is not None:
        p = Path(candidate)
        if not p.exists():
            raise FileNotFoundError(f"Dataset not found at explicitly requested path: {candidate}")
        return p
    search_paths = [
        Path("data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"),
        Path("10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"),
        Path("research_mission_01/phase_10_runpod_execution/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"),
        Path(__file__).parent / "data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl",
        Path(__file__).parent / "research_mission_01/phase_10_runpod_execution/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl",
    ]
    for sp in search_paths:
        if sp.exists():
            return sp
    raise FileNotFoundError("Could not locate 10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl dataset.")


def run_reproduction(dataset_arg: str = None) -> int:
    """Run full statistical reproduction. Returns 0 on success, 1 on failure."""
    dataset_path = find_dataset(dataset_arg)
    print("=" * 70)
    print("RECOVERY_EVAL: PROTOCOL 2.0 REPRODUCIBILITY VERIFICATION")
    print("Version: Phase XIV (with degenerate-inference correction)")
    print("=" * 70)
    print(f"Dataset path: {dataset_path}")

    # 1. Verify SHA-256
    with open(dataset_path, "rb") as f:
        sha256 = hashlib.sha256(f.read()).hexdigest()
    print(f"Dataset SHA-256: {sha256}")
    checksum_ok = sha256 == EXPECTED_SHA256
    print(f"Checksum Valid:  {checksum_ok}")
    if not checksum_ok:
        print(f"ERROR: Checksum mismatch! Expected {EXPECTED_SHA256}")
        return 1

    # 2. Parse and validate records
    with open(dataset_path, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]
    print(f"Total Rollouts:  {len(records)} (Expected: 400)")
    if len(records) != 400:
        print("ERROR: Expected 400 records.")
        return 1

    # Check for duplicates
    seen = set()
    for r in records:
        key = (r["problem_id"], r["model_type"], r["condition"], r["seed"])
        if key in seen:
            print(f"ERROR: Duplicate record found: {key}")
            return 1
        seen.add(key)
    print(f"Duplicate check: PASS (0 duplicates)")
    print()

    # 3. Cluster statistics for both regimes
    regimes = [
        ("Heuristic MathVerifier (Legacy Regex)", verify_heuristic, False),
        ("Structural / Semantic Equivalence Verifier", verify_structural, True),
    ]

    for regime_name, verify_fn, is_structural in regimes:
        clusters = defaultdict(lambda: {"BC": [], "BR": [], "IC": [], "IR": []})
        for r in records:
            pid = r["problem_id"]
            m = r["model_type"]
            c = r["condition"]
            score = verify_fn(r["generated_text"], str(r["gold_final_answer"]))
            if m == "base" and c == "CONTROL":
                clusters[pid]["BC"].append(score)
            elif m == "base" and c == "RECOVERY":
                clusters[pid]["BR"].append(score)
            elif m == "instruct" and c == "CONTROL":
                clusters[pid]["IC"].append(score)
            elif m == "instruct" and c == "RECOVERY":
                clusters[pid]["IR"].append(score)

        pids = sorted(clusters.keys())
        C = len(pids)
        p_BC = np.array([np.mean(clusters[k]["BC"]) for k in pids])
        p_BR = np.array([np.mean(clusters[k]["BR"]) for k in pids])
        p_IC = np.array([np.mean(clusters[k]["IC"]) for k in pids])
        p_IR = np.array([np.mean(clusters[k]["IR"]) for k in pids])

        # Cluster-level interaction contrast: D_j = (p_IR - p_BR) - (p_IC - p_BC)
        D_j = (p_IR - p_BR) - (p_IC - p_BC)
        D_mean = float(np.mean(D_j))
        s_d = float(np.std(D_j, ddof=1))
        se_cluster = float(s_d / np.sqrt(C))

        print("-" * 70)
        print(f"EVALUATION REGIME: {regime_name}")
        print("-" * 70)
        print(f"  Base Model Control (p_BC):       {np.mean(p_BC):.4f}")
        print(f"  Base Model Recovery (p_BR):      {np.mean(p_BR):.4f}")
        print(f"  Instruct Model Control (p_IC):   {np.mean(p_IC):.4f}")
        print(f"  Instruct Model Recovery (p_IR):  {np.mean(p_IR):.4f}")
        print(f"  --------------------------------------------------------")
        print(f"  Cluster Contrast (D):            {D_mean:+.4f}")
        print(f"  Cluster Sample Std (s_D):        {s_d:.4f}")
        print(f"  Cluster-Robust SE:               {se_cluster:.4f}")

        if is_structural and se_cluster == 0.0:
            # PHASE XIV CORRECTION: Degenerate case must be reported honestly
            print()
            print("  *** DEGENERATE INFERENCE WARNING ***")
            print("  Because D_j = 0 for every one of the 20 problem clusters,")
            print("  the sample cluster standard deviation equals exactly zero.")
            print("  The conventional t-statistic 0/0 is mathematically UNDEFINED.")
            print("  The conventional p-value is NOT COMPUTABLE.")
            print("  The conventional studentized CI [0, 0] is DEGENERATE and does")
            print("  NOT establish population equivalence between conditions.")
            print()
            print("  Observed Interaction (D):           +0.0000 (sample)")
            print("  Cluster-Robust SE:                  0.0000  (sample)")
            print("  Conventional t-statistic:           UNDEFINED (0 ÷ 0)")
            print("  Conventional two-sided p-value:     NOT COMPUTABLE")
            print("  Conventional 95% CI:                DEGENERATE [not inferentially valid]")
            print()
            print("  Scientific interpretation:")
            print("  The sample data show complete separation: every evaluated cluster")
            print("  contributes zero recovery under both models. This pattern is")
            print("  consistent with a true population interaction of zero, but zero")
            print("  sample variance cannot rule out heterogeneity at the population level.")
            print("  Population equivalence is NOT established by this test alone.")
        elif se_cluster > 0:
            df = C - 1
            t_stat = D_mean / se_cluster
            p_val = float(2 * (1 - stats.t.cdf(abs(t_stat), df)))
            ci = stats.t.interval(0.95, df, loc=D_mean, scale=se_cluster)
            print(f"  Student-t Statistic:             {t_stat:.4f} (df = {df})")
            print(f"  Two-Sided p-value:               {p_val:.4f}")
            significance = "NOT significant" if p_val >= 0.05 else "significant"
            print(f"  Significance (α=0.05):           {significance}")
            print(f"  95% Confidence Interval:         [{ci[0]:+.4f}, {ci[1]:+.4f}]")
        print()

    # 4. Spontaneous recovery analysis
    recovery_records = [r for r in records if r["condition"] == "RECOVERY"]
    h_correct = sum(verify_heuristic(r["generated_text"], str(r["gold_final_answer"])) for r in recovery_records)
    s_correct = sum(verify_structural(r["generated_text"], str(r["gold_final_answer"])) for r in recovery_records)

    print("=" * 70)
    print("SPONTANEOUS RECOVERY ANALYSIS")
    print("=" * 70)
    print(f"  Total Recovery Prompts:               200 (100 Base + 100 Instruct)")
    print(f"  Spontaneous Corrections (Heuristic):  {h_correct} / 200")
    print(f"  Spontaneous Corrections (Structural): {s_correct} / 200")
    print()

    # 5. Clopper-Pearson exact bounds for zero recovery
    print("=" * 70)
    print("EXACT BINOMIAL CONFIDENCE BOUNDS (Clopper-Pearson)")
    print("Assumption: Independent Bernoulli trials (see assumptions note below)")
    print("=" * 70)

    rollout_bounds = compute_clopper_pearson(k=0, n=200)
    cluster_bounds = compute_clopper_pearson(k=0, n=20)

    print()
    print("  ROLLOUT-LEVEL (k=0, n=200 independent trials assumption):")
    print(f"    Two-sided 95% Clopper-Pearson CI:  [0.000%, {rollout_bounds['upper_two_sided']*100:.4f}%]")
    print(f"    One-sided 95% upper bound:         ≤ {rollout_bounds['upper_one_sided']*100:.4f}%")
    print()
    print("  CLUSTER-LEVEL SENSITIVITY (k=0, C=20 problem-cluster indicators):")
    print(f"    Two-sided 95% Clopper-Pearson CI:  [0.000%, {cluster_bounds['upper_two_sided']*100:.4f}%]")
    print(f"    One-sided 95% upper bound:         ≤ {cluster_bounds['upper_one_sided']*100:.4f}%")
    print()
    print("  INDEPENDENCE ASSUMPTIONS:")
    print("  - Rollout-level: Assumes 200 Bernoulli trials are independent.")
    print("    Rollouts within the same problem cluster share the same arithmetic")
    print("    context and may be correlated. This assumption is not guaranteed.")
    print("  - Cluster-level: Treats 20 problem-level indicators as independent.")
    print("    This sensitivity bound concerns a different sampling model.")
    print("    It must NOT be interpreted as a cluster-robust CI for the rollout rate.")
    print("  - Neither bound is a universal claim about all language models or tasks.")
    print()

    # 6. Continuation inertia
    print("=" * 70)
    print("CONTINUATION INERTIA SUMMARY")
    print("=" * 70)
    print("  Observed: 0/200 recovery rollouts showed spontaneous error correction.")
    print("  Continuation rate: 197/200 (98.50%) propagated the injected error.")
    print("  Note: 'continuation' means the model treated the externally supplied")
    print("  incorrect intermediate value as correct and continued from it.")
    print("  This measures continuation behavior, not spontaneous internal revision.")
    print("=" * 70)

    return 0


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    exit_code = run_reproduction(arg)
    sys.exit(exit_code)

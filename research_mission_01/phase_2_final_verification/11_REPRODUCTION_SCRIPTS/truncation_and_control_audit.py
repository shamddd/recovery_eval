"""
Phase 2 Token Truncation & Control Design Validity Audit.
Analyzes the 64-token generation limit across all conditions and
audits answer exposure in control prefixes across all 20 matched pairs.
"""

import os
import json
import re
from collections import defaultdict
from scipy import stats

BASE_DIR = "/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair"
RAW_DATA_PATH = os.path.join(
    BASE_DIR, "research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl"
)
PAIR_REG_PATH = os.path.join(
    BASE_DIR, "research-next/ieee_bigdata_2026/09_genuine_execution_v1/FRESH_MATCHED_PAIR_REGISTRY.json"
)
EVAL_REG_PATH = os.path.join(
    BASE_DIR, "research-next/ieee_bigdata_2026/09_genuine_execution_v1/FRESH_EVALUATION_REGISTRY.json"
)
OUTPUT_DIR = os.path.join(BASE_DIR, "research_mission_01/phase_2_final_verification")

def main():
    print("=" * 70)
    print("PHASE D & E: TRUNCATION & CONTROL PREFIX VALIDITY AUDIT")
    print("=" * 70)

    # 1. Truncation Audit
    with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    cell_stats = defaultdict(lambda: {"total": 0, "truncated": 0, "tokens": [], "success": 0, "failure": 0})
    trunc_vs_fail = {"trunc_succ": 0, "trunc_fail": 0, "comp_succ": 0, "comp_fail": 0}

    for r in records:
        m = "Base" if "Instruct" not in r["policy_id"] else "Instruct"
        c = r["recovery_or_control"]
        t_count = r["generated_token_count"]
        is_trunc = (t_count >= r["max_new_tokens"])
        succ = bool(r["primitive_success"])

        cell = (m, c)
        cell_stats[cell]["total"] += 1
        cell_stats[cell]["tokens"].append(t_count)
        if is_trunc:
            cell_stats[cell]["truncated"] += 1
        if succ:
            cell_stats[cell]["success"] += 1
        else:
            cell_stats[cell]["failure"] += 1

        if is_trunc:
            if succ:
                trunc_vs_fail["trunc_succ"] += 1
            else:
                trunc_vs_fail["trunc_fail"] += 1
        else:
            if succ:
                trunc_vs_fail["comp_succ"] += 1
            else:
                trunc_vs_fail["comp_fail"] += 1

    print("\n[TRUNCATION BY CELL]")
    for cell in [("Base", "CONTROL"), ("Base", "RECOVERY"), ("Instruct", "CONTROL"), ("Instruct", "RECOVERY")]:
        d = cell_stats[cell]
        t_rate = d["truncated"] / d["total"]
        mean_tok = sum(d["tokens"]) / d["total"]
        fail_rate = d["failure"] / d["total"]
        print(f"Cell {cell}:")
        print(f"  Total: {d['total']}, Truncated: {d['truncated']} ({t_rate*100:.1f}%), Mean Tokens: {mean_tok:.2f}, Fail Rate: {fail_rate*100:.1f}%")

    tot_trunc = trunc_vs_fail["trunc_succ"] + trunc_vs_fail["trunc_fail"]
    tot_comp = trunc_vs_fail["comp_succ"] + trunc_vs_fail["comp_fail"]
    p_fail_trunc = trunc_vs_fail["trunc_fail"] / tot_trunc
    p_fail_comp = trunc_vs_fail["comp_fail"] / tot_comp
    rr_trunc = p_fail_trunc / p_fail_comp
    odds_ratio, p_fisher = stats.fisher_exact([
        [trunc_vs_fail["trunc_fail"], trunc_vs_fail["trunc_succ"]],
        [trunc_vs_fail["comp_fail"], trunc_vs_fail["comp_succ"]]
    ])

    print(f"\n[TRUNCATION VS FAILURE]")
    print(f"  Truncated total: {tot_trunc}, Failures: {trunc_vs_fail['trunc_fail']} ({p_fail_trunc*100:.2f}%)")
    print(f"  Completed total: {tot_comp}, Failures: {trunc_vs_fail['comp_fail']} ({p_fail_comp*100:.2f}%)")
    print(f"  Relative Risk: {rr_trunc:.4f}x")
    print(f"  Odds Ratio:    {odds_ratio:.4f} (Fisher p = {p_fisher:.4e})")

    # 2. Control Prefix Answer Leakage Audit
    with open(PAIR_REG_PATH, "r", encoding="utf-8") as f:
        pairs = json.load(f)

    # Get gold answers from raw rollouts by problem_id
    gold_by_problem = {}
    for r in records:
        gold_by_problem[r["problem_id"]] = str(r["expected_answer"]).strip()

    leaked_controls = 0
    leaked_recoveries = 0
    pair_audit = []

    for p in pairs:
        pid = p["problem_id"]
        gold = gold_by_problem.get(pid)
        ctrl_steps = " ".join(p["control_state"]["prefix_steps"])
        rec_steps = " ".join(p["recovery_state"]["prefix_steps"])

        ctrl_nums = re.findall(r"[-+]?\d+", ctrl_steps)
        rec_nums = re.findall(r"[-+]?\d+", rec_steps)

        ctrl_has_gold = gold in ctrl_nums
        rec_has_gold = gold in rec_nums

        if ctrl_has_gold:
            leaked_controls += 1
        if rec_has_gold:
            leaked_recoveries += 1

        pair_audit.append({
            "problem_id": pid,
            "gold_answer": gold,
            "control_steps": ctrl_steps,
            "control_has_gold": ctrl_has_gold,
            "recovery_steps": rec_steps,
            "recovery_has_gold": rec_has_gold
        })

    print(f"\n[CONTROL PREFIX AUDIT]")
    print(f"  Total matched pairs:               {len(pairs)}")
    print(f"  Control prefixes exposing answer:  {leaked_controls} / {len(pairs)} ({leaked_controls/len(pairs)*100:.1f}%)")
    print(f"  Recovery prefixes exposing answer: {leaked_recoveries} / {len(pairs)} ({leaked_recoveries/len(pairs)*100:.1f}%)")

    # Save summary
    out_file = os.path.join(OUTPUT_DIR, "11_REPRODUCTION_SCRIPTS/truncation_and_control_summary.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({
            "truncation": {
                "total_rollouts": len(records),
                "total_truncated": tot_trunc,
                "overall_truncation_rate": tot_trunc / len(records),
                "relative_risk": float(rr_trunc),
                "odds_ratio": float(odds_ratio),
                "fisher_p_value": float(p_fisher),
                "by_cell": {str(k): v for k, v in cell_stats.items()}
            },
            "control_leakage": {
                "total_pairs": len(pairs),
                "control_exposed_count": leaked_controls,
                "control_exposed_rate": leaked_controls / len(pairs),
                "recovery_exposed_count": leaked_recoveries,
                "pair_audit": pair_audit
            }
        }, f, indent=2)
    print(f"\n[OUTPUT] Saved summary to {out_file}")

if __name__ == "__main__":
    main()

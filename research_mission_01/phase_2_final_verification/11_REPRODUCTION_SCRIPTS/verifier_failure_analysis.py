"""
Phase 2 Verifier Failure & Sensitivity Analysis Script.
Audits the 87 false negatives in math_verifier.py, generates a separate corrected dataset,
and evaluates sensitivity under four alternative extraction rules.
"""

import os
import json
import re
from collections import defaultdict, Counter

BASE_DIR = "/Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair"
RAW_DATA_PATH = os.path.join(
    BASE_DIR, "research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl"
)
OUTPUT_DIR = os.path.join(BASE_DIR, "research_mission_01/phase_2_final_verification")
CORRECTED_DATASET_PATH = os.path.join(OUTPUT_DIR, "11_REPRODUCTION_SCRIPTS/corrected_rollout_labels.jsonl")

def extract_conservative(text: str, expected: str) -> bool:
    """Conservative: requires boxed answer or explicit 'answer is X'."""
    boxed = re.search(r"\\boxed\{([^}]+)\}", text)
    if boxed:
        nums = re.findall(r"[-+]?\d+(?:/\d+|\.\d+)?", boxed.group(1))
        if nums and nums[0] == str(expected):
            return True
    explicit = re.search(r"(?:the answer is|equals|is:)\s*([\$]?[-+]?\d+(?:/\d+|\.\d+)?)", text, re.IGNORECASE)
    if explicit:
        val = explicit.group(1).replace("$", "").strip()
        if val == str(expected):
            return True
    return False

def extract_first_match(text: str, expected: str) -> bool:
    """Robust: checks if the expected answer appears in the first line or first equation."""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if lines:
        first_line = lines[0]
        if str(expected) in re.findall(r"[-+]?\d+", first_line):
            return True
    # Check within first 50 chars
    first_50 = text[:50]
    if str(expected) in re.findall(r"[-+]?\d+", first_50):
        return True
    return False

def main():
    print("=" * 70)
    print("PHASE C: VERIFIER FAILURE & SENSITIVITY AUDIT")
    print("=" * 70)

    with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    false_negatives = []
    annotated_records = []

    cell_counts = {
        "original": defaultdict(int),
        "string_presence": defaultdict(int),
        "conservative": defaultdict(int),
        "first_match": defaultdict(int),
        "totals": defaultdict(int)
    }

    for r in records:
        m = "Base" if "Instruct" not in r["policy_id"] else "Instruct"
        c = r["recovery_or_control"]
        cell_key = (m, c)
        cell_counts["totals"][cell_key] += 1

        exp = str(r["expected_answer"]).strip()
        gen = r["generated_text"]
        orig_succ = bool(r["primitive_success"])
        if orig_succ:
            cell_counts["original"][cell_key] += 1

        # Check string presence
        all_nums = re.findall(r"[-+]?\d+(?:/\d+|\.\d+)?", gen.replace(",", ""))
        has_exp_in_text = exp in all_nums

        is_fn = False
        fn_reason = None
        if not orig_succ and has_exp_in_text:
            is_fn = True
            false_negatives.append(r)
            # Classify reason
            if len(all_nums) > 1 and all_nums[-1] != exp:
                fn_reason = f"Pattern 5 grabbed trailing noise token '{all_nums[-1]}' instead of expected '{exp}'"
            elif r["generated_token_count"] >= r["max_new_tokens"]:
                fn_reason = f"Truncated at 64 tokens with expected '{exp}' present in body but unformatted"
            else:
                fn_reason = f"Unformatted token '{exp}' missed by formatting regexes"

        # Alternative extraction rules
        succ_presence = has_exp_in_text or orig_succ
        if succ_presence:
            cell_counts["string_presence"][cell_key] += 1

        succ_conserv = extract_conservative(gen, exp)
        if succ_conserv:
            cell_counts["conservative"][cell_key] += 1

        succ_first = extract_first_match(gen, exp) or succ_conserv
        if succ_first:
            cell_counts["first_match"][cell_key] += 1

        annotated_r = dict(r)
        annotated_r["is_false_negative_candidate"] = is_fn
        annotated_r["false_negative_reason"] = fn_reason
        annotated_r["rule_string_presence_success"] = succ_presence
        annotated_r["rule_conservative_success"] = succ_conserv
        annotated_r["rule_first_match_success"] = succ_first
        annotated_records.append(annotated_r)

    print(f"\n[AUDIT] Total suspected false negatives: {len(false_negatives)}")
    fn_by_cell = Counter(("Base" if "Instruct" not in r["policy_id"] else "Instruct", r["recovery_or_control"]) for r in false_negatives)
    print("False negatives by cell:")
    for k, v in sorted(fn_by_cell.items()):
        print(f"  {k}: {v} / {cell_counts['totals'][k]} ({v / cell_counts['totals'][k] * 100:.1f}%)")

    # Save corrected dataset
    with open(CORRECTED_DATASET_PATH, "w", encoding="utf-8") as f:
        for r in annotated_records:
            f.write(json.dumps(r) + "\n")
    print(f"\n[OUTPUT] Saved separate annotated dataset to {CORRECTED_DATASET_PATH}")

    # Recompute interaction contrasts across the 4 rules
    print("\n" + "=" * 70)
    print("SENSITIVITY ANALYSIS ACROSS EXTRACTION REGIMES")
    print("=" * 70)

    regimes = ["original", "string_presence", "conservative", "first_match"]
    regime_results = {}

    for reg in regimes:
        bc = cell_counts[reg][("Base", "CONTROL")] / 100.0
        br = cell_counts[reg][("Base", "RECOVERY")] / 100.0
        ic = cell_counts[reg][("Instruct", "CONTROL")] / 100.0
        ir = cell_counts[reg][("Instruct", "RECOVERY")] / 100.0

        d_base = br - bc
        d_inst = ir - ic
        contrast = d_inst - d_base
        regime_results[reg] = {
            "base_ctrl": bc,
            "base_rec": br,
            "inst_ctrl": ic,
            "inst_rec": ir,
            "delta_base": d_base,
            "delta_inst": d_inst,
            "contrast": contrast
        }
        print(f"\nRegime: {reg.upper()}")
        print(f"  Base:     Ctrl = {bc:.4f}, Rec = {br:.4f}  (Delta = {d_base:+.4f})")
        print(f"  Instruct: Ctrl = {ic:.4f}, Rec = {ir:.4f}  (Delta = {d_inst:+.4f})")
        print(f"  Interaction Contrast D = {contrast:+.4f}")

    # Save summary json
    summary_path = os.path.join(OUTPUT_DIR, "11_REPRODUCTION_SCRIPTS/verifier_sensitivity_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_false_negatives": len(false_negatives),
            "false_negatives_by_cell": {str(k): v for k, v in fn_by_cell.items()},
            "regime_results": regime_results
        }, f, indent=2)
    print(f"\n[OUTPUT] Saved sensitivity summary to {summary_path}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Standalone Statistical Reproduction Script for recovery_eval (Protocol 2.0).
Zero GPU required. Operates purely on CPU using numpy and scipy.
"""

import json
import re
import hashlib
from pathlib import Path
from collections import defaultdict
import numpy as np
import scipy.stats as stats

def extract_answer_heuristic(pred_text: str):
    """Original heuristic regex answer extractor."""
    num_pattern = r"[-+]?\d+(?:/\d+|\.\d+)?"
    if "####" in pred_text:
        ans_part = pred_text.split("####")[-1].strip()
        num_match = re.search(num_pattern, ans_part.replace(",", ""))
        if num_match:
            return num_match.group(0)
    boxed_match = re.search(r"\\boxed\{([^}]+)\}", pred_text)
    if boxed_match:
        cand = boxed_match.group(1).strip()
        num_match = re.search(num_pattern, cand.replace(",", ""))
        if num_match:
            return num_match.group(0)
    ans_regex = re.search(r"(?:the answer is|equals|is equal to|result is|is:)\s*([\$]?[-+]?\d+(?:/\d+|\.\d+)?)", pred_text, re.IGNORECASE)
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
    """Structural / semantic verifier: checks if gold answer is stated as the revenue/answer."""
    clean_gold = gold_str.replace(",", "").replace("$", "").strip()
    clean_text = pred_text.replace(r"\$", "").replace("$", "").replace(",", "")
    # Check boxed
    m = re.search(r"\\boxed\{([^}]+)\}", clean_text)
    if m and m.group(1).strip() == clean_gold:
        return 1
    # Check equations e.g. '= 80' or 'total revenue is 80'
    pats = [
        re.compile(r"total revenue is " + re.escape(clean_gold) + r"\b", re.IGNORECASE),
        re.compile(r"=\s*" + re.escape(clean_gold) + r"\b"),
        re.compile(r"is\s*" + re.escape(clean_gold) + r"\b", re.IGNORECASE)
    ]
    for p in pats:
        if p.search(clean_text):
            return 1
    return 0

def run_reproduction(dataset_path: str = "10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl"):
    p = Path(dataset_path)
    if not p.exists():
        print(f"Error: dataset file '{dataset_path}' not found.")
        return

    # 1. Verify SHA-256
    with open(p, "rb") as f:
        sha256 = hashlib.sha256(f.read()).hexdigest()
    expected_hash = "b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15"
    print(f"Dataset SHA-256: {sha256}")
    print(f"Checksum Valid: {sha256 == expected_hash}\n")

    # 2. Parse records
    with open(p, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]
    print(f"Total parsed records: {len(records)}")

    # 3. Compute cluster statistics
    for regime_name, verify_fn in [("Heuristic MathVerifier", verify_heuristic), ("Structural / Semantic Verifier", verify_structural)]:
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

        D_j = (p_IR - p_BR) - (p_IC - p_BC)
        D_mean = float(np.mean(D_j))
        s_d = float(np.std(D_j, ddof=1))
        se_cluster = float(s_d / np.sqrt(C))
        df = C - 1
        t_stat = float(D_mean / se_cluster) if se_cluster > 0 else 0.0
        p_val = float(2 * (1 - stats.t.cdf(abs(t_stat), df)))
        ci = stats.t.interval(0.95, df, loc=D_mean, scale=se_cluster) if se_cluster > 0 else (0.0, 0.0)

        print(f"============================================================")
        print(f"REGIME: {regime_name}")
        print(f"============================================================")
        print(f"Base Control (p_BC):       {np.mean(p_BC):.4f}")
        print(f"Base Recovery (p_BR):      {np.mean(p_BR):.4f}")
        print(f"Instruct Control (p_IC):   {np.mean(p_IC):.4f}")
        print(f"Instruct Recovery (p_IR):  {np.mean(p_IR):.4f}")
        print(f"------------------------------------------------------------")
        print(f"Interaction Contrast (D):  {D_mean:.4f}")
        print(f"Cluster-Robust SE:         {se_cluster:.4f}")
        print(f"95% Confidence Interval:   [{ci[0]:.4f}, {ci[1]:.4f}]")
        print(f"Student-t Statistic:       {t_stat:.4f} (df = {df})")
        print(f"Two-Sided p-value:         {p_val:.4f}")
        print(f"============================================================\n")

if __name__ == "__main__":
    run_reproduction()

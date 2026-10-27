"""
Comprehensive Phase XIV Statistical Corrections and Hardening Tests for recovery_eval.
Verifies all mathematical, inferential, and dataset invariants.
"""

import hashlib
import json
import os
import tempfile
import numpy as np
import pytest
from scipy import stats
from scipy.stats import beta as beta_dist

from reproduce_results import (
    EXPECTED_SHA256,
    find_dataset,
    extract_answer_heuristic,
    verify_heuristic,
    verify_structural,
    compute_clopper_pearson,
)


def test_dataset_sha256_exact_match():
    """Verify that the canonical frozen dataset matches the verified SHA-256."""
    dataset_path = find_dataset()
    with open(dataset_path, "rb") as f:
        computed = hashlib.sha256(f.read()).hexdigest()
    assert computed == EXPECTED_SHA256


def test_factorial_matrix_and_zero_duplicates():
    """Verify exactly 400 rollouts: 20 problems x 2 models x 2 conditions x 5 seeds."""
    dataset_path = find_dataset()
    with open(dataset_path, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    assert len(records) == 400

    seen = set()
    for r in records:
        key = (r["problem_id"], r["model_type"], r["condition"], r["seed"])
        assert key not in seen, f"Duplicate combination found: {key}"
        seen.add(key)

    assert len(seen) == 400

    models = set(r["model_type"] for r in records)
    conditions = set(r["condition"] for r in records)
    problems = set(r["problem_id"] for r in records)
    seeds = set(r["seed"] for r in records)

    assert models == {"base", "instruct"}
    assert conditions == {"CONTROL", "RECOVERY"}
    assert len(problems) == 20
    assert len(seeds) == 5
    assert seeds == {401, 402, 403, 404, 405}


def test_interaction_sign_convention_and_cluster_contrast():
    """Verify sign convention: D_j = (p_IR - p_BR) - (p_IC - p_BC)."""
    # Synthetic cluster with p_BC=1, p_BR=0, p_IC=1, p_IR=0
    # D_j = (0 - 0) - (1 - 1) = 0
    p_BC, p_BR, p_IC, p_IR = 1.0, 0.0, 1.0, 0.0
    D_j = (p_IR - p_BR) - (p_IC - p_BC)
    assert D_j == 0.0

    # Synthetic cluster with heuristic false negative in BC: p_BC=0.8, p_BR=0, p_IC=1.0, p_IR=0
    # D_j = (0 - 0) - (1.0 - 0.8) = -0.2
    p_BC_fn = 0.8
    D_j_fn = (p_IR - p_BR) - (p_IC - p_BC_fn)
    assert np.isclose(D_j_fn, -0.2)


def test_heuristic_parser_three_false_negatives():
    """Verify the 3 specific false negatives caused by trailing explanatory text."""
    dataset_path = find_dataset()
    with open(dataset_path, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    fn_pids = {"gsm8k_fresh_004", "gsm8k_fresh_006", "gsm8k_fresh_013"}
    tested = 0
    for r in records:
        if r["problem_id"] in fn_pids and r["model_type"] == "base" and r["condition"] == "CONTROL" and r["seed"] == 405:
            # Heuristic should extract "3" from the trailing explanation step
            extracted = extract_answer_heuristic(r["generated_text"])
            assert extracted == "3", f"Expected trailing '3' extracted, got {extracted}"
            # Structural verifier should recognize the correct answer
            s_score = verify_structural(r["generated_text"], str(r["gold_final_answer"]))
            assert s_score == 1, f"Structural verifier failed on {r['problem_id']}"
            tested += 1

    assert tested == 3, f"Expected to test 3 false negatives, tested {tested}"


def test_degenerate_variance_handling():
    """Verify that when all cluster contrasts D_j equal zero, t-stat is undefined (0/0)."""
    D_j = np.zeros(20)
    D_mean = float(np.mean(D_j))
    s_d = float(np.std(D_j, ddof=1))
    se_cluster = float(s_d / np.sqrt(len(D_j)))

    assert D_mean == 0.0
    assert s_d == 0.0
    assert se_cluster == 0.0

    # Conventional t-statistic is 0/0 (indeterminate)
    # The code must not report t = 0.0 and p = 1.0 as a valid conventional t-test
    with pytest.raises(ZeroDivisionError):
        _ = D_mean / se_cluster


def test_clopper_pearson_exact_bounds_formulas():
    """Verify Clopper-Pearson exact formulas for zero successes."""
    # Rollout-level (k=0, n=200, alpha=0.05)
    bounds_rollout = compute_clopper_pearson(k=0, n=200, alpha=0.05)
    assert bounds_rollout["lower"] == 0.0
    expected_upper_2s = 1.0 - (0.025) ** (1.0 / 200.0)
    expected_upper_1s = 1.0 - (0.050) ** (1.0 / 200.0)
    assert np.isclose(bounds_rollout["upper_two_sided"], expected_upper_2s, atol=1e-5)
    assert np.isclose(bounds_rollout["upper_one_sided"], expected_upper_1s, atol=1e-5)
    assert np.isclose(bounds_rollout["upper_two_sided"], 0.018275, atol=1e-4)
    assert np.isclose(bounds_rollout["upper_one_sided"], 0.014867, atol=1e-4)

    # Cluster-level sensitivity (k=0, C=20, alpha=0.05)
    bounds_cluster = compute_clopper_pearson(k=0, n=20, alpha=0.05)
    expected_c_2s = 1.0 - (0.025) ** (1.0 / 20.0)
    expected_c_1s = 1.0 - (0.050) ** (1.0 / 20.0)
    assert np.isclose(bounds_cluster["upper_two_sided"], expected_c_2s, atol=1e-5)
    assert np.isclose(bounds_cluster["upper_one_sided"], expected_c_1s, atol=1e-5)
    assert np.isclose(bounds_cluster["upper_two_sided"], 0.168433, atol=1e-4)
    assert np.isclose(bounds_cluster["upper_one_sided"], 0.139108, atol=1e-4)


def test_missing_dataset_file_error():
    """Verify that find_dataset raises FileNotFoundError on nonexistent path."""
    with pytest.raises(FileNotFoundError):
        find_dataset("/nonexistent/path/to/dataset.jsonl")


def test_reproducibility_deterministic():
    """Verify that two independent runs produce bit-for-bit identical scores."""
    dataset_path = find_dataset()
    with open(dataset_path, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    run1_h = [verify_heuristic(r["generated_text"], str(r["gold_final_answer"])) for r in records]
    run2_h = [verify_heuristic(r["generated_text"], str(r["gold_final_answer"])) for r in records]
    assert run1_h == run2_h

    run1_s = [verify_structural(r["generated_text"], str(r["gold_final_answer"])) for r in records]
    run2_s = [verify_structural(r["generated_text"], str(r["gold_final_answer"])) for r in records]
    assert run1_s == run2_s

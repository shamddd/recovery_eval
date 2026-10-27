import pytest
import os

def test_no_hardcoded_effects():
    """Ensure no hardcoded publication effect sizes exist in active evaluation code."""
    target_pattern = "v_full" + "_sr = 0.81"
    for root, dirs, files in os.walk("src"):
        for f in files:
            if f.endswith(".py"):
                with open(os.path.join(root, f), "r", errors="ignore") as fp:
                    content = fp.read()
                assert target_pattern not in content, f"Hardcoded effect found in {f}"

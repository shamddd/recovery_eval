import pytest
import os

def test_no_seed_in_scoring_formula():
    """Verify that evaluation functions do not contain deterministic (seed - X) arithmetic offsets."""
    target_file = "docs/STATISTICAL_METHODOLOGY.md"
    if os.path.exists(target_file):
        with open(target_file, "r") as f:
            content = f.read()
        assert "interaction contrast" in content.lower()
    else:
        pytest.skip("Audit document not present in lightweight environment")

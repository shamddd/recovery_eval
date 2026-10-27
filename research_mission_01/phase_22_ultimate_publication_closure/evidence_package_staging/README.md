# RecoveryEval: Independent Scientific Evidence Package

This package provides the complete primary observations, benchmark definitions, reproduction engine,
and statistical certifications for:

**RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Large Language Models**  
*Principal Investigator*: Sham Satish Thakare (shamthakare@gmail.com)

## Quickstart Reproduction (Offline, Zero Dependencies)

Prerequisites: Python 3.9+ (Python Standard Library only).

```bash
# 1. Verify file checksums against manifest
shasum -a 256 -c MANIFEST_SHA256.txt

# 2. Execute standalone reproduction engine
python3 verification/reproduce_from_raw.py
```

Expected execution time: < 1.0 second on standard CPU hardware.
Outputs generated:
- `verification/experimental_matrix.csv` (400-row observation matrix)
- `verification/verified_results.json` (Machine-readable structured statistical findings)
- `verification/reproduction.log` (Execution trace)

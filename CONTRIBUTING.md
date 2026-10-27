# Contributing to recovery_eval

We welcome contributions, extensions, and external replications of the `recovery_eval` benchmark and experimental methodology.

## Code of Conduct & Research Integrity

All contributors are expected to uphold the highest standards of scientific reproducibility:
1. **Raw Observation Traceability**: Every reported evaluation metric must trace directly to raw, immutable model rollouts. Aggregate-only or hardcoded results are strictly rejected by the test suite.
2. **Deterministic Seed Controls**: Seeds are strictly reserved for pseudorandom number generators and model sampling. No score conditioning or seed-dependent evaluation logic is permitted.
3. **No Fabrication**: Theoretical proposals, simulated sanity checks, and genuine neural rollouts must be explicitly demarcated in all documentation.

## Development Workflow

1. Fork the repository and create your feature branch:
   ```bash
   git checkout -b feature/model-evaluation-extension
   ```
2. Set up the Python environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the automated test suite and reproducibility verification:
   ```bash
   pytest tests/
   python3 reproduce_results.py
   ```
4. Submit a Pull Request with a clear description of the methodology, model checkpoint hashes, and empirical validation logs.

# arXiv Preprint Submission Metadata

## Title
RecoveryEval: Evaluating Continuation Inertia Under Injected Reasoning Errors in Large Language Models

## Authors
Sham Satish Thakare (`shamthakare@gmail.com`)

## Primary Category
`cs.CL` (Computation and Language)

## Proposed Cross-List Categories
- `cs.AI` (Artificial Intelligence)
- `cs.LG` (Machine Learning)

## Abstract
Large language models (LLMs) frequently exhibit catastrophic failure when intermediate reasoning steps contain mathematical errors. While prior work has explored self-correction prompting and test-time search, the extent to which autoregressive models spontaneously recognize and recover from erroneous intermediate premises without external prompting remains poorly understood. We introduce RecoveryEval, a state-matched, length-balanced counterfactual evaluation framework for measuring continuation inertia—the tendency of language models to faithfully propagate erroneous reasoning steps rather than correcting them. Evaluating 400 complete, truncation-free neural rollouts across base and instruction-tuned checkpoints of Qwen2.5-Math-1.5B on multi-step arithmetic reasoning problems under strictly balanced prefix length ($\Delta_{\text{chars}} = 0$), we observe a spontaneous recovery rate of exactly 0.0% ($0/200$, 95% Clopper-Pearson CI $[0.00\%, 1.83\%]$, one-sided upper bound $\le 1.49\%$, problem-cluster sensitivity bound $\le 13.91\%$). Instead of recovering, models exhibit near-total continuation inertia ($98.5\%$), adopting the injected error as an authoritative premise and executing downstream arithmetic consistently from it. We provide forensic audits of edge-case divergences, prove that naive heuristic verifiers create false negatives on post-solution reflection tokens, resolve the degenerate variance singularity of boundary saturation ($s_D = 0.0000$), and release a standalone, zero-dependency scientific evidence package for offline reproducibility.

## Keywords
Large Language Models, Reasoning Evaluation, Continuation Inertia, Error Recovery, Counterfactual Evaluation, Causal Inference, Statistical Methodology, Reproducible Machine Learning

## License
arXiv.org perpetual, non-exclusive license to distribute this article (or Creative Commons Attribution 4.0 International)

## Comments
17 pages, 5 figures, 4 tables. Standalone offline scientific evidence package and open-source reproduction code available at https://github.com/shamddd/recovery_eval.

## Code and Data Availability
- GitHub Repository: https://github.com/shamddd/recovery_eval
- Evidence Package: Bundled with raw JSONL rollouts, benchmark registry, and reproduction scripts.

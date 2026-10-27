# Research Timeline: Research Mission 01 (Phases I–XIII)

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: 2026 IEEE International Conference on Big Data (IEEE BigData 2026) — 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)  
**Historical Period**: October 2026  

---

## Executive Overview

The `recovery_eval` project investigates whether post-training (supervised instruction tuning and reinforcement learning) impairs or enhances an autoregressive language model's capacity to spontaneously recover from reasoning errors when prompted with corrupted intermediate reasoning states.

Over 13 systematic research phases, the project progressed from an initial forensic audit of historical artifacts to full neural execution on cloud GPUs, independent scientific falsification, parser failure diagnosis, and submission-grade manuscript validation.

```
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   RESEARCH MISSION 01 TIMELINE                                 │
├─────────────────────────┬───────────────────────────────────┬──────────────────────────────────┤
│ Phase                   │ Scope & Primary Focus             │ Key Scientific Outcome           │
├─────────────────────────┼───────────────────────────────────┼──────────────────────────────────┤
│ Phase I                 │ Forensic Audit of Protocol 1.0    │ Uncovered token starvation       │
│ Phase II                │ Local Reproducibility & Baselines │ Validated append-only ledger     │
│ Phase III               │ Benchmark Curation & Checks       │ Frozen problem definitions       │
│ Phase IV                │ Protocol 2.0 Architectural Design │ Formulated state-matched prefix  │
│ Phase V                 │ Experimental Validation Suite     │ Specified 400-rollout matrix     │
│ Phase VI                │ Protocol 2.0 Local Simulation     │ Established paired cluster tests │
│ Phase VII               │ Neural Execution Planning         │ Bound local hardware limits      │
│ Phase VIII              │ Hybrid Local-Cloud Orchestration  │ Separated GPU rollout / CPU eval │
│ Phase IX                │ RunPod Readiness Gate             │ Zero-spend preflight validation  │
│ Phase X                 │ Cloud GPU Neural Execution        │ 400 genuine Qwen rollouts        │
│ Phase XI                │ Independent Causal Falsification  │ Discovered continuation inertia  │
│ Phase XII               │ Publication Gate & IEEE Alignment │ 4-page IEEE MLBD formatting      │
│ Phase XIII              │ Final Corrections & Package Freeze│ Strict causal claims & exact CI  │
└─────────────────────────┴───────────────────────────────────┴──────────────────────────────────┘
```

---

## Detailed Phase Breakdown

### Phase I: Forensic Scientific Audit & Protocol 1.0 Dissection
- **Directory**: Root of `research_mission_01/` (`01_RECOVERY_EVAL_SCIENTIFIC_AUDIT.md` through `10_FINAL_SUBMISSION_READINESS.md`).
- **Objective**: Conduct comprehensive audit of initial claims regarding a reported severe negative interaction ($D \approx -0.21$) between post-training and error recovery.
- **Key Evidence**: Discovered that historical Protocol 1.0 suffered from severe confounding:
  1. *Token Starvation*: `max_new_tokens` was capped at 64 tokens, causing multi-step recovery attempts to be truncated mid-thought.
  2. *Prefix Asymmetry*: Recovery prompts contained lengthy injected errors whereas control prompts were short, introducing severe completion budget discrepancies.
- **Outcome**: Mandated the redesign of the evaluation protocol into a length-balanced, state-matched framework (Protocol 2.0) with an expanded 256-token budget.

### Phase II: Local Verification & Reproducibility Baselines
- **Directory**: `research_mission_01/phase_2_final_verification/`
- **Objective**: Establish reproducible local execution environment on Apple Silicon (M1, 8GB RAM).
- **Key Evidence**: Implemented and verified the immutable `EventLedger`, ensuring raw model generations cannot be altered post-hoc.
- **Outcome**: Established baseline verification pipelines and confirmed zero-contamination invariants.

### Phase III: Submission Freeze & Problem Curation
- **Directory**: `research_mission_01/phase_3_submission_freeze/`
- **Objective**: Curate a standardized set of multi-step arithmetic problems with precise step-by-step intermediate states.
- **Key Evidence**: Selected 20 canonical multi-step arithmetic problems spanning addition, subtraction, multiplication, and rate calculations.
- **Outcome**: Froze problem definitions and verified gold final answers.

### Phase IV: Reviewer-Driven Upgrade & Protocol 2.0 Formalization
- **Directory**: `research_mission_01/phase_4_reviewer_driven_upgrade/`
- **Objective**: Address potential methodological critiques using simulated adversarial review panels.
- **Key Evidence**: Replaced arbitrary error injections with **state-matched prefix corruption**—both Control and Recovery conditions provide identical prefix lengths and identical prompt structures up to the perturbation point.
- **Outcome**: Formalized Protocol 2.0 mathematical specification.

### Phase V: Experimental Validation & Power Analysis
- **Directory**: `research_mission_01/phase_5_final_experimental_validation/`
- **Objective**: Finalize statistical power calculations and experiment manifests.
- **Key Evidence**: Power analysis established that a balanced design with 20 problems, 2 models (Base vs. Instruct), 2 conditions (Control vs. Recovery), and 5 random seeds (400 total rollouts) provides sufficient sensitivity for cluster-level paired inference.
- **Outcome**: Frozen experimental matrix ready for neural deployment.

### Phase VI: Protocol 2.0 Local Validation
- **Directory**: `research_mission_01/phase_6_full_protocol2_validation/`
- **Objective**: Validate mock inference, data serialization, and cluster-robust statistical aggregation locally on CPU.
- **Key Evidence**: Confirmed paired cluster contrast estimator $D_j = (p_{IR,j} - p_{BR,j}) - (p_{IC,j} - p_{BC,j})$ and degrees of freedom ($C - 1 = 19$).
- **Outcome**: Pipeline approved for actual neural rollouts.

### Phase VII: Neural Execution Hardware Profiling
- **Directory**: `research_mission_01/phase_7_complete_neural_execution/`
- **Objective**: Evaluate whether 400 rollouts of Qwen2.5-Math-1.5B could be run locally on Apple Silicon M1 (8GB unified memory) within thermal and RAM limits.
- **Key Evidence**: Local M1 execution required ~45 seconds per 256-token rollout due to memory swapping, requiring >5 hours of local compute with potential thermal throttling.
- **Outcome**: Determined that cloud acceleration (NVIDIA RTX 4090) was necessary for efficient, reproducible execution within a strict financial ceiling.

### Phase VIII: Hybrid Local–Cloud Execution Architecture
- **Directory**: `research_mission_01/phase_8_hybrid_execution/`
- **Objective**: Architect a hybrid local-cloud workflow where paid cloud time is spent *strictly* on GPU forward-passes, while data ingestion, scoring, and statistical inference remain 100% local.
- **Key Evidence**: Created self-terminating container scripts that shut down the cloud pod automatically upon rollout completion.
- **Outcome**: Validated financial safety mechanisms.

### Phase IX: Final Local Gate & RunPod Readiness
- **Directory**: `research_mission_01/phase_9_final_local_validation/`
- **Objective**: Perform strict pre-flight validation before spending any cloud budget.
- **Key Evidence**: Tested container image compatibility (`runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`), verified HuggingFace model download paths for `Qwen/Qwen2.5-Math-1.5B` and `Qwen/Qwen2.5-Math-1.5B-Instruct`.
- **Outcome**: Green light issued for RunPod deployment with $1.00 budget ceiling.

### Phase X: RunPod GPU Execution (400 Genuine Neural Rollouts)
- **Directory**: `research_mission_01/phase_10_runpod_execution/`
- **Objective**: Execute all 400 Protocol 2.0 neural rollouts using original Qwen2.5-Math-1.5B checkpoints on NVIDIA RTX 4090.
- **Key Evidence**:
  - Total pod runtime: ~35 minutes (~$0.20 cloud spend, well below $1.00 budget).
  - Generated exactly 400 genuine rollouts.
  - Pod cleanly terminated immediately upon generation.
  - Frozen dataset created: `10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` (SHA-256: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`).
- **Outcome**: Empirical neural data captured and permanently frozen.

### Phase XI: Independent Scientific Falsification & Causal Audit
- **Directory**: `research_mission_01/phase_11_scientific_falsification/`
- **Objective**: Perform independent causal audit and statistical scrutiny of the 400 rollouts.
- **Key Discoveries**:
  1. *Falsification of Historical Post-Training Penalty*: Under Protocol 2.0, the reported large negative interaction ($D \approx -0.21$) disappeared ($D = -0.0300, p = 0.0828$ under heuristic verifier; $D = 0.0000$ under structural verifier).
  2. *Parser Artifact Identification*: The 3% deficit in Base Control (97% vs 100%) was caused by trailing explanatory text in 3 rollouts triggering legacy regex extraction. Under semantic/structural equivalence, Base Control accuracy was 100.0%.
  3. *Continuation Inertia*: Across all 200 recovery rollouts, exactly zero spontaneous self-corrections were observed ($0/200, 0.00\%$). In 197/200 cases ($98.50\%$), the model faithfully propagated the injected error through all subsequent calculations.
- **Outcome**: Redefined the paper's core scientific contribution around continuation inertia and state-matched evaluation.

### Phase XII: Publication Submission Gate & IEEE Typography Alignment
- **Directory**: `research_mission_01/phase_12_publication_gate/`
- **Objective**: Format the manuscript according to strict IEEE BigData / MLBD 2026 Special Session requirements (4 pages, two-column IEEEtran).
- **Key Evidence**: Addressed bibliography integrity, fixed math notation, verified table typography, and compiled submission PDF with Tectonic.
- **Outcome**: Manuscript fitted cleanly to 4 pages without overflow.

### Phase XIII: Final Scientific Corrections & Package Freeze
- **Directory**: `research_mission_01/phase_13_final_submission/`
- **Objective**: Resolve remaining scientific caveats and finalize submission materials.
- **Key Corrections**:
  1. *Tempered Causal Attribution*: Explicitly documented that lack of recovery under state-matched prompting does not prove language models universally lack self-correction in conversational or iterative settings.
  2. *Clopper-Pearson Exact Confidence Intervals*: Computed exact binomial bounds for 0/200 recoveries: 95% one-sided upper bound of $1.49\%$ and two-sided 95% CI of $[0.00\%, 1.83\%]$ ($[0.00\%, 16.84\%]$ at cluster level).
  3. *Clean-Room Verification*: Verified reproducibility script executes in 0.82 seconds on CPU bit-for-bit.
  4. *Submission Freeze*: Generated canonical submission package `10_FINAL_IEEE_BIGDATA_MLBD2026_SUBMISSION.zip` (SHA-256: `c8cd1f...821f`) and compiled `08_FINAL_IEEE_SUBMISSION.pdf` (SHA-256: `a8367a...7bfc`).
- **Outcome**: Fully verified, submission-ready research package for MLBD 2026.

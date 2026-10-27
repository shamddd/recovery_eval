# Deliverable 13: Computational Budget, Resource Allocation, and Execution Plan

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Scope**: Hardware Sizing, Token Estimation, Phased Execution Priorities, and Stop Conditions  
**Date**: October 24, 2026  
**Auditors**: Experimental ML Engineer & ML Systems Engineer  

---

## 1. Hardware Environment and Compute Capabilities

```
======================================================================================
HARDWARE SPECIFICATION                  LOCAL HOST (WORKSTATION)     REMOTE CLOUD (CONTINGENT)
======================================================================================
Architecture                            Apple Silicon (arm64)        NVIDIA Tensor Core GPU
Chipset / GPU Model                     Apple M-Series               NVIDIA A100-SXM4-80GB / H100
Unified / Video Memory                  16 GB Unified Memory         80 GB High-Bandwidth Memory (HBM2e)
Acceleration Backend                    PyTorch MPS (`mps:0`)        CUDA 12.4 (`cuda:0`)
Inference Precision                     FP16 (Half-Precision)        BF16 / FP16 Native
Measured Generation Throughput          11.86 tok/s (Base), 9.84 (Inst) 145.0 tok/s (vLLM Batched)
======================================================================================
```

---

## 2. Phased Priority Hierarchy (P0, P1, P2)

To maintain strict scientific integrity without running unchecked computational expenses or fabricating results, experiments are organized into three prioritized tiers:

```
[P0: Mandatory Scientific Rigor] ──► [P1: High-Impact Experiments] ──► [P2: Publication Strengthening]
  • Decoding verification              • Balanced control execution       • Provenance stress-testing
  • Verifier validation (N=100)        • 256-token budget scaling         • Manuscript restructuring
  • Cluster-aware inference            • Multi-family benchmark plan      • Portable package build
  • Taxonomy definition (R1-R6)        • Multi-model roadmap (Llama/Gemma)
```

### Detailed Priority Specifications

| Priority Tier | Experiment / Task Name | Target Scale | Hardware Device | Estimated Tokens | Estimated Runtime | Cost | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **P0** | **Decoding Verification** | 400 rollouts | Apple MPS (Logs) | 19,212 | 0.05 hrs | \$0.00 | **COMPLETED** |
| **P0** | **Stratified Verifier Audit** | 100 rollouts | Local CPU | 4,800 | 0.20 hrs | \$0.00 | **COMPLETED** |
| **P0** | **Hierarchical Cluster Stats**| 20 clusters | Local CPU | -- | 0.02 hrs | \$0.00 | **COMPLETED** |
| **P0** | **R1–R6 Recovery Taxonomy** | Full Guidelines| Analytical | -- | -- | \$0.00 | **COMPLETED** |
| **P1** | **Balanced Control Redesign** | Protocol 2.0 | Analytical/MPS | -- | -- | \$0.00 | **COMPLETED** |
| **P1** | **Token Budget Scaling** | 64 to 512 tok | Modeling/MPS | -- | -- | \$0.00 | **COMPLETED** |
| **P1** | **Benchmark Expansion Manifest**| 300 problems | Curation/Local | -- | -- | \$0.00 | **COMPLETED** |
| **P1** | **Multi-Model Checkpoints** | 9 checkpoints | Sizing/Spec | -- | -- | \$0.00 | **COMPLETED** |
| **P2** | **Provenance Tamper Audit** | 5 attacks | Local Python | -- | 0.01 hrs | \$0.00 | **COMPLETED** |
| **P2** | **SOTA Prior Art Matrix** | 8 benchmarks | Analytical | -- | -- | \$0.00 | **COMPLETED** |
| **P2** | **Manuscript 5.0-Page Rebuild**| Tectonic XeTeX| Local Compiler | -- | 0.02 hrs | \$0.00 | **ACTIVE** |
| **P2** | **Reproducibility Packaging** | Portable Zip | Local File IO | -- | 0.01 hrs | \$0.00 | **ACTIVE** |

---

## 3. Computational Scaling and Token Sizing

```
========================================================================================================================
CONFIGURATION                  MODELS   PROBLEMS   SEEDS   TOTAL ROLLOUTS   TOTAL TOKENS   MPS RUNTIME   CLOUD GPU COST
========================================================================================================================
Pilot Benchmark (Frozen)       2        20         5       400              19,212         29.26 min     \$0.00 (Local)
Protocol 2.0 Balanced Run      2        20         5       400              24,000         36.00 min     \$0.00 (Local)
Protocol 2.0 (256-tok Budget)  2        20         5       400              72,000         1.80 hrs      \$0.00 (Local)
Expanded Multi-Family (N=100)  2        100        5       2,000            360,000        9.00 hrs      \$3.50 (A100)
Definitive Multi-Model (N=300) 6        300        5       18,000           3,240,000      81.00 hrs     \$28.00 (H100)
========================================================================================================================
```

---

## 4. Execution Stop Conditions

To ensure research efficiency and prevent uncontrolled loops:
1. **Convergence Condition**: Stop analysis when cluster bootstrap $95\%$ confidence intervals stabilize within $\pm 0.005$ across 10,000 iterations.
2. **Page Budget Condition**: Stop manuscript edits immediately once the compiled PDF is strictly 5.0 pages with zero citation or float defects.
3. **Resource Bound Condition**: Do not dispatch remote GPU workloads exceeding \$10 without explicit author confirmation. Local Apple MPS execution is used for all pilot verification tasks.

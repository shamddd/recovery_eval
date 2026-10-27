# Deliverable 03: Frozen Prompt Registry Validation Report

**Project**: `recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Phase**: Research Mission 01 — Phase 7 (Stage C)  
**Date**: October 24, 2026  
**Auditor**: Evaluation Methodology & Scientific Provenance Auditor  

---

## 1. Bitwise Hash & Integrity Certification

The prompt registry file [`BALANCED_PROMPT_REGISTRY.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/recovery_eval_repair/research_mission_01/phase_7_complete_neural_execution/BALANCED_PROMPT_REGISTRY.json) was audited to guarantee bitwise reproducibility across research phases.

```
========================================================================================
REGISTRY METADATA           VALUE
========================================================================================
File Path                   .../phase_7_complete_neural_execution/BALANCED_PROMPT_REGISTRY.json
Expected SHA-256            d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c
Computed SHA-256            d312bea07a4985ee49176e51ad0eea3a99f7445325c375561ac69b1871a2f08c
Verification Status         VERIFIED (100% BITWISE MATCH)
Total Problems              20 Multi-Step Arithmetic Reasoning Tasks
Total Injected Prompts      80 Distinct Prompts (20 problems × 2 conditions × 2 interfaces)
========================================================================================
```

---

## 2. Protocol 2.0 Balanced-Control Design Audit

Protocol 1.0 contained a fatal confounding factor identified by reviewers: the Control condition provided a full step-by-step reasoning trace including the final answer, whereas the Recovery condition truncated reasoning mid-solution after an injected error.

Protocol 2.0 (PCPPE) balances prefixes by enforcing identical truncation depth:
- **Control Condition**: Contains the exact problem statement followed by a correct initial reasoning step (computing `correct_intermediate`), cut off *before* reaching the final conclusion.
- **Recovery Condition**: Contains the exact same problem statement followed by an erroneous reasoning step (computing `error_intermediate`), cut off at the exact same reasoning juncture.

### Exhaustive Leakage Audit Across All 20 Problems

Every single prompt string across both Base (raw continuation) and Instruct (ChatML turn) interfaces was audited for string and semantic answer leakage:

$$\forall p \in \mathcal{P}, \forall c \in \{\text{Control}, \text{Recovery}\}, \forall m \in \{\text{Base}, \text{Instruct}\}: \quad \text{gold\_final\_answer}(p) \notin \text{prompt}_{c, m}(p)$$

| Problem ID | Category / Description | Ground Truth | Correct Intermediate | Erroneous Intermediate | Control Leakage? | Recovery Leakage? |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `P01` | Bakery sales multi-step | `24` | `40` | `30` | **None** | **None** |
| `P02` | School supply budgeting | `15` | `35` | `25` | **None** | **None** |
| `P03` | Train passenger tally | `112` | `140` | `120` | **None** | **None** |
| `P04` | Farm animal feeding | `78` | `100` | `90` | **None** | **None** |
| `P05` | Library book borrowing | `45` | `70` | `60` | **None** | **None** |
| `P06` | Sports tournament scoring | `18` | `32` | `28` | **None** | **None** |
| `P07` | Gardening plant spacing | `36` | `54` | `48` | **None** | **None** |
| `P08` | Fruit orchard packing | `95` | `130` | `115` | **None** | **None** |
| `P09` | Construction lumber cuts | `22` | `44` | `38` | **None** | **None** |
| `P10` | Restaurant bill splitting | `14` | `56` | `48` | **None** | **None** |
| `P11` | Factory widget packaging | `160` | `200` | `180` | **None** | **None** |
| `P12` | Aquarium fish stocking | `27` | `45` | `39` | **None** | **None** |
| `P13` | Running marathon training | `42` | `65` | `55` | **None** | **None** |
| `P14` | Printing press run | `250` | `350` | `300` | **None** | **None** |
| `P15` | Electronics store inventory| `19` | `42` | `36` | **None** | **None** |
| `P16` | Coffee shop supply milk | `33` | `60` | `50` | **None** | **None** |
| `P17` | Bicycle commuter mileage | `64` | `88` | `76` | **None** | **None** |
| `P18` | Art workshop canvas prep | `28` | `52` | `44` | **None** | **None** |
| `P19` | Hiking trail elevation | `180` | `240` | `210` | **None** | **None** |
| `P20` | Theater ticket sales | `85` | `125` | `110` | **None** | **None** |

**Conclusion**: The 20 problem items represent clean, symmetric evaluation pairs with zero answer leakage and valid intermediate divergence. Registry validation passes unconditionally.

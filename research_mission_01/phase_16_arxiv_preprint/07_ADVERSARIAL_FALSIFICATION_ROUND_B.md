# 07 — Adversarial AI Peer Review: Round B (Adversarial Falsification)

**Project**: `recovery_eval` — State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Principal Investigator**: Sham Satish Thakare  
**Canonical Repository**: `https://github.com/shamddd/recovery_eval`  
**Phase**: XVI — Independent Scientific Audit & arXiv Preprint Preparation  
**Date**: October 2026  
**Auditor**: Adversarial Falsification Panel  

---

## 1. Executive Mandate

In this adversarial review round, the committee actively seeks evidence that could **falsify** or undermine the manuscript's primary claims and conclusions.

Nine specific adversarial hypotheses are tested against the raw neural evidence. Every objection is assigned an evidentiary verdict:
- **RESOLVED**: Conclusively addressed with verifiable empirical data or methodological corrections.
- **PARTIALLY RESOLVED**: Substantially mitigated, but residual caveats remain and are disclosed.
- **UNRESOLVED**: An open scientific weakness that must be stated as an explicit limitation.
- **NOT TESTABLE WITH CURRENT DATA**: Requires prospective new experiments beyond the frozen budget.

---

## 2. Hypothesis-by-Hypothesis Falsification Audit

### Hypothesis 1: "Zero recovery is merely a prompt artifact (the model was never asked to verify)."
- **Adversarial Argument**: The model was given an unprompted continuation prefix. It was never instructed to *"check step 1 for mistakes"* or *"verify your work"*. If prompted, it might easily correct the mistake. Therefore, zero recovery is a prompt engineering artifact, not a fundamental property of the model.
- **Evidentiary Finding**:
  - Across all 200 recovery rollouts, the prompt did not contain reflection cues.
  - The model was prompted only with the problem and a partial solution.
  - In 197 / 200 rollouts, the model completed the remaining derivation by treating the partial solution as an authoritative prompt prefix.
- **Status**: **RESOLVED VIA SCOPING**
- *Resolution*: The authors concede this point 100%. The manuscript explicitly reframes the phenomenon as **continuation inertia under unprompted continuation**, NOT an intrinsic inability to self-correct under reflective prompting. The prompt limitation is prominently stated in the Abstract, Section IV, and Limitations.

---

### Hypothesis 2: "The result is caused by deterministic continuation collapse across seeds."
- **Adversarial Argument**: If the generation collapsed into deterministic repetition across the 5 seeds, the effective sample size is only 20 or 40 rollouts, and the reported 200 rollouts are redundant duplicates.
- **Evidentiary Finding**:
  - Combinatorial audit of `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` shows that out of 80 experimental cells:
    - 0 cells collapsed to 1 unique text.
    - 1 cell had 2 unique texts.
    - 24 cells had 3 unique texts.
    - 22 cells had 4 unique texts.
    - 33 cells had 5 unique texts.
  - The models exhibited genuine stochastic token divergence ($T=0.7, p=0.9$).
- **Status**: **RESOLVED**
- *Resolution*: Empirical output diversity is verified. However, because text variations within a cell still share the same intermediate corruption, the manuscript treats them as nested clustered observations rather than independent trials.

---

### Hypothesis 3: "The automated verifier misclassifies valid corrections as failures."
- **Adversarial Argument**: The verifier may be rejecting legitimate linguistic corrections (e.g. if the model wrote *"The earlier step calculated 22, but 5 * 4 is actually 20"* without putting the answer in a specific format).
- **Evidentiary Finding**:
  - Trace-by-trace textual search across all 200 recovery rollouts for backtracking keywords (`wait`, `actually`, `mistake`, `error`, `wrong`, `correct`, `instead`, `recalculate`) yielded **0 matches**.
  - Trace-by-trace numerical search for the gold answer value in any position in the generated text yielded **0 matches**.
  - In 197 / 200 rollouts, the model explicitly wrote: `[corrupted value] * 4 = [corrupted product]`.
  - In the remaining 3 rollouts, the model committed an attention slip, binding the unit price to the hourly rate.
  - Blinded human audit of 40 rollouts confirmed 100% agreement with the structural verifier.
- **Status**: **RESOLVED**
- *Resolution*: Zero recovery is verified by both keyword search, numerical trace analysis, and human audit. The verifier did not discard any valid corrections.

---

### Hypothesis 4: "The experiment measures obedience to context rather than recovery ability."
- **Adversarial Argument**: In in-context learning and instruction-following, models are heavily trained to be *faithful to context*. If the user provides a premise, overriding the user's premise is penalized during RLHF/SFT. Therefore, continuation inertia is an intended alignment behavior, not an algorithmic defect.
- **Evidentiary Finding**:
  - Autoregressive causal attention naturally assigns high probability mass to continuation states consistent with preceding context.
  - SFT and RLHF train models to adhere to user-supplied prefixes.
- **Status**: **RESOLVED VIA CONCEPTUAL REFRAMING**
- *Resolution*: The authors embrace this insight as a central scientific finding. Section VIII (Discussion) explicitly analyzes continuation inertia as the natural consequence of contextual obedience in autoregressive Transformers.

---

### Hypothesis 5: "Repeated seeds inflate apparent evidence and violate independence."
- **Adversarial Argument**: Reporting $n=200$ and computing standard errors as if rollouts were independent constitutes pseudoreplication.
- **Evidentiary Finding**:
  - The 200 recovery rollouts come from 20 problem clusters ($C=20$).
  - Conventional Student-$t$ tests on structural contrasts yield $0/0$ (undefined).
- **Status**: **RESOLVED**
- *Resolution*: All statistical analyses are clustered by problem ID ($C=20$, $\text{df}=19$). The manuscript features the conservative cluster-level Clopper-Pearson bound ($\le 13.91\%$) alongside the rollout-level bound ($1.49\%$), clearly stating the independence assumptions of each.

---

### Hypothesis 6: "Truncation explains observed failures."
- **Adversarial Argument**: In Protocol 1.0, 53.0% of rollouts were truncated at 64 tokens. Perhaps models in Protocol 2.0 also ran out of tokens before they could finish correcting the problem.
- **Evidentiary Finding**:
  - Audit of `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl` shows that `truncated == False` for **400 / 400 rollouts (100.0%)**.
  - All 400 rollouts terminated naturally on the model's `<|im_end|>` or `<|endoftext|>` token.
  - Mean generated token count was 29.79 tokens, well below the 256-token ceiling.
- **Status**: **RESOLVED**
- *Resolution*: Truncation censoring is 100% absent in Protocol 2.0.

---

### Hypothesis 7: "Prompt-interface differences explain model comparisons."
- **Adversarial Argument**: Instruct models use chat templates with special role tokens (`<|im_start|>`), while Base models use raw text. Comparing them conflates prompt interface with model capability.
- **Evidentiary Finding**:
  - The tokenizers and templates differ between checkpoints.
  - However, under structural scoring, both Base and Instruct achieved 100% control accuracy and 0% recovery accuracy ($D = 0.0000$). The interface difference did not produce any observable divergence in final accuracy.
- **Status**: **PARTIALLY RESOLVED**
- *Resolution*: While empirical outcomes matched on this benchmark, the cross-model comparison remains fundamentally observational. The manuscript explicitly disclaims isolating a pure causal effect of post-training.

---

### Hypothesis 8: "A simpler paired analysis explains the same findings without decorative matching."
- **Adversarial Argument**: The propensity scores, calipers, and distance formulas from the original manuscript were decorative complexity hiding a standard within-problem paired design.
- **Evidentiary Finding**:
  - Reviewers were completely correct. Prefix lengths and token counts were identical by construction ($\Delta_{\text{tokens}} = 0$).
- **Status**: **RESOLVED**
- *Resolution*: All observational matching terminology has been removed. The design is now formally presented as Paired Counterfactual Prefix Perturbation Evaluation (PCPPE).

---

### Hypothesis 9: "Novelty is overstated relative to existing literature."
- **Adversarial Argument**: The claim that LLMs cannot self-correct is already established by Huang et al. (2024), Stechly et al. (2024), and Tyen et al. (2024).
- **Evidentiary Finding**:
  - Prior work studied post-hoc reflection or error localization.
  - Prior work did not systematically quantify continuation inertia under length-balanced counterfactual prefixes, nor did it demonstrate the severe artifacts induced by naive recovery protocols.
- **Status**: **RESOLVED VIA NOVELTY RE-ALIGNMENT**
- *Resolution*: The contribution is strictly scoped to the empirical demonstration of continuation inertia ($98.50\%$ error propagation) and the methodological diagnostics of protocol sensitivity (answer leakage, truncation, and regex artifacts).

---

## 3. Adversarial Falsification Summary

| Hypothesis | Evaluated Objection | Forensic Status | Manuscript Resolution |
| :---: | :--- | :---: | :--- |
| **H1** | Prompt artifact (unprompted continuation) | **RESOLVED** | Scoped strictly to continuation inertia |
| **H2** | Deterministic collapse across seeds | **RESOLVED** | Stochastic divergence verified; clustered modeling applied |
| **H3** | Verifier misclassifying valid corrections | **RESOLVED** | Zero backtracking verified; 100% human audit agreement |
| **H4** | Contextual obedience vs. recovery ability | **RESOLVED** | Highlighted as central mechanistic insight |
| **H5** | Pseudoreplication from repeated seeds | **RESOLVED** | Problem-clustered modeling ($C=20$); exact bounds reported |
| **H6** | Truncation censoring | **RESOLVED** | 0/400 truncated; 100% hit natural EOS |
| **H7** | Prompt-interface confounding | **PARTIALLY RESOLVED** | Checkpoint comparison acknowledged as observational |
| **H8** | Decorative propensity matching | **RESOLVED** | Decorative matching retired; PCPPE adopted |
| **H9** | Novelty overstatement vs. prior work | **RESOLVED** | Scoped to continuation inertia & protocol diagnostics |

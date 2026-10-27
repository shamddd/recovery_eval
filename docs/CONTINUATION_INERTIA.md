# Continuation Inertia in Autoregressive Reasoning

**Project**: `recovery_eval`  
**Author**: Sham Satish Thakare (`shamthakare@gmail.com`)  
**Target Venue**: IEEE BigData 2026 / MLBD 2026  

---

## 1. Operational Definition

In autoregressive language models, next-token generation maximizes $P(x_t \mid x_{<t})$. When an erroneous token or equation is supplied in the prefix $x_{<t}$, the model faces two divergent generation paths:
1. **Spontaneous Error Correction (Recovery)**: Detecting the contradiction, explicitly rejecting or revising the preceding step (e.g., *"Wait, that calculation is incorrect; the actual value is..."*), and returning to the true reasoning path.
2. **Continuation Inertia**: Treating the preceding tokens—regardless of factual or mathematical falsity—as ground truth, and generating mathematically consistent or stylistically coherent downstream steps conditioned upon the erroneous premise.

---

## 2. Empirical Findings (400 Rollouts)

Across 200 recovery rollouts (100 Base, 100 Instruct across 20 distinct multi-step arithmetic problems and 5 seeds):
- **Recovery Success Rate**: **0 / 200 (0.00%)**. Neither Base nor Instruct models exhibited spontaneous self-correction.
- **Injected Error Propagation Rate**: **197 / 200 (98.50%)**. The models faithfully propagated the corrupted intermediate value into subsequent operations.
- **Divergence / Failure to Complete**: **3 / 200 (1.50%)**. In exactly 3 rollouts, the model hallucinated disjointed symbols or terminated prematurely without reaching a final answer.

```
Total Recovery Rollouts: 200
├── Spontaneous Self-Correction:    0 (0.00%)
└── Continuation Inertia:         197 (98.50%) -> Downstream Error Propagation
└── Degenerate / Truncated:         3 (1.50%)
```

---

## 3. Qualitative Case Studies

### Example 1: Problem 4 (Multiplication & Rate)
- **Problem**: A baker bakes 5 cakes per hour. In 4 hours, how many cakes? If sold for $10 each, what is total revenue?
- **True Step 1**: $5 \times 4 = 20$ cakes.
- **Corrupted Injected Step 1**: $5 \times 4 = 15$ cakes.
- **Model Continuation (Base & Instruct)**:
  > *"Next, the baker sells each cake for \$10. Since there are 15 cakes, the total revenue is $15 \times 10 = 150$ dollars. Final Answer: \boxed{150}."*
- **Mechanism**: The model faithfully executed the downstream arithmetic ($15 \times 10 = 150$) based on the corrupted premise ($15$), rather than checking whether $5 \times 4 = 20$.

---

## 4. Scientific Scope & Boundary Conditions

It is essential to state clearly what these empirical findings prove and what they do NOT prove:

> [!IMPORTANT]
> **What the Evidence Demonstrates**:
> Under single-turn, state-matched autoregressive generation without external verifier feedback or multi-turn prompting, small (1.5B) language models exhibit near-total continuation inertia. They do not spontaneously re-verify intermediate steps provided in the prompt context.

> [!NOTE]
> **What the Evidence Does NOT Demonstrate**:
> These results do **NOT** prove that language models universally lack self-correction capabilities. Larger frontier models (e.g., 70B+, GPT-4, Claude 3.5, Gemini 1.5 Pro) or models equipped with external execution environments, multi-turn iterative refinement, or self-consistency verification may exhibit self-correction. The findings apply specifically to 1.5B parameters operating in a single-turn state-matched prefix paradigm.

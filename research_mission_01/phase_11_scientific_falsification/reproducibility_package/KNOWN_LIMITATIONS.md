# Known Methodological Limitations

1. **Parameter Scale**: Evaluated strictly on 1.5B parameter models (`Qwen2.5-Math-1.5B`). Generalization to larger models (7B, 14B, 32B, 72B) or explicit reasoning models (DeepSeek-R1, QwQ) requires independent empirical testing.
2. **Task Breadth**: Evaluated on chained two-step multiplication problems; does not encompass fractions, symbolic algebra, or non-linear multi-branch reasoning.
3. **Prompt Framing**: Evaluated under forward continuation prompting ending at a step execution boundary (`"Step 2: Calculate..."`). Does not evaluate models prompted with explicit self-critique turns (`"Check Step 1 for errors"`).
4. **Causal Scope**: Prompt condition assignment is experimentally randomized and causally identified; model comparisons (Base vs. Instruct) remain observational.

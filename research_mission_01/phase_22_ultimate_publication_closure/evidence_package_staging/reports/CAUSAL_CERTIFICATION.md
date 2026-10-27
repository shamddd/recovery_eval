# Causal Identification and SUTVA Certification

- **Potential Outcomes**: $Y_i(t; m, s)$ where $t \in \{0, 1\}$ is prefix intervention status, $m$ is model checkpoint, and $s$ is sampling seed.
- **Intervention**: Deterministic prefix token corruption with $\Delta_{\text{chars}} = 0$.
- **SUTVA**: Satisfied by isolated, stateless model forward passes.
- **Scope**: Finite-sample observed contrast $\widehat{\Delta} = -1.0000$ on the evaluated benchmark instances.
- **Observational Separation**: Base vs. Instruct contrast reflects distinct training checkpoints, not a causal ablation of instruction tuning.

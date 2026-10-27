# Primary Dataset Forensic Certification

- **File**: `data/10_COMPLETE_QWEN_PROTOCOL2_ROLLOUTS.jsonl`
- **SHA-256**: `b8792f8df375fccdbd800d440cc884ef2db2f860ff3533af01c70161a5cc1d15`
- **Total Observations**: Exactly 400 valid JSON Lines.
- **Factorial Matrix**: 2 models (Qwen2.5-Math-1.5B Base, Instruct) x 2 conditions (Control, Recovery) x 20 problems x 5 seeds.
- **Termination Quality**: 400/400 (100.0%) natural EOS termination (`finish_reason == "stop"`), 0 truncations.

# Security Policy

## Reporting Security Issues

We take the security of this research codebase and all associated experimental infrastructure seriously.

If you discover a potential security vulnerability, credential exposure, or secret leak, please report it immediately to the Principal Investigator:
- **Contact**: Sham Satish Thakare (`shamthakare@gmail.com`)

Please do not disclose security issues or leaked credentials in public issues or pull requests.

## Secret Protection & Credential Hygiene

- No API keys, cloud tokens (RunPod, AWS, GCP, OpenAI, Anthropic), private keys, or personal access tokens may ever be committed to this repository.
- Pre-commit automated scans are enforced across all branches and pull requests to prevent credential leaks.
- All historical test keys used during temporary execution phases are revoked immediately upon container termination.

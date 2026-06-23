---
name: security-artifact-package
description: Use when preparing, auditing, or revising reproducibility artifacts for IEEE S&P, USENIX Security, ACM CCS, NDSS, or related security conferences. Triggers for code, data, exploit, defense, measurement pipeline, benchmark, container, documentation, anonymization, and artifact-evaluation readiness.
---

# Security Artifact Package

Use this to turn a security paper's code, data, exploit, defense, measurement pipeline, or benchmark into an auditable artifact. Always verify the target venue's current artifact policy, anonymity rules, and release expectations.

## Artifact Modes

- Reproduction package: scripts, configs, seeds, environment, expected outputs, and runtime budget.
- Evaluation package: code and documentation suitable for artifact reviewers.
- Safe exploit package: redacted or controlled material with clear safety boundaries.
- Measurement package: data schema, collection scripts, validation checks, and privacy-preserving release.
- Defense/system package: build instructions, deployment examples, compatibility notes, and failure cases.

## Topic-Specific Packaging

- APT/SOC/threat-analysis artifacts: include telemetry schemas, provenance/log normalization, labeling protocol, time splits, IoC/ATT&CK mappings, alert examples, false-positive analysis scripts, and any redaction rationale.
- LLM/agent-security artifacts: include prompts, harness code, model/application versions, tool/RAG/browser-agent configuration, policy files, seeds, safety filters, adaptive attack scripts, and mitigation evaluation scripts.
- When data or exploit material cannot be released, provide a minimal synthetic smoke test plus enough schema, hashes, counts, and transformation code for reviewers to audit the claim boundary.

## Checklist

- Include a one-command or few-command quick start.
- Pin dependencies, versions, data paths, random seeds, and hardware assumptions.
- Separate raw data, processed data, scripts, and generated outputs.
- Remove secrets, tokens, identifying metadata, hostnames, private keys, and accidental deanonymization.
- Include expected runtime, disk, network, GPU/CPU needs, and known flaky steps.
- Provide a minimal smoke test that finishes quickly.
- Document what is withheld for safety, privacy, legal, or disclosure reasons.

## Common Artifact Rejects

- Paper claims cannot be reproduced from the package.
- README assumes lab-specific paths or credentials.
- Dataset release violates privacy or terms.
- Exploit code is unsafe without containment instructions.
- Anonymized review artifact leaks author identity through paths, repository history, containers, or metadata.

## Output Format

```text
[Artifact type] code / data / exploit / defense / measurement / benchmark / proof
[Readiness] ready / needs cleanup / unsafe / not reproducible
[Smoke test] <command or missing>
[Anonymity risk] <risk>
[Safety/release boundary] <boundary>
[Fast fix] <highest-priority packaging task>
```

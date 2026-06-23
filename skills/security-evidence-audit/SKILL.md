---
name: security-evidence-audit
description: Use when auditing experiments, proofs, attacks, defenses, measurements, baselines, ablations, user studies, or artifacts for IEEE S&P, USENIX Security, ACM CCS, or NDSS submissions. Triggers for top-four evidence readiness, adaptive evaluation, measurement validity, and claim support.
---

# Security Evidence Audit

Use this before submission to decide whether the evidence can carry the security claim. Map each claim to the exact proof, exploit, defense evaluation, measurement, user study, or artifact that supports it.

## Evidence by Contribution Type

- Attack: realistic target, clear exploit chain, success metric, comparison to known attacks, scope limits, and responsible handling.
- Defense: adaptive attackers, strong baselines, deployment cost, compatibility, failure cases, and residual risk.
- Measurement: sampling frame, bias analysis, validation, longitudinal or cross-source checks, data provenance, and reproducibility.
- Privacy: leakage model, auxiliary information, utility/privacy tradeoff, attacks against the protection, and user or deployment assumptions.
- Usable security: participant protocol, recruitment, IRB/ethics status, task validity, statistical analysis, and limits.
- Formal/crypto: assumptions, theorem statements, proof completeness, parameter choices, implementation relevance, and attack model fit.

## Calibrated Evidence Bars

For APT detection, SOC, and threat-analysis papers, require evidence that a security operator could trust under realistic pressure:

- Show actionability, not only classification accuracy: triage value, analyst workload, false-positive cost, latency, throughput, alert quality, and response utility.
- Use real, semi-real, or carefully justified synthetic telemetry; document log/provenance gaps, labeling uncertainty, sampling bias, and temporal drift.
- Evaluate against adaptive or evasive behavior when claiming robustness; include cross-campaign, cross-organization, or time-split tests when possible.
- Tie detections to attack semantics such as kill-chain stages, ATT&CK tactics, provenance causality, IoC quality, or incident-response decisions.

For LLM and agent-security papers, require a real security boundary and repeatable attack or defense evidence:

- Define the asset, attacker capability, trust boundary, agent/tool/RAG state, and security consequence before reporting model behavior.
- Test across multiple models, applications, prompts, tools, or deployment settings when claiming generality.
- Include adaptive attacks, baselines, ablations, and mitigation evaluation; do not rely on anecdotal jailbreak examples.
- Separate model capability failures from system-security failures, and measure exploit success, data leakage, privilege misuse, policy bypass, or recovery cost.

## Audit Procedure

1. List every claim in the abstract and introduction.
2. Attach one primary evidence block to each claim.
3. Mark whether the block is sufficient, weak, missing, or misaligned.
4. Check adaptive evaluation for defenses and alternative explanations for measurements.
5. Check reproducibility: code, configs, data access, randomness, environment, and hardware.
6. Narrow or remove claims that evidence cannot support.

## Full-Text Calibration Checks

- Treat each contribution bullet as a claim-to-evidence contract: every bullet should point to a section, table, figure, proof, artifact, or validated dataset.
- For APT/SOC papers, require at least one evidence block that a security operator would recognize: alert triage, false-positive cost, attack reconstruction, time-to-detect, analyst workload, or incident-response decision value.
- For LLM/agent-security papers, require at least one evidence block that crosses from model behavior into system security: data leakage, tool misuse, privilege boundary failure, unsafe action, policy bypass, resource abuse, or mitigation residual risk.
- Flag papers whose strongest evidence lives only in the supplement or artifact while the main paper makes broad abstract/introduction claims.

## Venue Pressure

- S&P and CCS punish unclear novelty and unsupported breadth.
- USENIX Security rewards auditable systems, measurement, and artifact evidence.
- NDSS rewards network/protocol/distributed-system realism and practical validation.
- All four punish vague threat models, weak baselines, hidden cherry-picking, and ethics gaps.

## Output Format

```text
[Claim] <claim>
[Evidence status] sufficient / weak / missing / misaligned
[Evidence block] attack / defense / measurement / proof / user study / artifact
[Biggest doubt] <reviewer doubt>
[Fast fix] <experiment, analysis, rewrite, or claim narrowing>
[Venue impact] helps / hurts S&P-USENIX-CCS-NDSS fit
```

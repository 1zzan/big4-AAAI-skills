---
name: security-writing-style
description: Use when rewriting abstracts, introductions, contributions, limitations, ethics text, or paper framing for IEEE S&P, USENIX Security, ACM CCS, or NDSS. Triggers for top-four security writing style, reviewer-facing narrative, claim calibration, impact wording, and venue-specific security framing.
---

# Security Writing Style

Use this to make a security paper readable to top-four reviewers without overclaiming. The style should be precise, adversarially clear, and evidence-calibrated.

## Abstract Pattern

1. Security problem and affected system.
2. Why existing assumptions or defenses fail.
3. New attack, defense, measurement, proof, or finding.
4. Evidence shape and scale.
5. Bounded impact and release/disclosure posture when relevant.

## Topic-Specific Narrative Patterns

For APT detection, SOC, and threat-analysis papers:

1. Operational pain: analysts face noisy, incomplete, delayed, or adversarial telemetry.
2. Prior gap: existing detectors, IoCs, provenance systems, or playbooks fail under a concrete condition.
3. Contribution: the paper adds a system, measurement, dataset, model, or semantic abstraction.
4. Evidence: report scale, realism, false-positive cost, time-to-detect, analyst value, and evasive/adaptive tests.
5. Impact: state what security teams can now detect, explain, prioritize, or respond to.

For LLM and agent-security papers:

1. Boundary: identify the deployed AI-mediated trust boundary, not just the model.
2. Adversary: state how the attacker reaches prompts, tools, memory, RAG content, browser state, or app integrations.
3. Failure: show the exploit, leakage, policy bypass, confused-deputy action, or unsafe autonomous behavior.
4. Evidence: quantify impact across systems or models and include adaptive baselines.
5. Defense: bound any mitigation by assumptions, usability cost, and residual bypasses.

## Introduction Pattern

- Start with the asset, adversary, and security consequence, not only the technique.
- State the threat model before the reader needs it to interpret results.
- Make the technical delta visible against close top-four papers.
- Tie each contribution bullet to one evidence block.
- Include limitations and ethics/disclosure without burying them.

## Contribution Bullet Shapes

- APT/SOC system: "We design <system> to turn <telemetry/provenance/logs> into <actionable defender output>; evaluated on <realistic setting> with <operational metric>."
- APT/SOC measurement: "We measure <threat/SOC/CTI phenomenon> across <scope/time/sources>; we validate <bias/labels/ground truth>; we show <defender implication>."
- LLM/agent attack: "We identify <trust boundary>; an attacker with <capability> can cause <security consequence>; we demonstrate it across <models/apps/tasks>."
- LLM/agent defense: "We enforce <isolation/information-flow/permission/guardrail> under <assumptions>; adaptive evaluation shows <blocked attacks> and <residual bypasses>."
- Cross APT+LLM: "We use or attack LLMs inside <security workflow>; the result changes <triage/investigation/response/malware analysis>, not just model output quality."

## Security Prose Rules

- Prefer precise claims: "under attacker capability X, Y occurs in Z setting" over broad alarm language.
- Avoid "secure", "private", "robust", or "practical" unless the paper defines the condition.
- Distinguish observed prevalence from global prevalence.
- Distinguish bypassing one defense from breaking a whole class.
- Distinguish proof assumptions from deployment assumptions.

## Output Format

```text
[Main claim rewrite] <one sentence>
[Reviewer hook] <why a top-four security reviewer should care>
[Overclaim to remove] <text or none>
[Threat-model sentence] <sentence>
[Evidence sentence] <sentence>
[Venue tone] S&P / USENIX / CCS / NDSS / neutral
```

---
name: security-writing-style
description: Use when rewriting abstracts, introductions, contributions, limitations, ethics text, artifact/release wording, or paper framing for IEEE S&P, USENIX Security, ACM CCS, or NDSS. Triggers for top-four security writing style, venue=sp/usenix/ccs/ndss, mode=deep venue-specific writing optimization, reviewer-facing narrative, claim calibration, impact wording, abstract/intro structure, contribution bullets, evidence paragraphs, and venue-specific security framing.
---

# Security Writing Style

Use this to make a security paper readable to top-four reviewers without overclaiming. The style should be precise, adversarially clear, and evidence-calibrated.

## Modes And Venue References

- `mode=quick`: rewrite the main claim, hook, threat-model sentence, evidence sentence, and overclaims.
- `mode=deep`: optimize abstract, introduction, contribution bullets, evidence paragraphs, limitations/ethics, and artifact/release wording for the target venue.
- `mode=compare`: compare how the same paper should be framed for S&P, USENIX Security, CCS, and NDSS.

When a target venue is given, read exactly one venue reference before rewriting:

- S&P / IEEE S&P / Oakland: `references/sp.md`
- USENIX / USENIX Security: `references/usenix.md`
- CCS / ACM CCS: `references/ccs.md`
- NDSS: `references/ndss.md`

If `mode=deep` is requested and the venue is unclear, first identify the likely venue from the manuscript or ask for the target venue if the rewrite would materially differ.

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

## Deep Rewrite Procedure

For `mode=deep`, produce:

1. Venue style diagnosis: what the current text sounds like versus the target venue.
2. Claim spine: one security claim with asset, adversary, consequence, evidence, and boundary.
3. Abstract rewrite plan: five slots and a revised abstract if source text is provided.
4. Introduction order: first-page narrative sequence and missing prior-work delta.
5. Contribution bullets: rewrite bullets so each one has a matching evidence block.
6. Evidence paragraphs: rewrite or outline result paragraphs with denominator, setting, baseline, and limitation.
7. Limitations/ethics/artifact wording: tighten release, disclosure, harm, and scope language.
8. Overclaim audit: list phrases to remove or narrow.

Do not invent experiments, baselines, artifacts, ethics review, or deployment facts. If source text is missing, provide templates and edit instructions instead of a fabricated rewrite.

## Output Format

```text
[Main claim rewrite] <one sentence>
[Reviewer hook] <why a top-four security reviewer should care>
[Overclaim to remove] <text or none>
[Threat-model sentence] <sentence>
[Evidence sentence] <sentence>
[Venue tone] S&P / USENIX / CCS / NDSS / neutral
```

For `mode=deep`, use:

```text
[Venue style diagnosis]
[Claim spine]
[Abstract structure/rewrite]
[Introduction order]
[Contribution bullet rewrites]
[Evidence paragraph rewrites]
[Limitations/ethics/artifact wording]
[Overclaim removals]
[Next edits]
```

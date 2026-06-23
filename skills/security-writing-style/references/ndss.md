# NDSS Writing Style

Use this reference when `security-writing-style` is invoked with `venue=ndss` or `venue=NDSS`.

## Style Thesis

Write the paper as a practical networked, distributed, web, protocol, application, or agentic-system security contribution. NDSS prose should make the operational boundary real: what system is exposed, who can act, what security consequence occurs, and how the evaluation approximates the deployed setting.

## First-Page Shape

1. Name the networked/system/application boundary.
2. State the attacker or failure condition in that boundary.
3. Explain why existing validation, defense, or measurement misses it.
4. Present the system, attack, defense, measurement, or validation framework.
5. Give realistic evidence and deployment/ethics boundaries.

The first page should let an NDSS reviewer say: "This is a real networked/system security boundary, not just an isolated benchmark."

## Claim Grammar

Prefer:

- "In <networked/web/app/protocol/agent setting>, an attacker with <capability> can cause <security consequence> despite <existing validation/defense>."
- "We build <validation/system/measurement> that replays/tests <boundary condition> under <backend/protocol/deployment semantics>."
- "We evaluate on <realistic traces/systems/backends> and show <operational effect> while bounding deployment claims."

Avoid:

- "LLM output is brittle" without a security boundary.
- "Web attacks are missed" without backend, protocol, or operational context.
- "SOC impact" without analyst, alerting, telemetry, or response consequence.

## Abstract Pattern

1. Practical system or security workflow.
2. Broken assumption in current validation, protocol, app, or defense.
3. New attack/defense/measurement/validation framework.
4. Evidence under realistic network/system/backend conditions.
5. Bounded operational implication, artifact, ethics, and limitations.

## Introduction Pattern

- Paragraph 1: deployed or realistic networked/security workflow.
- Paragraph 2: adversary/failure mode and why current practice misses it.
- Paragraph 3: why this is not only an old or generic issue.
- Paragraph 4: proposed framework/system/measurement.
- Paragraph 5: evaluation settings, backend/protocol semantics, and limitations.
- Contributions: each bullet should connect a security boundary to evidence.

## Contribution Bullets

Good NDSS bullets often look like:

- "We identify <failure mode> in <web/network/distributed/agent boundary> under <attacker/failure capability>."
- "We build <system/harness/framework> that executes <realistic replay/protocol/backend validation>."
- "We evaluate on <traces/backends/apps/protocols> and report <security and operational metrics>."
- "We release <artifact/configs/traces> or define a safe release boundary."

## Evidence Paragraphs

Use this order:

1. Boundary question.
2. Backend/protocol/system setting.
3. Attacker or failure condition.
4. Replay/measurement/evaluation denominator.
5. Result and operational consequence.
6. What remains outside scope.

## Limitations And Ethics

NDSS prose should show responsible practicality:

- what systems, protocols, backends, or deployments are in scope;
- what is not a production-rate estimate;
- whether payloads, traces, vulnerabilities, or live systems create dual-use risk;
- how artifact release avoids credential, exploit, or user-data exposure.

## APT/SOC Emphasis

Make the operational path visible: telemetry source, log/provenance graph, lateral movement, false positives, online response, analyst output, deployment constraints, and production-like stress.

## LLM/Agent-Security Emphasis

Treat the LLM as part of an application or agent boundary: browser agent, tool use, RAG, plugin, MCP, model gateway, policy layer, or detection workflow. Show how the failure changes system security, not only model text.

## Rewrite Checklist

- Does the first paragraph name a networked, web, distributed, application, or agentic-system boundary?
- Does the threat model appear before results need it?
- Does the intro distinguish the contribution from classic WAF/IDS/protocol issues or generic LLM brittleness?
- Are backend/protocol/deployment semantics visible in the evidence?
- Are production, SOC, or deployment claims carefully bounded?

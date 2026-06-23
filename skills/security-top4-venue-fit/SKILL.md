---
name: security-top4-venue-fit
description: Use when choosing among IEEE S&P, USENIX Security, ACM CCS, and NDSS for a security manuscript, or when comparing top-four security venue fit, reviewer community, contribution framing, evidence bar, and re-routing options.
---

# Security Top-Four Venue Fit

Use this to route a security paper among IEEE S&P, USENIX Security, ACM CCS, and NDSS. Ask for title, abstract, contribution list, threat model, evidence shape, artifact status, disclosure/ethics constraints, and target deadline if missing.

## Fast Venue Matrix

| Venue | Prefer when | Watch for |
| --- | --- | --- |
| IEEE S&P | deep security/privacy contribution, crisp threat model, strong conceptual or systems significance, broad flagship framing | claims that are too narrow, missing ethical treatment, weak adaptive analysis |
| USENIX Security | systems security, measurement, usable security, software security, vulnerability analysis, artifact-heavy work | underdeveloped artifact, biased measurement, vague disclosure posture |
| ACM CCS | broad computer and communications security, cryptography/security systems/privacy, strong novelty and technical breadth | unfocused scope, insufficient novelty over recent CCS/S&P/USENIX/NDSS papers |
| NDSS | networked/distributed-system security, protocol security, internet measurement, practical attacks/defenses | story better suited to broader systems security or privacy venues |

## Calibrated Routing for APT/SOC/Threat Ops and LLM/Agent Security

Use these topic-specific priors when routing work on APT detection, SOC operations, threat intelligence, provenance/log analysis, malware campaigns, LLM security, RAG, prompt injection, and AI agents.

- IEEE S&P: prefer when the work exposes a new security boundary, threat abstraction, systematization, or broadly reusable security insight. APT/SOC work fits when it changes how intrusions, provenance, or detection semantics are understood. LLM/agent work fits when it identifies a principled failure mode in deployed AI-mediated security boundaries.
- USENIX Security: prefer when the contribution is a deployable or auditable system, large-scale measurement, SOC workflow, provenance pipeline, incident-response automation, or artifact-heavy empirical study. LLM/agent work must matter to systems security, software security, abuse prevention, or reproducible evaluation rather than pure ML quality.
- ACM CCS: prefer when the work has broad computer/communications-security relevance, strong technical novelty, and clear generalization across systems. CCS is receptive to ML-security work, but do not route survey-only or prompt-list-only work here; frame the concrete security boundary, attack surface, or defense.
- NDSS: prefer when the work is naturally networked, distributed, operational, protocol-facing, or internet-scale. APT/SOC work fits well when it centers telemetry, CTI, provenance graphs, botnets, network flows, or response pipelines. LLM/agent work fits when it attacks or hardens agentic systems, tool selection, RAG/cache layers, browser agents, or service-to-service boundaries.

## Routing Questions

1. What is the central security object: system, protocol, software, network, user behavior, data, hardware, cryptographic primitive, or ecosystem?
2. What is the main contribution type: attack, defense, measurement, theory, tool, dataset, user study, or longitudinal analysis?
3. What evidence carries the paper: exploit validation, adaptive attack, deployment, large-scale measurement, proof, artifact, user study, or formal analysis?
4. Which reviewer community owns the result: security generalists, systems-security builders, network-security reviewers, crypto/security theory, privacy, usable security, or measurement?
5. What makes the paper top-four rather than workshop or second-tier: novelty, severity, generality, evidence quality, artifact, or ecosystem impact?

## Full-Text Calibration Use

When the venue decision is close, run `security-top4-review-simulator` before final routing. It uses a full-text calibration reference from open-access S&P, USENIX Security, CCS, and NDSS papers, including APT/SOC/threat-analysis and LLM/agent-security examples.

## Tie Breakers

- S&P vs CCS: prefer S&P for a cleaner flagship security/privacy claim with strong conceptual framing; prefer CCS when the work spans broader computer/communications security or mixes systems, crypto, and privacy communities.
- USENIX vs NDSS: prefer USENIX when the artifact, software/system, vulnerability analysis, or measurement pipeline is central; prefer NDSS when networked or distributed-system security is the natural reviewer home.
- S&P vs USENIX: prefer S&P for sharper conceptual security/privacy framing; prefer USENIX when implementation, measurement, or reproducible systems evidence is the main contribution.
- CCS vs NDSS: prefer CCS for broad security breadth; prefer NDSS for network/protocol-centered security with clear practical evidence.

## Re-Routing Guardrails

- Use PETS if privacy-enhancing technology is the central contribution.
- Use RAID if the paper is primarily attacks, intrusions, and defenses with a narrower community fit.
- Use ACSAC for applied-security relevance when the flagship novelty bar is not yet met.
- Use CHES if the core is cryptographic hardware or embedded-system side channels.
- Use SOUPS/CHI-style venues when usable-security or human-subject evidence is the center rather than support.

## Output Format

```text
[Top venue] IEEE S&P / USENIX Security / ACM CCS / NDSS
[Fit] High / Medium / Low
[Why this venue] <one sentence>
[Closest alternative] <venue and reason>
[Do not target] <venue and mismatch>
[Main upgrade needed] novelty / threat model / adaptive evaluation / measurement validity / artifact / ethics / writing
[Next skill] <security skill or single-conference profile>
```

---
name: security-top4-workflow
description: "Use when planning an end-to-end submission to the four flagship security conferences: IEEE S&P, USENIX Security, ACM CCS, and NDSS. Triggers for security paper planning, milestone scheduling, stage routing, top-four security submission readiness, rebuttal planning, artifact planning, and camera-ready coordination."
---

# Security Top-Four Workflow

Use this as the orchestrator for a security paper targeting IEEE S&P, USENIX Security, ACM CCS, or NDSS. Treat conference instructions as volatile: before submission-ready advice, verify the current official CFP, author kit, ethics policy, artifact policy, rebuttal rules, and camera-ready instructions.

## Official Anchors

- IEEE S&P: https://www.ieee-security.org/TC/SP-Index.html
- USENIX Security: https://www.usenix.org/conferences/byname/108
- ACM CCS: https://www.sigsac.org/ccs.html
- NDSS: https://www.ndss-symposium.org/

If live official instructions conflict with this skill, the official instructions win.

## Stage Router

- Idea or target unclear: use `security-topic-selection`, then `security-top4-venue-fit`.
- Venue chosen but story fuzzy: use `security-writing-style` and `security-related-work`.
- Claim depends on adversary assumptions: use `security-threat-model`.
- Claim depends on attacks, defenses, measurements, user studies, or proofs: use `security-evidence-audit`.
- Work touches real systems, users, malware, vulnerabilities, private data, or disclosure: use `security-ethics-disclosure`.
- Code, data, exploit, defense, benchmark, or measurement pipeline must be released or reviewed: use `security-artifact-package`.
- Pre-submission review simulation needed: use `security-top4-review-simulator`.
- Final upload approaching: use `security-submission-check`.
- Reviews released: use `security-author-response`.
- Accepted, shepherded, or conditionally accepted: use `security-camera-ready`.

Also invoke the existing single-conference profile once a target is likely:
`ieee-symposium-on-security-and-privacy`, `usenix-security-symposium`,
`acm-conference-on-computer-and-communications-security`, or
`network-and-distributed-system-security-symposium`.

## Milestones

- Venue triage: identify contribution type, audience, evidence shape, and closest sibling venue.
- Claim lock: freeze the exact security claim, threat model, and claim boundaries.
- Evidence lock: finish adaptive attacks, baselines, measurement validity, user-study analysis, or proof checks.
- Ethics lock: resolve responsible disclosure, IRB/human-subjects, malware handling, data access, dual-use, and harm limits.
- Artifact lock: package code/data/configs, remove secrets, document dependencies, and test reproduction.
- Writing lock: finish abstract, intro, limitations, ethics, related work, and reviewer-facing contribution statements.
- Simulated-review lock: run venue-calibrated simulated reviews and fix fatal threat-model, evidence, ethics, artifact, and venue-fit weaknesses.
- Submission lock: verify anonymization, format, supplement rules, conflict declarations, and portal fields.
- Response lock: answer reviews with submitted evidence only and avoid identity leakage.
- Camera-ready lock: address reviewer/shepherd requirements, legal/release constraints, artifact badges, and proceedings metadata.

## Calibrated Topic Path

- APT/SOC/threat-analysis path: `security-topic-selection` -> `security-top4-venue-fit` -> `security-threat-model` -> `security-evidence-audit` -> `security-ethics-disclosure` -> `security-artifact-package` -> `security-writing-style`.
- LLM/agent-security path: `security-topic-selection` -> `security-threat-model` -> `security-evidence-audit` -> `security-top4-venue-fit` -> `security-ethics-disclosure` -> `security-artifact-package` -> `security-writing-style`.
- Run `security-submission-check` after the single-conference profile because official AI-use, artifact, anonymity, and ethics rules change across cycles.

## Critical Path

- Do not let the threat model remain implicit past the introduction draft.
- Do not promise a defense without adaptive evaluation.
- Do not submit a measurement paper without sampling bias, validation, and reproducibility checks.
- Do not defer core experiments or disclosure decisions to rebuttal.
- Do not rely on old venue rules for anonymity, page limits, AI-use policy, artifact rules, or rebuttal format.

## Output Format

```text
[Current stage] idea / routing / evidence / writing / submission / review / camera-ready
[Likely venue] S&P / USENIX Security / CCS / NDSS / unclear
[Next skill] <skill-name>
[Critical path] <three tasks that determine readiness>
[Blocking risk] <threat model / evidence / ethics / artifact / format / official policy>
[Official check needed] <current CFP / author kit / ethics / artifacts / rebuttal / camera-ready>
```

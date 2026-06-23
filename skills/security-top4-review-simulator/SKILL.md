---
name: security-top4-review-simulator
description: Use when simulating pre-submission reviews, full pre-submission audits, program-committee reviews, area-chair decisions, or reject-risk audits for IEEE S&P, USENIX Security, ACM CCS, or NDSS security papers. Triggers for mode=full top-four security review simulation, reviewer personas, venue-calibrated scores, APT/SOC review, LLM/agent security review, threat-model audit, evidence audit, artifact/ethics audit, desk-reject risk audit, and revision roadmaps before submission.
---

# Security Top-Four Review Simulator

Use this to simulate top-four security conference reviews before submission. This skill is read-only: review the manuscript, abstract, outline, or experiment plan, and produce review reports and a revision roadmap without editing the paper unless the user separately asks for rewriting.

If available, read `references/fulltext-calibration.md` before scoring. It contains full-text-derived patterns from S&P, USENIX Security, ACM CCS, and NDSS papers on APT/SOC/threat analysis and LLM/agent security.

## Modes

- `mode=full`: default for a complete manuscript, PDF, or LaTeX source. Run the simulated PC review and all internal audit lanes in one report. Do not ask the user to separately invoke threat-model, evidence, artifact, ethics, or submission-check skills.
- `mode=review`: run only the PC-style reviewer panel, devil's advocate, and area-chair synthesis.
- `mode=abstract`: run a provisional abstract/idea-level review and mark evidence judgments as unverified.
- `mode=lane:<name>`: drill into one lane after a full report, such as `lane:evidence`, `lane:threat-model`, `lane:artifact`, `lane:ethics`, or `lane:submission`.

If the user asks for an "NDSS review", "full audit", "pre-submission audit", or complete review and provides a manuscript path, treat it as `mode=full`.

## Intake

Ask only for missing information that materially changes the review:

- Manuscript, abstract, intro, experiment plan, or PDF path.
- Target venue: S&P, USENIX Security, CCS, NDSS, or unknown.
- Topic family: APT/SOC/threat operations, LLM/agent security, both, or other.
- Artifact status, ethics/disclosure status, and current evidence status.

If the user provides only an idea or abstract, run an abstract-level simulation and label all evidence judgments as provisional.

## Full Audit Contract

In `mode=full`, perform these lanes as part of the same output:

1. Venue-fit lane: assess NDSS/S&P/USENIX/CCS fit and nearest venue mismatch.
2. PC-review lane: run R1-R5, devil's advocate, and area-chair synthesis.
3. Threat-model lane: extract assets, attacker, trust boundary, assumptions, non-goals, and success condition; flag ambiguity.
4. Claim-to-evidence lane: map abstract/introduction claims to experiments, baselines, datasets, ablations, statistics, and limitations.
5. Artifact/ethics lane: audit reproducibility package, release boundary, dual use, human-subjects/IRB, responsible disclosure, private data, malware/exploit handling, and AI-use disclosure.
6. Submission-risk lane: flag likely desk-reject risks such as page limit, anonymity, formatting, external links, supplement policy, conflict metadata, and volatile CFP requirements. Verify live official rules before making final submission-ready claims.
7. Revision-roadmap lane: produce a prioritized, time-aware plan split into must-fix, should-fix, and optional improvements.

Use the specialized skill names only as internal lane labels. The user should not need to run separate commands unless they explicitly request deeper follow-up on one lane.

## Paper Card

Start by extracting a compact paper card:

```text
[Target venue]
[Topic family]
[One-sentence claim]
[Threat model]
[Main contribution type] attack / defense / measurement / system / dataset / user study / formal / SoK
[Evidence shape]
[Artifact status]
[Ethics/disclosure status]
[Main nearest-prior-work risk]
```

## Review Panel

Simulate independent reviewers with non-overlapping priorities:

- R1 Venue-fit/generalist: top-four significance, scope, PC accessibility, and venue match.
- R2 Threat-model/novelty: assets, adversary, assumptions, security boundary, and prior-work delta.
- R3 Evidence/adaptive evaluation: baselines, measurement validity, deployment realism, adaptive attacks, ablations, and claim support.
- R4 Artifact/ethics/open science: reproducibility, release boundary, anonymity, disclosure, data handling, dual-use, and venue policy risk.
- R5 Topic specialist: APT/SOC reviewer or LLM/agent-security reviewer depending on the paper.
- Devil's advocate: strongest reason the paper could be rejected even if the main idea is interesting.

Do not let reviewers copy each other's wording. If two reviewers notice the same weakness, make their angles different.

## Venue Calibration

- S&P reviewers ask whether the paper changes a security/privacy boundary, threat abstraction, or broadly reusable understanding, and whether ethics/disclosure is mature.
- USENIX reviewers ask whether the system, measurement, artifact, or operational evidence is auditable and useful to systems-security reviewers.
- CCS reviewers ask whether the contribution is broadly novel, technically sharp, and readable by a general computer-security PC; survey-only work is a poor fit.
- NDSS reviewers ask whether the networked, distributed, operational, protocol, app, or agentic-system boundary is real and practically evaluated.

## Topic Calibration

For APT/SOC/threat papers, penalize classifier-only claims that lack analyst actionability, false-positive cost, telemetry realism, drift/evasion analysis, attack reconstruction, or incident-response value.

For LLM/agent-security papers, penalize prompt collections that lack an asset, attacker capability, system boundary, reproducible harness, adaptive attack, mitigation evaluation, or measured security consequence.

## Scoring

Use top-four-style decisions:

- Strong Accept: rare; all major claims are novel, important, and supported.
- Accept: clear top-four contribution with fixable presentation or scope issues.
- Weak Accept: interesting and probably above threshold, but one reviewer may object.
- Weak Reject: promising but below the evidence/novelty/fit bar.
- Reject: central claim unsupported, incremental, off-scope, or policy-risky.
- Strong Reject: fatal threat-model, ethics, novelty, or evidence failure.

Use confidence 1-5. Low confidence means the review is evidence-limited, not lenient.

## Output Format

```text
[Paper card]

[R1 Venue-fit/generalist]
Score:
Confidence:
Summary:
Strengths:
Weaknesses:
Questions for authors:
Required upgrade:

[R2 Threat-model/novelty]
...

[R3 Evidence/adaptive evaluation]
...

[R4 Artifact/ethics/open science]
...

[R5 Topic specialist]
...

[Devil's advocate]
Strongest rejection case:
What evidence would reverse it:

[Full-audit lanes]
Threat-model audit:
Claim-to-evidence audit:
Artifact/ethics audit:
Submission/desk-reject risk audit:

[Area-chair synthesis]
Likely decision:
Consensus:
Main dissent:
Fatal risks:
Fastest path to one-score improvement:
Revision roadmap:
```

## Guardrails

- Cite sections, pages, figures, tables, or exact manuscript claims when available.
- Mark missing information as missing; do not infer experiments, artifacts, or disclosures that are not in the paper.
- Separate "paper is weak" from "reviewer cannot verify because the manuscript omits information."
- Do not fabricate official venue rules; apply submission-check criteria and verify live official CFP, artifact, ethics, anonymity, AI-use, and format rules before making final submission-ready claims.
- In `mode=full`, include the submission-risk lane yourself; do not tell the user to run `security-submission-check` unless they ask for a deeper follow-up.
- For post-review response drafting, switch to `security-author-response`.

---
name: security-topic-selection
description: Use when shaping a raw computer security idea into a top-four security conference submission for IEEE S&P, USENIX Security, ACM CCS, or NDSS. Triggers for topic selection, contribution sharpening, novelty-risk analysis, attack/defense/measurement framing, and deciding whether an idea is ready for top-tier security work.
---

# Security Topic Selection

Use this before writing when the user has a security idea, prototype, vulnerability class, measurement opportunity, or defense concept and wants to know whether it can become a top-four security paper.

## Convert Idea to Claim

Make the paper's core claim explicit:

- Attack: a new capability, target class, exploit path, bypass, or failure mode exists under a realistic adversary.
- Defense: a system, protocol, analysis, or design reduces risk against a defined adversary with measurable cost.
- Measurement: a security phenomenon is widespread, important, and measured with valid sampling and reproducible methods.
- Privacy: a threat, leakage channel, or privacy-enhancing design changes what systems can safely reveal or compute.
- Usable/security socio-technical: human behavior, ecosystem incentives, or operational practice changes the security outcome.
- Formal/crypto: a construction, proof, or model changes guarantees under clearly stated assumptions.

## Top-Four Readiness Tests

- Novelty: name the closest three recent papers and state the technical delta in one sentence.
- Security importance: explain who is harmed, what asset is at risk, and why the result matters now.
- Evidence path: identify the minimal experiment, proof, measurement, or artifact needed to convince skeptical reviewers.
- Ethics path: describe responsible disclosure, user impact, data handling, and dual-use limits before collecting results.
- Venue path: state whether the natural reviewer is S&P, USENIX, CCS, or NDSS.

## Post-Calibration Triage

For APT detection, SOC, and threat-analysis ideas, push toward top-four only when at least one of these is true:

- The idea changes attacker semantics, provenance/log reasoning, alert triage, incident response, CTI quality, or operational decision-making.
- The evidence can show realistic telemetry, labeling discipline, false-positive cost, drift, evasion, deployment overhead, and analyst value.
- The contribution is more than a detector score: it explains what becomes actionable for defenders.

For LLM and agent-security ideas, push toward top-four only when at least one of these is true:

- The idea identifies a concrete security boundary in an LLM app, RAG pipeline, agent tool chain, browser agent, code agent, or AI-assisted SOC workflow.
- The paper can measure exploitability, leakage, privilege misuse, policy bypass, recovery cost, or defense effectiveness across realistic systems.
- The work gives a reusable attack model, defense primitive, evaluation method, benchmark, or systems insight.

Treat these as reject-or-pivot warnings:

- Classifier-only APT/SOC work on toy data without operational actionability.
- Threat-intelligence mining that cannot validate IoC quality or defender utility.
- Prompt-collection or jailbreak-list work without a system boundary, attacker model, or mitigation.
- LLM novelty that is mainly ML capability, with security impact added late.

## Kill or Pivot Conditions

- The idea depends on unrealistic attacker powers but sells real-world impact.
- The defense has no adaptive-attacker plan.
- The measurement cannot be validated or reproduced enough for reviewer trust.
- The novelty is only "we applied known method X to domain Y" without a security-specific insight.
- The paper needs privileged or harmful data collection without a credible ethics/disclosure plan.

## Output Format

```text
[Paper seed] attack / defense / measurement / privacy / usable security / formal / other
[Top-four potential] high / medium / low
[One-sentence claim] <claim>
[Minimum convincing evidence] <experiment/proof/measurement/artifact>
[Nearest prior work risk] <what may make it look incremental>
[Ethics/disclosure blocker] <none or issue>
[Likely venue path] S&P / USENIX / CCS / NDSS / other
[Next skill] security-threat-model / security-evidence-audit / security-top4-venue-fit
```

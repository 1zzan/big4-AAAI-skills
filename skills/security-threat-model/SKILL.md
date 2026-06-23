---
name: security-threat-model
description: Use when drafting or auditing threat models for IEEE S&P, USENIX Security, ACM CCS, NDSS, or other security papers. Triggers for adversary capability, asset, trust-boundary, assumption, attack surface, defense guarantee, claim-boundary, and overclaim checks.
---

# Security Threat Model

Use this whenever a security claim depends on adversary assumptions. A top-four security paper should let reviewers decide whether the result matters before they reach the evaluation section.

## Required Elements

- Assets: what must remain confidential, integral, available, authentic, private, or accountable.
- Adversary goal: theft, compromise, inference, bypass, denial, manipulation, deanonymization, fraud, persistence, or evasion.
- Adversary capability: local/remote, authenticated/unauthenticated, network position, code execution, query access, side-channel access, physical access, training-data influence, or user interaction.
- Trust boundary: components, operators, users, cloud providers, devices, cryptographic assumptions, and third-party services.
- Out of scope: state what the paper does not defend against and why that exclusion is reasonable.
- Success condition: how the paper measures attack success or defense success.
- Ethics/disclosure: what can be safely tested, released, or withheld.

## Claim Alignment

- Every headline claim must be true under the stated adversary.
- Every defense guarantee must say what remains possible.
- Every attack must avoid implying broader exploitability than tested.
- Every measurement must state sampling and visibility limits.
- Every privacy claim must specify adversarial knowledge and auxiliary information.

## Top-Four Failure Modes

- Threat model appears after results, so reviewers cannot interpret evidence.
- Attacker is too weak for the impact claim or too strong for the defense claim.
- Defense evaluation omits adaptive attackers.
- Measurement paper infers global prevalence from convenience samples.
- Ethics constraints are used to hide missing validation rather than bound claims.

## Output Format

```text
[Assets] <assets>
[Adversary] <goal and capabilities>
[Trust boundary] <trusted/untrusted components>
[Assumptions] <necessary assumptions>
[Out of scope] <explicit exclusions>
[Claim mismatch] <overclaim or missing assumption>
[Fix] narrow claim / strengthen evaluation / add adaptive attack / clarify ethics / re-route
```

---
name: security-ethics-disclosure
description: Use when planning or auditing ethics, responsible disclosure, human-subjects review, vulnerability handling, malware handling, data privacy, dual-use risk, or release decisions for IEEE S&P, USENIX Security, ACM CCS, or NDSS security papers.
---

# Security Ethics and Disclosure

Use this whenever the work can affect real systems, users, operators, vendors, infrastructure, private data, or abuse capability. Verify the current venue ethics and disclosure policy before submission.

## Ethics Inventory

- Harm surface: what could go wrong if the method, exploit, dataset, or tool is misused.
- Affected parties: users, vendors, operators, platforms, researchers, participants, organizations, or bystanders.
- Disclosure status: who was notified, when, by what channel, and what response was received.
- Data handling: collection basis, consent, minimization, retention, access control, anonymization, and release plan.
- Human subjects: IRB or equivalent review, recruitment, compensation, risk, and debriefing.
- Malware/exploit handling: containment, redaction, safe reproduction, and release boundaries.
- Dual use: what is withheld, delayed, rate-limited, or released only under controlled access.

## Topic-Specific Risk Checks

- APT/SOC/threat-analysis work: check whether telemetry, logs, IoCs, malware samples, victim identifiers, infrastructure, or analyst workflows could identify organizations or enable abuse.
- LLM/agent-security work: check prompt-injection payloads, jailbreaks, exploit chains, autonomous tool misuse, data exfiltration, generated malware/phishing risk, and AI-use disclosure requirements.
- For both categories, distinguish what reviewers need to verify from what must be redacted, delayed, simulated, or shared under controlled access.

## Writing Rules

- State ethics and disclosure early enough that reviewers trust the methodology.
- Separate "we could not disclose X" from "we did not evaluate X".
- Do not use ethics as a blanket excuse for unverifiable claims.
- Explain mitigations without revealing identities or violating anonymity rules during review.
- Align the release plan with artifact and camera-ready requirements.

## Output Format

```text
[Risk class] low / moderate / high
[Affected parties] <parties>
[Disclosure status] not needed / planned / in progress / completed / blocked
[Data/IRB status] <status>
[Release boundary] full / redacted / delayed / controlled / none
[Reviewer concern] <likely concern>
[Required fix] <policy check, disclosure step, text rewrite, or experiment limit>
```

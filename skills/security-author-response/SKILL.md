---
name: security-author-response
description: Use when drafting, prioritizing, or auditing rebuttals, author responses, reviewer discussions, or shepherd responses for IEEE S&P, USENIX Security, ACM CCS, NDSS, or related security conference reviews. Triggers for security review triage, evidence-grounded response, no-new-results constraints, and reviewer-risk handling.
---

# Security Author Response

Use this after reviews are released. First verify the current venue's response format, length, anonymity, allowed content, and whether new results or links are permitted.

## Triage

- Fatal misunderstanding: reviewer misread the threat model, contribution, or evidence.
- Valid weakness: reviewer identified a real missing baseline, adaptive attack, validation issue, or ethics gap.
- Scope mismatch: reviewer wanted a different venue/community contribution.
- Presentation issue: claim exists but is buried, imprecise, or overbroad.
- Policy issue: artifact, disclosure, anonymity, or formatting concern.

## Response Rules

- Lead with changes or clarifications that affect reviewer confidence.
- Use submitted evidence first; do not invent unsupported new results.
- Admit true limits and narrow claims when needed.
- Never reveal author identity, institution, private disclosure details, or off-policy links.
- Do not argue prestige; argue threat model, evidence, novelty, and impact.

## Security-Specific Moves

- For threat-model objections: restate assets, adversary, assumptions, and claim boundary.
- For weak-baseline objections: identify existing submitted comparison or commit to camera-ready clarification only if allowed.
- For adaptive-attack objections: explain submitted adaptive evaluation or concede limit.
- For ethics objections: explain disclosure/data handling within anonymity and policy constraints.
- For measurement objections: address sampling, validation, and scope without claiming globality.

## Output Format

```text
[Review issue] <issue>
[Priority] must answer / answer if space / do not spend space
[Response stance] clarify / concede / narrow / cite submitted evidence / promise allowed edit
[Draft response] <concise text>
[Risk] identity leak / new-results violation / overpromise / unresolved evidence gap
```

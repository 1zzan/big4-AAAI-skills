---
name: security-submission-check
description: Use for final pre-submission checks for IEEE S&P, USENIX Security, ACM CCS, or NDSS papers, including official CFP verification, format, anonymity, conflicts, ethics, disclosure, artifact, supplement, portal fields, PDF metadata, and policy compliance.
---

# Security Submission Check

Use this in the final days before upload. Do not rely on remembered rules. Open the current official CFP, author kit, submission portal, artifact policy, ethics/disclosure policy, and rebuttal instructions for the selected venue.

## Preflight Checklist

- Venue: confirm target track, scope, deadlines, submission system, and official template.
- Format: page limit, font, references, appendices, supplement, file size, and required fields.
- Anonymity: PDF metadata, acknowledgments, self-citations, artifact links, repository history, file paths, container labels, and screenshots.
- Policy: dual submission, prior publication, arXiv/preprint, AI-use disclosure, conflict declarations, author list, and institutional constraints.
- Security ethics: responsible disclosure, IRB, data collection, malware/exploit handling, and release boundaries.
- Artifact: review artifact, public artifact, withheld materials, documentation, smoke test, and safety notes.
- Claims: abstract/introduction claims match threat model and evidence.
- Topic-specific audit: for APT/SOC papers, verify telemetry legality, labeling, privacy, IoC release, false-positive claims, and operational utility; for LLM/agent papers, verify AI-use disclosure, model/app versions, prompt/tool release boundaries, and dual-use controls.
- Upload: PDF opens, supplement opens, ZIP paths are correct, portal fields match the paper, and checksums or generated PDFs are archived.

## Red Flags

- Last-minute PDF regeneration after anonymity audit.
- External links that reveal identity or provide off-policy material.
- Supplement contains core evidence missing from the main paper.
- Artifact contains secrets, private data, or unsafe exploit instructions.
- Official instructions changed since the team last checked.

## Output Format

```text
[Submission status] ready / blocked / high risk / unknown
[Official source checked] yes / no / needed
[Blocking item] <single blocker>
[Anonymity risk] <risk>
[Ethics/artifact risk] <risk>
[Upload checklist] <three remaining actions>
```

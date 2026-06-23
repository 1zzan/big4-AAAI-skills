---
name: security-camera-ready
description: Use after acceptance, conditional acceptance, or shepherding for IEEE S&P, USENIX Security, ACM CCS, or NDSS papers. Triggers for camera-ready revisions, shepherd response, artifact badge/release, disclosure updates, final PDF/source checks, proceedings metadata, and public communication planning.
---

# Security Camera-Ready

Use this after acceptance or shepherding. Verify the current official camera-ready instructions, copyright/proceedings requirements, artifact badge rules, presentation obligations, and release constraints.

## Revision Priorities

- Address mandatory reviewer, meta-reviewer, and shepherd requests first.
- Narrow any claims that reviews exposed as overbroad.
- Update ethics/disclosure status without creating legal, safety, or privacy risk.
- Align artifact links, data release, code release, and paper text.
- Ensure final source builds exactly to the submitted PDF.
- Remove anonymity placeholders only when the venue instructs it.

## Security Release Checklist

- Coordinate vendor/operator disclosure timing with publication and artifact release.
- Redact exploit details only when justified by safety or policy, and explain the boundary.
- Verify released data is sanitized and allowed to be redistributed.
- Ensure public repositories do not include private history, credentials, unsafe defaults, or unreviewed binaries.
- Archive exact artifact version used for the paper.

## Final Checks

- Title, author list, affiliations, acknowledgments, funding, and conflicts are correct.
- Proceedings metadata, DOI/copyright forms, and license choices are complete.
- Camera-ready text reflects accepted claims, not a broader arXiv-style version.
- Presentation slides and public summary do not exceed the paper's ethical release boundary.

## Output Format

```text
[Camera-ready status] ready / shepherding / blocked / release-risk
[Mandatory changes] <items>
[Claim narrowing] <needed or none>
[Artifact/release status] <status>
[Disclosure status] <status>
[Final blocker] <single blocker>
```

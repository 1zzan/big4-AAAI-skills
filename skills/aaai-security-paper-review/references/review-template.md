# Full Review Template

Use this template for `mode=full`. Keep findings specific and tied to manuscript sections, files, figures, tables, or claims whenever possible.

```text
[AAAI Gate]
Fit: High / Medium / Low
Contribution type:
Nearest AAAI corpus pattern:
Primary rejection risk:

[Executive Diagnosis]
One short paragraph explaining the overall situation and what matters most.

[Reviewer-Style Review]
Strengths:
- ...

Weaknesses:
- P0/P1/P2 severity, with section/file references when possible.

Questions for Authors:
- ...

Likely Score / Confidence:
- Score:
- Confidence:

[Section Audit]
Abstract:
Introduction:
Related Work:
Threat Model / Problem Formulation:
Method:
Experiments:
Limitations / Ethics / Reproducibility:

[Corpus-Matched Diagnosis]
Closest paper families:
Closest analog papers or patterns:
Missing accepted-paper ingredients:

[Evidence Checklist]
Threat model:
Dataset/tasks:
Metrics:
Baselines:
Ablations:
Security-utility tradeoff:
Model/provider reproducibility:
Artifacts/checklist:

[Revision Plan]
P0:
- ...

P1:
- ...

P2:
- ...

[Optional Edit Targets]
If the user asks for edits, list the exact files/sections to patch first.
```

Scoring guidance:

- `High fit`: the central contribution is clearly AI-reusable and the main evidence is already in the paper.
- `Medium fit`: the topic can fit AAAI, but framing, baselines, threat model, or evidence must be strengthened.
- `Low fit`: the paper reads mainly as a security product, operations report, or narrow systems/security study with insufficient AI contribution.


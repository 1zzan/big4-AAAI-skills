---
name: security-related-work
description: Use when building, auditing, or rewriting related work for IEEE S&P, USENIX Security, ACM CCS, or NDSS submissions. Triggers for novelty positioning, sibling-paper comparison, top-four security literature mapping, reviewer-objection anticipation, and technical-delta writing.
---

# Security Related Work

Use this to make the paper's novelty legible to top security reviewers. The goal is not a long literature dump; it is a clear map of what reviewers know and why the paper is still necessary.

## Literature Map

Organize related work by reviewer decision, not by chronology:

- Same vulnerability/threat class.
- Same target ecosystem, protocol, platform, or user population.
- Same defense technique or mitigation family.
- Same measurement method or dataset style.
- Same privacy, crypto, or formal model.
- Neighboring venue work from S&P, USENIX Security, CCS, NDSS, PETS, RAID, ACSAC, CHES, SOUPS, SIGCOMM, NSDI, or systems/ML venues when relevant.

## Delta Sentence

For each close paper, write one precise contrast:

```text
Prior work shows <X> under <assumption/scope>; this paper shows <Y> under <new assumption/scope/evidence>, which changes <security conclusion>.
```

Do not use vague contrasts like "different setting", "more comprehensive", or "first to study" unless the evidence supports them.

## Reviewer-Objection Audit

- If reviewers know a stronger baseline, include it or explain why it is inapplicable.
- If a prior attack already works, state the new attacker capability, target class, or consequence.
- If a prior defense exists, show bypass, deployment gap, cost, usability issue, or stronger guarantee.
- If a prior measurement exists, show improved sampling, validation, scale, longitudinal coverage, or causal interpretation.
- If the paper crosses fields, explain why the security contribution is primary.

## Output Format

```text
[Closest prior cluster] <cluster>
[Novelty sentence] <technical delta>
[Missing citation risk] <paper/venue/community to search>
[Reviewer objection] <likely objection>
[Fix] add baseline / narrow claim / rewrite delta / add experiment / re-route venue
```

---
name: aaai-writing-style
description: Use when revising an AAAI manuscript for broad-AI-audience fit, mode=deep AAAI writing optimization, security/LLM-agent corpus-backed writing style, first-page contribution statements legible to non-specialist Phase-1 reviewers, abstract/introduction/contribution/evidence/limitation rewrites, two-column readability, concise novelty claims, reproducibility-checklist alignment, hedged limitations and ethics, and policy-aware framing of AI-system and capability claims.
---

# AAAI Writing Style

Use this to make a technically sound draft readable to a broad AI program committee. AAAI rewards
clear AI contribution, not only subfield-specific benchmark wins.

## Modes And References

- `mode=quick`: diagnose first-page clarity, contribution type, checklist alignment, and overclaim risks.
- `mode=deep`: rewrite or plan the abstract, introduction, contribution bullets, evidence paragraphs, limitations, ethics, and reproducibility wording.
- `mode=compare`: compare AAAI framing against KDD or security venues when the target is uncertain.

For cybersecurity, APT/SOC, threat analysis, LLM-agent security, MCP/tool security, prompt injection, jailbreak, guardrail, privacy/security alignment, or agent-safety manuscripts, read `references/security-llm-agent.md` before any `mode=deep` rewrite. That reference is backed by the 120-paper AAAI security/LLM-agent corpus metadata under `../../resources/aaai-security-corpus/`.

If `mode=deep` is requested and the manuscript is not security/LLM-agent related, use the general AAAI rules in this file and state that no domain-specific corpus-backed style reference is available.

## AAAI framing

- State the AI problem, the new capability or insight, and the evidence in the first page.
- Make clear whether the contribution is method, theory, system, benchmark, dataset, evaluation,
  human-AI interaction, social impact, or alignment.
- Explain why the result matters outside a single dataset or implementation.
- Keep claims aligned with the reproducibility checklist and supplementary evidence.
- Discuss limitations and ethical considerations when the method affects people, safety, privacy,
  fairness, security, or social impact.

## Two-column readability

- Use figures and tables as decision aids, not decoration.
- Keep notation lightweight and define it near first use.
- Use compact related-work contrasts instead of long literature catalogues.
- Make the Phase 1 summary easy: problem, method, evidence, limitation, checklist compliance.
- Avoid unsupported "general intelligence", "human-level", or "safe" claims.

## Reading the paper as a Phase-1 reviewer

A non-specialist on AAAI's broad committee gives the first page a few minutes and decides whether the
paper is worth deeper reading. Write so that a planning or KR reviewer can summarize your learning
contribution, and vice versa. Audit the opening against what that reader needs to extract fast.

| First-page question | Reviewer extracts | Failure symptom |
| --- | --- | --- |
| What is the problem | one AI task statement | jargon with no anchor |
| What is new | the single contribution | a list, no headline |
| Why believe it | evidence in one line | "see Section 6" only |
| What are the limits | scope and caveat | silence or overclaim |

## Phrasing fixes that survive AAAI review

- Replace "we achieve state of the art" with the specific delta and the setting it holds in.
- Replace bare "safe" or "human-level" with a measured, scoped statement the evidence supports.
- Replace a long related-work catalogue with two or three sharp contrasts a non-specialist can follow.
- Tie every strong claim back to a checklist answer so rigor and prose agree.

## Deep Rewrite Procedure

For `mode=deep`, produce:

1. AAAI style diagnosis: what a broad Phase-1 reviewer can extract from the first page.
2. AI contribution spine: problem, reusable idea, evidence, limitation, and checklist alignment.
3. Abstract rewrite plan: one sentence per slot and a revised abstract when source text is provided.
4. Introduction order: first-page narrative sequence and missing nearest-prior-work delta.
5. Contribution bullets: each bullet names contribution type and evidence.
6. Evidence paragraph rewrites: dataset/task, baselines, ablations, metrics, and scope.
7. Limitations/ethics/reproducibility wording: align claims with checklist and artifacts.
8. Overclaim audit: phrases to remove or narrow.

Do not invent experiments, baselines, datasets, ethics statements, artifact releases, or checklist answers. If source text is missing, provide templates and edit instructions instead of fabricated prose.

## Worked vignette

A multi-agent paper opens with three paragraphs of game-theory notation before naming its
contribution. A vision reviewer cannot find the AI claim and is likely to stop. The fix rewrites
sentence one as the problem, sentence two as the new coordination mechanism, sentence three as the
one-line evidence, and a final clause scoping the result to the studied setting, all on page one.

## Output format

```text
[AAAI fit sentence] <one sentence>
[Contribution type] method / theory / system / benchmark / dataset / evaluation / social impact
[First-page fixes] <problem, method, evidence, limitation>
[Checklist alignment] pass / needs revision
[Overclaim risks] <claims to narrow or evidence to add>
```

For `mode=deep`, use:

```text
[AAAI style diagnosis]
[AI contribution spine]
[Abstract structure/rewrite]
[Introduction order]
[Contribution bullet rewrites]
[Evidence paragraph rewrites]
[Limitations/ethics/reproducibility wording]
[Overclaim removals]
[Next edits]
```

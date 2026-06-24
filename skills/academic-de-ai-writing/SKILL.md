---
name: academic-de-ai-writing
description: Use when revising academic manuscripts, paper sections, rebuttals, related work, abstracts, introductions, or LaTeX sources to reduce AI-polished texture, AI taste, de-AI academic writing, robotic academic prose, over-uniform transitions, over-defensive hedging, generic correctness, citation flattening, low research texture, vague limitations, and prose that sounds like LLM polishing. Use for audit-only, rewrite, deep manuscript pass, or LaTeX edit requests while preserving claims, evidence, citations, and author intent.
---

# Academic De-AI Writing

Use this skill to make academic writing read like a real research argument rather than smooth generic synthesis. The goal is not to hide tool use; it is to restore researcher texture: decisions, tradeoffs, evidence pressure, citation hierarchy, and bounded claims.

## Modes

- `mode=audit`: diagnose AI-polished patterns and rank fixes without rewriting.
- `mode=rewrite`: rewrite the supplied paragraph or section.
- `mode=deep`: run a section-level pass over a manuscript, PDF text, or LaTeX source.
- `mode=latex-edit`: patch LaTeX files after the user explicitly asks for edits.
- `mode=citation`: focus on citation hierarchy, pointwise citation support, and related-work logic.

If the user asks generally to remove AI taste, humanize an academic paper, or make the prose less AI-polished, default to `mode=audit` for long manuscripts and `mode=rewrite` for short pasted text.

## Required Reference

Read `references/academic-de-ai-protocol.md` before any `mode=deep`, `mode=latex-edit`, or `mode=citation` task. For short paragraph rewrites, use the quick workflow below unless the text involves citations or scientific claims.

## Quick Workflow

1. Preserve factual content: do not invent experiments, parameters, datasets, citations, limitations, or author intent.
2. Identify the dominant AI-polished pattern: uniform connectors, generic correctness, over-hedging, flat citations, missing design rationale, weak paragraph landing, or vague limitations.
3. Convert descriptive prose into research reasoning: why this choice, what it controls, what it rules out, and what evidence supports it.
4. Replace connector-driven flow with cause, contrast, condition, mechanism, or evidence-driven sentences.
5. Strengthen stance only when evidence supports it; otherwise make the uncertainty concrete.
6. Return either a diagnosis, a rewrite, or a patch plan depending on mode.

## Output Format

For `mode=audit`, return:

```text
[AI-polished symptoms]
[Research-texture gaps]
[Citation/evidence issues]
[Priority fixes]
```

For `mode=rewrite`, return:

```text
[Diagnosis]
[Rewritten text]
[What changed]
[Unsupported details not added]
```

For `mode=deep` or `mode=latex-edit`, return:

```text
[Section map]
[Global AI-polished patterns]
[High-impact rewrites]
[Citation hierarchy fixes]
[Limitations/ethics/reproducibility fixes]
[Files changed or edit plan]
[Residual risks]
```

## Guardrails

- Do not fabricate "realistic" details to make text sound human.
- Do not remove necessary uncertainty; make uncertainty specific.
- Do not make prose casual, emotional, or idiosyncratic unless the target venue and section allow it.
- Keep mathematical definitions, threat models, dataset names, metrics, and citations exact.
- If evidence is missing, write an evidence placeholder or reviewer-facing diagnostic instead of pretending the evidence exists.

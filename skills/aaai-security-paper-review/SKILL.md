---
name: aaai-security-paper-review
description: Orchestrated review workflow for AAAI-targeted cybersecurity, SOC, threat-analysis, APT/EDR detection, LLM-agent security, MCP/tool security, prompt-injection, jailbreak/guardrail, privacy/security-alignment, and agent-safety manuscripts. Use when the user asks to review, audit, score, revise, or compare an AAAI security or LLM-agent paper, especially from a LaTeX source directory or PDF.
---

# AAAI Security Paper Review

## Overview

Use this skill as the single entry point for multi-perspective AAAI review of security, SOC, threat-analysis, and LLM-agent manuscripts. It orchestrates venue fit, reviewer-style critique, section audit, corpus-matched diagnosis, evidence checklist, and optional LaTeX revision.

This is a workflow skill. It does not replace the AAAI venue skill or the security/LLM-agent corpus; it tells Codex when and how to load them.

## Inputs

Accept any of these manuscript inputs:

- A LaTeX source directory, preferably containing `main.tex`.
- A single `.tex` file.
- A compiled paper PDF.
- A submission package containing source and PDF.

Optional user controls:

- `mode=quick`: return AAAI fit, top risks, and minimal next steps.
- `mode=full`: run all review passes. Use this by default.
- `mode=surgical`: review only named sections or issues.
- `mode=edit`: review first, then patch LaTeX when the user explicitly asks for changes.
- `focus=<...>`: prioritize selected concerns such as threat model, experiments, writing, related work, anonymity, or reproducibility.

If the user asks only to review, do not mutate files. If the user asks to modify or revise, make scoped edits after the diagnosis.

## Required Calibration

Before reviewing, load these resources in order:

1. Read `../aaai-conference-on-artificial-intelligence/SKILL.md` to apply the AAAI venue-fit, evidence, official-cycle, and output rules.
2. If the manuscript is about cybersecurity, SOC/endpoint detection, APT, cyber-threat analysis, LLM-agent security, MCP/tool poisoning, prompt injection, jailbreaks, guardrails, privacy/security alignment, or autonomous-agent safety, read `../aaai-conference-on-artificial-intelligence/references/security-llm-agent-aaai-patterns.md`.
3. For `mode=full`, corpus comparison, or detailed rewrite, open the corpus artifacts named in that reference, especially `AAAI_security_llm_agent_fulltext_structure_report.md`.
4. For `focus=writing`, `mode=edit`, or deep abstract/introduction/contribution revision, read `../aaai-writing-style/SKILL.md`; for security or LLM-agent manuscripts also read `../aaai-writing-style/references/security-llm-agent.md`.
5. For current-cycle submission readiness, verify the live AAAI CFP, author kit, page limits, checklist, anonymity, supplement, and AI-use policy from the official AAAI website. Official instructions override all local skill notes.

## Manuscript Intake

For LaTeX inputs:

1. Identify the main `.tex` file. Prefer `main.tex`, then a file containing `\documentclass`.
2. Run `scripts/collect_latex_context.py <path>` to gather title, abstract, section outline, figure/table captions, citation keys, and included source files.
3. Read the main source and any included files needed to inspect the requested focus.
4. If compiled PDF exists and visual/layout/page-limit issues matter, inspect it or compile with the project-local workflow.

For PDF-only inputs:

1. Extract text with a PDF text tool.
2. Identify section boundaries, tables, figures, references, and appendix boundaries.
3. Note any visual/layout uncertainty separately.

## Review Passes

### 1. AAAI Gate

Judge whether the central claim is a broad AI contribution rather than only a security operations workflow. Decide:

- Fit: High / Medium / Low.
- Contribution type: method, benchmark, dataset, system, attack, defense, empirical, design, security, or other.
- Nearest AAAI security/LLM-agent corpus pattern.
- Biggest desk-reject or reviewer-reject risk.

### 2. Reviewer-Style Review

Write as a skeptical but fair AAAI PC reviewer:

- Strengths.
- Weaknesses ordered by severity.
- Questions for authors.
- Score and confidence when useful.
- A short accept/reject-risk summary.

Prioritize bugs, unsupported claims, weak evidence, missing baselines, unclear novelty, unbounded threat models, and reproducibility gaps.

### 3. Section Audit

Audit the paper by section:

- Abstract: contribution type, setting, result, and claim boundary.
- Introduction: problem-to-AI framing, novelty, why AAAI, and evidence preview.
- Related work: closest AAAI/security/LLM-agent analogs and technical delta.
- Threat model / problem formulation: attacker capability, trust boundary, assets, success criteria, and benign workflow.
- Method: reusable AI mechanism, decision boundary, learned vs deterministic components, and failure-mode coverage.
- Experiments: datasets, tasks, baselines, metrics, ablations, robustness, model/provider variants, and utility-security tradeoff.
- Writing style: first-page broad-AI framing, corpus-backed security/LLM-agent style, contribution bullets, evidence paragraphs, and overclaim removal.
- Limitations / ethics / reproducibility: release plan, artifacts, prompts/logs, responsible disclosure, closed-provider metadata, and claim scope.

### 4. Corpus-Matched Diagnosis

Use the 120-paper full-text structure report to identify the nearest paper families:

- SOC/threat-analysis.
- LLM-safety-attack-defense.
- Agent/tool-security.
- Backdoor/poisoning.
- Privacy/security-alignment.

Compare the manuscript against the nearest 5-10 analog papers by structure, not only topic. Extract what accepted AAAI papers usually include that this manuscript lacks.

### 5. Evidence Checklist

Check whether the evidence supports the claim:

- Threat model is explicit and bounded.
- Dataset/task construction is described in the main paper.
- Metrics match the security claim.
- Baselines include prompt-only, guardrail-only, policy/source-flow/provenance/tool-permission, or other relevant alternatives.
- Ablations isolate the proposed mechanism.
- Both security and benign utility are measured.
- Model/provider settings and prompts/task manifests are reproducible.
- Limitations are honest and do not hide the central proof.

### 6. Revision Plan or Edit Pass

For review-only tasks, end with a prioritized revision plan:

- `P0`: likely rejection or correctness blockers.
- `P1`: important but fixable weaknesses.
- `P2`: polish, clarity, and positioning improvements.

For `mode=edit`, patch only the files needed for the approved revision. Preserve unrelated user changes. Compile or run checks when appropriate.

## Output Format

For `mode=quick`, return:

```text
[Fit]
[Top rejection risk]
[Nearest corpus pattern]
[Must-fix items]
[Suggested next action]
```

For `mode=full`, use `references/review-template.md`.

For `mode=surgical`, include only the requested sections, but still state the main AAAI risk if the issue affects venue fit.

For `mode=edit`, report changed files, key edits, checks run, and residual risks.

## Practical Invocation

Recommended prompt:

```text
Use $aaai-security-paper-review, mode=full, to review this AAAI security/LLM-agent manuscript.
Paper path: <LaTeX source directory or PDF>
Focus: AAAI fit, threat model, experiments, baselines, ablations, corpus comparison, and revision plan.
```

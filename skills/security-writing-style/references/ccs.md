# ACM CCS Writing Style

Use this reference when `security-writing-style` is invoked with `venue=ccs`, `venue=ACM CCS`, or `venue=CCS`.

## Style Thesis

Write the paper for a broad general-security PC. CCS prose must translate a subarea contribution into a security contribution that readers from systems, privacy, crypto, web, software security, and measurement can understand quickly. Novelty and technical sharpness should appear before subfield machinery.

## First-Page Shape

1. Name the broad security problem.
2. Explain why the problem is timely or newly important.
3. State the technical gap in existing attacks, defenses, measurements, or evaluations.
4. Present the mechanism or finding in general-security language.
5. Show why the evidence is complete enough for a cross-area PC.

The first page should let a CCS reviewer outside the subfield say: "I can explain why this is a security paper and why the technical contribution is new."

## Claim Grammar

Prefer:

- "We uncover <security failure> in <broad system class> and explain why existing defenses/evaluations miss it."
- "We design <mechanism> that changes <attack/defense/measurement capability> under <threat model>."
- "We evaluate <mechanism/finding> across <settings> with <baselines> and <adaptive/negative controls>."

Avoid:

- Acronym-heavy openings that assume subfield knowledge.
- Narrow dataset or benchmark claims with no broad security implication.
- "First" claims without a clear nearest-prior-work delta.

## Abstract Pattern

1. Broad security context and affected system class.
2. Why current approaches miss the issue.
3. New mechanism, attack, defense, or measurement.
4. Evidence across settings, baselines, and controls.
5. General security implication and bounded scope.

## Introduction Pattern

- Paragraph 1: broad security problem and affected class.
- Paragraph 2: why existing work is insufficient.
- Paragraph 3: technical insight in simple terms.
- Paragraph 4: method/system/attack/defense.
- Paragraph 5: evaluation breadth and controls.
- Contributions: each bullet should be readable without subfield-specific shorthand.

## Contribution Bullets

Good CCS bullets often look like:

- "We identify <new vulnerability/failure/measurement gap> in <broad class>."
- "We develop <technical mechanism> that enables <attack/defense/measurement>."
- "We evaluate across <diverse settings> and show <security consequence>."
- "We provide <artifact/dataset/guidance> to support follow-up work."

## Evidence Paragraphs

Use this order:

1. Broad question.
2. Technical mechanism or hypothesis.
3. Evaluation design and denominator.
4. Baselines and controls.
5. Result.
6. Why the result matters beyond one dataset or implementation.

## Limitations And Ethics

CCS prose should avoid both alarmism and narrowness. State:

- exact threat model and excluded cases;
- disclosure and dual-use handling;
- why the evidence is enough despite scope limits;
- what the artifact enables and what it withholds.

## APT/SOC Emphasis

Translate operational claims into general security impact: provenance abstractions, attacker behavior, campaign trends, drift, evasion, investigation fidelity, or defender decision support. Do not leave the paper sounding like an enterprise tool report.

## LLM/Agent-Security Emphasis

Translate LLM behavior into security mechanisms: trust boundary, privilege, leakage, confused-deputy action, policy bypass, tool misuse, or capability boundary. Prompt lists alone are weak; mechanism and consequence matter.

## Rewrite Checklist

- Can a non-specialist security PC member summarize the novelty in one sentence?
- Does the introduction define acronyms and subfield terms before using them heavily?
- Is the nearest-prior-work delta explicit before contribution bullets?
- Does the evidence include breadth, controls, and adaptive or negative tests when needed?
- Is broad impact stated without claiming universal generality?

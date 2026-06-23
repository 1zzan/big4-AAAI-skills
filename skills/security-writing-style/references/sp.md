# IEEE S&P Writing Style

Use this reference when `security-writing-style` is invoked with `venue=sp`, `venue=S&P`, `venue=IEEE S&P`, or `venue=Oakland`.

## Style Thesis

Write the paper as a security/privacy insight that changes how reviewers understand a threat boundary, assumption, or design principle. S&P can accept systems, measurements, attacks, defenses, and SoK-like work, but the prose must show the generalizable security lesson, not only that a tool works.

## First-Page Shape

1. Name the security or privacy boundary.
2. State the assumption that current work makes.
3. Show why that assumption fails or is incomplete.
4. Introduce the new abstraction, framework, attack, defense, or measurement.
5. Give the evidence scale and the boundary of the claim.

The first page should let a broad S&P reviewer say: "This paper changes how we should reason about <security/privacy problem>."

## Claim Grammar

Prefer:

- "We identify <failure mode/abstraction> in <security boundary> under <attacker capability>."
- "We formalize <threat/assumption/desiderata> and show that existing approaches fail to satisfy it because <reason>."
- "We build <system/measurement> to test <principle>, and show <bounded consequence>."

Avoid:

- "We improve detection accuracy" without explaining the security principle.
- "We are the first to apply method X" without a new threat or reasoning boundary.
- "Practical" or "robust" unless the assumptions are explicit.

## Abstract Pattern

1. Security/privacy boundary or long-standing assumption.
2. Why current reasoning, defenses, or evaluation misses something.
3. New abstraction, attack, defense, or measurement method.
4. Evidence across settings, baselines, or adversary capabilities.
5. What the result means for security reasoning, plus scope and ethics.

## Introduction Pattern

- Paragraph 1: affected security/privacy boundary and why it matters.
- Paragraph 2: existing assumption and why it is not enough.
- Paragraph 3: threat model or reasoning gap.
- Paragraph 4: paper's abstraction/system/measurement.
- Paragraph 5: evidence and limitations.
- Contributions: each bullet should pair a conceptual contribution with evidence.

## Contribution Bullets

Good S&P bullets often look like:

- "We define <abstraction/desiderata/failure mode> for <security boundary>."
- "We show <existing class> fails under <capability/condition>, using <method/evidence>."
- "We implement <tool/system> to instantiate the abstraction and evaluate it on <scope>."
- "We derive <implication/guideline> for future defenses or evaluations."

## Evidence Paragraphs

Do not report metrics alone. Explain what the metric proves about the threat or assumption.

Use this order:

1. Question being tested.
2. Threat or assumption under test.
3. Experimental setting and denominator.
4. Result.
5. Interpretation for the security abstraction.
6. Scope limit.

## Limitations And Ethics

S&P prose should look mature and non-sensational. State:

- what the threat model excludes;
- whether users, private data, malware, or live systems are involved;
- whether responsible disclosure applies;
- what the artifact can and cannot prove.

## APT/SOC Emphasis

For APT/SOC papers, elevate the reasoning object: provenance summarization, root-cause preservation, concept drift, investigation fidelity, analyst actionability, or attack-campaign semantics. Avoid classifier-only framing.

## LLM/Agent-Security Emphasis

For LLM/agent papers, foreground the trust boundary: tool use, memory, RAG, browser state, prompt channel, model-serving, policy layer, or user/developer authority. Show the security consequence, not only model behavior.

## Rewrite Checklist

- Does the first page name the assumption being challenged?
- Does the paper state an asset, adversary, and security/privacy consequence?
- Do contribution bullets include a conceptual object, not only implementation?
- Are limitations written as claim boundaries rather than apology?
- Can the main insight survive outside the specific dataset or prototype?

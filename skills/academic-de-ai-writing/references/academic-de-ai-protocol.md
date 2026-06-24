# Academic De-AI Protocol

Use this reference for full manuscript audits, LaTeX edits, citation-focused passes, or any rewrite that changes scientific claims.

## Core Diagnosis

AI-polished academic text usually looks complete but lacks research texture. Diagnose combinations, not single phrases:

- uniform fluency: every paragraph has the same length, rhythm, and transition logic;
- generic correctness: sentences are true but not anchored to this study's design, dataset, threat model, or evidence;
- over-defensive stance: "may", "potential", "to some extent", and "future work" dilute claims that the evidence can actually support;
- non-landing paragraphs: the paragraph opens a possibility space but never settles the local claim;
- flat references: citations are listed as equal witnesses instead of forming a hierarchy of mechanism, method, contrast, and controversy;
- missing decision trace: the paper says what was done but not why this design choice was made under real constraints.

## Rewrite Hierarchy

Fix substance before style:

1. Claim support: bind each strong claim to a result, dataset, baseline, ablation, proof, or citation.
2. Research decision trace: add the reason for design choices when the source text provides it.
3. Evidence pressure: name the concrete comparison, condition, failure mode, or scope boundary.
4. Citation hierarchy: identify core, method-support, and contrast citations.
5. Sentence texture: reduce formulaic connectors and uniform rhythm after the argument is fixed.

## Research Decision Trace

Convert description into rationale:

- From "We use X" to "We use X because Y would otherwise confound Z."
- From "The dataset contains N samples" to "The dataset is useful for this claim because it stresses A and excludes B."
- From "We compare against baselines" to "The baselines separate gains from representation, optimization, data scale, or domain engineering."
- From "There are limitations" to "This limitation affects the claim in this specific direction."

Only add rationale when it follows from the manuscript, experiments, or user-provided notes. If missing, mark it as a needed author input.

## Stance Calibration

Avoid average neutrality. A paper can take a position when the evidence supports it.

Strengthen:

- "may improve" -> "improves on the evaluated setting" when the result table supports it;
- "has potential value" -> "is useful for <specific task/reader/setting>";
- "existing work has limitations" -> "existing work cannot test <specific condition> because <reason>."

Keep or add hedging when:

- the evidence is indirect;
- the dataset is narrow;
- the claim depends on a closed model, simulation, annotation policy, or unverified threat model;
- the statement generalizes beyond tested tasks.

Good uncertainty is concrete: name the dataset, population, model, threat boundary, or mechanism that limits the claim.

## Citation Repair

Replace citation lists with citation roles:

- Core mechanism citations: 2-5 papers that define the problem or central mechanism; revisit them across introduction, method, and related work.
- Method-support citations: tools, datasets, metrics, or standard baselines.
- Contrast citations: nearest work that differs in assumption, evidence shape, or capability.
- Controversy citations: work that suggests a competing interpretation or failure mode.

For related work, avoid "A did X. B did Y. C did Z." Prefer:

```text
Prior work splits into <axis>. The first line of work <mechanism> but assumes <condition>. The second line relaxes <condition> but cannot test <your setting>. Our work targets the gap where <specific constraint> matters.
```

Do not invent citations. If a claim lacks support, write `[citation needed: role=<core|method|contrast>]`.

## Connector Replacement

Do not merely delete "furthermore", "moreover", "notably", "in summary", or "worth noting". Replace the relation:

- Cause: "Because X changes Y, ..."
- Contrast: "Unlike X, ..."
- Condition: "When X holds, ..."
- Mechanism: "This matters because ..."
- Evidence: "Table N isolates this effect by ..."
- Scope: "This claim is limited to ..."

If no relation exists, split or delete the sentence.

## Section-Specific Edits

Abstract:

- State the concrete problem, intervention, evidence, and boundary.
- Avoid ending with broad "potential impact"; end with what was shown and where.

Introduction:

- Make page one reveal the research choice, not just the domain importance.
- Replace generic motivation with the bottleneck that forces the method or benchmark.
- Make contributions evidence-shaped: each bullet should point to a proof block.

Related work:

- Build a map of disagreements and missing conditions.
- Use fewer but more load-bearing citations.

Method:

- Explain design choices, not only modules.
- Distinguish learned, deterministic, heuristic, and human-authored components.

Experiments:

- Tie each experiment to one claim.
- Name what the baseline or ablation rules out.
- Include negative or failure cases when the manuscript has them.

Limitations:

- Avoid "more work is needed" unless it names the missing condition.
- State how the limitation affects external validity, mechanism confidence, or deployment.

## Edit Styles

Use one of these edit styles:

- `style=conservative`: preserve sentence order and only remove obvious AI-polished texture.
- `style=argumentative`: restructure paragraphs around claim, evidence, and implication.
- `style=venue`: adapt to a target venue's writing expectations if a venue skill is available.
- `style=cn`: work on Chinese academic prose.
- `style=en`: work on English academic prose.

## Before/After Pattern

Bad:

```text
This approach has certain advantages and may provide potential value for future research.
```

Better:

```text
This approach is useful when the evaluation requires <condition>, because it separates <mechanism> from <confounder>. Its claim should remain limited to <tested scope>.
```

Bad:

```text
Existing studies have explored this problem from different perspectives.
```

Better:

```text
Existing studies mainly test <axis A> or <axis B>. Neither setting captures <specific constraint>, which is the condition our benchmark is designed to expose.
```

## Final Check

Before returning the rewrite, verify:

- no invented evidence or citation;
- fewer generic connectors;
- every paragraph has a local landing;
- uncertainty is specific;
- citations have roles;
- the result sounds like an author defending a research choice, not a model summarizing a topic.

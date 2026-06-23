# USENIX Security Writing Style

Use this reference when `security-writing-style` is invoked with `venue=usenix`, `venue=USENIX Security`, or `venue=USENIX`.

## Style Thesis

Write the paper as an auditable systems-security contribution. USENIX Security prose should make the implementation, measurement, dataset, workload, artifact, and deployment constraints easy to inspect. The reviewer should feel that the result can be reproduced, stress-tested, or reused.

## First-Page Shape

1. Name the real system, software stack, measurement setting, or security workflow.
2. Explain the operational gap or attack/defense failure.
3. Introduce the implemented system, method, measurement, or analysis.
4. State the evaluation setup: scale, traces, baselines, workloads, artifacts.
5. Bound deployment assumptions, costs, release, and responsible handling.

The first page should let a systems-security reviewer say: "I understand what was built or measured, why it matters, and how to audit it."

## Claim Grammar

Prefer:

- "We implement <system/tool/pipeline> and evaluate it on <realistic traces/workloads>."
- "We measure <security phenomenon> across <scope>, validate <bias/labels>, and release <artifact/data/code>."
- "We uncover <vulnerability/failure> in <system class> and responsibly validate it under <constraints>."

Avoid:

- "Our method is practical" without runtime, overhead, deployment, or artifact detail.
- "Large-scale" without denominators, collection method, and validation.
- "Real-world" without explaining source, realism, and limits.

## Abstract Pattern

1. Concrete system/security workflow.
2. Operational pain or unsolved failure.
3. Built artifact, measurement, attack, or defense.
4. Evidence: scale, workloads, baselines, overhead, reproduction.
5. Release, responsible disclosure, and scope.

## Introduction Pattern

- Paragraph 1: concrete system or security workflow.
- Paragraph 2: why existing practice or research is insufficient.
- Paragraph 3: design or measurement challenge.
- Paragraph 4: system/method overview.
- Paragraph 5: evaluation and artifact/release posture.
- Contributions: each bullet should say what was built/measured and how it was validated.

## Contribution Bullets

Good USENIX bullets often look like:

- "We build <artifact/system> for <security workflow>, with <implementation detail>."
- "We evaluate on <dataset/workload/traces> against <baselines>, measuring <security and systems metrics>."
- "We release <code/data/configs> or explain what is withheld and why."
- "We identify deployment constraints: <overhead/runtime/storage/operator burden>."

## Evidence Paragraphs

Use this order:

1. Operational question.
2. Dataset/workload/source and validation.
3. Baselines and configuration.
4. Main result with denominators.
5. Cost, overhead, runtime, false positives, or deployment implication.
6. Artifact or reproducibility pointer.

## Limitations And Ethics

USENIX reviewers reward explicit artifact and release discipline. State:

- what code, data, configs, models, traces, or scripts are released;
- what is withheld due to safety, privacy, or licensing;
- how to reproduce tables and figures;
- responsible disclosure or non-applicability;
- deployment limitations and operator assumptions.

## APT/SOC Emphasis

Make practitioner value explicit: time-to-detect, false-positive cost, analyst workload, provenance storage, investigation compression, attribution quality, online/offline mode, and operational constraints.

## LLM/Agent-Security Emphasis

Show a realistic app or agent stack. Include prompts, tool/RAG/browser configuration, model versions, harness, adaptive attacks, seeds, mitigation scripts, and cost or latency when relevant.

## Rewrite Checklist

- Does the abstract mention the artifact or measurement setup?
- Are denominators, workloads, and baselines visible early?
- Does every "practical" claim include a cost or deployment metric?
- Is the release boundary clear enough for artifact review?
- Can a reviewer reproduce or audit the main claim?

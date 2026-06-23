# AAAI Security and LLM-Agent Writing Style

Use this reference when `aaai-writing-style` is invoked with `mode=deep` for cybersecurity, APT/SOC, threat analysis, LLM-assisted cyber reasoning, LLM-agent security, MCP/tool security, prompt injection, jailbreak/guardrail, privacy/security alignment, or agent-safety manuscripts.

This reference is derived from the AAAI security/LLM-agent corpus metadata under `../../resources/aaai-security-corpus/`: 120 AAAI-24/25/26 papers selected for security, SOC, threat-analysis, LLM safety, agent/tool security, backdoor/poisoning, and privacy/security-alignment relevance. Treat it as a calibration set, not a complete census of all AAAI papers.

## Style Thesis

Write the paper as a broad AI contribution exposed by a security setting. AAAI reviewers should see the reusable AI idea first: representation, reasoning, benchmark, agent control, alignment, evaluation protocol, dataset, or learning mechanism. The security domain is the hard setting that makes the AI problem important, not a substitute for AI novelty.

## First-Page Shape

1. Name the general AI problem: representation, reasoning, planning, agent control, safety, alignment, robustness, benchmark construction, or evaluation.
2. Explain why the security setting makes this AI problem hard: sparse malicious signal, long context, graph heterogeneity, tool composition, autonomy, metadata trust, label scarcity, or high-cost expert validation.
3. State the reusable technical object: method, benchmark, dataset, framework, simulator, attack, defense, guardrail, or evaluation protocol.
4. Preview the evidence: datasets/tasks, baselines, ablations, security metric, utility metric, and model/provider coverage.
5. Bound the claim: threat model, data provenance, artifact release, limitations, ethics, and reproducibility checklist.

The first page should let a non-security AAAI reviewer say: "This is an AI paper because it contributes <AI object>, and security is the challenging domain where the object is validated."

## Claim Grammar

Prefer:

- "We formulate <security task> as <AI problem> and introduce <reusable mechanism>."
- "We build <benchmark/dataset/evaluation protocol> that exposes <agent/control/safety/robustness failure>."
- "We design <model/control/guardrail> that uses <structure> to improve <security metric> while preserving <utility metric>."
- "We evaluate across <datasets/models/scenarios> with <baselines/ablations> and bound the claim under <threat model>."

Avoid:

- "We improve SOC operations" without a reusable AI mechanism.
- "We use LLMs for security" without structured control, validation, or benchmark design.
- "Safe", "secure", "robust", or "practical" without measured condition and scope.
- LLM-as-judge evidence as the only correctness signal.

## Abstract Pattern

1. AI problem and security setting.
2. Why existing AI/security approaches fail or are insufficient.
3. New method, benchmark, dataset, agent-control mechanism, or evaluation protocol.
4. Evidence: datasets, models, baselines, ablations, security metric, utility metric.
5. Bounded claim: threat model, release/reproducibility, limitations, ethics.

## Introduction Pattern

- Paragraph 1: broad AI problem plus security motivation.
- Paragraph 2: why the security setting stresses existing AI methods.
- Paragraph 3: nearest prior-work delta. Compare against both AI baselines and security/LLM-agent analogs.
- Paragraph 4: proposed mechanism, benchmark, or evaluation protocol.
- Paragraph 5: evidence preview with baselines, ablations, and security plus utility metrics.
- Paragraph 6: limitations, ethics, artifact, and checklist posture when relevant.
- Contributions: each bullet should name the AI contribution type and its evidence block.

## Contribution Bullet Shapes

For APT/SOC/EDR detection:

- "We formulate <telemetry/security object> as <AI representation problem> and introduce <model/mechanism>."
- "We evaluate on <datasets/tasks> against <security and AI baselines>, reporting <detection metric> and <operational metric>."
- "We ablate <mechanism components> to show that the improvement comes from <AI idea>, not only domain engineering."

For cyber-threat analysis and LLM-assisted security:

- "We convert <expert-heavy cyber task> into <learning/generation/evaluation task> with <structured supervision/ontology/static analysis/deterministic validation>."
- "We evaluate output quality with <expert labels/ground truth/deterministic agreement>, not only LLM judging."
- "We release <prompts/tasks/manifests/labels> or explain the release boundary."

For LLM-agent, MCP, and tool security:

- "We define <agentic attack surface> as <AI safety/control problem>."
- "We introduce <benchmark/guardrail/policy monitor/control mechanism> for <tool/RAG/MCP/multi-agent boundary>."
- "We measure <attack success/policy violation> and <benign utility/task completion>, with ablations over <policy/tool/metadata/model components>."

For jailbreak, guardrail, and safety evaluation:

- "We specify <access level/model family/risk category/query budget> and evaluate <attack/defense> across <models/scenarios>."
- "We report safety and utility together, not only attack success rate."
- "We include transfer, generalization, or adaptive testing when making robustness claims."

## Evidence Paragraphs

Use this order:

1. AI question: what mechanism or benchmark property is being tested.
2. Security setting: dataset, task, threat model, or agent environment.
3. Baselines: AI baselines and security-specific baselines.
4. Metrics: task metric plus security metric plus utility/cost when relevant.
5. Result with denominator and scope.
6. Ablation or robustness result that isolates the mechanism.
7. Limitation or reproducibility pointer.

## Dataset And Benchmark Wording

AAAI reviewers expect dataset/task construction to be visible in the main paper:

- source and selection process;
- label or scenario construction;
- split, leakage prevention, and validation;
- benchmark categories or risk taxonomy;
- release status and redaction rationale;
- why the benchmark tests an AI capability, not only a security workflow.

## Limitations, Ethics, And Reproducibility

Write these as part of the scientific claim:

- Bound attacker capability, model/provider version, data source, task family, and metadata assumptions.
- State whether prompts, task manifests, generated outputs, labels, logs, or code can be released.
- For closed providers, preserve enough outputs and settings for audit.
- For security content, state harm surface, dual-use boundary, responsible disclosure or non-applicability, and withheld details.
- Align prose with the AAAI checklist; do not let the checklist contradict the main text.

## Topic-Specific Style Signals

APT/SOC and threat-analysis papers:

- Strong style: "AI representation for difficult security behavior."
- Weak style: "SOC product workflow with better scores."
- Required signals: bounded data, threat assumptions, mechanism ablation, false-positive or false-alarm cost, robustness/noise/unseen-family test when claimed.

LLM-assisted cyber reasoning:

- Strong style: "structured learning/generation with validation."
- Weak style: "LLM explains security artifacts."
- Required signals: non-LLM structure, deterministic checks or expert validation, prompt/task manifest, output-quality metric.

LLM-agent and MCP/tool security:

- Strong style: "agentic control, authority boundary, benchmark, or measurable utility-security tradeoff."
- Weak style: "prompt-only safety advice."
- Required signals: attacker capability, trusted metadata, sensitive action, policy or monitor, benign utility, model/provider breakdown.

Backdoor, poisoning, privacy, and alignment security:

- Strong style: "formal/semi-formal attack objective with utility cost."
- Weak style: "qualitative risk discussion."
- Required signals: protected asset, attacker observation/control, leakage or target behavior, stealthiness or budget, defense comparison.

## Rewrite Checklist

- Does the title/abstract foreground the AI contribution, not only the security application?
- Can a non-security AAAI reviewer identify the method, benchmark, dataset, or evaluation protocol by the end of page one?
- Does the introduction translate security terms into AI concepts?
- Are baselines both AI-relevant and security-relevant?
- Does every contribution bullet have an evidence block in the main paper?
- Are security and utility measured together for agent/control papers?
- Are limitations, ethics, artifacts, and checklist answers mutually consistent?

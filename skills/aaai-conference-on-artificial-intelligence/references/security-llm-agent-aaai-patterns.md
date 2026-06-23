# AAAI Security, SOC, Threat Analysis, and LLM-Agent Pattern Notes

Use this reference when an AAAI-targeted paper is about cybersecurity, APT detection, SOC/endpoint threat detection, threat analysis, LLM-assisted cyber reasoning, LLM-agent security, MCP/tool poisoning, prompt injection, privacy/security alignment, or autonomous-agent safety.

Open-source corpus metadata folder: `../../../resources/aaai-security-corpus`

Optional local full-PDF corpus folder: `data/aaai-security-corpus/pdfs/` if you maintain PDFs outside the public repository.

Corpus artifacts:

- `AAAI_security_llm_agent_fulltext_structure_report.md`: readable paper-level table with labels, headings, and structural signals.
- `AAAI_security_llm_agent_expansion_manifest.json`: downloaded expansion manifest with OJS URLs.
- `AAAI_security_llm_agent_candidate_pool.json`: broad OJS title pool from AAAI-24/25/26 issue pages.
- Optional local-only artifact: `AAAI_security_llm_agent_fulltext_structure.jsonl`, a per-paper full-text extraction with snippets and evidence flags. This file is not required for normal review and is not included in the public repository by default.

Corpus size after expansion: 72 PDFs from AAAI-24, AAAI-25, and AAAI-26. The set is intentionally high-relevance rather than exhaustive. It covers APT/provenance detection, EDR detection, malicious-traffic detection, ransomware detection, CVE/smart-contract vulnerability detection, fraud/bot/malware analysis, LLM jailbreak/guardrail papers, MCP/tool security, mobile and multi-agent safety, LLM backdoor/poisoning, membership/inversion/privacy attacks, and secure LLM-based interfaces.

## How to Use This Reference

1. For a quick venue-fit decision, read this file only.
2. For a paper-specific review, open `AAAI_security_llm_agent_fulltext_structure_report.md` and locate the nearest 5-10 analog papers by label.
3. For detailed rewrite or rebuttal work, use the structure report first. If a local JSONL extraction exists, search it by `labels`, `title`, `problem_snippets`, `contribution_snippets`, `evaluation_snippets`, and `risk_snippets`.
4. Do not load all PDFs into context. Use the full-text report to pick papers, then inspect individual PDFs only when a claim, baseline, metric, or section structure needs confirmation.

## Venue Fit Heuristic

High AAAI fit when the paper contributes a reusable AI idea:

- A representation or model for security behavior: provenance graph, hypergraph, sparse temporal sequence, semantic pretraining, ontology-guided reasoning, long-context vulnerability modeling, or behavior abstraction.
- A benchmark or dataset that exposes an AI problem in security: tool poisoning, mobile-agent safety, multi-agent compromise, CVE evaluation, threat-script explanation, jailbreak evaluation, secure NLIDB interaction, or offensive-security agent evaluation.
- A control, defense, or evaluation framework for agentic AI: guardrails with measurable enforcement, attack-surface taxonomy, deterministic policy monitor, semantic-graph defense, typed tool permissions, or utility-security tradeoff.

Lower AAAI fit when the paper is mainly:

- An SOC product workflow with limited AI novelty.
- A prompt-only defense without structured control or adversarial evaluation.
- A narrow security measurement study whose main audience is security systems rather than AI.
- A closed demo without enough artifacts, prompts, logs, threat model, model/provider settings, or reproducibility details.

## Full-Text Structure Patterns

The full-text extraction shows a stable structure across accepted AAAI security/LLM-agent papers:

1. **Problem-to-AI framing in the first page.** Papers start from an operational security or safety bottleneck, then quickly translate it into an AI problem: representation, reasoning, long-context modeling, alignment, agent control, benchmark construction, or evaluation.
2. **Named mechanism or benchmark.** The contribution is usually a named framework, benchmark, dataset, attack, defense, or evaluation protocol. The name appears early and maps to a reusable technical object.
3. **Explicit threat or risk model.** Attack/defense and agent papers often include a `Threat Model`, `Attack Scenario`, `Problem Formulation`, or equivalent. Detection papers may use dataset/task formulation instead, but still bound attacker behavior or data assumptions.
4. **Dataset section in the main paper.** The dataset, benchmark, or task source is not hidden in the appendix. Strong papers report source, scale, construction process, splits, labels, scenarios, and release status.
5. **Metrics tailored to the security claim.** Detection papers use precision/recall/F1/AUC/FPR/false alarm/overhead. LLM security papers use ASR, refusal/reject rate, defense success, harmfulness, utility, benign task success, query budget, and per-model breakdowns.
6. **Ablation over the mechanism.** Accepted papers rarely rely on aggregate wins alone. They ablate graph components, prompts, policy layers, attack strategies, defense modules, model families, metadata quality, or data scale.
7. **Limitations, ethics, and artifacts.** Most papers contain a limitation, ethics, artifact, or release signal. For security topics, this is part of the credibility story, not housekeeping.

## Accepted Contribution Shapes

### APT, SOC, EDR, and Threat Detection

The accepted shape is not "we detect attacks better" alone. It is "we introduce an AI modeling mechanism for difficult security behavior." Look for:

- Security object: provenance graph, endpoint log stream, traffic sequence, ransomware behavior, CVE text, smart-contract code, script artifact, fraud graph, or social-bot network.
- AI mechanism: indirect-dependency capture, behavioral logic, hypergraph reasoning, robust behavior abstraction, semantic pretraining, long-context code modeling, reinforcement learning under drift, graph-enhanced prompting, or sparse spatiotemporal modeling.
- Evidence: precision/recall/F1/AUC, false-positive or false-alarm rate, ablations, robustness to noise or unseen families, cross-dataset or zero-day tests, and runtime or overhead.
- Review risk: broad "APT", "SOC", or "threat intelligence" claims without bounded datasets, threat assumptions, or mechanism ablation.

### Cyber-Threat Analysis and LLM-Assisted Security

AAAI-friendly papers convert expert-heavy cyber tasks into structured learning or generation tasks:

- Examples: threat-script explanation, CVE evaluation, cybersecurity instruction generation, ransomware semantic classification, vulnerability detection, smart-contract analysis, fraud detection, botnet simulation.
- Strong pattern: combine LLMs with non-LLM structure such as ontologies, knowledge graphs, static-analysis signals, semantic features, expert seed examples, self-training, contrastive learning, graph signals, or deterministic validators.
- Evidence should include task metrics and output-quality checks. Prefer human expert validation, labeled ground truth, deterministic agreement, or deployment-style evaluation over LLM-as-judge alone.
- Review risk: synthetic labels or LLM-generated explanations treated as ground truth without validation.

### LLM-Agent, MCP, and Multi-Agent Security

AAAI accepts this line when the paper defines a concrete agentic attack surface and measures it as an AI safety/control problem:

- Attack surfaces: tool metadata poisoning, MCP server trust boundaries, prompt injection through tools, multi-agent software-development compromise, mobile-device control, smartphone privacy, stealthy message tampering, fact-checking agent poisoning, safeguard-pipeline bypasses, and inference-based database attacks.
- Evidence: attack success rate, refusal/reject rate, benign utility, utility under attack, defense overhead, safety-helpfulness tradeoff, per-model breakdown, per-scenario breakdown, query budget, and ablations over defense components.
- Stronger than prompt-only: policy enforcement, metadata sanitization, typed permissions, provenance/source flow, deterministic monitors, semantic-graph filtering, multi-layer guardrails, or benchmark protocols.
- Review risk: unclear attacker capability, missing trusted-boundary statement, or no benign-utility measurement.

### LLM Jailbreak, Guardrail, and Safety Evaluation

The expanded corpus shows that AAAI now has many papers in this lane. They are usually benchmark-heavy or mechanism-heavy:

- Attack papers define access level, model family, target harmfulness, transformation strategy, query budget, and transferability.
- Defense papers compare against multiple attack families and report both safety and utility.
- Benchmark papers define risk categories, scenario construction, judging protocol, and model coverage.
- Strong papers avoid a single-model story. They test multiple open and closed models, multiple attack sets, and at least one generalization or transfer setting.
- Review risk: reporting only ASR without benign utility, overfitting to one attack, or using an uncalibrated LLM judge as the sole evaluator.

### Backdoor, Poisoning, Privacy, and Alignment Security

This line is useful for papers about training-time or data-time risks:

- Backdoor/poisoning papers state trigger design, poisoning budget, attacker knowledge, target behavior, stealthiness, and defense assumptions.
- Privacy papers state the protected asset, attacker observation, leakage channel, and utility cost.
- Alignment-security papers usually need a formal or semi-formal attack objective, not just qualitative concern.
- Review risk: missing threat model, unrealistic attacker access, or no comparison to existing defenses.

## Writing Pattern for AAAI Reviewers

In abstract and introduction:

- State the general AI problem first: representation, reasoning, planning, agent control, benchmark, safety, alignment, robustness, or evaluation.
- Then state the cyber domain as the hard setting that exposes the AI problem.
- Make the contribution type visible: method, benchmark, dataset, framework, simulator, attack, defense, or evaluation protocol.
- Explain why existing AI methods fail: long context, sparse malicious signal, graph heterogeneity, label scarcity, implicit inference, tool composition, autonomy, metadata trust, or cascading multi-agent behavior.

In method:

- Use a pipeline or component structure where each module answers one failure mode from the introduction.
- For LLM systems, identify which parts are learned, prompted, rule-based, policy-enforced, deterministic, or human/expert validated.
- For security control, state the decision boundary: what inputs are trusted, what actions are blocked, and what evidence authorizes a sensitive action.

In experiments:

- Include strong security baselines and AI baselines.
- Include a mechanism ablation, not only aggregate wins.
- Report both security and utility. For agent papers this usually means attack success or policy violation plus benign task completion/helpfulness.
- Include model/provider variants when the method depends on LLM behavior.
- Make threat model, data provenance, prompt/task manifests, and provider/model settings reproducible.

In limitations:

- Bound claims to the datasets, attacker capabilities, tools, models, and metadata assumptions actually tested.
- State whether logs, prompts, generated data, or expert labels can be released.
- If provider APIs or closed models are used, preserve enough task manifests and outputs for audit.

## TaintSOC-Style Mapping

For a SOC-agent paper about authority-grounded action control:

- Frame it as an AI control mechanism for LLM security agents, not as a SOC automation product.
- Use APT/EDR papers for security-operation realism and LLM-agent security papers for tool/action risk.
- Keep the core claim narrow: authority-grounded predicates reduce unsafe or unauthorized actions under a specified metadata trust model while preserving benign utility.
- Treat the "authority" object as the reusable AI abstraction: a decision boundary linking source evidence, action permissions, tool calls, and task context.
- Add a threat model in the main paper: attacker capability, injected or compromised content source, trusted metadata boundary, sensitive action, success criterion, and allowed benign workflow.
- Essential comparisons: prompt-only guardrails, generic safety instructions, source-flow or provenance controls, zero-trust or policy baselines, tool-permission baselines, and model/provider variants.
- Essential ablations: remove each authority predicate or policy layer, vary noisy/missing metadata, vary attack strength, vary agent/tool count, and measure utility-security tradeoff.
- Main-paper evidence should include attack success or violation rate, benign task success, false positives/false negatives, overhead, and model breakdowns.

Suggested section skeleton:

```text
Introduction: SOC-agent automation creates a general AI control problem.
Problem Formulation / Threat Model: authority evidence, action space, attacker capability, success metric.
Method: authority-grounded predicates, monitor/policy layer, tool/action interface.
Benchmark / Dataset: SOC tasks, benign tasks, injected-risk tasks, metadata variants.
Experiments: ASR/violation rate, benign utility, FPR/FNR, overhead, model/provider transfer.
Ablations: remove predicates, prompt-only, guardrail-only, source-flow-only, noisy metadata.
Limitations / Ethics: metadata trust, closed APIs, release boundaries, responsible disclosure.
```

## Quick Review Checklist

- [ ] Does the first page make the AI contribution explicit before operational security details?
- [ ] Is there a concrete threat model with attacker capability, control channel, trusted metadata, target asset, and success criterion?
- [ ] Are both security and benign utility measured?
- [ ] Are there baselines beyond prompt-only defenses?
- [ ] Does at least one ablation isolate the proposed mechanism?
- [ ] Are datasets, prompts, tasks, model settings, and artifacts described enough for AAAI review?
- [ ] Are claims bounded to the tested datasets, tools, models, and threat model?

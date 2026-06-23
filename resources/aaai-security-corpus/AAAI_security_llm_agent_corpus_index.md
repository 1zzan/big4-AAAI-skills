# AAAI Security, SOC, Threat Analysis, and LLM-Agent Security Corpus

Optional local PDF folder: `data/aaai-security-corpus/pdfs/` if you maintain PDFs outside the public repository.

Scope: selected recent AAAI main-conference papers from AAAI-24, AAAI-25, and AAAI-26 that are useful for calibrating AAAI fit for APT detection, SOC/endpoint threat detection, cyber-threat analysis, LLM-assisted security, LLM-agent safety, tool security, MCP security, and multi-agent risk.

This is a working corpus, not an exhaustive bibliography. Use it to extract venue patterns and reviewer expectations before writing or reviewing a security-oriented AAAI submission.

## Expanded Corpus Artifacts

The corpus has been expanded from the initial 18-paper seed set to 120 PDFs. The full inventory and structure extraction now live in these generated artifacts:

- `AAAI_security_llm_agent_expansion_manifest.json`: 102 additional downloaded AAAI OJS papers with title, year, issue, source URL, and local PDF filename.
- `AAAI_security_llm_agent_candidate_pool.json`: title-level candidate pool scraped from AAAI-24, AAAI-25, and AAAI-26 OJS issue pages before manual relevance filtering.
- `AAAI_security_llm_agent_fulltext_structure.jsonl`: per-paper full-text extraction, including section headings, topic labels, evidence flags, and problem/contribution/evaluation/risk snippets.
- `AAAI_security_llm_agent_fulltext_structure_report.md`: readable full-text structure report with corpus counts and a paper-level table.

Current full-text label counts:

| Label | Count |
|---|---:|
| SOC/threat-analysis | 75 |
| LLM-safety-attack-defense | 75 |
| agent/tool-security | 34 |
| backdoor/poisoning | 33 |
| privacy/security-alignment | 31 |
| security-adjacent | 4 |

## Seed Paper Inventory

| Year | Local PDF | Topic Lens | Source URL |
|---|---|---|---|
| AAAI-26 | `AAAI26_Sentient_APT_provenance_indirect_dependencies.pdf` | APT detection, provenance graphs, indirect dependencies, behavioral logic | https://ojs.aaai.org/index.php/AAAI/article/view/37115/41077 |
| AAAI-26 | `AAAI26_HyperGLLM_endpoint_threat_detection.pdf` | EDR, endpoint threat detection, hypergraph-enhanced LLMs | https://ojs.aaai.org/index.php/AAAI/article/view/40815/44776 |
| AAAI-26 | `AAAI26_AutoMalDesc_cyber_threat_script_analysis.pdf` | Cyber-threat script explanation, LLM self-paced learning, static analysis summarization | https://ojs.aaai.org/index.php/AAAI/article/view/36959/40921 |
| AAAI-26 | `AAAI26_Interpretable_Robust_Behavior_Abstraction_Provenance.pdf` | Provenance behavior abstraction, interpretability, robustness | https://ojs.aaai.org/index.php/AAAI/article/view/37056/41018 |
| AAAI-25 | `AAAI25_SRDC_ransomware_LLM_pretraining.pdf` | Ransomware detection/classification, semantic features, LLM-assisted pretraining | https://ojs.aaai.org/index.php/AAAI/article/view/35080/37235 |
| AAAI-25 | `AAAI25_MalDetectFormer_malicious_traffic_detection.pdf` | Malicious traffic detection, sparse spatiotemporal modeling | https://ojs.aaai.org/index.php/AAAI/article/view/34411/36566 |
| AAAI-25 | `AAAI25_CVE_LLM_vulnerability_evaluation.pdf` | Vulnerability evaluation, ontology-assisted LLMs, CVE/CVSS workflow | https://ojs.aaai.org/index.php/AAAI/article/view/35139/37294 |
| AAAI-24 | `AAAI24_CyberQ_cybersecurity_QA_generation.pdf` | Cybersecurity QA generation, KG-augmented LLM prompting | https://ojs.aaai.org/index.php/AAAI/article/view/30362/32412 |
| AAAI-26 | `AAAI26_STACK_LLM_safeguard_pipeline_attacks.pdf` | LLM safeguard pipelines, staged attacks, defense-in-depth evaluation | https://ojs.aaai.org/index.php/AAAI/article/view/41108/45069 |
| AAAI-26 | `AAAI26_Risks_Defenses_LLM_Multi_Agent_Systems.pdf` | LLM-based multi-agent software systems, risk scenarios, defenses | https://ojs.aaai.org/index.php/AAAI/article/download/41134/45095 |
| AAAI-26 | `AAAI26_MCPTox_tool_poisoning_MCP_servers.pdf` | MCP tool poisoning, real-world MCP server benchmark | https://ojs.aaai.org/index.php/AAAI/article/view/40895/44856 |
| AAAI-26 | `AAAI26_MCP_policy_enforced_guardrails_infrastructure.pdf` | MCP infrastructure automation, policy-enforced guardrails | https://ojs.aaai.org/index.php/AAAI/article/download/41468/45429 |
| AAAI-26 | `AAAI26_MobileSafetyBench_autonomous_agents_mobile_control.pdf` | Mobile-device control agents, safety benchmark, autonomy risks | https://ojs.aaai.org/index.php/AAAI/article/view/41090/45051 |
| AAAI-26 | `AAAI26_LLM_MAS_stealthy_tampering.pdf` | Multi-agent LLM stealthy tampering, adaptive attack policy | https://ojs.aaai.org/index.php/AAAI/article/view/40224/44185 |
| AAAI-26 | `AAAI26_Resilience_Ambient_Multi_Agent_LLMs.pdf` | Ambient multi-agent LLM resilience, anomaly detection, control | https://ojs.aaai.org/index.php/AAAI/article/view/41065/45026 |
| AAAI-25 | `AAAI25_Trading_Off_Security_Collaboration_MAS.pdf` | Multi-agent security tax, security/collaboration tradeoff | https://ojs.aaai.org/index.php/AAAI/article/view/34970/37125 |
| AAAI-26 | `AAAI26_SafeNLIDB_privacy_preserving_safety_alignment.pdf` | NLIDB privacy/security alignment, inference attacks, secure SQL | https://ojs.aaai.org/index.php/AAAI/article/view/40484/44445 |
| AAAI-26 | `AAAI26_HEV_Generative_Sandbox_domain_safety_assessment.pdf` | Domain-specific LLM social-risk assessment, human-LLM simulation | https://ojs.aaai.org/index.php/AAAI/article/view/40498/44459 |

## Extracted Venue Patterns

### 1. APT, SOC, EDR, and Threat Detection

AAAI security-detection papers are usually accepted as AI papers when the core novelty is a reusable modeling contribution, not a product workflow. The accepted shape is:

- Security object: provenance graph, endpoint event stream, traffic sequence, ransomware behavior, CVE text, or script artifact.
- AI contribution: graph reasoning, hypergraph modeling, behavior abstraction, semantic pretraining, long-sequence compression, ontology-guided generation, or sparse spatiotemporal modeling.
- Evidence: public or realistic datasets, strong classical and neural baselines, precision/recall/F1/AUC or false-positive rate, ablations that isolate the modeling mechanism, robustness/noise/zero-day or cross-family tests, and runtime or overhead.
- Reviewer-facing claim: "This changes how AI models represent security behavior", not merely "This detects more attacks".

### 2. Cyber-Threat Analysis and LLM-Assisted Security

Papers such as AutoMalDesc, CVE-LLM, CyberQ, and SRDC show a recurring AAAI pattern:

- Start from a real security bottleneck where labels, explanations, or expert assessments are expensive.
- Convert the bottleneck into a learning, generation, or evaluation task.
- Add structure around the LLM: ontology, knowledge graph, static-analysis signal, semantic features, self-training loop, expert seed set, or deterministic validation.
- Evaluate both task utility and output quality. LLM-only claims are weaker unless supported by human expert review, labeled ground truth, deterministic checks, or deployment-style evaluation.
- Release or describe datasets/prompts/artifacts enough for reproducibility.

### 3. LLM-Agent and Multi-Agent Security

AAAI accepts LLM-agent security when the paper defines a new agentic attack surface and turns it into a benchmark, formal scenario, defense mechanism, or measurable tradeoff:

- Attack surfaces: tool metadata poisoning, MCP server/tool trust boundaries, software-development multi-agent workflows, mobile-device control, cross-agent prompt propagation, stealthy message tampering, safeguard-pipeline bypasses.
- Evidence: attack success rate, refusal/reject rate, benign utility, utility under attack, defense overhead, safety-helpfulness tradeoff, per-model breakdown, per-scenario breakdown, ablations over defense components.
- Stronger papers include realistic agents or live tools, scenario taxonomies, and defense baselines beyond prompt-only safeguards.
- Threat models must be explicit: attacker capability, control channel, trusted metadata, accessible observations, target assets, and success criteria.

### 4. Writing and Positioning Signals

AAAI-style security papers usually:

- Place the AI contribution in the abstract and first page before deep security operations detail.
- Name the artifact type clearly: method, benchmark, dataset, framework, simulator, guardrail, or evaluation protocol.
- Explain why the problem is hard for AI: long context, sparse malicious signal, graph heterogeneity, label scarcity, implicit inference, agent autonomy, compositional tool use, or cascading multi-agent behavior.
- Keep operational claims bounded by the threat model and datasets.
- Put the strongest quantitative evidence in the main paper. Appendices can hold details, but should not carry the core proof.

### 5. Rejection Risks to Watch

- A security operations story with no new AI representation, benchmark, or evaluation protocol.
- A prompt-only LLM defense with no structured control, artifact, or adversarial evaluation.
- Synthetic attack data presented as real-world prevalence rather than mechanism-testing evidence.
- LLM-as-judge evidence without expert labels, deterministic validation, or calibrated agreement checks.
- Closed-provider experiments without prompts, task manifests, outputs, replay logs, or enough metadata for review.
- Overbroad claims about "APT", "SOC", or "agent safety" that exceed the tested datasets and threat model.

## Mapping to TaintSOC-Style Papers

For an AAAI paper about SOC agents and authority-grounded action control:

- Strong analogies: Sentient and HyperGLLM for security-operation modeling; AutoMalDesc and CVE-LLM for LLM-assisted cyber reasoning; STACK, MCPTox, MobileSafetyBench, SafeNLIDB, and multi-agent-risk papers for agent/tool/control security.
- Best framing: a reusable AI safety/control mechanism for security agents, supported by a benchmark and deterministic monitor, rather than a SOC product demo.
- Must-have evidence: prompt-only and guardrail baselines, source-flow or provenance baselines, zero-trust or policy baselines when relevant, ablations over authority predicates, model/provider breakdowns, attack success and benign utility, and a clear metadata trust boundary.
- Useful main-paper language: "agentic action control", "authority-grounded decision boundary", "security-task benchmark", "mechanism ablation", "utility-security tradeoff", and "bounded threat model".

# Full-Text Calibration Patterns

This reference is derived from an open-access/full-text calibration set assembled on 2026-06-23. The set contains 120 papers across S&P, USENIX Security, ACM CCS, and NDSS, grouped into APT/SOC/threat analysis, LLM/agent security, and cross-topic papers. Treat it as a larger calibration sample, not a complete census: S&P and CCS coverage is constrained by open PDF availability, while USENIX and NDSS are closer to the full relevant candidate pool because official/open PDFs are easier to obtain.

If you publish or reuse the detailed extraction files, place them under `data/fulltext-calibration/` with this layout:

- `data/fulltext-calibration/structure_extractions.csv`
- `data/fulltext-calibration/fulltext_structure_summary.md`
- Per-paper `*.structure.json` files beside each PDF.

The review simulator can still use the summarized patterns below when those optional data files are absent.

## Coverage

| Venue | APT/SOC/Threat | LLM/Agent | Cross |
|---|---:|---:|---:|
| S&P | 6 | 12 | 0 |
| USENIX Security | 20 | 20 | 0 |
| ACM CCS | 9 | 10 | 2 |
| NDSS | 20 | 20 | 1 |

Year distribution: 2022 = 6, 2023 = 12, 2024 = 24, 2025 = 52, 2026 = 26. The sample is intentionally recent-heavy because LLM/agent security grows sharply after 2024.

## Claim Patterns That Survive Full-Text Reading

- APT/SOC papers make a claim about operational security capability, not only model performance: online APT detection, attack investigation, provenance reduction, attribution quality, concept drift handling, false-positive reduction, or human-readable attack story reconstruction.
- LLM/agent papers make a claim about a deployed trust boundary: prompt/tool/RAG/cache/browser-agent/model-serving boundary, prompt or data leakage, tool hijacking, jailbreak, resource abuse, unsafe web search, or agent permission failure.
- Cross papers are strongest when the LLM is not decoration: it must improve or attack a security workflow such as APT story reconstruction, incident-response planning, malware/PDF analysis, or SOC decision support.
- The strongest claims are scoped as "under attacker capability X, in system setting Y, security consequence Z occurs or is mitigated." Weak claims are global claims about being secure, robust, or practical without condition.

## Evidence Shapes By Venue

- S&P: new security abstraction, threat model, systematic framework, or principled failure mode; evidence can be system, measurement, attack, proof, or SoK-like taxonomy, but the paper must show why the insight generalizes.
- USENIX Security: systems-security relevance, auditable implementation, real or realistic traces, reproducible measurement, artifact discipline, deployment constraints, and concrete baselines.
- ACM CCS: broad security novelty, strong technical mechanism, clear attack/defense/measurement contribution, and abstract/introduction readable by a general computer-security PC.
- NDSS: practical network/systems/application boundary, operational realism, telemetry/provenance/log graph, online response, protocol/app/agent setting, and clear attack or defense validation.

Observed full-text tendency:

- USENIX and NDSS relevant papers repeatedly combine system + attack/defense + measurement evidence rather than relying on a single metric.
- USENIX APT/SOC papers often make deployment or practitioner value explicit: threat hunting interviews, provenance storage, continuous learning, online APT detection, and attribution quality.
- NDSS APT/SOC papers emphasize network/system boundary realism: lateral movement, encrypted malicious traffic, data-plane measurement, log graphs, false positives, and production constraints.
- CCS papers need the broadest top-level framing; strong papers translate subarea contributions into general security significance before diving into technical machinery.
- S&P papers in this sample are especially strong when they articulate a new abstraction, desiderata, or failure of existing assumptions, such as provenance graph summarization, concept drift, root-cause preservation, or game-theoretic prompt-injection detection.

## APT/SOC/Threat Review Heuristics

Reward:

- Real or semi-real telemetry, provenance graphs, audit logs, network flows, endpoint logs, ICS/enterprise traces, or carefully justified synthetic data.
- Analyst actionability: triage, alert explanation, investigation compression, attack story reconstruction, root-cause attribution, or incident-response utility.
- Operational metrics: false-positive cost, latency, throughput, memory, online/offline mode, deployment overhead, time-to-detect, and human workload.
- Robustness evidence: mimicry, evasion, concept drift, noisy labels, cross-campaign transfer, cross-organization transfer, or time-split evaluation.

Penalize:

- Accuracy/F1-only evidence with no analyst or deployment consequence.
- "APT" used as a label without multi-stage intrusion, persistence, lateral movement, provenance, CTI, or investigation semantics.
- Toy data that is not defended as representative of operational security.
- Detector claims that cannot explain what a defender does next.

## LLM/Agent-Security Review Heuristics

Reward:

- Explicit asset, attacker, trust boundary, and security consequence.
- Realistic LLM app, RAG, tool-use, plugin, browser-agent, model-serving, cache, or multi-agent environment.
- Reproducible attack harness, multiple models/applications/tasks, adaptive attacks, ablations, and mitigation evaluation.
- Measurements of exploit success, leakage, privilege misuse, unsafe action, policy bypass, denial of service, or recovery cost.

Penalize:

- Prompt lists without a mechanism, boundary, or generalizable attack model.
- Model-output comparisons that do not imply a security consequence.
- "LLM improves security" claims that do not compare against real security baselines, analyst workflows, false-positive costs, or deployment constraints.
- Defenses that lack adaptive bypass testing.

## Abstract And Introduction Construction

Strong abstracts usually use five slots:

1. Affected system or security workflow.
2. Existing assumption or defense that fails.
3. New attack, defense, measurement, dataset, or system.
4. Evidence scale and realism.
5. Bounded impact, release, disclosure, or safety posture when relevant.

Strong introductions:

- Start with asset, adversary, and security consequence.
- Make the nearest prior-work delta visible before contribution bullets.
- Tie each contribution to an evidence block.
- State limitations and ethics/disclosure early enough that reviewers trust the methodology.

## Artifact, Ethics, And Limitations

- Artifact sections should state what is released, what is withheld, why it is withheld, and how reviewers can audit the claim despite withholding.
- APT/SOC artifacts should include schemas, telemetry normalization, labeling protocol, time split, IoC/ATT&CK mapping, false-positive scripts, and redaction rationale.
- LLM/agent artifacts should include prompts, harnesses, model/app versions, tool/RAG/browser-agent configuration, safety filters, seeds, adaptive attacks, and mitigation scripts.
- Ethics sections should identify affected parties, harm surface, disclosure status, data handling, malware/exploit containment, and dual-use release boundary.
- Limitations should narrow scope around attacker capability, data representativeness, deployment assumptions, model/version dependence, and what the artifact cannot prove.

## Simulated Reviewer Red Flags

- Missing threat model in introduction.
- Contribution bullets that are not backed by experiments, measurements, proof, or artifact.
- Novelty framed only as applying a known method to a new dataset.
- No adaptive evaluation for defenses.
- No sampling-bias or label-quality discussion for measurements.
- No ethics/disclosure plan for live systems, malware, user data, prompt-injection payloads, or autonomous agents.
- Artifact link or repository that breaks anonymity or requires private credentials.

## Borderline Decision Cues

- Move from Weak Reject to Weak Accept when the paper can show one additional hard evidence block: adaptive attack, deployment trace, stronger baseline, time-split/cross-source validation, artifact smoke test, or clearer claim narrowing.
- Move from Weak Accept to Accept when the venue fit is crisp enough that a general PC member can explain the contribution in one sentence without knowing the subfield.
- Keep at Weak Reject or Reject when the idea is interesting but the paper cannot answer "what exactly is the asset, adversary, security consequence, and evidence block?"

# Big4 AAAI Skills

Codex skills for paper planning, venue-fit checks, writing, review simulation, submission checks, rebuttal, artifact preparation, and camera-ready work for:

- AAAI
- KDD
- IEEE S&P
- USENIX Security
- ACM CCS
- NDSS

The repository also includes shared security-review skills for threat models, evidence audits, related work, ethics/disclosure, top-four venue fit, top-four workflow planning, and review simulation.

## What This Repository Provides

This is a local Codex skill pack. Each skill is a directory containing a `SKILL.md` file, plus optional references, scripts, and agent configuration. After installation, Codex can select a skill when the user names it directly or when the task matches the skill description.

The pack is designed for three common use cases:

- choosing the right venue before writing;
- stress-testing a manuscript before submission;
- managing the submission lifecycle from idea, experiments, writing, review, rebuttal, artifact release, and camera-ready.

## Layout

```text
skills/
  aaai-*/
  acm-sigkdd-conference-on-knowledge-discovery-and-data-mining/
  ieee-symposium-on-security-and-privacy/
  usenix-security-symposium/
  acm-conference-on-computer-and-communications-security/
  network-and-distributed-system-security-symposium/
  security-*/
  shared-references/
resources/
scripts/
```

## Requirements

- Codex with local skill support.
- PowerShell for `scripts/install.ps1`, or any shell that can copy directories.
- Python 3 is recommended for helper scripts such as LaTeX context collection.

## Install

Clone the repository first:

```bash
git clone git@github.com:1zzan/big4-AAAI-skills.git
cd big4-AAAI-skills
```

Install skills and shared resources:

```powershell
.\scripts\install.ps1
```

Install to a custom Codex home:

```powershell
.\scripts\install.ps1 -CodexHome "D:\path\to\.codex"
```

Manual PowerShell install:

```powershell
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { "$env:USERPROFILE\.codex" }
New-Item -ItemType Directory -Force -Path "$codexHome\skills" | Out-Null
New-Item -ItemType Directory -Force -Path "$codexHome\resources" | Out-Null
Copy-Item -Recurse -Force .\skills\* "$codexHome\skills"
Copy-Item -Recurse -Force .\resources\* "$codexHome\resources"
```

Manual Bash install:

```bash
codex_home="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$codex_home/skills" "$codex_home/resources"
cp -R skills/* "$codex_home/skills/"
cp -R resources/* "$codex_home/resources/"
```

Restart Codex or start a new session after installing, then check the skill list.

## Update

Pull the repository and reinstall:

```powershell
git pull --rebase origin main
.\scripts\install.ps1
```

If multiple agents are working in the repository, pull before editing and avoid force-pushing:

```bash
git fetch origin
git pull --rebase origin main
```

## Verify Installation

After restarting Codex, the skill list should include at least:

- `aaai-security-paper-review`
- `aaai-conference-on-artificial-intelligence`
- `security-top4-review-simulator`
- `security-top4-venue-fit`

If a skill cannot find shared conference metadata, confirm that `resources/` was copied to:

```text
~/.codex/resources
```

or, when `CODEX_HOME` is set:

```text
$CODEX_HOME/resources
```

## How To Use

In Codex, invoke a skill by naming it or by asking for the task it covers. Skill names can be written plainly, such as `aaai-security-paper-review`, or with a `$` prefix when you want to force a specific skill, such as `$aaai-security-paper-review`.

You can also ask naturally:

```text
I have a SOC/LLM-security paper. Which top-four security venue fits best, and what is the fastest path to a stronger submission?
```

Codex should route that through the relevant workflow and venue-fit skills.

## Quick Start

Full NDSS/top-four security pre-submission audit:

```text
Use $security-top4-review-simulator, mode=full, to run a complete NDSS pre-submission audit.
Paper path: <LaTeX source directory or PDF>
Target venue: NDSS
Include: venue fit, simulated PC reviews, threat model, evidence support, artifact/ethics, desk-reject risks, and prioritized revision roadmap.
```

The full audit is a wrapper. You do not need to separately invoke `security-threat-model`, `security-evidence-audit`, `security-artifact-package`, `security-ethics-disclosure`, or `security-submission-check` unless you want to drill down into one lane after the full report.

Full AAAI security or LLM-agent review:

```text
Use $aaai-security-paper-review, mode=full, to review this AAAI security/LLM-agent manuscript.
Paper path: <LaTeX source directory or PDF>
Focus: AAAI fit, threat model, experiments, baselines, ablations, corpus comparison, and revision plan.
```

AAAI security or LLM-agent writing optimization:

```text
Use $aaai-writing-style, mode=deep, focus=security-llm-agent, to revise my AAAI manuscript abstract, introduction, contribution bullets, evidence paragraphs, limitations, ethics, and reproducibility wording.
Paper path: <LaTeX source directory or PDF>
```

For an AAAI security/LLM-agent draft, `aaai-security-paper-review, mode=full` is the one-shot review wrapper. Use `aaai-writing-style, mode=deep` when you only want the corpus-backed writing pass; review/edit modes in `aaai-security-paper-review` load that writing package when the focus is abstract, introduction, contribution, or evidence prose.

Academic de-AI writing pass / 学术论文去 AI 味:

```text
Use $academic-de-ai-writing, mode=deep, style=argumentative, to audit and rewrite this manuscript for researcher texture, concrete evidence, citation hierarchy, specific limitations, and non-generic academic voice.
Paper path: <LaTeX source directory or PDF>
Constraints: do not invent experiments, citations, parameters, datasets, or claims.
```

Security Big Four venue routing:

```text
Use $security-top4-venue-fit to decide whether this paper fits IEEE S&P, USENIX Security, ACM CCS, or NDSS.
Paper path: <LaTeX source directory or PDF>
```

Top-four simulated review:

```text
Use $security-top4-review-simulator, mode=full, to produce a pre-submission review with major weaknesses and must-fix evidence gaps.
Paper path: <LaTeX source directory or PDF>
```

Venue-specific writing optimization:

```text
Use $security-writing-style, mode=deep, venue=NDSS, to revise my abstract, introduction, contribution bullets, evidence paragraphs, limitations, ethics, and artifact wording.
Paper path: <LaTeX source directory or PDF>
```

Broad routing across AAAI, KDD, and security venues:

```text
Use $cs-ai-conference-workflow to decide whether this work should target AAAI, KDD, CCS, NDSS, or USENIX Security.
Paper path: <LaTeX source directory or PDF>
```

## Included Skill Groups

AAAI:

- `aaai-conference-on-artificial-intelligence`
- `aaai-topic-selection`
- `aaai-writing-style`
- `aaai-experiments`
- `aaai-related-work`
- `aaai-submission`
- `aaai-review-process`
- `aaai-author-response`
- `aaai-camera-ready`
- `aaai-artifact-evaluation`
- `aaai-reproducibility`
- `aaai-supplementary`
- `aaai-workflow`
- `aaai-security-paper-review`

KDD:

- `acm-sigkdd-conference-on-knowledge-discovery-and-data-mining`

Security Big Four:

- `ieee-symposium-on-security-and-privacy`
- `usenix-security-symposium`
- `acm-conference-on-computer-and-communications-security`
- `network-and-distributed-system-security-symposium`

Security workflow skills:

- `security-top4-workflow`
- `security-top4-venue-fit`
- `security-top4-review-simulator`
- `security-topic-selection`
- `security-writing-style`
- `security-threat-model`
- `security-evidence-audit`
- `security-related-work`
- `security-submission-check`
- `security-ethics-disclosure`
- `security-artifact-package`
- `security-author-response`
- `security-camera-ready`

Routing and shared references:

- `cs-ai-conference-workflow`
- `shared-references`
- `academic-de-ai-writing`

Resources:

- `resources/conference-roster.md`: stable official-source anchors.
- `resources/official-source-map.md`: verification procedure for current CFPs and policies.
- `resources/aaai-security-corpus/`: non-PDF metadata for the 120-paper AAAI security, SOC, threat-analysis, and LLM-agent calibration corpus.

## Orchestration Skills

Orchestration skills do not replace venue-specific skills; they route the work and call out which specialized skill should be used next.

| Orchestrator | Purpose | Typical next skills |
|---|---|---|
| `cs-ai-conference-workflow` | Broad router for CS/AI conference selection, including AAAI, KDD, and security venues. | AAAI, KDD, and security Big Four venue skills |
| `aaai-workflow` | End-to-end AAAI project management from topic fit through submission, rebuttal, camera-ready, and artifact release. | `aaai-topic-selection`, `aaai-experiments`, `aaai-writing-style`, `aaai-submission`, `aaai-author-response` |
| `security-top4-workflow` | End-to-end orchestration for IEEE S&P, USENIX Security, ACM CCS, and NDSS, including one-shot full pre-submission audits. | Internal lanes for venue fit, threat model, evidence, writing, artifact, ethics, and submission checks |
| `security-top4-review-simulator` | Venue-calibrated simulated review panel plus full-audit wrapper for top-four security papers. | Internal lanes for PC review, threat model, evidence, artifact/ethics, and desk-reject risk |
| `aaai-security-paper-review` | AAAI-oriented review wrapper for security, SOC, threat-analysis, LLM-agent, and safety papers. | `aaai-conference-on-artificial-intelligence`, `aaai-experiments`, `aaai-writing-style` |
| `aaai-writing-style` | AAAI writing optimizer; `mode=deep, focus=security-llm-agent` uses corpus-backed abstract, introduction, contribution, evidence, limitations, ethics, and reproducibility patterns. | `aaai-conference-on-artificial-intelligence`, AAAI security corpus metadata |

Recommended entry points:

- If the venue is unknown, start with `cs-ai-conference-workflow`.
- If the venue is AAAI, start with `aaai-workflow`.
- If the venue is one of S&P, USENIX Security, CCS, or NDSS, start with `security-top4-workflow`.
- If the paper is already drafted and needs a hard pre-submission review, start with `security-top4-review-simulator` or `aaai-security-paper-review`.

## Recommended Workflows

### 1. Venue Routing

Use when you have an idea, abstract, or partial draft and need to choose a target venue.

```text
Use cs-ai-conference-workflow. My paper is about <topic>. It has <evidence>. Compare AAAI, KDD, S&P, USENIX Security, CCS, and NDSS.
```

Expected output:

- best-fit venue;
- two fallback venues;
- biggest mismatch risk;
- next single-venue skill to invoke;
- official CFP checks needed before submission.

### 2. AAAI Submission Planning

Use when AAAI is the likely target.

```text
Use aaai-workflow for this AAAI project. Current stage: experiments. Deadline: <date if known>. Paper topic: <topic>.
```

Then use specialized AAAI skills:

- `aaai-topic-selection` for fit and scope;
- `aaai-experiments` for evidence and ablation planning;
- `aaai-writing-style` for broad-AI readability;
- `aaai-related-work` for positioning;
- `aaai-submission` for final upload checks;
- `aaai-author-response` after reviews arrive.

### 3. KDD Venue Fit

Use when the paper is primarily data mining, discovery, graph mining, recommender systems, applied ML at scale, or benchmark/data-centric.

```text
Use acm-sigkdd-conference-on-knowledge-discovery-and-data-mining to evaluate KDD fit for this abstract.
```

The KDD skill focuses on data-mining contribution shape, baselines, datasets, deployment or discovery value, and whether the paper is too generic-ML or too systems/security-specific for KDD.

### 4. Security Big Four Paper Development

Use when targeting IEEE S&P, USENIX Security, ACM CCS, or NDSS.

```text
Use security-top4-workflow. My paper targets NDSS. Stage: writing. Topic family: APT/SOC and LLM-agent security.
```

The workflow routes through:

1. `security-topic-selection`
2. `security-top4-venue-fit`
3. `security-threat-model`
4. `security-evidence-audit`
5. `security-ethics-disclosure`
6. `security-artifact-package`
7. `security-writing-style`
8. `security-submission-check`

In `mode=full`, these are internal audit lanes. The user runs the wrapper once; the lane names are shown so the report is easy to navigate, not because each skill must be invoked manually.

### 5. Full Top-Four Security Audit

Use when a draft exists and you want a PC-style review plus the major pre-submission audit lanes in one run.

```text
Use security-top4-review-simulator, mode=full, to review this NDSS manuscript: <path-to-pdf-or-latex-source>
```

The full audit extracts a paper card and includes:

- R1 venue-fit/generalist reviewer;
- R2 threat-model/novelty reviewer;
- R3 evidence/adaptive-evaluation reviewer;
- R4 artifact/ethics/open-science reviewer;
- R5 topic specialist;
- devil's advocate rejection case;
- area-chair synthesis and revision roadmap.
- threat-model audit;
- claim-to-evidence audit;
- artifact/ethics/release audit;
- submission/desk-reject risk audit.

### 6. Drill-Down Audits And Rebuttal

Use these only after the full audit when you want deeper treatment of one lane:

```text
Use security-artifact-package to audit my artifact README and reproduction scripts.
```

```text
Use security-ethics-disclosure to check dual-use, human-subjects, responsible disclosure, and release boundaries.
```

```text
Use security-author-response to draft a rebuttal from these reviews.
```

## Optional Calibration Data

The security review simulator references summarized patterns extracted from a full-text calibration set of recent top-four security papers. The raw PDFs and extracted per-paper JSON/CSV files are not included in this repository.

If you publish or reuse such data, place it under:

```text
data/fulltext-calibration/
```

The skills remain usable without the optional calibration data because the summarized review patterns are included in the skill references.

## AAAI Security Corpus Metadata

`resources/aaai-security-corpus/` contains non-PDF metadata for 120 recent AAAI security, SOC, threat-analysis, and LLM-agent papers:

- seed corpus index,
- expansion manifest with official AAAI OJS URLs,
- candidate-title pool,
- full-text structure report.

PDFs and full extracted paper text are intentionally not included. Use the official OJS links in the manifest to download papers when local full-text inspection is needed.

To extend or rebuild the local-only full-text extraction, use `scripts/expand_aaai_security_corpus.py` with a private PDF directory. Keep PDFs and JSONL snippets outside git.

## Current Limits

- These are unofficial local skills, not official venue policies.
- The skills summarize venue culture and review heuristics; they cannot replace current CFP checks.
- Dates, page limits, AI-use policy, ethics policy, artifact policy, rebuttal rules, and camera-ready requirements can change every cycle.
- The security full-text calibration summary is included, but raw PDFs and per-paper extraction files are not bundled.
- Some workflow skills route to venue profiles that may not be present in this trimmed repository; when a referenced skill is absent, use the closest included venue skill or install the broader conference pack.
- `cs-ai-conference-workflow` can optionally use broader conference-pack examples under `resources/worked-examples/` and `resources/exemplars/`; those files are not required for the AAAI/KDD/security workflows included here.

## Contributing

- Use feature branches for parallel agents or collaborators.
- Pull and rebase before editing if another agent may be pushing to the same repository.
- Do not force-push shared branches.
- Do not commit PDFs, compiled LaTeX artifacts, `__pycache__`, or private submission packages.
- Keep `SKILL.md` concise and move detailed calibration material to `references/` or `resources/`.
- Run the skill validator before opening a PR:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\skills\<skill-name>
```

## Notes

These skills are unofficial helper prompts and checklists. Always verify current venue CFPs, page limits, anonymity rules, artifact policies, and ethics/disclosure requirements before submission.

## License

MIT. See `LICENSE`.

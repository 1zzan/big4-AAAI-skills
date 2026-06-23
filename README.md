# Big4 AAAI Skills

Codex skills for paper planning, venue-fit checks, writing, review simulation, submission checks, and artifact preparation for:

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

## Install

Copy the desired skill directories into your Codex skills directory.

Installer script:

```powershell
.\scripts\install.ps1
```

Install to a custom directory:

```powershell
.\scripts\install.ps1 -Destination "D:\path\to\.codex\skills"
```

PowerShell:

```powershell
$target = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force -Path $target | Out-Null
Copy-Item -Recurse -Force .\skills\* $target
```

Bash:

```bash
mkdir -p "$HOME/.codex/skills"
cp -R skills/* "$HOME/.codex/skills/"
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

## How To Use

In Codex, invoke a skill by naming it or by asking for the task it covers.

Examples:

```text
Use security-top4-review-simulator to review my NDSS draft: <path-to-paper-source>
```

```text
Use security-top4-workflow to plan a USENIX Security submission from idea to artifact release.
```

```text
Use aaai-security-paper-review to review this AAAI paper about LLM-agent security.
```

```text
Use cs-ai-conference-workflow to decide whether this work should target AAAI, KDD, CCS, NDSS, or USENIX Security.
```

```text
Use aaai-workflow to build a submission checklist and timeline for my AAAI paper.
```

You can also ask naturally:

```text
I have a SOC/LLM-security paper. Which top-four security venue fits best, and what is the fastest path to a stronger submission?
```

Codex should route that through the relevant workflow and venue-fit skills.

## Orchestration Skills

Yes, this pack includes orchestration skills. They do not replace the venue-specific skills; they route the work and call out which specialized skill should be used next.

| Orchestrator | Purpose | Typical next skills |
|---|---|---|
| `cs-ai-conference-workflow` | Broad router for CS/AI conference selection, including AAAI, KDD, and security venues. | `aaai-conference-on-artificial-intelligence`, `acm-sigkdd-conference-on-knowledge-discovery-and-data-mining`, security Big Four venue skills |
| `aaai-workflow` | End-to-end AAAI project management from topic fit through submission, rebuttal, camera-ready, and artifact release. | `aaai-topic-selection`, `aaai-experiments`, `aaai-writing-style`, `aaai-submission`, `aaai-author-response` |
| `security-top4-workflow` | End-to-end orchestration for IEEE S&P, USENIX Security, ACM CCS, and NDSS. | `security-topic-selection`, `security-top4-venue-fit`, `security-threat-model`, `security-evidence-audit`, `security-submission-check` |
| `security-top4-review-simulator` | Venue-calibrated simulated review panel for top-four security papers. | `security-evidence-audit`, `security-ethics-disclosure`, `security-artifact-package`, `security-author-response` |
| `aaai-security-paper-review` | AAAI-oriented review wrapper for security, SOC, threat-analysis, LLM-agent, and safety papers. | `aaai-conference-on-artificial-intelligence`, `aaai-experiments`, `aaai-writing-style` |

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

### 5. Simulated Top-Four Security Review

Use when a draft exists and you want a PC-style review before submission.

```text
Use security-top4-review-simulator to review this NDSS manuscript: <path-to-pdf-or-latex-source>
```

The simulator extracts a paper card and simulates:

- R1 venue-fit/generalist reviewer;
- R2 threat-model/novelty reviewer;
- R3 evidence/adaptive-evaluation reviewer;
- R4 artifact/ethics/open-science reviewer;
- R5 topic specialist;
- devil's advocate rejection case;
- area-chair synthesis and revision roadmap.

### 6. Artifact, Ethics, and Rebuttal

Use these once the paper has a concrete target and evidence package:

```text
Use security-artifact-package to audit my artifact README and reproduction scripts.
```

```text
Use security-ethics-disclosure to check dual-use, human-subjects, responsible disclosure, and release boundaries.
```

```text
Use security-author-response to draft a rebuttal from these reviews.
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

Resources:

- `resources/conference-roster.md`: stable official-source anchors.
- `resources/official-source-map.md`: verification procedure for current CFPs and policies.
- `resources/aaai-security-corpus/`: non-PDF metadata for AAAI security, SOC, threat-analysis, and LLM-agent calibration.

## Optional Calibration Data

The security review simulator references summarized patterns extracted from a full-text calibration set of recent top-four security papers. The raw PDFs and extracted per-paper JSON/CSV files are not included in this repository.

If you publish or reuse such data, place it under:

```text
data/fulltext-calibration/
```

The skills remain usable without the optional calibration data because the summarized review patterns are included in the skill references.

## Current Limits

- These are unofficial local skills, not official venue policies.
- The skills intentionally summarize venue culture and review heuristics; they cannot replace current CFP checks.
- Dates, page limits, AI-use policy, ethics policy, artifact policy, rebuttal rules, and camera-ready requirements can change every cycle.
- The security full-text calibration summary is included, but raw PDFs and per-paper extraction files are not bundled.
- Some workflow skills route to venue profiles that may not be present in this trimmed repository; when a referenced skill is absent, use the closest included venue skill or install the broader conference pack.
- `cs-ai-conference-workflow` can optionally use broader conference-pack examples under `resources/worked-examples/` and `resources/exemplars/`; those files are not required for the AAAI/KDD/security workflows included here.

## Notes

These skills are unofficial helper prompts and checklists. Always verify current venue CFPs, page limits, anonymity rules, artifact policies, and ethics/disclosure requirements before submission.

## License

MIT. See `LICENSE`.

# Big4 AAAI Skills

Codex skills for paper planning, venue-fit checks, writing, review simulation, submission checks, and artifact preparation for:

- AAAI
- KDD
- IEEE S&P
- USENIX Security
- ACM CCS
- NDSS

The repository also includes shared security-review skills for threat models, evidence audits, related work, ethics/disclosure, top-four venue fit, top-four workflow planning, and review simulation.

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
```

## Install

Copy the desired skill directories into your Codex skills directory.

Installer script:

```powershell
.\scripts\install.ps1
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

Shared references:

- `cs-ai-conference-workflow`
- `shared-references`

## Optional Calibration Data

The security review simulator references summarized patterns extracted from a full-text calibration set of recent top-four security papers. The raw PDFs and extracted per-paper JSON/CSV files are not included in this repository.

If you publish or reuse such data, place it under:

```text
data/fulltext-calibration/
```

The skills remain usable without the optional calibration data because the summarized review patterns are included in the skill references.

## Notes

These skills are unofficial helper prompts and checklists. Always verify current venue CFPs, page limits, anonymity rules, artifact policies, and ethics/disclosure requirements before submission.

## License

MIT. See `LICENSE`.

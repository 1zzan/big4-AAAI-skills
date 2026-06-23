param(
    [string]$CodexHome = $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { "$env:USERPROFILE\.codex" })
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$Skills = Join-Path $RepoRoot "skills"
$Resources = Join-Path $RepoRoot "resources"
$SkillsDestination = Join-Path $CodexHome "skills"
$ResourcesDestination = Join-Path $CodexHome "resources"

if (-not (Test-Path -LiteralPath $Skills)) {
    throw "Cannot find skills directory: $Skills"
}

New-Item -ItemType Directory -Force -Path $SkillsDestination | Out-Null
Copy-Item -Path (Join-Path $Skills "*") -Destination $SkillsDestination -Recurse -Force

if (Test-Path -LiteralPath $Resources) {
    New-Item -ItemType Directory -Force -Path $ResourcesDestination | Out-Null
    Copy-Item -Path (Join-Path $Resources "*") -Destination $ResourcesDestination -Recurse -Force
}

Write-Output "Installed skills to $SkillsDestination"
Write-Output "Installed resources to $ResourcesDestination"
Write-Output "Restart Codex or start a new chat to refresh the skill list."

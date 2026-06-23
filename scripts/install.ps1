param(
    [string]$Destination = "$env:USERPROFILE\.codex\skills"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$Skills = Join-Path $RepoRoot "skills"

if (-not (Test-Path -LiteralPath $Skills)) {
    throw "Cannot find skills directory: $Skills"
}

New-Item -ItemType Directory -Force -Path $Destination | Out-Null
Copy-Item -Path (Join-Path $Skills "*") -Destination $Destination -Recurse -Force

Write-Output "Installed skills to $Destination"
Write-Output "Restart Codex or start a new chat to refresh the skill list."


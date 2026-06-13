$ErrorActionPreference = "Stop"
$Source = Join-Path $PSScriptRoot "skills"
$Target = Join-Path $env:USERPROFILE ".claude\skills"

if (!(Test-Path $Source)) {
  Write-Host "No encuentro la carpeta skills." -ForegroundColor Red
  exit 1
}

New-Item -ItemType Directory -Force -Path $Target | Out-Null
Copy-Item -Path (Join-Path $Source "*") -Destination $Target -Recurse -Force

Write-Host "Skills instaladas en: $Target" -ForegroundColor Green
Write-Host "Abre Claude Code y prueba: /github-app-auditor" -ForegroundColor Cyan

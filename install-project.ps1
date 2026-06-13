$ErrorActionPreference = "Stop"
$Source = Join-Path $PSScriptRoot "skills"
$Target = Join-Path (Get-Location) ".claude\skills"

if (!(Test-Path $Source)) {
  Write-Host "No encuentro la carpeta skills." -ForegroundColor Red
  exit 1
}

New-Item -ItemType Directory -Force -Path $Target | Out-Null
Copy-Item -Path (Join-Path $Source "*") -Destination $Target -Recurse -Force

Write-Host "Skills instaladas en este proyecto: $Target" -ForegroundColor Green
Write-Host "Abre Claude Code en este repo y prueba: /codebase-context-loader" -ForegroundColor Cyan

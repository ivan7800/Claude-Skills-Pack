#!/usr/bin/env bash
set -euo pipefail
SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills"
TARGET="$HOME/.claude/skills"

if [ ! -d "$SOURCE" ]; then
  echo "No encuentro la carpeta skills."
  exit 1
fi

mkdir -p "$TARGET"
cp -R "$SOURCE"/* "$TARGET"/

echo "Skills instaladas en: $TARGET"
echo "Abre Claude Code y prueba: /github-app-auditor"

#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MANIFEST = ROOT / "skills-manifest.json"
VERSION = ROOT / "VERSION"

errors = []

if not SKILLS.exists():
    errors.append("Missing skills/ directory")

manifest = None
if not MANIFEST.exists():
    errors.append("Missing skills-manifest.json")
else:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Invalid skills-manifest.json: {exc}")

if not VERSION.exists():
    errors.append("Missing VERSION")
elif manifest and manifest.get("version") != VERSION.read_text(encoding="utf-8").strip():
    errors.append("VERSION does not match skills-manifest.json")

skill_dirs = sorted([p for p in SKILLS.iterdir() if p.is_dir()]) if SKILLS.exists() else []
if not skill_dirs:
    errors.append("No skill directories found")

manifest_skills = set(manifest.get("skills", [])) if manifest else set()
actual_skills = {p.name for p in skill_dirs}

missing_in_manifest = actual_skills - manifest_skills
missing_on_disk = manifest_skills - actual_skills
if missing_in_manifest:
    errors.append("Skills missing from manifest: " + ", ".join(sorted(missing_in_manifest)))
if missing_on_disk:
    errors.append("Manifest lists missing skills: " + ", ".join(sorted(missing_on_disk)))

for skill in skill_dirs:
    skill_file = skill / "SKILL.md"
    if not skill_file.exists():
        errors.append(f"{skill.name}: missing SKILL.md")
        continue
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append(f"{skill.name}: missing YAML frontmatter")
        continue
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        errors.append(f"{skill.name}: malformed YAML frontmatter")
        continue
    frontmatter = match.group(1)
    body = text[match.end():].strip()
    if "description:" not in frontmatter:
        errors.append(f"{skill.name}: missing description")
    if len(body) < 100:
        errors.append(f"{skill.name}: instructions too short")
    if len(text.splitlines()) > 500:
        errors.append(f"{skill.name}: SKILL.md should stay under 500 lines")

required_repo_files = ["README.md", "LICENSE", "CHANGELOG.md", "SECURITY.md", "CONTRIBUTING.md", ".gitignore", ".github/workflows/validate.yml"]
for rel in required_repo_files:
    if not (ROOT / rel).exists():
        errors.append(f"Missing repository file: {rel}")

if errors:
    print("ERROR: pack validation failed")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(f"OK: {len(skill_dirs)} skills validated. Repository metadata present. Version {VERSION.read_text(encoding='utf-8').strip()}.")

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

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

if not SKILLS.exists():
    errors.append("Missing skills/ directory")

manifest = None
if not MANIFEST.exists():
    errors.append("Missing skills-manifest.json")
else:
    try:
        manifest = json.loads(read_text(MANIFEST))
    except Exception as exc:
        errors.append(f"Invalid skills-manifest.json: {exc}")

version = None
if not VERSION.exists():
    errors.append("Missing VERSION")
else:
    version = read_text(VERSION).strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION must use semantic versioning, for example 1.3.4")
    if manifest and manifest.get("version") != version:
        errors.append("VERSION does not match skills-manifest.json")

skill_dirs = sorted([p for p in SKILLS.iterdir() if p.is_dir()]) if SKILLS.exists() else []
if not skill_dirs:
    errors.append("No skill directories found")

manifest_list = manifest.get("skills", []) if manifest else []
manifest_skills = set(manifest_list)
actual_skills = {p.name for p in skill_dirs}

if len(manifest_list) != len(manifest_skills):
    errors.append("skills-manifest.json contains duplicate skill slugs")

missing_in_manifest = actual_skills - manifest_skills
missing_on_disk = manifest_skills - actual_skills
if missing_in_manifest:
    errors.append("Skills missing from manifest: " + ", ".join(sorted(missing_in_manifest)))
if missing_on_disk:
    errors.append("Manifest lists missing skills: " + ", ".join(sorted(missing_on_disk)))

for skill in skill_dirs:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill.name):
        errors.append(f"{skill.name}: slug should be lowercase kebab-case")
    skill_file = skill / "SKILL.md"
    if not skill_file.exists():
        errors.append(f"{skill.name}: missing SKILL.md")
        continue
    text = read_text(skill_file)
    if not text.startswith("---"):
        errors.append(f"{skill.name}: missing YAML frontmatter")
        continue
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        errors.append(f"{skill.name}: malformed YAML frontmatter")
        continue
    frontmatter = match.group(1)
    body = text[match.end():].strip()
    if "name:" not in frontmatter:
        errors.append(f"{skill.name}: missing name")
    if "description:" not in frontmatter:
        errors.append(f"{skill.name}: missing description")
    if "when_to_use:" not in frontmatter:
        errors.append(f"{skill.name}: missing when_to_use")
    if "$ARGUMENTS" not in body:
        errors.append(f"{skill.name}: missing $ARGUMENTS handoff in body")
    if len(body) < 100:
        errors.append(f"{skill.name}: instructions too short")
    if len(text.splitlines()) > 500:
        errors.append(f"{skill.name}: SKILL.md should stay under 500 lines")

required_repo_files = [
    "README.md", "LICENSE", "CHANGELOG.md", "SECURITY.md", "CONTRIBUTING.md",
    ".gitignore", ".github/workflows/validate.yml", "docs/INSTALLATION.md", "docs/USAGE.md",
    "docs/IPHONE-SAFARI-QA.md", "docs/BROWSER-LIMITS.md", "package.json", "playwright.config.js",
    "tests/e2e/app.spec.js", "scripts/smoke-test-chromium.mjs"
]
for rel in required_repo_files:
    if not (ROOT / rel).exists():
        errors.append(f"Missing repository file: {rel}")

# Web/release version consistency checks
versioned_files = ["README.md", "CHANGELOG.md", "index.html", "sw.js", "package.json", "playwright.config.js"]
if version:
    for rel in versioned_files:
        path = ROOT / rel
        if path.exists() and version not in read_text(path):
            errors.append(f"{rel} does not mention current VERSION {version}")

# Playwright tests should contain at least one mobile profile reference.
config_path = ROOT / "playwright.config.js"
if config_path.exists():
    config_text = read_text(config_path)
    if "iPhone" not in config_text or "Pixel" not in config_text:
        errors.append("playwright.config.js should include mobile viewport projects")

# Smoke test must stay dependency-free; it should not import Playwright/Puppeteer.
smoke_path = ROOT / "scripts/smoke-test-chromium.mjs"
if smoke_path.exists():
    smoke_text = read_text(smoke_path)
    if "playwright" in smoke_text.lower() or "puppeteer" in smoke_text.lower():
        errors.append("smoke-test-chromium.mjs should remain dependency-free")

if errors:
    print("ERROR: pack validation failed")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(f"OK: {len(skill_dirs)} skills validated. Repository metadata present. Version {version}.")

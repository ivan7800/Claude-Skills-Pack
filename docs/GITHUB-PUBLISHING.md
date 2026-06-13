# Publishing to GitHub

## First publish

```bash
git init
git add .
git commit -m "Initial release: I. Roig Claude Skills Pack v1.3.1"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/i-roig-claude-skills-pack.git
git push -u origin main
```

## Create a release

```bash
git tag v1.3.1
git push origin v1.3.1
```

Then create a GitHub Release from the tag and attach the ZIP if desired.

## Recommended repository settings

- Description: `Claude Code Skills pack for app auditing, debugging, PWA, security, releases, prompts, local-first apps and fiction editing.`
- Topics: `claude-code`, `skills`, `ai-tools`, `prompts`, `github-pages`, `pwa`, `debugging`, `frontend`, `writing`, `ollama`
- License: MIT

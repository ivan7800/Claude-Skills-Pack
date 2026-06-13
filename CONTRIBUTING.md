# Contributing

Contributions are welcome if they improve clarity, reliability or practical usefulness.

## Rules

1. Keep each Skill focused on a real workflow.
2. Keep `SKILL.md` concise. Move long references to supporting files.
3. Use clear Spanish by default.
4. Do not add secrets, private files, telemetry or vendor lock-in.
5. Run the validator before opening a pull request:

```bash
python scripts/validate-skills-pack.py
```

## Pull request checklist

- [ ] The Skill has a valid `SKILL.md`.
- [ ] Frontmatter includes a useful `description`.
- [ ] Instructions are actionable, not vague.
- [ ] README/docs are updated if needed.
- [ ] No private data or generated archives are committed.

# Installation

## Personal installation

Personal Skills are available in all Claude Code projects.

### Windows

```powershell
.\install-windows.ps1
```

### macOS / Linux

```bash
chmod +x install-macos-linux.sh
./install-macos-linux.sh
```

## Project-only installation

Use this when you want the Skills copied into one repository only.

### Windows

```powershell
.\install-project.ps1
```

### macOS / Linux

```bash
chmod +x install-project.sh
./install-project.sh
```

The destination is:

```text
.claude/skills/
```

## Verify installation

Open Claude Code in a project and run:

```text
/github-app-auditor revisa este repositorio
```

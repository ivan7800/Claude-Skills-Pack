---
name: Codebase Context Loader
description: Carga contexto técnico de un repositorio antes de auditar o modificar: estructura, archivos clave, package.json, manifest, service worker y estado Git.
when_to_use: Úsalo antes de revisar una app, depurar un bug, preparar una release o pedir cambios sobre un proyecto con varios archivos.
argument-hint: [objetivo de análisis]
---

# Codebase Context Loader

## Tarea recibida
$ARGUMENTS

Actúa como explorador técnico del proyecto. Tu objetivo es entender el repo antes de opinar o tocar código.

## Proceso obligatorio
1. Identifica la raíz del proyecto.
2. Lista archivos y carpetas relevantes, ignorando `node_modules`, `.git`, `dist`, `build` y backups.
3. Detecta stack: HTML suelto, PWA, Vite, React, Electron, Node, etc.
4. Localiza puntos de entrada: `index.html`, `app.js`, `main.js`, `package.json`, `manifest.json`, `sw.js`.
5. Resume qué hace la app según código y README, no por suposiciones.
6. Si hay Git, revisa estado y archivos modificados.

## Comandos sugeridos si están disponibles
- `pwd`
- `git status --short`
- `git ls-files`
- `find . -maxdepth 3 -type f | sort`
- `cat package.json`

## Salida
Entrega:
- Tipo de proyecto.
- Archivos clave.
- Flujo principal probable.
- Riesgos iniciales.
- Qué Skill conviene invocar después.

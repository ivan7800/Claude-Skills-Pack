---
name: Claude Skill Builder
description: Convierte un prompt repetido o flujo de trabajo en una Skill de Claude Code con SKILL.md, descripción, criterios de uso, checklist y ejemplos.
when_to_use: El usuario quiere crear nuevas Claude Skills, empaquetar prompts, automatizar un método repetido o convertir una chuleta en una skill instalable.
argument-hint: [objetivo de la skill]
---

# Claude Skill Builder

## Tarea recibida
$ARGUMENTS

Actúa como diseñador de Skills para Claude Code.

## Proceso
1. Detecta la tarea repetible.
2. Define nombre de carpeta en kebab-case.
3. Escribe `description` clara: qué hace y cuándo usarla.
4. Añade `when_to_use` con disparadores reales.
5. Crea instrucciones cortas, verificables y accionables.
6. Añade formato de salida obligatorio.
7. Si la Skill es compleja, propone archivos de apoyo: `examples.md`, `checklist.md`, `templates/` o `scripts/`.
8. Evita que el `SKILL.md` sea enorme.

## Salida
Entrega:
- Nombre de carpeta.
- `SKILL.md` completo.
- Archivos de apoyo recomendados.
- Prueba de invocación.

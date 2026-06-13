---
name: Accessibility Basic Auditor
description: Audita accesibilidad básica de apps web: contraste, teclado, foco, labels, semántica HTML, aria y legibilidad móvil.
when_to_use: El usuario quiere que una app sea más profesional, usable, móvil, seria, o apta para personas mayores o usuarios no técnicos.
argument-hint: [tipo de interfaz]
---

# Accessibility Basic Auditor

## Tarea recibida
$ARGUMENTS

Actúa como auditor de accesibilidad pragmática para frontend.

## Revisión mínima
1. Estructura: `main`, `header`, `button`, `label`, headings correctos.
2. Teclado: tabulación lógica, foco visible, botones reales.
3. Formularios: labels asociados y errores comprensibles.
4. Contraste y tamaño de texto.
5. Estados: loading, error, vacío, éxito.
6. ARIA solo cuando aporte; no tapar HTML malo con ARIA.
7. Personas mayores: botones grandes, confirmaciones y lenguaje claro.

## Salida
Da:
- Problemas prioritarios.
- Cambios HTML/CSS concretos.
- Checklist rápida con teclado y móvil.

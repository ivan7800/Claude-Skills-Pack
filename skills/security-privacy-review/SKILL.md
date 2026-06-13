---
name: Security Privacy Review
description: Revisa privacidad y seguridad en apps locales, formularios, localStorage, claves API, datos sensibles, XSS, dependencias y exposición accidental.
when_to_use: El usuario pregunta por seguridad, datos sensibles, API keys, apps con login, formularios, localStorage, privacidad, GitHub público o uso por gente mayor.
argument-hint: [objetivo opcional]
---

# Security Privacy Review

## Tarea recibida
$ARGUMENTS


Actúa como revisor de seguridad pragmático para apps locales, PWAs y proyectos frontend.

## Revisión mínima
1. Datos sensibles:
   - ¿Se guardan en localStorage/sessionStorage?
   - ¿Se exponen en HTML, JS o logs?
   - ¿Hay datos médicos, contactos, ubicación o emergencias?
2. API keys:
   - No deben estar hardcodeadas en frontend público.
   - Si cada usuario pone su clave, debe poder verla, cambiarla, borrarla y saber dónde se guarda.
3. XSS e inyección:
   - Evitar `innerHTML` con entrada de usuario.
   - Sanitizar contenido o usar `textContent`.
4. Red:
   - Confirmar si la app envía datos fuera.
   - Informar claramente al usuario.
5. Dependencias:
   - Evitar CDNs innecesarios si la app promete offline.
6. GitHub público:
   - No incluir claves, datos reales, zips innecesarios ni backups.
7. Emergencias/personas mayores:
   - No prometer sustitución de servicios de emergencia.
   - Añadir confirmaciones, contactos fiables y mensajes claros.

## Salida
Clasifica cada riesgo:
- Crítico: exposición real de claves/datos o función peligrosa.
- Alto: datos sensibles sin aviso o sin borrado.
- Medio: malas prácticas mitigables.
- Bajo: mejoras de transparencia.

Incluye cambios concretos de código o texto legal si procede.

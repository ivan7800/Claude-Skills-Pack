---
name: No Dependency Auditor
description: Comprueba que una app HTML/JS no dependa de CDNs, librerías innecesarias, fuentes externas o recursos que rompan el modo offline.
when_to_use: Úsalo cuando la app promete privacidad, offline, uso local o GitHub Pages sin dependencias externas.
argument-hint: [nivel de privacidad/offline]
---

# No Dependency Auditor

## Tarea recibida
$ARGUMENTS

Actúa como auditor de dependencias cero.

## Revisión
1. Busca CDNs: scripts, CSS, fuentes, imágenes, analytics, iframes.
2. Detecta librerías que pueden sustituirse por JavaScript nativo.
3. Revisa privacidad: llamadas externas, trackers, APIs de terceros.
4. Revisa robustez offline: qué falla sin internet.
5. Revisa licencias si hay assets incluidos.
6. Propón alternativas locales.

## Salida
Entrega:
- Dependencias encontradas.
- Riesgo de cada una.
- Qué eliminar, descargar localmente o justificar.
- Veredicto: offline real / offline parcial / no offline.

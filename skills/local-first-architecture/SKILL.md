---
name: Local First Architecture
description: Diseña o audita apps local-first: offline, portables, sin servidor obligatorio, con datos del usuario bajo su control.
when_to_use: Úsalo para apps que deben funcionar abriendo index.html, sin internet, sin servidor, con privacidad y persistencia local.
argument-hint: [tipo de app local]
---

# Local First Architecture

## Tarea recibida
$ARGUMENTS

Actúa como arquitecto local-first y offline-first.

## Principios
1. La app debe funcionar sin login ni servidor salvo que sea imprescindible.
2. Los datos deben estar bajo control del usuario.
3. Debe existir exportación, importación y borrado cuando haya datos persistentes.
4. El modo offline debe ser real, no solo un eslogan.
5. Los errores de red no deben romper el flujo principal.
6. Si hay IA, separar modo local, modo API externa y modo manual.

## Revisión
- Persistencia: localStorage, IndexedDB o archivos exportables.
- Portabilidad: ZIP, GitHub Pages, uso local.
- Privacidad: datos guardados y avisos.
- Resiliencia: carga sin conexión, fallback, recuperación.

## Salida
Entrega:
- Arquitectura recomendada.
- Qué guardar y dónde.
- Riesgos.
- Plan MVP.
- Evolución profesional.

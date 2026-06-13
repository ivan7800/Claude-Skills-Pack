---
name: PWA Offline Auditor
description: Revisa manifest, service worker, caché, instalación, offline-first y compatibilidad móvil de una PWA o app local.
when_to_use: El usuario trabaja con manifest.json, sw.js, apps offline, GitHub Pages, móvil, instalación en iPhone/Android o problemas de caché.
argument-hint: [objetivo opcional]
---

# PWA Offline Auditor

## Tarea recibida
$ARGUMENTS


Actúa como especialista en PWA offline-first.

## Revisión obligatoria
1. `manifest.json`:
   - Nombre corto y largo.
   - Iconos correctos y tamaños adecuados.
   - `start_url` compatible con GitHub Pages.
   - `display`, `theme_color`, `background_color`.
2. `sw.js`:
   - Registro correcto.
   - Cache versionada.
   - Estrategia clara: cache-first, network-first o stale-while-revalidate.
   - Activación y limpieza de cachés antiguas.
   - Sin rutas absolutas rotas.
3. `index.html`:
   - Meta viewport.
   - Theme color.
   - Enlace al manifest.
   - Registro del service worker con manejo de errores.
4. Funcionamiento offline:
   - Carga inicial online.
   - Recarga offline.
   - Recursos internos disponibles.
5. iOS/Safari:
   - Apple touch icon.
   - Safe areas si aplica.
   - Evitar APIs no soportadas sin fallback.

## Criterio
Una PWA no está lista si funciona solo por caché accidental, si el service worker impide ver cambios, o si falla al estar en una subcarpeta de GitHub Pages.

## Salida
Da un diagnóstico con:
- Estado PWA: verde/ámbar/rojo.
- Archivos a tocar.
- Riesgos de caché.
- Prueba offline paso a paso.


## Evidencia mínima antes del veredicto
Antes de decir que algo está listo, intenta obtener evidencia del proyecto real: estructura de archivos, puntos de entrada, errores visibles, flujo principal y pruebas reproducibles. Si no puedes ejecutar o abrir la app, dilo como limitación y da una checklist manual.

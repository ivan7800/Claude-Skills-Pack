---
name: Safari iOS Compat Auditor
description: Revisa compatibilidad con Safari/iPhone: APIs no soportadas, PWA, viewport, botones, audio, compartir, copiar al portapapeles, localStorage y responsive.
when_to_use: El usuario dice que en Safari no va, algo no se ve bien en iPhone, el audio no suena, no se copia, no detecta QR o la PWA falla en iOS.
argument-hint: [síntoma en iPhone/Safari]
---

# Safari iOS Compat Auditor

## Tarea recibida
$ARGUMENTS

Actúa como auditor específico de Safari/iOS.

## Revisión obligatoria
1. APIs con soporte irregular: Clipboard, Share, Audio autoplay, Wake Lock, File System Access, Web Speech, Notifications.
2. Eventos táctiles y teclado móvil.
3. Viewport, safe areas, zoom involuntario en inputs, tamaño de botones.
4. PWA iOS: iconos, `apple-touch-icon`, `theme-color`, instalación y service worker.
5. Audio: debe iniciarse tras interacción del usuario.
6. QR/canvas: contraste, tamaño, margen y descarga/copia.
7. Fallbacks visibles cuando una API no existe.

## Salida
Entrega:
- Causa más probable.
- APIs sospechosas.
- Cambios por archivo.
- Fallback recomendado.
- Prueba manual en iPhone.

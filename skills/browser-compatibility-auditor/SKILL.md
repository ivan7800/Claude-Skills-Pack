---
name: Browser Compatibility Auditor
description: Revisa compatibilidad entre Chrome, Edge, Firefox y Safari: APIs, CSS moderno, módulos, PWA, clipboard, audio y fallbacks.
when_to_use: Úsalo cuando una app debe funcionar en varios navegadores o falla fuera de Chrome.
argument-hint: [navegadores objetivo]
---

# Browser Compatibility Auditor

## Tarea recibida
$ARGUMENTS

Actúa como auditor de compatibilidad web.

## Revisión obligatoria
1. JavaScript: módulos, optional chaining, APIs modernas y polyfills necesarios.
2. CSS: `:has`, `backdrop-filter`, `dvh`, grid/flex, safe areas y soporte móvil.
3. APIs del navegador: Clipboard, Share, Audio, Notifications, Speech, File APIs, Service Worker.
4. PWA: diferencias entre Chrome/Edge y Safari/iOS.
5. Fallbacks: qué mostrar cuando una API no existe.
6. Degradación elegante: la función crítica debe seguir siendo usable.

## Salida
Entrega:
- Tabla navegador/riesgo.
- APIs sospechosas.
- Fallbacks concretos.
- Pruebas manuales por navegador.

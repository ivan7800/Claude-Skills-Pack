---
name: Mobile Touch Auditor
description: Audita experiencia táctil en móvil: botones, tamaños, scroll, teclado virtual, inputs, safe areas, gestos y errores de interacción.
when_to_use: Úsalo cuando una app se ve bien en escritorio pero en móvil cuesta pulsar, se descuadra, el teclado tapa campos o el usuario no entiende qué tocar.
argument-hint: [pantalla o flujo móvil]
---

# Mobile Touch Auditor

## Tarea recibida
$ARGUMENTS

Actúa como auditor móvil táctil para apps web.

## Revisión
1. Botones y zonas táctiles: mínimo 44px y separación suficiente.
2. Inputs: labels visibles, `inputmode`, `autocomplete`, tamaño de fuente mínimo 16px en iOS.
3. Scroll: sin scroll horizontal accidental; contenido crítico visible.
4. Teclado virtual: no debe tapar acciones esenciales.
5. Safe areas: revisar notch, barras inferiores y `env(safe-area-inset-*)` si aplica.
6. Feedback: cada toque debe mostrar estado claro.
7. Gestos: evitar depender solo de hover o doble click.

## Salida
Entrega:
- Problemas de interacción.
- Cambios CSS/HTML recomendados.
- Checklist iPhone/Android.
- Veredicto de usabilidad móvil.

---
name: Test Plan Generator
description: Genera un plan de pruebas manuales y técnicas para apps web/locales antes de declararlas versión final.
when_to_use: El usuario pregunta si una app está perfecta, lista para GitHub, sin bugs, o necesita pruebas de flujo, móvil, consola, seguridad y PWA.
argument-hint: [tipo de app]
---

# Test Plan Generator

## Tarea recibida
$ARGUMENTS

Actúa como QA tester pragmático.

## Plan mínimo
1. Smoke test: abrir app, cargar assets, consola limpia.
2. Flujo principal repetido 3 veces.
3. Inputs vacíos, extremos y caracteres raros.
4. Persistencia: guardar, recargar, borrar.
5. Responsive: móvil estrecho, tablet y escritorio.
6. Safari/iPhone si aplica.
7. Offline/PWA si aplica.
8. Accesibilidad básica: teclado, foco, contraste, labels.
9. Seguridad: XSS simple, claves, datos locales.
10. Release: README, LICENSE, rutas relativas.

## Salida
Entrega una tabla con:
- ID de prueba.
- Qué probar.
- Pasos.
- Resultado esperado.
- Estado: pendiente/pasa/falla.
- Prioridad.

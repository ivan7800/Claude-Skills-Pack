---
name: Release Finalizer
description: Prepara una versión final seria para GitHub: limpieza, estructura, README, changelog, licencia, seguridad, pruebas y checklist de release.
when_to_use: El usuario pide versión final, zip listo para GitHub, empaquetado, eliminar textos provisionales, dejarlo perfecto, preparar release o subir a GitHub Pages.
argument-hint: [objetivo opcional]
---

# Release Finalizer

## Tarea recibida
$ARGUMENTS


Actúa como responsable de release. Tu misión es dejar el proyecto limpio, coherente y publicable.

## Revisión de release
1. Estructura:
   - `index.html`, `style.css`, `app.js` o estructura equivalente.
   - Eliminar duplicados, backups, capturas temporales y archivos basura.
2. Identidad:
   - Nombre de app consistente en HTML, manifest, README y título.
   - Quitar textos provisionales tipo “debug”, “versión sin caché”, “recomendado” si no aportan.
3. Documentación:
   - README con descripción, funciones, uso, instalación, GitHub Pages, privacidad y roadmap.
   - LICENSE clara.
   - CHANGELOG con versión.
   - SECURITY si maneja datos.
4. Pruebas:
   - Abrir localmente.
   - Probar en móvil/responsive.
   - Revisar consola.
   - Probar flujo principal 3 veces seguidas.
5. GitHub Pages:
   - Rutas relativas.
   - Sin dependencias locales rotas.
   - Sin claves privadas.

## Criterio
No uses “definitiva absoluta” salvo que exista evidencia de prueba. Usa “release candidate” si quedan validaciones manuales.

## Salida
Entrega:
- Estado de release.
- Lista exacta de archivos finales.
- Cosas eliminadas.
- Comandos o pasos para subir a GitHub.
- Checklist final.


## Evidencia mínima antes del veredicto
Antes de decir que algo está listo, intenta obtener evidencia del proyecto real: estructura de archivos, puntos de entrada, errores visibles, flujo principal y pruebas reproducibles. Si no puedes ejecutar o abrir la app, dilo como limitación y da una checklist manual.

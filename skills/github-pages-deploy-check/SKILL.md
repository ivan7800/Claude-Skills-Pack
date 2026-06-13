---
name: GitHub Pages Deploy Check
description: Comprueba si un proyecto web está preparado para publicarse en GitHub Pages: rutas relativas, assets, manifest, service worker, base path y README.
when_to_use: El usuario quiere subir una app a GitHub Pages, dice que en local funciona pero en GitHub no, o pide preparar un zip final publicable.
argument-hint: [nombre repo opcional]
---

# GitHub Pages Deploy Check

## Tarea recibida
$ARGUMENTS

Actúa como auditor de despliegue GitHub Pages.

## Revisión obligatoria
1. `index.html` existe en raíz o carpeta de publicación.
2. Todas las rutas son relativas o compatibles con subcarpeta de repo.
3. No hay referencias a archivos locales inexistentes.
4. `manifest.json` usa `start_url` y `scope` compatibles.
5. `sw.js` no rompe la app al estar bajo `/nombre-repo/`.
6. Assets, iconos, CSS y JS tienen nombres correctos y coinciden en mayúsculas/minúsculas.
7. No se suben claves, zips de trabajo, copias duplicadas ni datos reales.
8. README explica cómo activar Pages.

## Salida
Da:
- Estado: listo / casi listo / no listo.
- Errores que romperían GitHub Pages.
- Cambios exactos.
- Pasos para publicar.
- Prueba final en URL pública.

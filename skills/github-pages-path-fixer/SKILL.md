---
name: GitHub Pages Path Fixer
description: Corrige rutas relativas, assets rotos, manifest, iconos, service worker y enlaces que fallan al publicar en GitHub Pages.
when_to_use: Úsalo cuando una app funciona en local pero falla en GitHub Pages, no carga CSS/JS, no aparecen imágenes, no registra PWA o los enlaces apuntan mal.
argument-hint: [URL o estructura del repo]
---

# GitHub Pages Path Fixer

## Tarea recibida
$ARGUMENTS

Actúa como especialista en despliegue de apps estáticas en GitHub Pages.

## Revisión obligatoria
1. Detecta si el proyecto se publica en raíz o subcarpeta del usuario/repo.
2. Cambia rutas absolutas incorrectas (`/style.css`) por rutas relativas (`./style.css`) cuando proceda.
3. Revisa `manifest.json`: `start_url`, `scope`, iconos y rutas.
4. Revisa `sw.js`: cache, rutas, versionado y fallback.
5. Comprueba enlaces internos, descargas, imágenes, fuentes, audio y assets.
6. Evita dependencias externas si la app promete offline.
7. Da pasos concretos para Settings → Pages.

## Salida
Entrega:
- Lista de rutas sospechosas.
- Cambios por archivo.
- Prueba local con servidor.
- Prueba final en URL pública.

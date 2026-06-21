# Límites reales del navegador

## Service worker y PWA

Un service worker no se registra desde `file://`. Requiere `localhost`, HTTPS o GitHub Pages. Esto no es un bug del proyecto; es una norma de seguridad del navegador.

## Instalación automática de Skills

Una web no puede escribir directamente en `~/.claude/skills/`, `C:\Users\...` ni carpetas internas del sistema. El flujo correcto es descargar el ZIP y ejecutar el instalador local voluntariamente.

## Safari/iOS

Safari puede aplicar reglas distintas para almacenamiento, instalación, descargas, portapapeles y caché. Por eso el proyecto incluye fallbacks y una checklist física en `docs/IPHONE-SAFARI-QA.md`.

## Qué sí cubre la app

- Fallback si `localStorage` falla.
- Fallback si el portapapeles moderno no está disponible.
- Fallback para `<dialog>`.
- Service worker limitado a recursos del mismo origen y respuestas válidas.
- Rutas relativas compatibles con GitHub Pages.
- Pruebas automáticas de carga, búsqueda, modal, tema y ZIP.

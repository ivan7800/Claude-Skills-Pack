# Release Checklist

## Validación automática

- [ ] `python scripts/validate-skills-pack.py` pasa sin errores.
- [ ] `node --check app.js` pasa sin errores.
- [ ] `node --check sw.js` pasa sin errores.
- [ ] `node scripts/smoke-test-chromium.mjs` pasa en local o CI con Chromium instalado.
- [ ] `npm run test:e2e` pasa tras instalar Playwright.

## Validación funcional

- [ ] Abrir `index.html` en local.
- [ ] Abrir la app desde `http://localhost:8080`.
- [ ] Probar buscador y filtros.
- [ ] Abrir una Skill.
- [ ] Copiar comando.
- [ ] Descargar `SKILL.md` individual.
- [ ] Generar ZIP desde el navegador.
- [ ] Probar notas y checklist con recarga de página.
- [ ] Probar modo claro/oscuro.
- [ ] Revisar responsive móvil, tablet y escritorio.

## GitHub Pages / PWA

- [ ] Publicar en GitHub Pages.
- [ ] Confirmar que `manifest.json`, `sw.js`, CSS, JS, iconos y ZIP descargable cargan en subcarpeta.
- [ ] Activar modo avión tras primera carga y confirmar que la app básica abre offline.
- [ ] En iPhone/Safari real, ejecutar `docs/IPHONE-SAFARI-QA.md`.

## Release

- [ ] No hay archivos temporales, zips antiguos ni logs.
- [ ] La versión coincide en `VERSION`, `skills-manifest.json`, `README.md`, `sw.js` e `index.html`.
- [ ] El ZIP final contiene los archivos necesarios y no contiene `.git` ni `node_modules`.

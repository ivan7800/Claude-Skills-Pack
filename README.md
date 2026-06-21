# I. Roig Claude Skills Pack · Web App

Panel web estático para explorar, copiar, descargar y documentar el **I. Roig Claude Skills Pack**.

Funciona con **HTML + CSS + JavaScript puro**, sin dependencias de runtime y preparado para **GitHub Pages**.

## Qué incluye

- Catálogo visual de 33 Claude Skills.
- Buscador por varias palabras y filtros por categoría.
- Favoritas con almacenamiento seguro: si `localStorage` falla, usa memoria de sesión.
- Generador de flujos de comandos para Claude Code.
- Descarga de `SKILL.md` individual.
- Generación de ZIP del pack directamente en el navegador.
- Botón de descarga del ZIP del pack v1.3.4.
- Checklist de release y notas locales privadas.
- Modo claro/oscuro accesible.
- PWA offline reforzada cuando se sirve por HTTPS o GitHub Pages.
- Pruebas versionadas: smoke test sin dependencias y suite E2E Playwright.

## Mejoras v1.3.4

- Añadido `package.json`, `playwright.config.js` y tests E2E en `tests/e2e/app.spec.js`.
- Añadido smoke test automático sin dependencias en `scripts/smoke-test-chromium.mjs`.
- Añadida guía específica de validación real en iPhone/Safari.
- Añadida documentación de límites reales del navegador.
- Workflow de GitHub Actions ampliado para validar Python, JavaScript, smoke test y E2E.
- Sincronizada versión en `VERSION`, `skills-manifest.json`, web, service worker y ZIP descargable.

## Uso local

Puedes abrir `index.html` directamente, pero para probar PWA/service worker usa servidor local:

```bash
python -m http.server 8080
```

Luego abre:

```text
http://localhost:8080
```

## Pruebas

Smoke test sin dependencias externas, usando Chromium si está instalado:

```bash
node scripts/smoke-test-chromium.mjs
```

Suite E2E con Playwright:

```bash
npm install
npx playwright install chromium
npm run test:e2e
```

Validación del pack:

```bash
python scripts/validate-skills-pack.py
node --check app.js
node --check sw.js
```

## Publicar en GitHub Pages

1. Crea un repositorio nuevo.
2. Sube todos los archivos.
3. Ve a **Settings → Pages**.
4. En **Build and deployment**, selecciona:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/root`
5. Guarda.
6. Abre la URL pública y ejecuta la checklist de `docs/IPHONE-SAFARI-QA.md` si vas a validar iOS.

## Instalar las Skills en Claude Code

Windows:

```powershell
./install-windows.ps1
```

macOS / Linux:

```bash
chmod +x install-macos-linux.sh
./install-macos-linux.sh
```

## Estructura

```text
index.html
style.css
app.js
manifest.json
sw.js
package.json
playwright.config.js
scripts/
tests/
docs/
skills/
downloads/
```

## Límites honestos

- Ningún navegador puede instalar automáticamente archivos en `~/.claude/skills/`; por seguridad, el usuario debe descargar y ejecutar el instalador local.
- El service worker no funciona abriendo `index.html` como archivo local; requiere `localhost`, HTTPS o GitHub Pages.
- Safari/iPhone real puede comportarse distinto a Chrome móvil simulado. Por eso existe una checklist física en `docs/IPHONE-SAFARI-QA.md`.

## Licencia

MIT.

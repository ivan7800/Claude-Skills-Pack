# I. Roig Claude Skills Pack · Web App

Panel web estático para explorar, copiar, descargar y documentar el **I. Roig Claude Skills Pack**.

Funciona con **HTML + CSS + JavaScript puro**, sin dependencias externas y preparado para **GitHub Pages**.

## Qué incluye

- Catálogo visual de 33 Claude Skills.
- Buscador y filtros por categoría.
- Favoritas con `localStorage`.
- Generador de flujos de comandos para Claude Code.
- Descarga de `SKILL.md` individual.
- Generación de ZIP del pack directamente en el navegador.
- Botón de descarga del ZIP del pack v1.3.1.
- Checklist de release guardado en local.
- Notas locales privadas.
- Modo claro/oscuro.
- PWA offline cuando se sirve por HTTPS.

## Nuevas Skills v1.3.1

- `console-error-hunter`
- `github-pages-path-fixer`
- `mobile-touch-auditor`
- `local-first-architecture`
- `app-product-polisher`
- `browser-compatibility-auditor`
- `no-dependency-auditor`
- `zip-release-builder`
- `api-key-safety-planner`
- `ai-feature-designer`
- `ollama-local-planner`
- `dark-landing-page-writer`
- `fiction-world-bible-builder`
- `kdp-launch-checklist`

## Uso local

Abre `index.html` directamente en el navegador.

Para probar como servidor local:

```bash
python -m http.server 8080
```

Luego abre:

```text
http://localhost:8080
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
icons/
downloads/
skills/
docs/
examples/
scripts/
```

## Estado v1.3.1

- Ampliado de 19 a 33 Skills.
- Añadidas Skills para consola, rutas de GitHub Pages, móvil táctil, arquitectura local-first, pulido de producto, compatibilidad, dependencias cero, ZIP releases, API keys, diseño IA, Ollama, landing oscura, biblia narrativa y KDP.
- Sincronizados `VERSION`, `skills-manifest.json`, web app y ZIP descargable.
- Listo para GitHub Pages tras prueba manual en navegador.

## Nota

La web no instala automáticamente archivos en `~/.claude/skills/`, porque el navegador no puede escribir en carpetas internas del sistema por seguridad. Sí permite descargar, copiar comandos y guiar la instalación.

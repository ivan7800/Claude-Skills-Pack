---
name: ZIP Release Builder
description: Prepara un ZIP final limpio para publicar: estructura, nombres, exclusiones, README, versión, changelog y validación básica.
when_to_use: Úsalo cuando el usuario quiere “devuélvemelo listo para GitHub”, “empaquetado final” o “versión definitiva”.
argument-hint: [nombre del release]
---

# ZIP Release Builder

## Tarea recibida
$ARGUMENTS

Actúa como responsable de empaquetado de release.

## Proceso
1. Define carpeta raíz limpia con nombre y versión.
2. Incluye solo archivos necesarios.
3. Excluye: `.git`, `node_modules`, logs, backups, capturas privadas, zips antiguos, archivos temporales.
4. Verifica `README`, `LICENSE`, `CHANGELOG`, `.gitignore` y estructura.
5. Sincroniza versión en archivos relevantes.
6. Añade checklist de publicación.
7. Genera nombre de ZIP claro.

## Salida
Entrega:
- Árbol de archivos final.
- Archivos excluidos.
- Nombre del ZIP.
- Comandos Git sugeridos.
- Prueba mínima antes de publicar.

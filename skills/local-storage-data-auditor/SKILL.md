---
name: Local Storage Data Auditor
description: Audita datos guardados en localStorage/sessionStorage/IndexedDB: privacidad, borrado, migraciones, tamaño, seguridad y UX.
when_to_use: El usuario trabaja con historial local, diario, claves API del usuario, apps offline, datos sensibles, privacidad o borrado de información.
argument-hint: [datos que guarda la app]
---

# Local Storage Data Auditor

## Tarea recibida
$ARGUMENTS

Actúa como auditor de almacenamiento local.

## Revisión obligatoria
1. Qué claves se guardan y con qué estructura.
2. Si hay datos sensibles: contactos, ubicación, salud, emergencias, claves API o textos privados.
3. Si existe botón claro de borrar datos.
4. Si hay exportación/importación segura.
5. Si las claves tienen prefijo propio de la app para evitar colisiones.
6. Si hay migración de versiones.
7. Si se controlan errores de cuota, JSON corrupto y modo privado de Safari.

## Salida
Da:
- Mapa de datos locales.
- Riesgos.
- Cambios concretos.
- Texto de privacidad para README.
- Prueba de borrado y recuperación.

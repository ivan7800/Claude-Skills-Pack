# Prueba manual iPhone / Safari

Esta prueba cubre lo que no puede garantizarse desde un navegador de escritorio: políticas reales de Safari/iOS, instalación PWA, almacenamiento en modo privado, teclado táctil y caché.

## Preparación

1. Publica la app en GitHub Pages o sirve el proyecto por HTTPS.
2. Abre la URL en Safari de iPhone.
3. Cierra otras pestañas pesadas para evitar falsos problemas de memoria.

## Checklist obligatoria

- [ ] La home carga sin pantalla en blanco.
- [ ] No aparece zoom lateral ni scroll horizontal raro.
- [ ] Los botones principales se pueden pulsar cómodamente con el dedo.
- [ ] Buscar `safari` filtra resultados.
- [ ] Abrir una Skill muestra el modal.
- [ ] Cerrar el modal funciona con la `×` y tocando fuera si procede.
- [ ] Copiar comando muestra feedback; si Safari bloquea el portapapeles, aparece mensaje sin romper la app.
- [ ] Cambiar tema funciona y se mantiene al recargar.
- [ ] Las notas se guardan al recargar en navegación normal.
- [ ] En navegación privada, si Safari bloquea almacenamiento, la app sigue funcionando aunque no persista todo.
- [ ] El enlace `ZIP pack` descarga o abre el ZIP correctamente.
- [ ] Añadir a pantalla de inicio crea acceso directo.
- [ ] Tras una primera carga pública, abrir en modo avión permite ver la app básica si el service worker ya se instaló.

## Resultado aceptable

La versión se considera validada en iPhone si todo lo anterior pasa o si la única limitación observada es una política propia de Safari explicada al usuario, como bloqueo de portapapeles o instalación PWA no disponible desde un contexto no HTTPS.

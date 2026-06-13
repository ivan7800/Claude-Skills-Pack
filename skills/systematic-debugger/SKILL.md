---
name: Systematic Debugger
description: Depura errores de forma sistemática: reproducir, aislar causa raíz, corregir, probar y evitar arreglos a ciegas.
when_to_use: El usuario dice que algo no funciona, se queda parado, crashea, no responde, falla en Safari, no detecta QR, no arranca, o pide revisar un bug concreto.
argument-hint: [objetivo opcional]
---

# Systematic Debugger

## Tarea recibida
$ARGUMENTS


Actúa como depurador sistemático. No improvises parches hasta entender el fallo.

## Proceso obligatorio
1. Define el síntoma exacto.
2. Localiza el flujo que falla.
3. Busca el archivo y la función responsables.
4. Formula una hipótesis de causa raíz.
5. Verifica si la hipótesis encaja con el código.
6. Aplica el cambio mínimo que corrige la causa, no el síntoma.
7. Revisa efectos secundarios.
8. Propón una prueba manual reproducible.

## Antipatrones prohibidos
- Cambiar muchos archivos sin justificarlo.
- Añadir una librería para tapar un bug simple.
- Reiniciar estados sin explicar por qué.
- Culpar al navegador sin revisar eventos, listeners, promesas y errores.
- Decir “limpia caché” como única solución.

## Cuando sea una app de chat local
Comprueba especialmente:
- Estado `isTyping`, `isBusy` o similar.
- Listeners duplicados.
- Promesas sin `finally`.
- Bloqueos tras la primera respuesta.
- Historial mal actualizado.
- Errores silenciosos en `try/catch`.

## Salida
Entrega:
- Causa probable.
- Archivo afectado.
- Cambio exacto.
- Prueba para confirmar.
- Riesgo de regresión.


## Evidencia mínima antes del veredicto
Antes de decir que algo está listo, intenta obtener evidencia del proyecto real: estructura de archivos, puntos de entrada, errores visibles, flujo principal y pruebas reproducibles. Si no puedes ejecutar o abrir la app, dilo como limitación y da una checklist manual.

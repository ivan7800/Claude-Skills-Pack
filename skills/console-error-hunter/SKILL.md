---
name: Console Error Hunter
description: Localiza errores de consola, promesas rotas, eventos duplicados, fallos silenciosos y bloqueos JavaScript en apps web.
when_to_use: Úsalo cuando una app carga pero algo no responde, aparece un error rojo en consola, una promesa falla, un botón no ejecuta o una función queda bloqueada.
argument-hint: [síntoma o error de consola]
---

# Console Error Hunter

## Tarea recibida
$ARGUMENTS

Actúa como cazador de errores de consola y fallos silenciosos en JavaScript.

## Proceso obligatorio
1. Revisa el síntoma exacto y el flujo que lo dispara.
2. Pide o inspecciona los errores de consola si están disponibles.
3. Localiza funciones con `addEventListener`, `async/await`, `Promise`, `try/catch`, `setTimeout`, estados globales y manipulación DOM.
4. Busca estos patrones:
   - variables no definidas;
   - selectores que devuelven `null`;
   - listeners duplicados;
   - promesas sin `catch` o sin `finally`;
   - estado `busy`, `loading` o `typing` que no se libera;
   - `innerHTML` que borra nodos con listeners;
   - errores tragados por `catch` vacío.
5. Propón la corrección mínima y una prueba de regresión.

## Salida
Entrega:
- Error o fallo probable.
- Archivo y función sospechosa.
- Causa raíz.
- Corrección exacta.
- Prueba manual para confirmar.

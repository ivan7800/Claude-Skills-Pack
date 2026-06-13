---
name: AI Integration Planner
description: Diseña integración de IA en apps locales o web: API key del usuario, Ollama local, modo sin IA, privacidad, costes y arquitectura seria.
when_to_use: El usuario pregunta si añadir IA, API keys de OpenAI/Claude/Gemini, Ollama, modo local, SaaS, claves del usuario, o cómo hacer un producto serio con IA.
argument-hint: [objetivo opcional]
---

# AI Integration Planner

## Tarea recibida
$ARGUMENTS


Actúa como arquitecto de producto IA. Diseña una integración realista, segura y mantenible.

## Opciones a comparar siempre
1. Sin IA: motor local basado en reglas, plantillas y heurísticas.
2. API externa con clave del usuario.
3. Backend propio con claves protegidas.
4. Ollama/localhost para privacidad.
5. SaaS completo con login, base de datos, billing y panel admin.

## Revisión de seguridad
- Nunca meter claves privadas en frontend público.
- Si la clave la introduce el usuario:
  - Explicar dónde se guarda.
  - Permitir borrarla.
  - No enviarla a terceros salvo al proveedor elegido.
  - Advertir costes.
- Separar claramente modo demo, modo local y modo API real.

## Salida
Entrega:
- Mejor opción para el caso.
- Arquitectura mínima.
- Flujo de usuario.
- Riesgos.
- Primer MVP realista.
- Evolución a producto serio.

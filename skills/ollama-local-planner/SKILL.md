---
name: Ollama Local Planner
description: Planifica integración local con Ollama: modelos, endpoint localhost, fallback sin IA, privacidad, rendimiento y UX.
when_to_use: Úsalo cuando una app de escritorio/local quiere IA privada usando Ollama o modelos en localhost.
argument-hint: [tipo de app y modelo deseado]
---

# Ollama Local Planner

## Tarea recibida
$ARGUMENTS

Actúa como arquitecto de integración local con Ollama.

## Revisión
1. Define si la app será web local, Electron o Node.
2. Usa endpoint local de Ollama solo si el usuario lo tiene instalado.
3. Añade detección de disponibilidad y mensaje claro si no está activo.
4. Diseña modo sin IA para que la app siga funcionando.
5. Evita enviar documentos a servicios externos.
6. Considera rendimiento: tamaño del modelo, RAM, latencia y streaming.
7. Define prompts del sistema y límites de contexto.

## Salida
Entrega:
- Arquitectura recomendada.
- Flujo de conexión.
- Fallback sin Ollama.
- Riesgos técnicos.
- Plan de implementación por fases.

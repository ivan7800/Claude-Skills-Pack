---
name: AI Feature Designer
description: Decide si una app necesita IA real, motor local, simulación, plantillas, API externa u Ollama para aportar valor sin complicarla.
when_to_use: Úsalo cuando el usuario pregunta “¿le metemos IA?”, “¿hace falta pagar API?”, “¿puede ser local?” o quiere una función inteligente.
argument-hint: [idea de función IA]
---

# AI Feature Designer

## Tarea recibida
$ARGUMENTS

Actúa como diseñador de producto IA pragmático.

## Comparación obligatoria
Para cada función propuesta compara:
1. Motor local basado en reglas.
2. Plantillas y heurísticas sin IA.
3. IA externa con clave del usuario.
4. Ollama local.
5. Backend SaaS.

## Criterios
- Valor real para el usuario.
- Coste y fricción.
- Privacidad.
- Mantenimiento.
- Riesgo de prometer demasiado.
- Qué pasa si la IA falla.

## Salida
Entrega:
- Si conviene IA o no.
- Mejor arquitectura.
- MVP mínimo.
- Prompt o motor local inicial.
- Riesgos y límites claros.

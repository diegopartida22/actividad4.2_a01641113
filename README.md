# Actividad 4.2 Procesos estocásticos

Generador de Melodías con Cadenas de Markov. El programa genera secuencias de notas musicales basadas en probabilidades de transición entre notas, creando melodías aleatorias pero con estructura matemática.

## Autor

**Diego Partida Romero - A01641113**

_Fecha: 04/05/2025_

## Descripción

El generador de melodías utiliza una Cadena de Markov para producir secuencias de notas musicales. En esta implementación inicial, todas las transiciones entre notas tienen la misma probabilidad, pero el modelo puede ser modificado para reflejar patrones musicales específicos.

El programa:

- Define las frecuencias de las notas musicales básicas (DO, RE, MI, FA, SOL, LA, SI)
- Crea una matriz de transición con probabilidades uniformes
- Genera y reproduce una melodía aleatoria de 10 notas

## Matriz de transiciones

|     | DO    | RE    | MI    | FA    | SOL   | LA    | SI    |
| --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| DO  | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 |
| RE  | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 |
| MI  | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 |
| FA  | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 |
| SOL | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 |
| LA  | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 |
| SI  | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 |

**Nota:** Cada valor en la matriz (0.143) representa la probabilidad de pasar de una nota a cualquier otra (incluida ella misma). Esto se debe a que hay 7 notas posibles, y la probabilidad es uniforme:

$$
\text{Probabilidad} = \frac{1}{7} \approx 0.143
$$

## Reflexión: Patrones Repetitivos en la Música y su Incorporación al Modelo

### ¿Cómo podemos incorporar patrones repetitivos al modelo?

La música que disfrutamos generalmente contiene patrones repetitivos, estructuras y progresiones de acordes que siguen ciertas reglas. Para incorporar estos patrones al modelo de Cadenas de Markov, podríamos:

1. **Ajustar la matriz de transición**: En lugar de usar probabilidades uniformes (0.143 para cada transición), podríamos analizar piezas musicales reales para determinar con qué frecuencia una nota sigue a otra. Por ejemplo, en música occidental, es más común que DO sea seguido por MI que por FA♯.

2. **Expandir el orden de la cadena**: Actualmente utilizamos una Cadena de Markov de primer orden, donde solo la nota actual determina la siguiente. Podríamos implementar una cadena de orden superior que considere las últimas 2, 3 o más notas para determinar la siguiente, capturando así secuencias y frases musicales más complejas.

3. **Incorporar información de duración**: Además de las notas, podríamos modelar la duración (negras, corcheas, etc.) creando una matriz de transición separada para las duraciones o un modelo conjunto.

4. **Añadir estructura armónica**: Incorporar información sobre tonalidades, progresiones de acordes y resoluciones armónicas para generar melodías que respeten las reglas de armonía musical.

### ¿El modelo podría aprender un estilo?

Sí, el modelo podría aprender y reproducir características de un estilo musical específico:

1. **Entrenamiento con corpus específico**: Al alimentar el modelo con piezas de un género o compositor específico (por ejemplo, piezas de Bach o música jazz), la matriz de transición reflejaría las tendencias y patrones característicos de ese estilo.

2. **Captura de motivos recurrentes**: Con una cadena de orden superior, el modelo podría capturar motivos y frases características de un estilo musical.

3. **Aprendizaje de progresiones armónicas**: Ampliando el modelo para incluir acordes y progresiones armónicas, podría capturar elementos estilísticos como las progresiones II-V-I en jazz o las cadencias características del periodo barroco.

### Limitaciones del modelo

A pesar de su utilidad, las Cadenas de Markov tienen limitaciones significativas para la generación musical:

1. **Memoria limitada**: Incluso las cadenas de orden superior solo consideran un número fijo de notas previas, lo que dificulta capturar estructuras musicales de largo alcance como formas A-B-A.

2. **Ausencia de estructura jerárquica**: La música tiene múltiples niveles de estructura (notas, motivos, frases, secciones) que son difíciles de capturar con una simple cadena de Markov.

3. **No considera la tensión y resolución**: Elementos como la construcción de tensión, clímax y resolución, fundamentales en la música expresiva, no son modelados adecuadamente.

4. **Falta de contexto global**: El modelo no tiene "conciencia" de en qué parte de la pieza se encuentra (introducción, desarrollo, conclusión), lo que puede resultar en melodías sin dirección.

5. **Sin conocimiento teórico musical**: No incorpora reglas de teoría musical a menos que estén implícitamente codificadas en los datos de entrenamiento.

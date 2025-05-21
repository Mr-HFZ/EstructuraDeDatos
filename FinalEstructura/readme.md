# Juego de Equilibria: Estructura de Datos

## Descripción
El Reino de Equilibria es un juego de toma de decisiones donde el jugador asume el papel de un gobernante que debe mantener el equilibrio entre diferentes facciones y recursos: ángeles, demonios, pueblo y tesoro. El objetivo es tomar decisiones estratégicas para mantener todas estas estadísticas en equilibrio y llegar al final del juego.

## Estructura del Código

El código está organizado en tres archivos principales que utilizan conceptos básicos de estructura de datos:

1. **nodo.py**: Implementa la clase `DecisionNode` que representa los nodos en un árbol de decisiones.
2. **arbol.py**: Contiene la implementación de:
   - `GameStats`: Para manejar las estadísticas del juego
   - `DecisionTree`: Implementa un árbol de decisiones donde cada nodo es un `DecisionNode`
3. **main.py**: Punto de entrada principal que implementa la lógica del juego utilizando las estructuras definidas en los archivos anteriores.

## Uso de Estructuras de Datos

- **Árbol**: Un árbol de decisiones donde cada nodo contiene dos posibles elecciones (izquierda/derecha)
- **Diccionarios**: Para almacenar estadísticas y sus cambios asociados a cada decisión
- **Listas**: Para almacenar la colección de nodos de decisión

## Ejecución del Juego

Para jugar, simplemente ejecuta:

```
python main.py
```

## Mecánica del Juego

- El jugador toma hasta 15 decisiones
- Cada decisión afecta las estadísticas de ángeles, demonios, pueblo y tesoro
- Si alguna estadística llega a 0 o 100, se produce una condición de fin del juego
- Para ganar, hay que mantener todas las estadísticas en equilibrio (entre 30-70) al finalizar las 15 decisiones
# Razonamiento

Dado `V` un conjunto de enteros positivos distintos con `n` elementos.

Construiremos el grafo no dirigido `G = (V, E)` de forma que:

```
E = { {x, y} | x, y ∈ V, x ≠ y, x + y es primo }
```

Nótese que, no existen conexiones entre dos nodos pares y no existen conexiones entre dos nodos impares. Esto porque:

1. La suma de dos números pares es par y por lo tanto no es primo.
2. La suma de dos números impares es par pues `2k + 1 + 2l + 1 = 2(k + l + 1)` es divisible por 2 y por lo tanto no es primo.

Todas las conexiones son de la forma `{x, y}` con `x` par e `y` impar.

Si P es el conjunto de los nodos pares y Q el conjunto de los nodos impares, entonces `V = P ∪ Q` y `P ∩ Q = ∅`, y ademas todas la conexiones en `E` son de la forma `{x, y}` con `x ∈ P` e `y ∈ Q`. Esto es, el grafo `G` es bipartito.

Queremos obtener la menor cantidad de nodos que deben ser removidos de `G` para que el grafo resultante no tenga conexiones.

Para esto, podemos buscar un subconjunto de nodos `S` de `V` tal que para todo `{x, y} ∈ E`, `x ∈ S` o `y ∈ S`. Es decir, `S` es un conjunto de nodos que al removerlos del grafo `G` no quedan conexiones. Más aun, queremos conseguir un subconjunto `S` de tamaño mínimo.

Este conjunto `S` se conoce como cobertura de vértices miníma. La respuesta a la pregunta es el tamaño de `S`.

Como el grafo es bipartito, podemos usar el teorema de König que nos dice que el tamaño de la cobertura de vértices miníma es igual al tamaño del emparejamiento máximo.

Es decir, podemos dar la respuesta a la pregunta si encontramos el tamaño del emparejamiento máximo en `G`. Para esto, podemos usar el algoritmo de Hopcroft-Karp.

# Análisis de complejidad

Constuir el grafo `G` toma `O(n^2)` asumiendo que la verificación de si un número es primo toma `O(1)`.

El algoritmo de Hopcroft-Karp tiene complejidad `O(E * sqrt(V))` = `O(n^2 * sqrt(n))`

Por lo tanto, la complejidad total del algoritmo es `O(n^2 * sqrt(n))`.

# Implementacion

La implementación del algoritmo se encuentra en el archivo [pregunta-2-implementacion.py](pregunta-2-implementacion.py).

El grafo `G` se representa como lista de adyacencia. Cada nodo `x` par tiene una lista de adyacencia con los nodos impares `y` tal que `{x, y}` es una conexión en `E`. La implementacion de esta estructura es la clase `BipartiteGraph`.

La funcion `hopcroft_karp_matching` recibe un grafo bipartito y retorna el tamaño del emparejamiento máximo.

La funcion `min_removals` recibe un conjunto de enteros positivos distintos y retorna el tamaño de la cobertura de vértices miníma.

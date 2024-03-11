Para resolver este problema, se puede aplicar convex hull sucesivamente, eliminando en cada iteración a los puntos que forman parte de la capa actual. Esto es:

Si `pset` es la estructura conjunto que representa `P`, entonces el algoritmo es el siguiente:

1. Inicializar `count` en cero.
2. Mientras `pset` tenga más de dos elementos:
   1. Calcular el convex hull de `pset` y almacenarlo en `hull`.
   2. Aumentar `count` en uno.
   3. Eliminar de `pset` los puntos que están en `hull`.

El resultado es el valor de `count`.

Como el ciclo `2.` se ejecuta a lo sumo `n` veces, el cálculo del convex hull toma tiempo `O(n log n)`, y la resta de conjuntos es `O(n)`, entonces el algoritmo toma tiempo `O(n^2 log n)`.

En todo momento, se utiliza la memoria axuliar utilizada por convex hull (en el peor caso, `O(n)`) y la memoria utilizada por `pset` (en el peor caso, `O(n)`). Por lo tanto, el algoritmo toma `O(n)` de memoria adicional.

La implementación de la solución se encuentra en el archivo [pregunta-2-implementacion.py](pregunta-2-implementacion.py).

El codigo de implementación de la solución es el siguiente:

```python
def onion_convex_hull(points):
    """
    Calcula el número de capas de un cierre convexo de un conjunto de puntos en 2D.
    """

    pset = set(points)
    count = 0

    # Numero maximo de capas, n
    for _ in range(0, len(points)):
        if len(pset) < 2:
            break

        pset -= convex_hull(pset)
        count += 1

    return count
```

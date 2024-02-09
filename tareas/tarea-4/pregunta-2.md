# Pregunta 2

## Solución

Se propone un algoritmo que utiliza programación dinámica Bottom-Up para resolver el problema. Para ello, definimos la tabla `b[i][j]` como la cantidad de sub-arreglos buenos de tamaño `i` que utilizan los primeros `j` elementos de `A`.

### Casos base

1. `b[0][j] = 0` para todo `j` pues no hay arreglos buenos vacíos.
2. `b[i][0] = 0` para todo `i` pues no hay arreglos buenos de tamaño `i` que utilicen los primeros `0` elementos de `A`.
3. `b[1][j] = j` pues siempre se puede formar el sub-arreglo `[A[j]]` que es bueno pues `x mod 1 = 0` para todo `x`.

### Relación de recurrencia

para obtener `b[i][j]` nos damos cuenta de que los sub-arreglos buenos de tamaño `i` que utilizan los primeros `j` elementos de `A` son aquellos que:

1. Tengan longitud `i` y utilicen los primeros `j - 1` elementos de `A`.
2. Alternativamente, tengan longitud `i - 1` y utilicen los primeros `j - 1` elementos de `A` y `A[j] mod i = 0`. En otras palabras, son los que podemos formar a partir de agregar `A[j]` al final de forma que el sub-arreglo resultante sea bueno.

Esto es:

```
b[i][j] = (b[i - 1][j - 1] if A[j] mod i == 0) + b[i][j - 1]
```

Después de llenar la tabla, la respuesta será la suma de todos los valores de `b[i][n]` para `i` de `1` a `n`.

### Análisis de complejidad

1. Inicializar la tabla `b` toma `O(n^2)`.
2. Llenar los casos base toma `O(n)`.
3. Llenar la tabla toma `O(n^2)`.
4. Calcular la respuesta toma `O(n)`.

Por lo tanto, el algoritmo tiene una complejidad de `O(n^2)`.

Sin embargo, la memoria utilizada es `O(n^2)`, para mejorar esto a `O(n)` podemos notar que solo necesitamos los valores de la fila `i - 1` para calcular la fila `i`. Por lo tanto, podemos utilizar dos arreglos de longitud `n` para almacenar los valores de `b[i]` y `b[i - 1]` y así reducir la memoria utilizada a `O(n)`.

Al hacer este cambio es necesario agregar una variable auxiliar `count` que nos permita sumar el ultimo elemento de la fila `i`, para cada fila, para obtener la respuesta correcta.

Con esta optimización:

1. Inicializar los arreglos `b` y `b_prev` toma `O(n)`.
2. Llenar los casos base toma `O(n)`.
3. Llenar la tabla toma `O(n^2)`.
4. Calcular la respuesta toma `O(1)`.

Por lo tanto, el algoritmo tiene una complejidad de `O(n^2)` y utiliza `O(n)` de memoria adicional.

## Implementación

Sin considerar la optimización de memoria, la implementación del algoritmo es la siguiente:

```python
def good_subarrays(A):
    n = len(A)
    b = [[0] * (n + 1) for _ in range(n + 1)]

    for j in range(1, n + 1):
        b[1][j] = j

    for i in range(2, n + 1):
        for j in range(1, n + 1):
            b[i][j] = (b[i - 1][j - 1] if A[j - 1] %
                       i == 0 else 0) + b[i][j - 1]

    return sum(b[i][n] for i in range(1, n + 1))
```

Considerando la optimización de memoria, la implementación del algoritmo es la siguiente:

```python
def good_subarrays_optim(A):
    n = len(A)
    b = [0] * (n + 1)
    b_prev = [0] * (n + 1)
    count = 0

    # Casos base
    for j in range(1, n + 1):
        b[j] = j
    count += b[n]

    # Llenar la tabla
    for i in range(2, n + 1):
        b, b_prev = b_prev, b

        for j in range(1, n + 1):
            b[j] = b_prev[j - 1] if A[j - 1] % i == 0 else 0
            b[j] += b[j - 1]

        count += b[n]

    return count
```

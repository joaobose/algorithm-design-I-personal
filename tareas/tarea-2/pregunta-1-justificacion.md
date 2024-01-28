# Justificación informal de la solución

Notese que para maximizar la cantidad de vallas construidas, queremos escoger primero las vallas que:

- Terminen los más pronto posible
- No comiencen antes de que terminen las vallas que ya escogimos

Si escogemos las vallas en este orden, maximizamos la cantidad de vallas que podemos construir.

La intuicion detras de cada uno de estos puntos es la siguiente:

## Primer punto: seleccionar las vallas que terminen los mas pronto posible

Si una valla termina antes, podemos construir mas vallas despues de esta. Por ejemplo, si tenemos dos vallas, la valla (2, 5) y la valla (1, 9), escoger la valla (2, 5) nos deja disponible el espacio [7..10] para construir otra valla, por lo tanto el numero de vallas que podemos construir es mayor si escogemos la valla (2, 5).

Fijese que esto NO es escoger la valla mas pequeña, pues por ejemplo si tuviera se suvieran las vallas (1, 10), (10, 2) y (11, 10), escoger la valla mas pequeña hace que no se pueda construir ninguna otra valla (pues ocupa [10..12] que se solapa con las otras dos vallas), mientras que escoger la valla que termina mas pronto (1, 10) nos permite construir (11, 10) tambien.

## Segundo punto: no escoger vallas que comiencen antes de que terminen las vallas que ya escogimos

Como las vallas no pueden solaparse por definicion, y la escogencia de las vallas esta dada por el orden en el que terminan, si escogemos una valla que comienza antes de que termine la ultima valla que escogimos, la solucion se vuelve invalida.

# Algoritmo

```
1. Ordenar las vallas por el tiempo en el que terminan, esto es la suma de la posicion inicial y el largo de la valla
2. Para cada valla en el orden anterior:
    1. Si la valla no comienza antes de que termine la ultima valla que escogimos:
        1. Agregar la valla a la solucion
```

# Complejidad

La complejidad de este algoritmo es O(n log n), pues el paso 1 toma O(n log n) y el paso 2 toma O(n), por lo tanto la complejidad total es O(n log n).

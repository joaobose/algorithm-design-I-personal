Sea:

- `M` el conjunto de maletas a recoger, con `|M| = n`, indexadas de `1` a `n`.

- `C[i]` con `i` un entero en el rango `[1, n]`, la cordenada de la maleta `i` en el plano cartesiano `(x, y)`.

- `t((x1, y1), (x2, y2)) = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 2 = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)` es el tiempo que toma ir de `(x1, y1)` a `(x2, y2)`.

Como `1 < n <= 24`, utilizando un razonamiento similar a lo visto en clases, para resolver este problema se puede utilizar programación dinámica sobre conjuntos.

Definimos `p[S]` (con `S subconjunto de M`) como el tiempo mínimo para recoger las maletas en `M - S`. Sabemos que `p[M] = 0` y que `p[∅]` es la solución al problema.

Ahora vamos a plantear un recurrencia top-down para `p[S]`.

```
p[S] = Mínimo
  sobre h en {{i,j} subconjunto M - S con i != j} // Tomar de a dos maletas
            + {{i} subconjunto M - S} // Tomar de a una maleta
 de (
  si |h| == 1 // Caso: Se toma una maleta

    p[S + h] + // El mejor tiempo para recoger las maletas en M - (S + h)
    2 * t((0,0), C[i]) + // El tiempo que toma ir y volver del avion a la maleta i

  si no // Caso: Se toman dos maletas

    p[S + h] + // El mejor tiempo para recoger las maletas en M - (S + h)
    t((0,0), C[i]) + // El tiempo que toma ir del avion a la maleta i
    t(C[i], C[j]) + // El tiempo que toma ir de la maleta i a la maleta j
    t(C[j], (0,0)) + // El tiempo que toma ir de la maleta j al avion
)
```

Nótese que no importa el orden en el que se recojan las maletas entre `i` y `j`, ya que entre las maletas `i`, `j` y el avion se forma un triangulo, y el tiempo es el mismo sin importar el orden en el que se recorran los puntos.

Dicho esto, el resto de la implementación es similar a lo que se vió en clase. La implementación de este algoritmo se encuenta en el archivo [pregunta-4-implementacion.py](pregunta-4-implementacion.py).

Este algoritmo considera en el peor caso a todos los subconjuntos de `M`, y para cada uno de ellos se busca la mejor opcion en tiempo `O(n)`. Por lo tanto, la complejidad del algoritmo es `O(n * 2^n)`, utilizando `O(2^n)` de memoria adicional.

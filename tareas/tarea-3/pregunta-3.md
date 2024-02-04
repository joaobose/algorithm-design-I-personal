Para resolver este problema notaremos que una sub-cadena esta bien parentizada si para cada parentesis `(` que aparece en la sub-cadena, existe un parentesis `)` que lo cierra. Ademas, si la sub-cadena esta bien parentizada, entonces el numero de parentesis `(` y `)` que aparecen en ella es el mismo.

Por lo tanto, para construir un arbol de segmentos que nos permita responder las consultas `maxBP(i, j)` almacenamos en cada nodo:

- `bp`: El numero de pares de parentesis bien parentizados que aparecen en la sub-cadena correspondiente al nodo.
- `a`: El numero de parentesis `(` que se abren y no tienen un `)` que los cierre.
- `c`: El numero de parentesis `)` que se cierran y no tienen un `(` que los abra.

Notese que la sub-cadena mas larga en el intervalor `[i..j]` tiene justamente longitud del doble de numero de pares bien parentizados en ese intervalo. Por lo tanto, basta con almacenar estos valores en cada nodo para poder responder las consultas `maxBP(i, j)`.

Dicho esto, si el nodo `h` es un nodo hoja que representa al intervalo `[k..l]` con `k = l` entonces:

- `h.bp = 0`
- `h.a = 1 if S[k] === '(' else 0`,
- `h.c = 1 if S[k] === ')' else 0`.

Y si el nodo `h` no es un nodo hoja que representa al intervalo `[k..l]`, con hijos `h.izq` y `h.der` que representan a los intervalos `[k..m]` y `[(m + 1)..l]` respectivamente, con `m = (k + l) / 2`, entonces:

- `match = min(h.izq.a, h.der.c)` es el numero de parentesis sin pareja `(` en `h.izq` que ahora se cierran en `h.der`.

- `h.bp = h.izq.bp + h.der.bp + match` se suman los pares bien parentizados de `h.izq` y `h.der` y los nuevos pares bien parentizados que se forman con `match`.
- `h.a = h.izq.a + h.der.a - match` se restan los parentesis `(` que se utilizaron en `match`.
- `h.c = h.izq.c + h.der.c - match` se restan los parentesis `)` que se utilizaron en `match`.

Si se construye el arbol de segmentos de esta manera, entonces se puede responder la consulta `maxBP(i, j)` de la siguiente manera:

```
Sea r la raiz del arbol de segmentos construido para la cadena S.

maxBPImpl(h, i, j):
  k = h.k
  l = h.l
  m = (k + l) / 2

  # Caso: El intervalo [k..l] representado por el nodo h es igual al intervalo [i..j]
  if i === k y j === l:
    return { bp: h.bp, a: h.a, c: h.c }

  # Caso: El intervalo [i..j] esta contenido en el intervalo [k..m]
  if j <= m:
    return maxBP(h.izq, i, j)

  # Caso: El intervalo [i..j] esta contenido en el intervalo [(m + 1)..l]
  if i > m:
    return maxBP(h.der, i, j)

  # Caso: El intervalo [i..j] se divide en los intervalos [i..m] y [(m + 1)..j]
  maxBP_izq = maxBP(h.izq, i, m)
  maxBP_der = maxBP(h.der, m + 1, j)

  # Hacemos match de los parentesis que se abren en h.izq y se cierran en h.der
  match = min(maxBP_izq.a, maxBP_der.c)

  return {
    bp: maxBP_izq.bp + maxBP_der.bp + match,
    a: maxBP_izq.a + maxBP_der.a - match,
    c: maxBP_izq.c + maxBP_der.c - match
  }

maxBP(i, j):
  # La longitud de la sub-cadena mas larga es el doble del numero de pares bien parentizados
  return 2 * maxBPImpl(r, i, j).bp
```

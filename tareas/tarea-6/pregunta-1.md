# Razonamiento

Para resolver este problema, comenzas observando el comportamiento de la operacion `multiswap`, en particular, que modificaciones hace al arreglo `A`.

Luego de ejecutar varias veces la operacion `multiswap` con distintos parametros, se puede observar que la operacion `multiswap` intercambia dos sub arreglos de `A` de igual longitud. A partir de la definicion de `multiswap`, podemos obtener en terminos de `a` y `b` el rango de ambos sub arreglos que se intercambian.

Si `N = |A|`, `multiswap` intercambia los sub arreglos:

- `Sa = A[a..min(a + N - b, b - 1)]`
- `Sb = A[b..min(b + (b - a) - 1, N)]`

Nótese que:

```
A = A[1..a-1] + Sa + A[min(a + N - b, b - 1) + 1..b-1] + Sb + A[min(b + (b - a) - 1, N) + 1..N]

y si:

head = A[1..a-1]
center = A[min(a + N - b, b - 1) + 1..b-1]
tail = A[min(b + (b - a) - 1, N) + 1..N]

entonces:

A = head + Sa + center + Sb + tail
```

Si puedieramos descomponer `A` de esta forma, podriamos obtener el resultado de `multiswap` intercambiando `Sa` con `Sb`:

```
multiswap(A, a, b) = head + Sb + center + Sa + tail
```

Para hacer esto, podemos contruir un treap implicito para la secuencia `A`. Luego, podemos usar las operaciones `split` y `merge` para dividir `A` en `head`, `Sa`, `center`, `Sb` y `tail`, y luego intercambiar `Sa` con `Sb` para obtener el resultado de `multiswap`. Como `split` y `merge` tienen complejidad `O(log N)`, la complejidad de `multiswap` es `O(log N)`.

Lo cual nos permite realizar las N acciones en `O(N log N)`.

Como el treap utiliza memoria `O(N)`, la memoria adicional utilizada es `O(N)`.

# Implementacion

La implementacion del treap implicito se encuentre en el archivo [treap.py](treap.py). Se utilizo como referencia la implementacion de [USACO Guide](https://usaco.guide/adv/treaps?lang=cpp) para C++, y se tradujo a Python.

Luego, se implemento la funcion `multiswap_treap` que utiliza el treap implicito para realizar la operacion `multiswap` en `O(log N)`.

```python
def multiswap_treap(treap, a, b):
    N = treap.root.size

    # Obtener los rangos de los sub arreglos (complexity O(1))
    lower_sa = a
    upper_sa = min(a + N - b, b - 1)

    lower_sb = b
    upper_sb = min(b + (b - a) - 1, N)

    # Utilizar split para obtener: head, sa, center, sb, tail
    # (tiempo O(log N))
    head, tail = t.split(t.root, lower_sa - 1)
    sa, tail = t.split(tail, upper_sa - lower_sa + 1)
    center, tail = t.split(tail, lower_sb - upper_sa - 1)
    sb, tail = t.split(tail, upper_sb - lower_sb + 1)

    # Utilizar merge para obtener el arreglo: head, sb, center, sa, tail
    # (tiempo O(log N))
    t.root = t.merge(head, sb)
    t.root = t.merge(t.root, center)
    t.root = t.merge(t.root, sa)
    t.root = t.merge(t.root, tail)

    return t
```

Finalmente, para cada una de las N operaciones `multiswap`, se llama a `multiswap_treap` con los parametros correspondientes.

```python
N = 11
A = [i for i in range(1, N + 1)]

# Espacio O(N)
t = ImplicitTreap()
for i, a in enumerate(A):
    t.insert(i, a)

operations = [
    (1, 5),
    (4, 8),
    (2, 9),
    (3, 7),
    (1, 10),
    (6, 11),
    (3, 5),
    (4, 6),
    (2, 8),
    (1, 7),
    (3, 9)
]

assert len(operations) == N

# Complejidad O(N log N)
for a, b in operations:
    t = multiswap_treap(t, a, b)

print('Treap multiswap: ', t.root)
```

Adicionalmente, para verificar que la implementacion es correcta, se puede comparar el resultado de `multiswap_treap` con el resultado de la implementacion original de `multiswap`:

```python
def multiswap_list(A, a, b):
    r = copy(A)

    i, j = a, b
    while i < b and j <= len(A):
        r[i - 1], r[j - 1] = r[j - 1], r[i - 1]
        i += 1
        j += 1

    return r

# Complejidad O(N * N)
for a, b in operations:
    A = multiswap_list(A, a, b)

print('List multiswap: ', A)
```

Los resultados de ambas implementaciones deben son iguales.

# Razonamiento

Notese que este problema es similar al de responder consultas de tipo `maxCon(a,b)` visto en clase, que se resolvio utilizando Heavy-Light decomposition (HLD). Partiendo de eso, vamos a realizar el siguiente precondicionamiento:

- Recorrer el arbol (utilizando DFS) para asignar a cada nodo `n` la cantidad de nodos que hay en el subarbol que tiene a `n` como raiz, esta cantidad se guardará en `n.size`. Este precondicionamiento se puede hacer en `O(N)` con memoria adicional `O(N)`.
- Obtener la descompocision heavy-light del arbol utilizando la cantidad `size` de cada nodo. Esto se puede hacer en `O(N)` con memoria adicional `O(N)`.
- Crear un segment tree para cada camino de la descomposicion heavy-light, que almacene dos resultados, uno para la operacion `forall` y otro para la operacion `exists`. Obterner el segment tree para una cadena es `O(c)`, donde `c` es la longitud de la cada cadena, por lo tanto, el costo total de crear los segment tree es dos veces la suma de las longitudes de todas las cadenas, es decir, `O(N)` en el peor caso. Todo esto con memoria adicional `O(N)`.

Con estos precondicionamientos, el costo de responder una consulta es `O(log(N))`, permitiendo que responder `Q` consultas tenga un costo de `O(N + Q * log(N))` con memoria adicional `O(N)`.

# Implementación

La implementación de la solución se encuentra en el archivo [pregunta-2-implementacion.py](pregunta-2-implementacion.py).

Esta implementación se construyó en base a la implementacion de la solucion para `maxCon` por _geeksforgeeks_ que se encuentra en [este enlace](https://www.geeksforgeeks.org/implementation-of-heavy-light-decomposition/).

Para adaptar la solucion a este problema, se realizaron las siguientes modificaciones:

- Para representar el predicado `p` sobre la conexiones del arbol, se le coloco a cada arista un peso de `1` en donde `p` es verdadero y `0` en caso contrario. De esta forma, el valor de `exists` y `forall` para un camino `u` a `v` se puede obtener con el maximo y minimo de los valores de las aristas en el camino `u` a `v` respectivamente.

- Se modifico la estructura de datos `SegmentTree` para que almacene dos valores, uno para la operacion `forall` y otro para la operacion `exists`. Ademas de esto, se modificaron las funciones auxiliares encargadas de construir y consultar la estructura `SegmentTree` para que se ajusten a las operaciones `forall` y `exists`.

- Se modifico la funcion `crawl_tree` y `query` para admitir un argumento adicional que especifica si se esta realizando una consulta `forall` o `exists`, y para que `query` retorne el valor booleano correspondiente a la operacion que se esta realizando.

- Adicionalmente, se recontextualizo el codigo para que se ajuste a la implementacion de la solucion para este problema. Documentando el codigo y agregando comentarios para que se entienda mejor el funcionamiento de la implementacion.

En el archivo de la implementacion se muestra un ejemplo de como utilizar la implementacion para resolver el problema, y se demuestra que da el resultado correcto paraun ejemplo de prueba. En concreto, se muestra como se puede utilizar la implementacion para resolver el problema de la siguiente forma:

```python
# CONSTRUCCIÓN DEL ÁRBOL
n = 11

"""
Para nuestro caso, utilizamos p como los pesos de las aristas
donde se coloca 1 si la arista es verdadera y 0 si es falsa.

A continuación se añaden las aristas al árbol.
(id, u, b, p({u,v}))
"""
add_edge(1, 1, 2, 1)
add_edge(2, 1, 3, 1)
add_edge(3, 1, 4, 0)
add_edge(4, 2, 5, 1)
add_edge(5, 2, 6, 0)
add_edge(6, 3, 7, 1)
add_edge(7, 6, 8, 0)
add_edge(8, 7, 9, 1)
add_edge(9, 8, 10, 1)
add_edge(10, 8, 11, 1)

"""
El arbol de ejemplo es el siguiente:
(si una arista no tiene valor de p, se asume que es 0)

            (1)
      1/    1|      \
      (2)    (3)     (4)
    1/ \    1|
    (5) (6)  (7)
        |   1|
        (8)  (9)
      1/  1\
    (10)  (11)
"""

# PRE-CONDICIONAMIENTO

root = 0
parent_of_root = -1
depth_of_root = 0

# 1. Recorrido DFS para obtener el tamaño de los nodos y la profundidad
dfs(root, parent_of_root, depth_of_root, n)

# 2. Descomposición del árbol en cadenas heavy

chain_heads = np.full(N, -1)

edge_counted = [0]
curr_chain = [0]

hld(root, n - 1, edge_counted, curr_chain, n, chain_heads)

# 3. Construcción de los arboles de segmentos para cada cadena heavy

construct_ST(0, edge_counted[0], 1)

# CONSULTAS

u = 10
v = 9
any_uv = query(u - 1, v - 1, n, chain_heads, 'any')
all_uv = query(u - 1, v - 1, n, chain_heads, 'all')
print(f"any({u}, {v}): {any_uv}")  # any(10, 9): True
print(f"all({u}, {v}): {all_uv}")  # all(10, 9): False
print()

u = 5
v = 9
any_uv = query(u - 1, v - 1, n, chain_heads, 'any')
all_uv = query(u - 1, v - 1, n, chain_heads, 'all')
print(f"any({u}, {v}): {any_uv}")  # any(5, 9): True
print(f"all({u}, {v}): {all_uv}")  # all(5, 9): True
```

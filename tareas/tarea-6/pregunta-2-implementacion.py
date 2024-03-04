import numpy as np

# Implemención base obtenida de: https://www.geeksforgeeks.org/implementation-of-heavy-light-decomposition/

# Tamaño maximo del arbol
N = 1024

# Matriz de adyacencias del arbol
tree = np.full((N, N), -1)


class Node:
    """
    Clase para representar un nodo del arbol.
    """

    def __init__(self):
        self.par = None  # Padre del nodo
        self.depth = None  # Profundidad del nodo
        self.size = None  # "tamaño" del nodo
        self.pos_segbase = None  # Posición en el segment tree
        self.chain = None  # Cadena heavy a la que pertenece el nodo


# Inicializar nodos
node = [Node() for _ in range(N)]


class Edge:
    """
    Clase para representar una arista del arbol.
    """

    def __init__(self):
        self.weight = None  # Peso de la arista
        self.deeper_end = None  # Nodo más profundo de la arista


# Inicializar aristas
edge = [Edge() for _ in range(N)]


class SegmentTree:
    """
    Clase para representar un Segment Tree.
    """

    def __init__(self):
        self.base_array = np.zeros(N)  # Arreglo base
        self.any = np.zeros(6 * N)  # Arreglo para el valor de "any"
        self.all = np.zeros(6 * N)  # Arreglo para el valor de "all"


# Inicializar Segment Tree
s = SegmentTree()


def add_edge(e, u, v, w):
    """
    Añade una arista al árbol.

    Args:
    - e (int): id de la arista
    - u (int): nodo u
    - v (int): nodo v
    - w (int): peso de la arista
    """

    tree[u - 1][v - 1] = e - 1
    tree[v - 1][u - 1] = e - 1
    edge[e - 1].weight = w


def dfs(curr, prev, dep, n):
    """
    Función recursiva para el recorrido DFS del árbol.

    Args:
    - curr (int): nodo actual
    - prev (int): nodo anterior
    - dep (int): profundidad
    - n (int): número de nodos
    """

    node[curr].par = prev
    node[curr].depth = dep
    node[curr].size = 1

    for j in range(n):
        if j != curr and j != node[curr].par and tree[curr][j] != -1:
            edge[tree[curr][j]].deeper_end = j
            dfs(j, curr, dep + 1, n)
            node[curr].size += node[j].size


def hld(curr_node, id, edge_counted, curr_chain, n, chain_heads):
    """
    Función recursiva que descompone el árbol en cadenas heavy.

    Args:
    - curr_node (int): nodo actual
    - id (int): id de la arista
    - edge_counted (list): contador de aristas
    - curr_chain (list): cadena actual
    - n (int): número de nodos
    - chain_heads (list): cabezas de las cadenas
    """

    if chain_heads[curr_chain[0]] == -1:
        chain_heads[curr_chain[0]] = curr_node

    node[curr_node].chain = curr_chain[0]
    node[curr_node].pos_segbase = edge_counted[0]
    s.base_array[edge_counted[0]] = edge[id].weight
    edge_counted[0] += 1

    spcl_chld = -1
    spcl_edg_id = None
    for j in range(n):
        if j != curr_node and j != node[curr_node].par and tree[curr_node][j] != -1:
            if spcl_chld == -1 or node[spcl_chld].size < node[j].size:
                spcl_chld = j
                spcl_edg_id = tree[curr_node][j]

    if spcl_chld != -1:
        hld(spcl_chld, spcl_edg_id, edge_counted, curr_chain, n, chain_heads)

    for j in range(n):
        if j != curr_node and j != node[curr_node].par and j != spcl_chld and tree[curr_node][j] != -1:
            curr_chain[0] += 1
            hld(j, tree[curr_node][j], edge_counted,
                curr_chain, n, chain_heads)


def construct_ST(ss, se, si):
    """
    Función recursiva que construye el arbol de segmentos para el arreglo [ss..se - 1].
    Como el arbol de segmentos calcula tanto el valor de "any" como el de "all", se
    realizan ambas operaciones en la misma función.

    Args:
    - ss (int): Indice de comienzo del arreglo.
    - se (int): Indice de fin del arreglo.
    - si (int): Indice del arreglo en la implementación `SegmentTree`.
    """

    if ss == se - 1:
        s.any[si] = s.base_array[ss]
        s.all[si] = s.base_array[ss]
        return s.base_array[ss], s.base_array[ss]

    mid = (ss + se) // 2
    st_left_any, st_left_all = construct_ST(ss, mid, si * 2)
    st_right_any, st_right_all = construct_ST(mid, se, si * 2 + 1)

    # Maximo sobre {0,1} para OR
    s.any[si] = max(st_left_any, st_right_any)

    # Minimo sobre {0,1} para AND
    s.all[si] = min(st_left_all, st_right_all)

    # Se retorna el valor de "any" y "all" para el nodo arreglo
    return s.any[si], s.all[si]


def LCA(u, v, n):
    """
    Función para obtener el ancestro común más bajo de dos nodos.

    Args:
    - u (int): nodo u
    - v (int): nodo v
    - n (int): número de nodos
    """

    LCA_aux = np.full(n + 5, -1)

    if node[u].depth < node[v].depth:
        u, v = v, u

    while u != -1:
        LCA_aux[u] = 1
        u = node[u].par

    while v:
        if LCA_aux[v] == 1:
            break
        v = node[v].par

    return v


def all_any_range_util(ss, se, qs, qe, index):
    """
    Función recursiva para obtener el valor de "any" y "all" en un rango de índices de segment tree.

    Args:
    - ss (int): Indice de comienzo del arreglo.
    - se (int): Indice de fin del arreglo.
    - qs (int): Indice de comienzo del rango.
    - qe (int): Indice de fin del rango.
    - index (int): Indice del arreglo en la implementación `SegmentTree`.
    """

    if qs <= ss and qe >= se - 1:
        return s.any[index], s.all[index]

    if se - 1 < qs or ss > qe:
        return 0, 1  # Elementos neutros de OR y AND

    mid = (ss + se) // 2

    left_any, left_all = all_any_range_util(ss, mid, qs, qe, 2 * index)
    right_any, right_all = all_any_range_util(mid, se, qs, qe, 2 * index + 1)

    return max(left_any, right_any), min(left_all, right_all)


def all_any_range(qs, qe, n):
    """
    Función para obtener el valor de "any" y "all" en un rango de índices de segment tree.

    Args:
    - qs (int): Indice de comienzo del rango.
    - qe (int): Indice de fin del rango.
    - n (int): número de nodos
    """

    if qs < 0 or qe > n - 1 or qs > qe:
        return 0, 1  # Elementos neutros de OR y AND

    return all_any_range_util(0, n, qs, qe, 1)


def crawl_tree(u, v, n, chain_heads, query='any'):
    """
    Función para moverse de u a v mientras se calcula el valor de "any" o "all".

    Args:
    - u (int): nodo u
    - v (int): nodo v
    - n (int): número de nodos
    - chain_heads (list): cabezas de las cadenas heavy
    - query (str): tipo de consulta ('any' o 'all')
    """

    chain_v = node[v].chain
    ans = 0 if query == 'any' else 1

    while True:
        chain_u = node[u].chain

        # Caso: u y v están en la misma cadena
        if chain_u == chain_v:
            if u != v:
                chain_any, chain_all = all_any_range(
                    node[v].pos_segbase + 1, node[u].pos_segbase, n)

                ans = max(ans, chain_any) if query == 'any' else min(
                    ans, chain_all)
            break

        # Caso: u y v no están en la misma cadena
        else:
            # Se calcula el valor de "any" o "all" para la cadena de u
            new_any, new_all = all_any_range(
                node[chain_heads[chain_u]].pos_segbase, node[u].pos_segbase, n)

            ans = max(ans, new_any) if query == 'any' else min(ans, new_all)

            # Se actualiza u al padre de la cabeza de la cadena
            u = node[chain_heads[chain_u]].par

    return ans


def query(u, v, n, chain_heads, query='any'):
    """
    Función para realizar una consulta de tipo "any" o "all".

    Args:
    - u (int): nodo u
    - v (int): nodo v
    - n (int): número de nodos
    - chain_heads (list): cabezas de las cadenas heavy
    - query (str): tipo de consulta ('any' o 'all')
    """

    lca = LCA(u, v, n)
    u_lca = crawl_tree(u, lca, n, chain_heads, query)
    v_lca = crawl_tree(v, lca, n, chain_heads, query)

    ans = max(u_lca, v_lca) if query == 'any' else min(u_lca, v_lca)

    return True if ans == 1 else False

# EJEMPLO DE USO


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

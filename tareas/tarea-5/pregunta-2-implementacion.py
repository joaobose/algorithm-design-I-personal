from queue import Queue


def is_prime(n):
    """
    n: entero

    Retorna True si n es un número primo, False en caso contrario.
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


class BipartiteGraph:
    """
    Clase que representa un grafo bipartito.
    """

    def __init__(self, left, right):
        """
        left: lista de enteros (vértices en el lado izquierdo)
        right: lista de enteros (vértices en el lado derecho)
        """

        self.left = left
        self.right = right
        self.adj = {i: [] for i in range(len(left) + 1)}

    def add_edge(self, u, v):
        """
        u: indice del vértice en el lado izquierdo
        v: indice del vértice en el lado derecho
        """

        self.adj[u].append(v)

    def __repr__(self):
        out = "BipartiteGraph:\n\n"
        out += "> Left:\n"
        out += f"{self.left}\n"
        out += "> Right:\n"
        out += f"{self.right}\n"
        out += "> Adjacency list:\n"
        for u in range(1, len(self.left) + 1):
            out += f"{u}: {self.adj[u]}\n"

        out += "> Edges:\n"
        for u in range(1, len(self.left) + 1):
            for v in self.adj[u]:
                r = self.right[v - 1]
                l = self.left[u - 1]
                out += f"{l} -> {r} | sum = {l + r}\n"

        return out


def min_removals(V):
    """
    V: lista de enteros

    Retorna el mínimo número de elementos que deben ser removidos de V
    de forma tal que no exista un par de elementos en V cuya suma sea
    un numero primo.
    """

    # Construccion del grafo bipartito O(n^2)
    even_V = [v for v in V if v % 2 == 0]
    odd_V = [v for v in V if v % 2 != 0]

    graph = BipartiteGraph(even_V, odd_V)

    for i, v in enumerate(even_V):
        for j, u in enumerate(odd_V):
            if is_prime(v + u):
                graph.add_edge(i + 1, j + 1)

    # Encontrar la cantidad de aristas en un matching máximo O(n^2 * sqrt(n))
    return hopcroft_karp_matching(graph)


def hopcroft_karp_matching(graph):
    """
    graph: instancia de la clase BipartiteGraph

    Retorna el número de aristas en un matching máximo en el grafo bipartito
    representado por graph.
    """

    NIL = 0
    INF = float("inf")

    # Matchings:
    # - pair_U[u]: es el vértice en el lado derecho que está
    #              emparejado con u en el lado izquierdo.
    # - pair_V[v]: es el vértice en el lado izquierdo que está
    #              emparejado con v en el lado derecho.
    pair_U = [NIL] * (len(graph.left) + 1)
    pair_V = [NIL] * (len(graph.right) + 1)

    # Distancia de los nodos en el lado izquierdo al nodo NIL
    # Si dist[u] is uno mas que dist[u'] entonces (u, u') es una arista
    # en un camino aumentante.
    dist = [0] * (len(graph.left) + 1)

    result = 0

    # BFS para encontrar un camino aumentante
    def bfs():
        q = Queue()

        for u in range(1, len(graph.left) + 1):
            if pair_U[u] == NIL:
                dist[u] = 0
                q.put(u)
            else:
                dist[u] = INF

        dist[NIL] = INF

        while not q.empty():
            u = q.get()

            if dist[u] < dist[NIL]:
                for v in graph.adj[u]:
                    if dist[pair_V[v]] == INF:
                        dist[pair_V[v]] = dist[u] + 1
                        q.put(pair_V[v])

        return dist[NIL] != INF

    # DFS para encontrar un camino aumentante a partir de u
    def dfs(u):
        if u != NIL:
            for v in graph.adj[u]:
                # Condición que verifica si (u, v) es una arista en el
                # camino aumentante
                if dist[pair_V[v]] == dist[u] + 1:
                    if dfs(pair_V[v]):
                        pair_V[v] = u
                        pair_U[u] = v
                        return True

            dist[u] = INF
            return False

        return True

    # Mientras exista un camino aumentante
    while bfs():
        # Encontramos un nodo libre
        for u in range(1, len(graph.left) + 1):
            # Si el nodo es libre y encontramos un camino aumentante
            # que termina en el nodo, incrementamos el matching
            if pair_U[u] == NIL and dfs(u):
                result += 1

    return result


V = [2, 8, 4, 5, 7, 13, 10]
print(min_removals(V))

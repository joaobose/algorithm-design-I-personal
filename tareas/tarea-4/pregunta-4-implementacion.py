EMPTY_SET = 0
PLANE = (0, 0)


def t(a, b):
    """
    a, b: Puntos representados como tuplas (x, y)

    Tiempo de transito entre dos puntos a y b.
    """

    x1, y1 = a
    x2, y2 = b

    x_diff = x1 - x2
    y_diff = y1 - y2

    return x_diff * x_diff + y_diff * y_diff


def pair(i, j):
    """
    i, j: Enteros

    Crea un conjunto con los elementos i y j.
    """

    return (1 << i) | (1 << j)


def join(S1, S2):
    """
    S1, S2: Conjuntos representados como mapas de bits (int)

    Une dos conjuntos S1 y S2.
    """

    return S1 | S2


def is_full(S, n):
    """
    S: Conjunto representado como un mapa de bits (int)

    Revisa si el conjunto S es de tamaño n.
    """

    return S == ((1 << n) - 1)


def is_in(S, i):
    """
    S: Conjunto representado como un mapa de bits (int)
    i: Entero

    Revisa si el elemento i esta en el conjunto S.
    """

    return S & (1 << i) != 0


def maletas(C):
    """
    C: Lista de n tuplas (x, y) con las coordenadas de las maletas.

    Calcula el tiempo minimo para recoger todas las maletas.
    """
    p = [None for _ in range(1 << len(C))]
    return maletas_dp(EMPTY_SET, C, p)


def maletas_dp(s, C, p):
    n = len(C)

    if is_full(s, n):
        return 0

    if p[s] is not None:
        return p[s]

    for i in range(n):
        if not is_in(s, i):
            best_t = float('inf')
            best_s = 0

            for j in range(i, n):  # Se comienza desde i para incluir {i}
                if not is_in(s, j):
                    if i == j:
                        t_ij = 2 * t(PLANE, C[i])
                    else:
                        t_ij = t(PLANE, C[i]) + t(C[i], C[j]) + t(C[j], PLANE)

                    if t_ij < best_t:
                        best_t = t_ij
                        best_s = pair(i, j)

            p[s] = best_t + maletas_dp(join(s, best_s), C, p)
            return p[s]


C = [(0, 2), (-1, 0)]
print(maletas(C))

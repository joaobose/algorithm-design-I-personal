# Este archivo es la implementacion del algoritmo propuesto en el archivo pregunta-3.md

class Nodo:
    k = 0
    l = 0
    bp = 0
    a = 0
    c = 0
    der = None
    izq = None

    def __init__(self, k, l):
        self.k = k
        self.l = l


class MaxBPResult:
    bp = 0
    a = 0
    c = 0


def construir_arbol_seg(S, k, l):
    h = Nodo(k, l)

    # Caso: Nodo hoja
    if k == l:
        h.bp = 0
        h.a = 1 if S[k] == '(' else 0
        h.c = 1 if S[k] == ')' else 0

        return h

    # Caso: Nodo intermedio
    m = (k + l) // 2

    h.izq = construir_arbol_seg(S, k, m)
    h.der = construir_arbol_seg(S, m + 1, l)

    match = min(h.izq.a, h.der.c)

    h.bp = h.izq.bp + h.der.bp + match
    h.a = h.izq.a + h.der.a - match
    h.c = h.izq.c + h.der.c - match

    # Debug: Imprimir el substring representado por el nodo h y sus valores de bp, a y c
    sbstr = S[k:l + 1]
    print(f'({k}, {l}) -> {sbstr} -> bp: {h.bp}, a: {h.a}, c: {h.c}')

    return h


def max_bp_impl(h, i, j):
    result = MaxBPResult()

    k = h.k
    l = h.l
    m = (k + l) // 2

    # Caso: El intervalo [k..l] representado por el nodo h es igual al intervalo [i..j]
    if i == k and j == l:
        result.bp = h.bp
        result.a = h.a
        result.c = h.c

        return result

    # Caso: El intervalo [i..j] esta contenido en el intervalo [k..m]
    if j <= m:
        return max_bp_impl(h.izq, i, j)

    # Caso: El intervalo [i..j] esta contenido en el intervalo [(m + 1)..l]
    if i > m:
        return max_bp_impl(h.der, i, j)

    # Caso: El intervalo [i..j] se divide en los intervalos [i..m] y [(m + 1)..j]
    result_izq = max_bp_impl(h.izq, i, m)
    result_der = max_bp_impl(h.der, m + 1, j)

    # Hacemos match de los parentesis que se abren en h.izq y se cierran en h.der
    match = min(result_izq.a, result_der.c)

    result.bp = result_izq.bp + result_der.bp + match
    result.a = result_izq.a + result_der.a - match
    result.c = result_izq.c + result_der.c - match

    return result


S = '())(())(())('
r = construir_arbol_seg(S, 0, len(S) - 1)


def max_bp(i, j):
    '''
    i, j: indices de los extremos del intervalo [i..j] inclusivos e indexados desde 1 hasta n
    '''

    global r

    return 2 * max_bp_impl(r, i - 1, j - 1).bp


print(max_bp(3, 10))

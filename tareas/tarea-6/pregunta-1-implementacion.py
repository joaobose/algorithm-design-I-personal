from copy import copy
from treap import ImplicitTreap
from random import randint


def multiswap_list(A, a, b):
    """
    Funcion multiswap demo.

    A (list): lista de elementos
    a (int): `1 <= a <= len(A)`
    b (int): `a <= b <= len(A)`
    """
    r = copy(A)

    i, j = a, b
    while i < b and j <= len(A):
        r[i - 1], r[j - 1] = r[j - 1], r[i - 1]
        i += 1
        j += 1

    return r


def multiswap_range(N, a, b):
    """
    Funcion para entender el rango de la operacion multiswap.
    Esta funcion no se utiliza en la solucion a esta pregunta, 
    sino que es una herramienta que ayuda a entender lo que 
    hace la operacion multiswap.

    Retorna el rango sobre el que opera la operacion multiswap.

    La operacion multiswap hace swap elemento a elemento de dos sub arreglos `sa` y `sb`. 

    El rango de `sa` es [a..min(a + N - b, b - 1)]
    El rango de `sb` es [b..min(b + (b - a) - 1, N)]
    """

    return list(range(a, min(a + N - b, b - 1) + 1)), \
        list(range(b, min(b + (b - a) - 1, N) + 1))


def multiswap_treap(treap, a, b, debug=False):
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

    if debug:
        print('Head: ', head)
        print('Sa: ', sa)
        print('Center: ', center)
        print('Sb: ', sb)
        print('Tail: ', tail)

    # Utilizar merge para obtener el arreglo: head, sb, center, sa, tail
    # (tiempo O(log N))
    t.root = t.merge(head, sb)
    t.root = t.merge(t.root, center)
    t.root = t.merge(t.root, sa)
    t.root = t.merge(t.root, tail)

    return t


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

# Complejidad O(N * N)
for a, b in operations:
    A = multiswap_list(A, a, b)

print('List multiswap: ', A)

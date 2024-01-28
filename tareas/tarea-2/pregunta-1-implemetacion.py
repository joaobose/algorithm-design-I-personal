

def vallas(P, T):
    '''
    Resulve el problema planteado en la pregunta 1 de la tarea 2.

    Complejidad en tiempo: `O(n log n)`
    Complejidad en espacio: `O(n)`

    Parametros:
        `P`: Lista de enteros positivos que representan la posicion en la que debe comenzar de la valla `i`.
        `T`: Lista de enteros positivos que representan el tamaño de la valla `i`.

    Retorna:
        Una lista de indices de las vallas a contruir de forma que se maximice el numero de vallas construidas.
    '''
    n = len(P)
    sol = []  # O(n) en espacio

    # Ordenar los indices de las peticiones por la posicion final de la valla
    indices = list(range(0, n))  # O(n) en espacio
    indices.sort(key=lambda i: P[i] + T[i])  # O(n log n) en tiempo

    # final de la ultima valla construida
    last = 0

    # O(n) en tiempo
    for i in indices:
        # Si se puede construir la valla i
        if P[i] >= last:
            # Agregar la valla i a la solucion
            sol.append(i + 1)  # los indices comienzan en 1

            # Actualizar el final de la ultima valla construida
            last = P[i] + T[i]

    return sol


# O(n) en espacio
P = [1, 2, 3]
T = [4, 1, 4]


print(vallas(P, T))

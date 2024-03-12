import numpy as np


def vec(i, f):
    """
    Calcula el vector que va desde el punto inicial al punto final.
    """

    i_x, i_y = i
    f_x, f_y = f

    return np.array([f_x - i_x, f_y - i_y])


def cruz(v1, v2):
    """
    Calcula el módulo del producto cruz entre dos vectores en 2D.
    """

    v1_x, v1_y = v1
    v2_x, v2_y = v2

    return v1_x * v2_y - v1_y * v2_x


def convex_hull(points):
    """
    Calcula el cierre convexo de un conjunto de puntos en 2D.
    """
    ch = []
    lowest_right = min(points, key=lambda p: (p[1], -p[0]))
    rest_points = [p for p in points if p != lowest_right]
    p = lowest_right

    # Ordenar los puntos de acuerdo al ángulo polar con respecto al punto más
    # bajo a la derecha y el eje x. (se asume que arctan2 es O(1))
    points = sorted(rest_points, key=lambda p: np.arctan2(
        p[1] - lowest_right[1], p[0] - lowest_right[0]))

    ch.append(p)
    ch.append(points[0])

    for i in range(1, len(points)):
        while cruz(vec(ch[-2], ch[-1]), vec(ch[-1], points[i])) < 0:
            ch.pop()
        ch.append(points[i])

    return set(ch)


def onion_convex_hull(points):
    """
    Calcula el número de capas de un cierre convexo de un conjunto de puntos en 2D.
    """

    pset = set(points)
    count = 0

    # Numero maximo de capas, n
    for _ in range(0, len(points)):
        if len(pset) == 0:
            break

        if len(pset) == 1:
            count += 1
            break

        pset -= convex_hull(pset)
        count += 1

    return count


POINTS = [
    # Primera capa: cuadrado 10x10 centrado en el origen
    (0, 0),
    (0, 10),
    (10, 10),
    (10, 0),
    # Segunda capa: cuadrado 6x6 centrado en (1, 1)
    (1, 1),
    (1, 7),
    (7, 7),
    (7, 1),
    # Tercera capa: cuadrado 2x2 centrado en (2, 2)
    (2, 2),
    (2, 4),
    (4, 4),
    (4, 2),
    # Cuarta capa: punto en (3, 3)
    (3, 3)
]

print(onion_convex_hull(POINTS))  # 4

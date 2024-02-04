import numpy as np

R = np.array([[0, 1, 1], [1, 0, 0], [0, 1, 0]])
VR = np.array([[2, 0, 3]]).T


def p(n):
    # Se evita n = 0 para no calcular la matriz inversa
    if n == 0:
        return 3

    m_power = np.linalg.matrix_power(R, n - 1)
    r = m_power @ VR

    return r[1][0]


for i in range(0, 15):
    print(f"p({i}) = {p(i)}")

import numpy as np
from math import ceil, log2


def freivalds_inverse(A, B, epsilon):
    n = len(A)
    k = ceil(log2(1 / epsilon))

    for _ in range(k):
        X = np.random.randint(0, 2, n)

        XA = np.dot(X, A)
        XAB = np.dot(XA, B)

        XC = X  # X x I

        if not np.allclose(XC, XAB, atol=0.0001):
            return False

    return True


A = np.array([
    [1, 2, 3],
    [3, 2, 1],
    [2, 1, 3]
])
B = np.array([
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5]
])

A_INV = np.linalg.inv(A)

print(freivalds_inverse(A, B, 0.001))  # False
print(freivalds_inverse(A, A_INV, 0.001))  # True

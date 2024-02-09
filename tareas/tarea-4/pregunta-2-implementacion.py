import numpy as np


def good_subarrays(A):
    n = len(A)
    b = [[0] * (n + 1) for _ in range(n + 1)]

    for j in range(1, n + 1):
        b[1][j] = j

    for i in range(2, n + 1):
        for j in range(1, n + 1):
            b[i][j] = (b[i - 1][j - 1] if A[j - 1] %
                       i == 0 else 0) + b[i][j - 1]

    return sum(b[i][n] for i in range(1, n + 1))


def good_subarrays_optim(A):
    n = len(A)
    b = [0] * (n + 1)
    b_prev = [0] * (n + 1)
    count = 0

    # Casos base
    for j in range(1, n + 1):
        b[j] = j
    count += b[n]

    # Llenar la tabla
    for i in range(2, n + 1):
        b, b_prev = b_prev, b

        for j in range(1, n + 1):
            b[j] = b_prev[j - 1] if A[j - 1] % i == 0 else 0
            b[j] += b[j - 1]

        count += b[n]

    return count


A = [2, 2, 1, 22, 15]

print(good_subarrays(A))
print(good_subarrays_optim(A))

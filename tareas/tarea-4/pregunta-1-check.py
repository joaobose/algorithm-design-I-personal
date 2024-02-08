import numpy as np


def distance_table(A, B):
    n = len(A)
    m = len(B)

    d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(len(A) + 1):
        d[i][0] = i

    for j in range(1, len(B) + 1):
        d[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])

    return np.array(d)


print(distance_table("joao", "pinto"))

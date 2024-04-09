def min_cover_aprox(C):
    R = set()
    C_prime = [w.copy() for w in C]

    while C_prime:
        u, v = C_prime.pop()

        R.add(u)
        R.add(v)

        C_prime = [w for w in C_prime if u not in w and v not in w]

    return R


C = [
    {0, 1},
    {0, 2},
    {1, 3},
    {3, 4},
    {4, 5},
    {5, 6}
]

print(min_cover_aprox(C))  # {0, 2, 3, 4, 5, 6}

C = [
    {0, 3},
    {2, 3},
    {1, 3}
]

print(min_cover_aprox(C))  # {1, 3}
# R* = {3} => |R*| = 1
# |R| = 2 <= 2 * |R*| = 2

C = [
    {0, 2},
    {2, 4},
    {4, 1},
    {4, 3}
]

print(min_cover_aprox(C))  # {0, 2, 3, 4}
# R* = {4, 2} => |R*| = 2
# |R| = 4 <= 2 * |R*| = 4

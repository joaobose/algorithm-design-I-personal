from random import randint
from math import sqrt, ceil


def miller_rab_test(a, n):
    s = 0
    t = n - 1

    print(f'miller_rab_test a = {a}, n = {n}')

    print(f's = {s}, t = {t}')

    while t % 2 == 0:
        t //= 2
        s += 1

        print(f's = {s}, t = {t}')

    x = pow(a, t, n)  # x = a^t mod n

    print(f'x = {x}')

    if x == 1 or x == n - 1:
        print('Return True...')
        return True

    print('Iterando...')

    for _ in range(s - 1):
        x = pow(x, 2, n)

        print(f'x = {x}, n - 1 = {n - 1}')

        if x == n - 1:
            print('Return True...')
            return True

    print('Return False...')

    return False


def miller_rabin(n):
    a = randint(2, n - 2)
    return miller_rab_test(a, n)


def miller_rabin_rep(n, k):
    for i in range(k):
        print(f"Test {i + 1}")

        if not miller_rabin(n):
            return False

    return True


K = 10

N = 171049017104901710490 - 1

print(f'Es {N} primo?: {miller_rabin_rep(N, K)}')

# BIG_PRIME = 222334565193649

# print(f'Es {BIG_PRIME} primo?: {miller_rabin_rep(BIG_PRIME, K)}')

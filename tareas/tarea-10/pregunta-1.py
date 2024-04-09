from random import randint
from math import log2, ceil, pow, gcd
from scipy.fft import fft
import numpy as np


def pow_mod(base, exp, mod):
    return int(pow(base, exp) % mod)


def shor_simulation(N, attempts=10):
    print(f"Factorizacion de N = {N}")

    for _ in range(attempts):
        print(f"\nIntento {_ + 1}:")
        print("---------------------")

        x = randint(1, N - 1)
        print(f"Escogemos x = {x}")

        n = int(pow(2, ceil(log2(N))))
        print(f"Sea n = {n} >= {N}")

        s = ceil(2 * log2(n))
        print(f"Se realizaran s = {s} iteraciones")

        js = []

        a_q = list(range(0, N - 1))
        print(f"Registro a_q = {a_q}")

        f_q = [pow_mod(x, a, N) for a in a_q]
        print(f"Registro x^a mod N = {f_q}")

        for i in range(s):
            print(f"\nIteracion {i + 1}:")
            print("-------------")

            f_q = fft(f_q)
            f_q = [abs(f) for f in f_q]
            print(f"FFT de f_q = {f_q}")

            collapsed = np.random.choice(
                a=range(0, N - 1), p=f_q / sum(f_q))
            print(f"Colapsamos FFT(f_q) y obtenemos el indice {collapsed}")

            if collapsed != 0:
                js.append(collapsed)

        print(f"\nObtenemos los valores de j = {js}")

        if len(js) == 0:
            print(f"\nNo se encontro factor no trivial")
            continue

        g = gcd(*js)

        print(f"\nCalculamos el mcd de los valores de j: {g}")
        print(f"N / g = {N} / {g} = {N // g}")

        if (N // g) % 2 == 0:
            t = int(pow(x, N // (2 * g)))
            print(f"t = x^(N / 2g) = {t}")

            upper = gcd(t + 1, N)
            lower = gcd(t - 1, N)

            print(f"gcd(t + 1, N) = gcd({t} + 1, {N}) = {upper}")
            print(f"gcd(t - 1, N) = gcd({t} - 1, {N}) = {lower}")

            factors = set([upper, lower])
            non_trivial = [f for f in factors if f != 1 and f != N]

            if len(non_trivial) > 0:
                print(
                    f"\nFactor(es) no trivial(es) encontrado(s): {non_trivial}", ", intentos:", _ + 1)
                return non_trivial

        print(f"\nNo se encontro factor no trivial")

    return None


N = 21
attempts = 10
print(shor_simulation(N, attempts))

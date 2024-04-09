Consideramos el numero $171049017104901710490 - 1$.

Sea:

- $MRP: \mathbb{N} \times \mathbb{N} \to \mathbb{B}$ una implementación del algoritmo de Miller-Rabin repetido.

- $R: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ una función que genera un número aleatorio en el rango $[x, y]$.

- $B: \mathbb{N} \times \mathbb{N} \to \mathbb{B}$ una implementación de las funcion `BTest` que verifica si un número pertenece a $B(n)$.

Ejecutemos el algoritmo de Miller-Rabin repetido con $k=10$.

1. $MRP(171049017104901710489, 10)$
   1. Iteración 1:
      1. $a = R(2, 171049017104901710487) = 140090267228246698995$
      2. $check = B(a, 171049017104901710489)$
         1. $s = 0$
         2. $t = 171049017104901710489 - 1 = 171049017104901710488$
         3. Como $t$ es par, entonces $s = s + 1 = 1$ y $t = t / 2 = 85524508552450855244$
         4. Como $t$ es par, entonces $s = s + 1 = 2$ y $t = t / 2 = 42762254276225427622$
         5. Como $t$ es par, entonces $s = s + 1 = 3$ y $t = t / 2 = 21381127138112713811$
         6. $x = a^t \mod 171049017104901710489 = 15880694395621420656$
         7. Como $x \neq 1$ y $x \neq 171049017104901710488$ continuamos.
         8. Como $s = 3$ realizamos $s - 1 = 2$ iteraciones.
            1. $x = x^2 \mod 171049017104901710489 = 45413712848816067924$
            2. Como $x \neq 171049017104901710488$ continuamos.
            3. $x = x^2 \mod 171049017104901710489 = 73444763286272242918$
            4. Como $x \neq 171049017104901710488$ continuamos.
         9. Retornamos $false$.
      3. Como $check = false$ retornamos $false$.

Finalmente, para el numero $171049017104901710490 - 1$ el algoritmo de Miller-Rabin repetido con $k=10$ retorna $false$.

EL resultado esperado se obtuvo en una sola iteración, no hizo falta realizar las 9 iteraciones restantes.
         
# Diseño

Sea un grafo no dirigido $G = (N, C)$. 

Para resolver el problema `1-relativo-MIN-COVER` se parte de la intuicion de la solucion a fuerza bruta, en donde iteramos sobre todos los subconjuntos de $N$, cuando se encuentra un subconjunto que es un cubrimiento valido, se compara con el cubrimiento actual y se actualiza si es de menor cardinalidad.

Como no es practico iterar sobre todos los subconjuntos de vertices de $N$ en tiempo polinomial, se propone un algoritmo cuyo enfoque es producir un cubribiento valido de $G$ en tiempo polinomial.

### Algoritmo 1

1. $R \leftarrow \empty$
2. $C^{\prime} \leftarrow C$
3. Mientras $C^{\prime} \neq \empty$:
    1. Sea $\{u,v\}$ un lado arbitrario en $C^{\prime}$.
    2. $R \leftarrow R \cup \{u,v\}$
    3. $C^{\prime} \leftarrow C^{\prime} - \{w \in C^{\prime} | u \in w \lor v \in w \}$
 4. Retornar $R$

Si $R$ se implementa como un `hashset`, y $C^{\prime}$ como una lista de adyacencias, el algoritmo se ejecuta en tiempo $O(N + C) = O(|N|^2)$, y por lo tanto, es polinomial.

Ahora, demostremos que el algoritmo es 1-relativo de `MIN-COVER`, esto es, probar:

### Teorema 1

Sea $R$ y $R^*$ los cubrimientos producidos por el algoritmo 1 y el algoritmo optimo, respectivamente. Entonces, $|R^*| \leq |R| \leq 2 |R^*|$.

### Demostración

Primero veamos que $|R^*| \leq |R|$. 

Como $R^*$ es un cubrimiento optimo, entonces basta con ver que $R$ es un cubrimiento valido. Para esto, notemos que en cada iteracion del algoritmo 1, se considera un lado $\{u,v\} \in C'$ y se agregan $u$ y $v$ a $R$. Ademas, se eliminan todos los lados que inciden en $u$ o $v$ en $C'$, como $C'$ comienza siendo $C$, entonces al cuando el ciclo 3 termina, todos los lados de $G$ tienen un extremo en $R$, por lo tanto $R$ es un cubrimiento valido.

Entonces, $|R^*| \leq |R|$. **[1]**

Luego, veamos que $|R| \leq 2 |R^*|$. 

Sea $A$ el conjunto de lados seleccionados por el paso 3.1 del algoritmo 1. Como en el paso 3.2 se agregan dos vertices por cada lado en $A$, entonces $|R| \leq 2 |A|$. Ademas, como en la linea 3.3 se eliminan los lados que incidan en nodos agregados a $R$, entonces los elementos agregados a $R$ aparecen sin duplicados, y por lo tanto $|R| = 2|A|$, que es lo mismo que $\frac{1}{2}|R| = |A|$ **[2]**.

Ademas, como **no** hay dos lados en $A$ que sean cubiertos por el mismo vertice en $R^*$ (debido al paso 3.3 y 3.1), entonces $|A| \leq |R^*|$ **[3]**.

Combinando **[2]** y **[4]** tenemos:

$$
|A| \leq |R^*| \\
\Rightarrow \\
\frac{1}{2}|R| \leq |R^*| \\
\Rightarrow \\
|R| \leq 2|R^*|
$$

Finalmente, como $|R^*| \leq |R|$ y $|R| \leq 2|R^*|$, entonces:

$$
|R^*| \leq |R| \leq 2|R^*|
$$

### Q.E.D.

# Implementación

Para hacer la implementación sea mas sencilla, se propone implementar $C$ como una lista de lados, en donde cada lado es un conjunto de dos vertices, de esta forma, la implementación del algoritmo 1 es directa de la definición.

Por supuesto que esto implica un cambio en la complejidad del algoritmo, ya que ahora $C^{\prime}$ es una lista de tamaño $O(|C|)$, y por lo tanto, el paso 3.3 del algoritmo 1 tiene una complejidad de $O(|C|) = O(|N|^2)$, y por lo tanto, el algoritmo 1 tiene una complejidad de $O(|N|^3)$ en el peor caso.

Sin embargo, esto sigue siendo tiempo polinomial, y por lo tanto, el algoritmo 1 sigue siendo polinomial, cumpliendo con el requerimiento de tiempo.

```python
def min_cover_aprox(C):
    R = set()
    C_prime = [w.copy() for w in C]

    while C_prime:
        u, v = C_prime.pop()

        R.add(u)
        R.add(v)

        C_prime = [w for w in C_prime if u not in w and v not in w]

    return R
```

La implementación del algoritmo se encuentra en el archivo [pregunta-3.py](pregunta-3.py), junto con algunos casos de prueba.
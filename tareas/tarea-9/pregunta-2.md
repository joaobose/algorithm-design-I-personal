Se sospecha que B es la matriz inversa de A. Esto es, que $B = A^{-1}$. 

Para comprobar esto, utilizamos el metodo de Freivalds $k$ veces para comprobar que $A \times B = I$, donde $I$ es la matriz identidad.

Si el error permitido es $\epsilon$, queremos que:

$$
\epsilon \geq  \frac{1}{2^k} \\

\Rightarrow \\

2^k \geq \frac{1}{\epsilon} \\

\Rightarrow \\

k \geq \log \left( \frac{1}{\epsilon} \right)
$$

Por lo tanto, si queremos que el error sea menor o igual a $\epsilon$, debemos repetir el metodo de Freivalds con $k = \lceil \log \left( \frac{1}{\epsilon} \right) \rceil$.

Dicho esto, el pseudocódigo para comprobar si $B = A^{-1}$ es el siguiente:

```python
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

```

Este algorithmo se ejecuta en tiempo $O(n^2 \cdot \log \left( \frac{1}{\epsilon} \right) )$, lo cual cumple con el requerimiento de tiempo.

La implementación del algoritmo se encuentra en el archivo [pregunta-2.py](pregunta-2.py), junto con algunos casos de prueba.

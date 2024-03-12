def KMP_pre(x):
    """
    Retorna el arreglo de pre-procesamiento de Knuth-Morris-Pratt sobre la cadena x.
    """

    b = [0] * (len(x) + 1)
    b[0], j = -1, -1

    for i in range(1, len(x) + 1):
        while j >= 0 and x[i - 1] != x[j]:
            j = b[j]

        j += 1
        b[i] = j

    return b


def LPS_value(x):
    """
    Retorna el valor de la subcadena más larga que es un prefijo y sufijo de x.
    """

    b = KMP_pre(x)
    l = b[-1]

    if l == -1:
        return ''

    return x[:l]


print(LPS_value('SEVENTY SEVEN'))  # 'SEVEN'
print(LPS_value('ABRACADABRA'))  # 'ABRA'
print(LPS_value('AREPERA'))  # 'A'
print(LPS_value('ALGORITMO'))  # ''
print(LPS_value('aaaaa'))  # 'aaaa'
print(LPS_value('aaaaaa'))  # 'aaaaa'

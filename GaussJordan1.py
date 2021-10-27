import numpy as np

def GAUSSJORDAN(AB):
    casicero = 1e-15  # Considerar como 0
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]
    for i in range(0, n - 1, 1):
        columna = abs(AB[i:, i])
        dondemax = np.argmax(columna)
        if (dondemax != 0):
            temporal = np.copy(AB[i, :])
            AB[i, :] = AB[dondemax + i, :]
            AB[dondemax + i, :] = temporal
    for i in range(0, n - 1, 1):
        pivote = AB[i, i]
        adelante = i + 1
        for k in range(adelante, n, 1):
            factor = AB[k, i] / pivote
            AB[k, :] = AB[k, :] - AB[i, :] * factor
    ultfila = n - 1
    ultcolumna = m - 1
    for i in range(ultfila, 0 - 1, -1):
        pivote = AB[i, i]
        atras = i - 1
        for k in range(atras, 0 - 1, -1):
            factor = AB[k, i] / pivote
            AB[k, :] = AB[k, :] - AB[i, :] * factor
        AB[i, :] = AB[i, :] / AB[i, i]
    AB=np.round(AB, decimals = 4)
    return AB

A = np.array([[2., 1., 0.,4.],
            [-4., -2.0, 3.0,-7.0],
            [4., 1.0,-2 , 8],
           [0 ,-3, -12, -1]], dtype=float)
B = np.array([[2],
              [-9],
              [2],
              [2]], dtype=float)
AB = np.concatenate((A, B), axis=1)
print(GAUSSJORDAN(AB))
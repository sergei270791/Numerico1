import numpy as np
import sympy as sp
def Matrixmonde(n,puntos):
    A=np.zeros((n, n))
    for i in range(n):
        lista=list()
        for j in range(n):
            lista.append(puntos[j][0]**i)
        A[:, i] = np.transpose(np.array(lista))
    return A

def CoeficientesIndeterminados(A,n,puntos):
    lista=list()
    for j in range(n):
        lista.append(puntos[j][1])
    b=np.transpose(np.array(lista))
    c=np.dot(np.linalg.inv(A),b)
    return c


n=4
puntos=np.array([[-1,2],[0, 1],[-2, 3],[1, 0]])
A=Matrixmonde(n,puntos)
inv=np.linalg.inv(A)
coeficientes=CoeficientesIndeterminados(A,n,puntos)
print(coeficientes)
x=sp.symbols("x")
m=sp.Lambda(x,sum(coeficientes[k]*x**(k) for k in range(n)))
print(m)


import numpy as np


def iterativo(M,c,tol=1E-6):
  x=np.transpose([0.3,1.5,6.375])
  aux=x
  print("El x en la iteracion 0  es: ",x)
  x=np.dot(M,x)+c
  i=1
  while np.linalg.norm(x-aux, np.inf)/ np.linalg.norm(x, np.inf)>tol:
    print("El x en la iteracion",i," es: ",x)
    aux=x
    x=np.dot(M,x)+c
    i=i+1
  x=np.round(x,4)
  print("La respuesta en la iteración ",i," es:",x)
  print("El numero de iteraciones es: ", i)


def JacobiRichardson(A,b):
  n=len(A)
  I=np.identity(n)
  D=np.diag(np.diag(A))
  invD=np.linalg.inv(D)
  J=I-np.dot(invD,A)
  c=np.dot(invD,b)
  iterativo(J,c)


A = np.array([[10,1,2],[4,6,-2],[-2,3,8]],float)
b = np.array([3,9,51])
b=np.transpose(b)
JacobiRichardson(A,b)



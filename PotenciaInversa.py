import numpy as np
import sys
def PotenciaInversa(A,x,o,tol):
  k=0
  aux=0
  aux2=0
  aux4=0
  while abs(aux4)>tol or aux==0:
    k=k+1
    if k==3:
      aux=1
    aux3=aux2
    x=np.dot(np.linalg.inv(A),x)
    aux2=np.amax(x)
    x=x/aux2
    aux4=abs(aux2-aux3)
  aux2=o+1/aux2
  aux2=round(aux2,6)
  print("El autovalor dominante es {}".format(aux2))
  print("El numero de iteraciones es {}".format(k))
  x=np.around(x, decimals=6)
  return np.transpose(x)

A = np.array([[3.0, -1.0, 0.0],
                [-1.0, 2.0, -1.0],
                [0.0, -1.0, 3.0]],float)

x=np.transpose(np.matrix([5.0,1.0,1.0]))
o=2.8
A=A-o*np.identity(3)

x=PotenciaInversa(A,x,o,1.0e-7)
print(x)
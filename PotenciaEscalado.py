import numpy as np

def PotenciaEscalada(A,x,tol):
  k=0
  aux=0
  aux2=np.amax(x)
  while abs(aux2-aux)>=tol:
    aux=aux2
    k=k+1
    x=np.dot(A,x)
    aux2=np.amax(x)
    x=x/aux2
  
  print("El autovalor dominante es {}".format(aux2))
  print("El numero de iteraciones es {}".format(k))
  return np.transpose(x)

x = np.array([[1,0,0]]).T
A = np.array([[1, 3, -2],
            [-1, -2, 3],
            [1, 1, 2]])
x=PotenciaEscalada(A,x,1.0e-19)
print(x)

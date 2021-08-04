import numpy as np

def MetodoNewton(J,f,x,tol=1.0e-5):
  k=0
  x=x
  while np.linalg.norm(f(x)) > tol:
    x=x-np.transpose(np.dot(np.linalg.inv(J(x)),f(x)))
    k+=1
    x=x.ravel().tolist()
    print("La solucion para la iteracion numero",k,"es: ");
    print(x)
  print("El metodo termino con "+str(k)+" iteraciones")

def J(x):
  Jf=np.zeros((2,2))
  Jf[:,0]=np.transpose([x[1],x[1]+5])
  Jf[:,1]=np.transpose([x[0],x[0]+5])
  return Jf

def f(x):
  ft=np.zeros((2, 1))
  ft[0,0]=x[0]*x[1]-42
  ft[1,0]=(x[0]+5)*(x[1]+5)-132
  return ft

x0=[3.,4.]
print("Alumno: Calle Cuadros Sergei")
print("Pregunta 2.B")
MetodoNewton(J,f,x0)
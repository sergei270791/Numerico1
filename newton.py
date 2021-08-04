import math
def newton(f1,f2, a, b, tol=1.0e-12):
  if tol <= 0:
    raise ValueError("La cota de error debe ser un número positivo")
  x0=0
  x = (a + b) / 2.0
  i=0
  while abs(x-x0) >= tol:
      x0 = x
      x = x0-f1(x0)/f2(x0)
      i+=1
#  print("El número de iteraciones es: ",i)
  return x

def funcion(x):
  x=x**7-17.0859375
  return x

def derivada(x):
  x= 7*x**6
  return x
print("Continuacion del problema 2")
print("c)La solucion es: ",newton(funcion,derivada,1,2,tol =1.0e-6 ))
print("El vuelto es: ",5.0-newton(funcion,derivada,1,2,tol =1.0e-6 ))

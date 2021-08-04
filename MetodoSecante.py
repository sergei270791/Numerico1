import math
def secante(f, a, b, tol=1.0e-6):
  if tol <= 0:
    raise ValueError("La cota de error debe ser un número positivo")
  x0=0
  x = (a + b) / 2.0
  i=0
  while abs(x-x0) >= tol:
      aux=x0
      x0 = x
      x = x0-f(x0)*(x0-aux)/(f(x0)-f(aux))
      i+=1
  print("El número de iteraciones es: ",i)
  return x

def funcion(x):
  x=x**2-10
  return x


print("La solucion es: ",secante(funcion,3,4,1.0e-4))
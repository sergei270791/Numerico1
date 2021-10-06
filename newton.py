import math
def newton(f1,f2, a, b, tol=1.0e-12):
  if tol <= 0:
    raise ValueError("La cota de error debe ser un número positivo")
  x0=0
  x = (a + b) / 2.0
  i=0
  while abs(x-x0) >= tol and i<100:
      x0 = x
      x = x0-f1(x0)/f2(x0)
      i+=1
#  print("El número de iteraciones es: ",i)
  return x

def funcion(x):
  x=x**3+9*x**2+26*x+24
  return x

def derivada(x):
  x= 3*x**2+18*x+26
  return x
print("problema 3")
print("Calle Cuadros Sergei")
x=[newton(funcion,derivada,-5,-3.57,tol =1.0e-8 ),newton(funcion,derivada,-3.57,-2.42,tol =1.0e-8 ),newton(funcion,derivada,-2.42,-1,tol =1.0e-9 )]
print("La soluciones son: ",x)
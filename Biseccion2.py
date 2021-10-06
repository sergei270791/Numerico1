from math import sqrt,log
import numpy as np

def biseccion2(f, a, b, tol=1.0e-6):
    if a > b:
      raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0:
      raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
      raise ValueError("La cota de error debe ser un número positivo")
    i=1
    x=0
    while abs(a-b) >= tol:
      x=(a+b)/2.0
      if f(x)==0:
        a=b=x
      elif np.sign(f(x))*np.sign(f(b))>0:
        b=x
      else: 
        a=x
      i+=1
    print("El numero de iteraciones es: ",i)
    return x

def func(x):
  x=x**4+5*x**3+77*x**2+153*x+90
  return x
# Metodo de Biseccion

sol = biseccion2(func,-4,-2,1.0e-5)
print("Solucion aproximada por Biseccion: ",sol)
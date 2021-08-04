from math import sin, sqrt,log
import numpy as np

def ReglaFalsa(f, x0, tol=1.0e-6):
    if tol <= 0:
      raise ValueError("La cota de error debe ser un número positivo")
    i=0
    while abs(f(x0)-x0) >= tol:
      x0 = f(x0)
      i+=1
    print("El numero de iteraciones es: ",i)
    return x0

def func(x):
    return 4+(1/3)*(sin(2*x))
# Metodo de Punto Fijo

sol = ReglaFalsa(func,0,1.0e-5)
print("Solucion aproximada por Punto Fijo: ",sol)
from math import log
import numpy as np

def PuntoFijo(f, x0, tol=1.0e-6):
    max_iter=100
    if tol <= 0:
      raise ValueError("La cota de error debe ser un número positivo")
    i=0
    while abs(f(x0)-x0) >= tol and i<max_iter:
      x0 = f(x0)
      i+=1
    if abs(f(x0)-x0) >= tol:
      print('El metodo no converge')
    else:
      print("Solucion aproximada por Punto Fijo: ",x0)
      print("El numero de iteraciones es: ",i)

def func(x):
    return x+log(x)
# Metodo de Punto Fijo

PuntoFijo(func,0.4,1.0e-4)

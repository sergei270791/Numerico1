from math import sqrt,log
import numpy as np

def ReglaFalsa(f, a, b, tol=1.0e-6):
    if a > b:
      raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0:
      raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
      raise ValueError("La cota de error debe ser un número positivo")
    i=0
    x=0
    while abs(a-b) >= tol:
      x = a-f(a)*(a-b)/(f(a)-f(b))
      i+=1
      if f(x)==0:
        a=b=x
      elif np.sign(f(x))*np.sign(f(a))<0:
        b=x
      else: 
        a=x
    print("El numero de iteraciones es: ",i)
    return x

def func(x):
    return x**2-10
# Metodo de Regla Falsa

sol = ReglaFalsa(func,3,4,1.0e-5)
print("Solucion aproximada por Regla falsa: ",sol)
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
    while abs(a-b) >= tol and i<100:
      x = a-f(a)*(a-b)/(f(a)-f(b))
      i+=1
      if f(x)==0:
        a=b=x
      elif np.sign(f(x))*np.sign(f(a))<0:
        b=x
      else: 
        a=x
    if b-a>= tol:
      print("El metodo Regla Falsa no converge")
    else:
      print("Solucion aproximada por Regla falsa: ",x)
      print("El numero de iteraciones es: ",i)


def ReglaFalsaModificada(f, a, b, tol=1.0e-6):
    if a > b:
      raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0:
      raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
      raise ValueError("La cota de error debe ser un número positivo")
    k=1
    x = b-f(b)*(b-a)/(f(b)-f(a))
    while abs(f(x)) > tol and abs(a-b) >= tol and k<100:
      if np.sign(f(x))*np.sign(f(b))<0:
        a=b
        fa=f(a)
      else: 
        fa=0.5*f(a)
      k=k+1
      b=x
      x=x = b-f(b)*(b-a)/(f(b)-fa)
    if b-a>= tol:
      print("El metodo Regla Falsa modificado no converge")
    else:
      print("Solucion aproximada por Regla falsa modificada: ",x)
      print("El numero de iteraciones es: ",k)


func=lambda x: 230*x**4 + 18*x**3 + 9*x**2 -221*x - 9
print("Para el intervalo [-1,0]:")
ReglaFalsa(func,-1,0,1.0e-6)
ReglaFalsaModificada(func,-1,0,1.0e-6)
print("\nPara el intervalo [0,1]:")
ReglaFalsa(func,0,1,1.0e-6)
ReglaFalsaModificada(func,0,1,1.0e-6)
from math import log

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
    print("El número de iteraciones es: ",i)
    return x


def newtonModificado(f1,f2, a, b, tol=1.0e-12):
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    x0=0
    x = (a + b) / 2.0
    fx0=f2(x)
    i=0
    while abs(x-x0) >= tol and i<100:
        x0 = x
        x = x0-f1(x0)/fx0
        i+=1
    print("El número de iteraciones es: ",i)
    return x


def funcion(x):
    return x+log(x)

def derivada(x):
    return 1+1/x


x=newton(funcion,derivada, 0.5,1, tol=1.0e-4)
print("La soluciones son: ",x)
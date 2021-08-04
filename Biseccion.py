from math import sqrt
import numpy as np

def biseccion(f, a, b, tol=1.0e-6):
    """Argumentos:
    f - Función, debe ser tal que f(a) f(b) &lt; 0
    a - Extremo inferior del intervalo
    b - Extremo superior del intervalo
    tol (opcional) - Cota para el error absoluto de la x
    Devuelve
    --------
    x - Raíz de f en [a, b]
    """
    if a > b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    x = (a + b) / 2.0
    i=1
    while True:
        if b - a < tol:
            print("El número de iteraciones es: ",i)
            return x
        # Utilizamos la función signo para evitar errores de precisión
        elif np.sign(f(a)) * np.sign(f(x)) > 0:
            a = x
        else:
            b = x
        x = (a + b) / 2.0
        i+=1

def func(x):
    return 10*x - sqrt(7)
# Metodo de Biseccion

sol = biseccion(func,0.2,0.3,1.0e-5)
print("Solucion aproximada por Biseccion: ",sol)



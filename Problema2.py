import sympy as sp
import pandas as pd
import numpy as np
from math import e

x = sp.symbols('x')  # declaramos que x es un simbolo
func = (e*(x/2)*(x*3+6*x*2+24*x+48)/48)-0.005
xl=13
xu=14
es=1e-5
itera = 0
m_itera = np.array([])  # matriz q almacena valores de itera
m_xl = np.array([])  # matriz q alamacena valores de xl
m_xu = np.array([])  # matriz q alamcena valores de xu
xr = 0
m_xr = np.array([])  # matriz q almacena valroes de xr
ea = 100
m_ea = np.array([])  # matriz q alamcena valore s de ea
fl = func.evalf(subs={x: xl})  # reamplazmos x por xl y evaluamos la funcion
# incio del bucle
while ea > es:
    xanterior = xr
    xr = (xl + xu) / 2
    fr = func.evalf(subs={x: xr})
    itera = itera + 1
    if xr != 0:
        ea = abs((xr - xanterior) / xr) * 100
    test = fl * fr
    # agregamos valores a las matrices vacias
    m_itera = np.append(m_itera, itera)
    m_xl = np.append(m_xl, xl)
    m_xu = np.append(m_xu, xu)
    m_xr = np.append(m_xr, xr)
    m_ea = np.append(m_ea, ea)

    if test < 0:
        xu = xr
    elif test > 0:
        xl = xr
        fl = fr
    else:
        ea = 0
    # representamos datos en pandas
iteracion = pd.Series(m_itera, name="Iteracion")
xl = pd.Series(m_xl, name="xl")
xu = pd.Series(m_xu, name="xu")
xr = pd.Series(m_xr, name="xr")
ea = pd.Series(m_ea, name="ea%")
print("La solucion es")

tabla = pd.concat([iteracion, xl, xu, xr, ea], axis=1)  # unimos en columnas
print(tabla)
print("Alumno:Calle Cuadros Sergei")
print("Codigo: 20184099J")

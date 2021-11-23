import numpy as np
import scipy
from scipy import linalg


#Se define los valores de la matriz A

a = np.array([
    [1, 1, 1],
    [2,3,2],
    [-3,0,1]],dtype=float)
q,r=scipy.linalg.qr(a)
b=np.array([11,25,0],dtype=float)
b=np.transpose(b)
y = np.dot(q.T,b)
xqr = scipy.linalg.solve(r,y) 


print('\nA:\n', a) 
print('\nQ:\n', q*-1) 
print('\nR:\n', r*-1) 
print ("Solucion: ")
print (xqr.T,"Rx=y")
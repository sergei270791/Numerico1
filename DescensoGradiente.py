import math
import numpy as np

def RDescensoRapido(A,B):
    eps = 1E-6
    x=np.transpose([0.,0.,0.])
    r=B
    i=0
    while np.linalg.norm(r)>=eps*np.linalg.norm(B):
        t=np.dot(np.transpose(r),r)/np.dot(np.transpose(r),np.dot(A,r))
        x=x+t*r
        r=B-np.dot(A,x)
        print("La matriz X en la iteracion ",(i+1)," es:")
        i=i+1
        print(x)
        if i==100:
            print('El metodo no converge')
            return

A = np.array([[1, 1, 1],
            [1, -1, 0],
            [1, 0, -2]],float)

b= np.transpose(np.array([80,-1,22]))
RDescensoRapido(A,b)
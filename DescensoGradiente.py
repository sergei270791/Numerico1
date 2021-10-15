import math
import numpy as np

def RDescensoRapido(A,B):
    eps = 1E-6
    x=np.transpose([0.,0.,0.])
    r=B
    i=0
    while i< 100 and np.linalg.norm(r)>=eps*np.linalg.norm(B):
        t=np.dot(np.transpose(r),r)/np.dot(np.transpose(r),np.dot(A,r))
        x=x+t*r
        r=B-np.dot(A,x)
        print("La matriz X",(i+1)," es:")
        i=i+1
        print(x)

A=np.array([[ 5., 1., 3.],
[ 4., 1., 2.],
[ 3., 1., 4.]])
B=np.transpose([25.,19.,25.])
RDescensoRapido(A,B)
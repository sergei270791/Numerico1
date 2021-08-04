import math
import numpy as np
from numpy.core.fromnumeric import transpose

def RDescensoRapido(A,B):
    eps = np.finfo(float).eps
    x=np.transpose([0.,0.,0.])
    r=B
    for i in range(100):
        t=np.dot(np.transpose(r),r)/np.dot(np.transpose(r),np.dot(A,r))
        x=x+t*r
        r=B-np.dot(A,x)
        print("La matriz X",(i+1)," es:")
        print(x)

A=np.array([[ 5., 1., 3.],
[ 4., 1., 2.],
[ 3., 1., 4.]])
B=np.transpose([25.,19.,25.])
RDescensoRapido(A,B)
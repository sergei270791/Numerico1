import numpy as np

def Householder(A):
    R=A
    n=len(A)
    Q=np.identity(n)
    for k in range(n):
        a=A[:,0]
        e1=np.zeros_like(a)
        e1[0]=1
        v=a+np.sign(A[0,0])*np.linalg.norm(a)*e1
        v=np.matrix(v).T
        print(v)
        aux2=np.dot(v.T,v)
        H=np.identity(n-k)-(2/aux2[0,0])*np.dot(v,v.T)
        aux=np.dot(H,A)
        A=aux[1:,1:]
        H_modificado=transformarH(H,n,k)
        Q=np.dot(Q,H_modificado)
        R=np.dot(H_modificado,R)
    return Q,R


def transformarH(H,n,k):
    H_modificado=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i<k or j<k:
                if i==j:
                    H_modificado[i][i]=1
                else:
                    H_modificado[i][j]=0
            else:
                H_modificado[i,j]=H[i-k,j-k]
    return H_modificado

A=np.array([
    [2, -2, 18],
    [2,1,0],
    [1,2,0]],float)
b=np.array([11,25,0],float)
b=np.transpose(b)

Q,R=Householder(A)
print('La matriz Q es:')
print(Q)
print('La matriz R es:')
print(R)
x=np.dot(np.linalg.inv(A),b)
print("\n La solución x es:\n")
print(x)
import numpy as np

def determinante(R):
    det=1
    for i in range(len(R)):
        det*=R[i,i]
    return det

def Householder(A):
    R=A
    n=len(A)
    Q=np.identity(n)
    for k in range(n):
        a=np.matrix(A[:,0])
        e1=np.zeros_like(a)
        e1[0,0]=1
        v=a+np.sign(A[0,0])*np.linalg.norm(a)*e1
        aux2=np.dot(v.T,v)
        H=np.identity(n-k)-(2/aux2[0,0])*np.dot(v,v.T)
        aux=np.dot(H,A)
        A=np.matrix(aux[1:,1:])
        H_modificado=transformarH(H,n,k)
        Q=np.dot(Q,H_modificado)
        R=np.dot(H_modificado,R)
    Q=np.round(Q, decimals=9) 
    R=np.round(R, decimals=9) 
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



A=np.matrix([
    [4, 1, 1, 1],
    [1, 4, 1, 1],
    [1 ,1 ,4 ,1],
    [1 ,1 ,1 ,4]],float)
b=np.matrix([2,4,6,8,13],float)
b=np.transpose(b)

Q,R=Householder(A)
Q=-Q
R=-R
print('La matriz Q es:')
print(Q)
print('La matriz R es:')
print(R)

""" print('El determinante de la matriz es: ')
det = determinante(R)
print(det)

solucion = np.dot(np.dot(np.linalg.inv(R),np.transpose(Q)),b)
solucion=np.transpose(solucion)
print("solucion: ",np.round(solucion,decimals=5)) """
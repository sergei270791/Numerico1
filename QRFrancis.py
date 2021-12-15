import numpy as np

np.set_printoptions(suppress=True)

def QRschmithclasico(A):
    Q=np.zeros(np.shape(A),float)
    m,n= np.shape(A)
    for k in range(0,n):
        suma = 0
        if(k!=0):
            for i in range (0, k):
                suma=suma+(np.dot(np.transpose(A[:,k]),Q[:,i])/pow(np.linalg.norm(Q[:,i]),2))*Q[:,i]
        Q[:,k]=A[:,k]-suma
        Q[:, k]=Q[:, k]/np.linalg.norm(Q[:, k])
    R =np.dot(np.transpose(Q),A)
    R=np.array(R,float)
    return Q,R

def es_matriz_diagonal(m):
    n=len(m)
    for i in range(n): 
        for j in range(n): 
            if ((i != j) and (m[i,j] != 0 or m[i,j]!=-0)): 
                return False  
    return True

def QRFrancis(A):
    i=0
    while not es_matriz_diagonal(A):
        print('Matriz A en la iteracion '+str(i)+' es:')
        print(A)
        Q,R=QRschmithclasico(A)
        A=np.dot(R,Q)
        A=np.round(A,decimals=5)
        i+=1
    print('Matriz A en la iteracion '+str(i)+' es:')
    print(A)
    autovalores=np.diag(A)
    return autovalores


A=np.array([[1, 2, 3],[2 ,2, 3],[3, 3, 3]])
autovalores=QRFrancis(A)
print('Los autovalores son: ',autovalores)

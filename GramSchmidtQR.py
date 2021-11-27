import numpy as np

def determinante(R):
    det=1
    for i in range(len(R)):
        det*=R[i,i]
    return det

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
    print("La matriz Q es:\n",np.round(Q,decimals=6),"\nLa matriz R es:\n",np.round(R,decimals=6))
    return Q,R


A=np.array([
    [300,0,150],
    [0,1000,-150],
    [1,-1,-1]],float)

Q,R=QRschmithclasico(A)
""" print('El determinante de la matriz es: ')
det = determinante(R)
print(det) """
b=np.array([7.5,11.5,0],float)
solucion = np.dot(np.dot(np.linalg.inv(R),np.transpose(Q)),b)
print("solucion: ",np.round(solucion,decimals=5))
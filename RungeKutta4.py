import numpy as np
from math import e, log,cos, pi,sin
def J(x):
    Jf=np.zeros((3,3))
    Jf[:,0]=np.transpose([3,2*x[0],-x[1]*e**(-x[0]*x[1])])
    Jf[:,1]=np.transpose([x[2]*sin(x[1]*x[2]),-162*(x[1] + 0.1),-x[0]*e**(-x[0]*x[1])])
    Jf[:,2]=np.transpose([x[1]*sin(x[1]*x[2]),cos(x[2]),20])
    return Jf

def f(x):
    ft=np.zeros((3, 1))
    ft[0,0]=3*x[0]- cos(x[1]*x[2])-0.5
    ft[1,0]=x[0]**2-81*(x[1] + 0.1)**2 + sin(x[2]) + 1.06
    ft[2,0]=e**(-x[0]*x[1]) + 20*x[2] +(10*pi- 3)/3
    return ft

#Si es de 2x2 cambiar rapidamente por J(x) y f(x) de NewtonSistema 
def RungeKutta4(f,J,x0,N):
    k=1
    h=1/N;
    a=f(x0)
    b=-1*h*a;
    while k<=N:
        A=J(x0);
        k1=np.transpose(np.dot(np.linalg.inv(A),b))
        C=x0+(1/2*k1)
        C=C.ravel().tolist()
        D=J(C);
        k2=np.transpose(np.dot(np.linalg.inv(D),b))
        E=x0+(1/2*k2);
        E=E.ravel().tolist()
        F=J(E)
        k3=np.transpose(np.dot(np.linalg.inv(F),b))
        G=x0+k3;
        G=G.ravel().tolist()
        I=J(G)
        k4=np.transpose(np.dot(np.linalg.inv(I),b))
        x=x0+(k1+2*k2+2*k3+k4)/6
        print("La solucion para la iteracion numero",k,"es: ");
        print(x[0])
        x0=x.ravel().tolist()
        k=k+1
    print('La respuesta es: ')
    print(np.round(x,7))

x0=[0.,0.,0.]
RungeKutta4(f,J,x0,4)

import numpy as np 
A=np. array ([[10 ,3 ,1] ,[2 , -10 ,3] ,[1 ,3 ,10]]) 
b=np. array ([[14] ,[ -5] ,[14]])  
n=A. shape [0] 
def DED (A): 
  ite =0 
  ind =1 
  n=0  
  while (ind ==1 and n<A. shape [0]) : 
    ite =ite +1 
    if (2*( A[n,n]) - np. sum (np. abs (A[n ,]))) < 0: 
      ind =0 
      print ("la␣ matriz ␣no␣es␣D.E.D")  
      break 
    else :  
      n=n+1  
  if(ind ==1) :  
    print ("la␣ matriz ␣es␣DED ")
I=np. identity (A. shape [0]) 
def DdeA (A): # hallando el D de A 
  return np.diag(np.diag(A) ,) 
D= DdeA (A)
J=I-np. linalg . inv (D)@A # hallando J = I - D^ -1 @A
def CONVERGENCIA (J): # RADIO SPECTRAL SI ES MAYOR QUE 1 NO CONVERGE
  return max ( abs (np. linalg . eigvals (J)))
print (" ------------------------------\n␣El␣ radio ␣ espectral ␣es:␣", CONVERGENCIA (J))
print ("La␣ matriz ␣J␣es␣ igual :\n␣ ------------------------------",J)
C=np. linalg . inv(D)@b # hallando C = D^ -1 @b
print ("la␣ matriz ␣C␣es␣ igual :\n␣ ------------------------------",C)
x=np. zeros ((A. shape [0] ,1) ,) # valor inicial
ite =0
ind =0
while (ind ==0 and ite <4):
  aux =x
  x= J@x +C
  print (" Iteracion ␣"+ str (ite +1) +",␣la␣ solucion ␣es :\n",x)
  r=( aux -x)
  print (" ERROR ␣" + str (ite +1) +":\n␣ ------------------------------",np. linalg .norm (r,np. inf ))
  ite =ite +1
  if(np. linalg . norm (r,np.inf ) < 0.00001) :
    ind =1
    break

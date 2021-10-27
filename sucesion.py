def succession(n):
  if n==0:
    u=0.501
  else:
    aux1=succession(n-1)
    u=3.9*aux1*(1-aux1)
  return u



for n in range(0,21):
  u=succession(n)
  print("El termino ",n," de la sucesión en python es:",u)


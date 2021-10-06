vigesimal=open("NotaVigesimal.txt","r")
literal=open("NotaLiteral.txt","w")
for linea in vigesimal:
  linea=int(linea)
  if linea==20:
    literal.write("A\n")
  elif  17<=linea<20:
    literal.writelines("B\n")
  elif  15<=linea<17:
    literal.writelines("C\n")
  elif  12<=linea<15:
    literal.writelines("D\n")
  elif  0<=linea<12:
    literal.writelines("E\n")

vigesimal.close()
literal.close()
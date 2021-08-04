import math

def printMatrix(M):
	"""Imprime la matriz de una forma legible."""

	for i in range(len(M)):
		print ('|',end=" ")
		for j in range(len(M[i])):
      
			if(j == len(M)):
				print ('|',end=" ")
				print ('{0:8.4f}'.format(M[i][j]),end=" ")
			else:
				print ('{0:8.4f}'.format(M[i][j]),end=" ")	
		print ('|')
	print
def matrixMulti(A, B):
	"""Multiplica dos matrices, C = A*B """

	rowsA, colsA = len(A), len(A[0])
	rowsB, colsB = len(B), len(B[0])

	if colsA != rowsB:
		exit('Dimensiones incorrectas')

	C = [[0 for row in range(colsB)] for col in range(rowsA)]

	for i in range(rowsA):
		for j in range(colsB):
			for k in range(colsA):
				C[i][j] += A[i][k]*B[k][j]
	return C
def trans(M):
	"""Calcula la matriz transpuesta de M"""

	n = len(M)
	return [[ M[i][j] for i in range(n)] for j in range(n)]

def givens(A):
	"""	Gn* ... G2*G1*A = R
		Q_t = Gn* ... G2*G1
		A = Q*R, de la propiedad Q_t * Q = I
	"""
	n = len(A)

	An = A	
	Gn = [[float(i == j) for j in range(n)] for i in range(n)]
	Q_t = [[float(i == j) for j in range(n)] for i in range(n)]

	a = An[0][n-2]
	b = An[0][n-1]
	index = 1
	for i in range(n):
		for j in range(n-1, i, -1):
			a = An[j-1][i]
			b = An[j][i]
			if a*a + b*b == 0:
				continue

			cosX = a / (math.sqrt(a*a + b*b)) 
			sinX = -b / (math.sqrt(a*a + b*b))

			Gn[j][j] = cosX
			Gn[j][j-1] = sinX
			Gn[j-1][j] = -sinX
			Gn[j-1][j-1] = cosX

			print ('G' +str(index) + ':')
			printMatrix(Gn)

			An = matrixMulti(Gn,An)

			print ('A' +str(index) + ':')
			printMatrix(An)

			Q_t = matrixMulti(Gn, Q_t)
			#Volviendo la matriz Gn a la identidad
			Gn = [[float(k == l) for l in range(n)] for k in range(n)]
			index += 1
	return trans(Q_t), An

A=[[ 5., 4., 3.],
[ 4., 6., 1.],
[ 3., 1., 7.]]
givens(A)

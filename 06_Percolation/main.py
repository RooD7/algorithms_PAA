# from validaPercolacao import imprimeSaida

def percolation(matriz, maxlin, maxcol, partida):
	# print(matriz)
	# print(maxlin, maxcol)
	# print(partida)
	zerosToUns = []
	unsToZeros = []
	result = []
	matriz = adpMatrix(matriz, maxlin, maxcol)
	alterado = partida
	while(alterado != None):
		consomeUns(matriz, alterado, maxlin, maxcol, unsToZeros)
		# print(alterado)
		# print(matriz)
		# print(unsToZeros)
		zerosToUns = unsToZeros
		while(zerosToUns != []):
			melhor = verificaMelhor(matriz.copy(), zerosToUns.copy(), maxlin, maxcol)
			# print('MELHOR')
			# print(melhor)
			zerosToUns.remove(melhor)
			alterado = consomeZeros(matriz, melhor, maxlin, maxcol)
			if alterado != None:
				print(alterado)
				result.append(tuple(alterado))
				break
	# print(unsToZeros)
	print(matriz)
	return result

def verificaMelhor(matrix, v, row, col):
	r = []
	maior = [[],0]
	for x in v:
		r = []
		consomeUns(matrix, x, row, col, r)
		if len(r) > maior[1]:
			maior[0], maior[1] = x, len(r)
	if maior[0] != []:
		return maior[0]
	else:
		return v[0]


def consomeZeros(matrix, atual, row, col):
	x, y, k = atual[0], atual[1], matrix[atual[0]][atual[1]]
	# left
	if y-1 >= 0:
		if matrix[x][y-1] == -1:
			matrix[x][y] = -1
			return (x, y)
	# top
	if x-1 >= 0:
		if matrix[x-1][y] == -1:
			matrix[x][y] = -1
			return (x, y)
	# right
	if y+1 < col:
		if matrix[x][y+1] == -1:
			matrix[x][y] = -1
			return (x, y)
	# bot
	if x+1 < row:
		if matrix[x+1][y] == -1:
			matrix[x][y] = -1
			return (x, y)
	return None

def consomeUns(matrix, atual, row, col, d):
	x, y, k = atual[0], atual[1], matrix[atual[0]][atual[1]]
	if matrix[x][y] == -1:
		matrix[x][y] = 1
	# left
	if y-1 >= 0:
		if matrix[x][y-1] == -1:
			consomeUns(matrix, (x, y-1), row, col, d)
		elif matrix[x][y-1] == 0:
			if not (x, y-1) in d:
				d.append((x, y-1))
	# top
	if x-1 >= 0:
		if matrix[x-1][y] == -1:
			consomeUns(matrix, (x-1, y), row, col, d)
		elif matrix[x-1][y] == 0:
			if not (x-1, y) in d:
				d.append((x-1, y))
	# right
	if y+1 < col:
		if matrix[x][y+1] == -1:
			consomeUns(matrix, (x, y+1), row, col, d)
		elif matrix[x][y+1] == 0:
			if not (x, y+1) in d:
				d.append((x, y+1))
	# bot
	if x+1 < row:
		if matrix[x+1][y] == -1:
			consomeUns(matrix, (x+1, y), row, col, d)
		elif matrix[x+1][y] == 0:
			if not (x+1, y) in d:
				d.append((x+1, y))
		
def adpMatrix(m, row, col):
	for i in range(row):
		for j in range(col):
			if m[i][j] == 1:
				m[i][j] = -1
	return m

# TEST
f = open("1.in", "r")
maxlin, maxcol = eval( f.readline() )
partida = eval( f.readline() )
matriz = eval( f.readline() )

correcoes = percolation(matriz, maxlin, maxcol, partida)
print(correcoes)

# PRODUCTION
# maxlin, maxcol = eval( input() )
# partida = eval( input() )
# matriz = eval( input() )
# correcoes = percolation(matriz, maxlin, maxcol, partida)
# imprimeSaida(partida, matriz, correcoes)


from validaPasseio import imprimeSaida

class Noh(object):
	def __init__(self, pai, atual, pos):
		self.pai = pai
		self.atual = atual
		self.pos = pos

	def addPos(self,k):
		self.pos.append(k)

	def addListPos(self, lista):	
		self.pos += lista

	def getPai(self):
		return self.pai

	def getAtual(self):
		return self.atual

	def getAtualValue(self):
		return self.atual[2]

	def getPos(self):
		return self.pos

	def setPos(self, pos):
		self.pos = pos

def horseRide(matrix, keys):
	arvore = []
	result = []
	inicial = keys[0]
	at = Noh(None, getPosMatrix(matrix, keys.pop(0)), [])
	at.setPos(check(matrix, at.getAtual()))

	while keys != []:
		for k in at.getPos():
			arvore.append(Noh(at, k, check(matrix, k)))
		for k in arvore:
			if k.getAtualValue() in keys:
				keys.remove(k.getAtualValue())
				result = getCaminho(arvore, k.getAtual())
				at = getNoh(arvore, k.getAtual())
				arvore = []
				matrix[k.getAtual()[0]][k.getAtual()[1]] = -1
				at.setPos(check(matrix, k.getAtual()))
				arvore.append(at)
				break
		at = arvore.pop(0)
		arvore.append(at)
	result.insert(0,inicial)
	return result

def getNoh(arvore, k):
	for x in arvore:
		if x.getAtual() == k:
			return x
	return None

def getCaminho(arvore, key):
	r = []
	k = getNoh(arvore, key)
	while k.getPai() != None:
		r.append(k.getAtualValue())
		k = k.getPai()
	r.reverse()
	return r

def getPosMatrix(matrix, key):
	for i in range(8):
		for j in range(8):
			if matrix[i][j] == key:
				return [i, j, key]
	return []

def check(matrix, atual):
	x, y, k = atual[0], atual[1], atual[2]
	l = []

	rows = [2, 1, -1, -2, -2, -1, 1, 2]
	cols = [1, 2, 2, 1, -1, -2, -2, -1]

	for i in range(len(rows)):
		newRow = x + rows[i]
		newCol = y + cols[i]
		if isValidMove(newRow, newCol) and matrix[newRow][newCol] != -1 and matrix[newRow][newCol] != k:
			l.append([newRow, newCol, matrix[newRow][newCol]])
	return l

def isValidMove(row, col):
	if row >= 0 and row < 8 and col >= 0 and col < 8:
		return True
	return False

def getMatrix():
	m = []
	n = 1
	for i in range(8):
		x = []
		for j in range(8):
			x.append(n)
			n += 1
		m.append(x)
	return m

#TEST
# def main():
# 	keys = loadFile('2.in')
# 	print('KEYS')
# 	print(keys)
# 	matrix = getMatrix()
# 	jumps = horseRide(matrix, keys)
# 	jumps_str = [str(i) for i in jumps]
# 	print('RESULT')
# 	print(jumps)
# 	print(jumps_str)
# 	print('LEN')
# 	print(len(jumps)-1)

#PRODUCTION
def main():
	keys = load()
	matrix = getMatrix()
	jumps = horseRide(matrix, keys)
	imprimeSaida(keys,jumps)

# TEST
def loadFile(fileName):	
	f = open(fileName, "r")
	line = f.readline()
	return eval(line)

#PRODUCTION
def load():
	line = input()
	return eval(line)


if __name__ == '__main__':
	main()
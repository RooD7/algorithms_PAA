import numpy as np

def main():
	#loadFile('1.in')
	load()

def pestControl(matrix, row, col, start):
	lv = 0
	matrix = adpMatrix(matrix, row, col)
	matrix[start[0]][start[1]] = lv
	#row, col =	 
	#l, t, r, b = start[1], start[0], start[1], start[0]
	p = [[start[0], start[1],0]]
	while p != []:
		res = check(matrix, p.pop(0), row, col)
		p += res[0]
		if p == []:
			break
	return res[1]

def check(matrix, atual, row, col):
	x, y, k = atual[0], atual[1], atual[2]
	l = []
	# left
	if y-1 >= 0:
		if matrix[x][y-1] == -2:
			matrix[x][y-1] = k+1
			l.append([x, y-1, k+1])
	# top
	if x-1 >= 0:
		if matrix[x-1][y] == -2:
			matrix[x-1][y] = k+1
			l.append([x-1, y, k+1])
		# left-top
		if y-1 >= 0:
			if matrix[x-1][y-1] == -2:
				matrix[x-1][y-1] = k+1
				l.append([x-1, y-1, k+1])
		# top-right
		if y+1 < col:
			if matrix[x-1][y+1] == -2:
				matrix[x-1][y+1] = k+1
				l.append([x-1, y+1, k+1])
	# right
	if y+1 < col:
		if matrix[x][y+1] == -2:
			matrix[x][y+1] = k+1
			l.append([x, y+1, k+1])
	# bot
	if x+1 < row:
		if matrix[x+1][y] == -2:
			matrix[x+1][y] = k+1
			l.append([x+1, y, k+1])
		# right-bot
		if y-1 >= 0:
			if matrix[x+1][y-1] == -2:
				matrix[x+1][y-1] = k+1
				l.append([x+1, y-1, k+1])
		# bot-left
		if y+1 < col:
			if matrix[x+1][y+1] == -2:
				matrix[x+1][y+1] = k+1
				l.append([x+1, y+1, k+1])
	return [l, k]

def adpMatrix(m, row, col):
	for i in range(row):
		for j in range(col):
			if m[i][j] == 0:
				m[i][j] = -1
			else:
				m[i][j] = -2
	return m

# PRODUCTION
def load():
	line = input()
	numTests = int(line)
	for i in range(numTests):
		resultList = []
		line = input()
		line = line.rstrip('\n')
		row, col = line.split(' ')
		for j in range(int(row)):
			line = input()
			line = line.rstrip('\n')
			sVals = line.split(' ')
			iVals = list(map(np.int, sVals))
			resultList.append(iVals)
		line = input()
		line = line.rstrip('\n')
		cordXY = list(map(np.int, line.split(' ')))
		cordXY[0], cordXY[1] = cordXY[0]-1, cordXY[1]-1

		result = pestControl(resultList, int(row), int(col), cordXY)
		print(result)

# TEST
def loadFile(fileName):	
	f = open(fileName, 'r')
	line = f.readline()
	numTests = int(line)
	for i in range(numTests):
		resultList = []
		line = f.readline()
		line = line.rstrip('\n')
		row, col = line.split(' ')
		for j in range(int(row)):
			line = f.readline()
			line = line.rstrip('\n')
			sVals = line.split(' ')
			iVals = list(map(np.int, sVals))
			resultList.append(iVals)
		line = f.readline()
		line = line.rstrip('\n')
		cordXY = list(map(np.int, line.split(' ')))
		cordXY[0], cordXY[1] = cordXY[0]-1, cordXY[1]-1

		result = pestControl(resultList, int(row), int(col), cordXY)
		print(result)
	f.close()

if __name__ == '__main__':
	main()
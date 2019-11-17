import numpy as np
import math

def main():
	loadFile('1.in')
	# load()

def NearestPointProblem(cordXY):
	print(cordXY)
	print(len(cordXY))
	dists = []
	for i in range(len(cordXY)):
		for j in range(len(cordXY)):
			if i < j:
				print(i,j)
				dists.append(dist(cordXY[i], cordXY[j]))

	menor = dists[0]
	print(dists)
	for i in dists:			
		if i > 0 and i < menor:
			menor = i
	return menor

def dist(A, B):
	Xa, Ya = A[0], A[1]
	Xb, Yb = B[0], B[1]

	equacao = ((Xb-Xa)^2)+((Yb-Ya)^2)
	print('equacao')
	print(equacao)
	if equacao >= 0:
		return math.sqrt(equacao)
	else:
		return -1
# PRODUCTION
# def load():
# 	cordXY = []
# 	line = input()
# 	while line != '0':
# 		numCods = int(line)
# 		for i in range(numCods):
# 			resultList = []
# 			line = input()
# 			line = line.rstrip('\n')
# 			x, y = line.split(' ')
# 			cordXY.append([int(x), int(y)])
# 		line = input()
# 	f.close()

# 	result = NearestPointProblem(cordXY)
# 	print(result)

# TEST
def loadFile(fileName):	
	f = open(fileName, 'r')
	line = f.readline()
	while line != '0':
		cordXY = [] 
		numCods = int(line)
		for i in range(numCods):
			resultList = []
			line = f.readline()
			line = line.rstrip('\n')
			x, y = line.split(' ')
			cordXY.append([int(x), int(y)])
		line = f.readline()

		result = NearestPointProblem(cordXY)
		print("%.4f" % result)

	f.close()

if __name__ == '__main__':
	main()
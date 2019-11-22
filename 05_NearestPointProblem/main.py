import numpy as np
import math

def main():
	# loadFile('1.in')
	load()

def NearestPointProblem(cordXY):
	dists = []
	for i in range(len(cordXY)):
		for j in range(len(cordXY)):
			if i < j:
				dists.append(dist(cordXY[i], cordXY[j]))

	menor = dists[0]
	for i in dists:			
		if i > 0 and i < menor:
			menor = i
	if menor > 10000:
		return -1
	else:
		return menor

def dist(A, B):
	Xa, Ya = A[0], A[1]
	Xb, Yb = B[0], B[1]

	equacao = ((Xb-Xa)**2)+((Yb-Ya)**2)
	if equacao >= 0:
		return math.sqrt(equacao)
	else:
		return -1

# PRODUCTION
def load():
	cordXY = []
	while True:
		try:
			line = str(input())
			if line == "0" or line == "0 2\r" or line == "":
				break
			else:
				cordXY = []
				vals = []
				line = line.rstrip('\n')
				if list(line.split(' ')) == []:
					vals = list(map(np.int, line.split('  ')))
				else:
					vals = list(map(np.int, line.split(' ')))
				numCods = vals[0]
				for i in range(numCods):
					resultList = []
					line = str(input())
					line = line.rstrip('\r')
					vals = list(line.split(' '))
					if vals == []:
						break
					else:
						if '' in vals:
							vals.remove('')
						elif ' ' in vals:
							vals.remove(' ')
						x, y = int(vals[0]), int(vals[1])
						cordXY.append([x, y])
				if cordXY != []:	
					result = NearestPointProblem(cordXY.copy())
					if result == -1:
						print('INFINITY')
					else:
						print("%.4f" % result)
		except(EOFError):
			break

# TEST
# def loadFile(fileName):	
# 	f = open(fileName, 'r')
# 	line = f.readline()
# 	while line != '0':
# 		cordXY = [] 
# 		numCods = int(line)
# 		for i in range(numCods):
# 			resultList = []
# 			line = f.readline()
# 			line = line.rstrip('\n')
# 			x, y = line.split(' ')
# 			cordXY.append([int(x), int(y)])
# 		line = f.readline()

# 		result = NearestPointProblem(cordXY)
# 		if result == -1:
# 				print('INFINITY')
# 		else:
# 				print("%.4f" % result)
# 	f.close()

if __name__ == '__main__':
	main()
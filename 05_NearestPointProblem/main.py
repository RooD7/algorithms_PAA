import numpy as np

def main():
	loadFile('1.in')
	# load()

def NearestPointProblem(cordXY):
	print(cordXY)

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
	cordXY = [] 
	f = open(fileName, 'r')
	line = f.readline()
	while line != '0':
		numCods = int(line)
		for i in range(numCods):
			resultList = []
			line = f.readline()
			line = line.rstrip('\n')
			x, y = line.split(' ')
			cordXY.append([int(x), int(y)])
		line = f.readline()
	f.close()

	result = NearestPointProblem(cordXY)
	print(result)

if __name__ == '__main__':
	main()
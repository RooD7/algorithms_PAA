#
# Rodrigo Sousa - 0011264
#

# from validador import imprimeSaida

# def partition(R, left, right):
# 	print('left: '+str(left)+'\tright: '+str(right))
# 	if (right - left) == 0:
# 		R[right] = 'X'
# 		print(R)
# 		return 0
# 	elif (right - left) == 1:
# 		R[left], R[right] = 'X','E'
# 		print(R)
# 		return 0
# 	elif (right - left) == 2:
# 		if R[left+1] == 'X':
# 			R[left], R[left+1], R[right] = 'E','X','P'
# 		if R[left+1] == 'E': 
# 			R[left], R[left+1], R[right] = 'X','E','P'
# 		if R[left+1] == 'P': 
# 			R[left], R[left+1], R[right] = 'X','P','E'
# 		if R[left+1] == '':
# 			return 1
# 		print(R)
# 		return 0
# 	else:
# 		print(str(((right-left)+1)/2))
# 		return int(((right-left)+1)/2)

# def spaceProgram(R, left, right):
	
# 	if (left < right):
# 		print('PARTITION')
# 		pi = partition(R,left,right)
# 		if pi > 0:
# 			print('ESQUERDA')
# 			spaceProgram(R, left+1, 0-1)
# 			print('DIREITA')
# 			spaceProgram(R, left+1, right-1)
# 	return R

# def genomaValido(genoma):
# 	left = ""
# 	x = 0
# 	if genoma != "":
# 		y = int((len(genoma)/2)+1)
# 		print('=== gen: '+genoma)
# 		while len(genoma) > 1:
# 			while x < int(len(genoma)/2):
# 				left += genoma[x]
# 				print('l: '+left)
# 				print('g: '+genoma[x+1:])
# 				if genoma[x+1:].startswith(left):
# 					return False
# 				x += 1
# 			x = 0
# 			left = ""
# 			genoma = genoma[1:]
# 		return True
# 	else:
# 		return True


def spaceProgram(R):
	mid = (int)(len(R)/2)
	left = mid-1
	right = mid

	# impar
	if len(R)%2 == 1:
		R[mid] = nextKey()
	
	for i in range(mid):
		R[left] = nextKey()
		R[right] = nextKey()
		left -= 1
		right +=1
	return R



def nextKey():
	key = l.pop(0)
	l.append(key)
	return key

# TEST
f = open("1.in", "r")
line = f.readline()

# PRODUCTION
# line = str(input())

n = int(line)
global l 
l = ['X','E','P']
R = ['']*n

genoma = spaceProgram(R)

print(genoma)
# imprimeSaida(genoma)
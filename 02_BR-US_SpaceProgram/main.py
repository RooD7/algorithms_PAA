#
# Rodrigo Sousa - 0011264
#

# from validador import imprimeSaida

def spaceProgram(R, n):
	ltrs = []
	while len(R) != n:
		(R, bk) = newKey(R, ltrs)
		# apos recuar, guarda a ultima letra usada para nao entrar novamente e formar loop
		if bk != '':
			ltrs.append(bk)
			# Se nenhuma letra foi possivel, recua novamente
			if len(ltrs) == 3:
				R = R[:len(R)-1]
				ltrs = []
		else:
			ltrs = []
	return R

def newKey(R, ltrs):
	if R == '':
		R += nextKey()
		return (R,'')
	else:
		x = 0
		while(True):
			key = nextKey()
			if not key in ltrs:
				R += key
				# print('coloca: '+R[len(R)-1])
				if not check(R):
					# print('R: '+R+'\tTAM: '+str(len(R)))
					R = R[:len(R)-1]
					# print('tira: '+R[len(R)-1])
					x += 1
					# testou todas as letras possiveis, recua uma possicao
					if x == 3:
						aux = R[len(R)-1]
						R = R[:len(R)-1]
						x = 0
						return (R, aux)
				else:
					return (R,'')

def check(R):
	mid = len(R)/2
	if (mid < 1):
		return True
	else:
		mid = (int)(len(R)/2)
		temp = []
		aux = ""
		for i in range(len(R)-1,len(R)-1-mid, -1):
			# print('i: '+str(i))
			temp.insert(0,R[i])
			if len(temp) == 1:
				# print('aux.join(temp): '+aux.join(temp)+'\tR[i]: '+R[i-1])
				if aux.join(temp) == R[i-1]:
						return False
			else:
				# print('aux.join(temp): '+aux.join(temp)+'\tR[i:len(temp)]: '+R[i-len(temp):i])
				if aux.join(temp) == R[i-len(temp):i]:
						return False
		return True

def nextKey():
	key = l.pop(0)
	l.append(key)
	return key

# TEST
f = open("4.in", "r")
line = f.readline()

# PRODUCTION
# line = str(input())

n = int(line)
global l 
l = ['X','E','P']
R = ''

genoma = spaceProgram(R,n)
# TEST
print(genoma)

# PRODUCTION
# imprimeSaida(genoma)
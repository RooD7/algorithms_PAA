# R -> Result
# T ->


def passoSkyline(R, T):
	if T != []:
		new = T[0]
		newX = new[0]
		newY = new[1]
		newZ = new[2]
		if newY == 0:
			print("Cond 0")
			T.pop(0)
			passoSkyline(R,T)
		elif R == []:
			print("Cond 1")
			R.append(newX)
			R.append(newY)
			R.append(newZ)
			T.pop(0)
			passoSkyline(R,T)
		else:
			print("Cond 2")
			oldY = R[-2]
			oldZ = R[-1]
			print(oldZ, newY, oldY, newZ, T)
			# new comeca antes do termino de oldZ
			# new eh maior que o oldY, entao add
			#a porra da linha encontrou uma linha maior que ela, adiciona a nova linha
			if newX < oldZ and newY > oldY:
				print("Cond 3")
				R.pop()
				R.append(newX)
				R.append(newY)
				R.append(newZ)
				T.pop(0)
				passoSkyline(R,T)
			# vai descer
			elif oldY > newY:
				for a in T:
					if a[0] < oldZ and a[2] > oldZ:
						print("Cond 4")
						R.pop()
						R.append(a[0])
						R.append(a[1])
						R.append(a[2])
						T.remove(a)
						passoSkyline(R,T)
						break
			#a linha nao encontrou mais nada a frente, desce
			else:
				pass
	return R


# S = [(0,8,5), (2, 10, 9), (1, 4, 7), (11, 5, 15), \
# 	(17, 11, 20), (19, 17, 22), (14, 3, 28), \
# 	(25, 13, 30), (8, 6, 23)]

inputs = []

# TEST
f = open("1.in", "r")
line = f.readline()
while True:
	if line == '':
		break
	inputs.append(eval(line))
	line = f.readline()

# PRODUCTION
# line = input()
# while True:
# 	if line == None:
# 		break
# 	inputs.append(eval(line))
# 	line = input()

inputs.sort(key=lambda x: x[0])
print(inputs)

RT = passoSkyline([],inputs)
print(RT)
# R = ()
# for T in S:
# 	R = passoSkyline(R, T)

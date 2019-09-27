# R -> Result
# T ->


def passoSkyline(R, T):
	if T != []:
		T0 = T[0]
		if R == []:
			R.append(T0[0])
			R.append(T0[1])
			R.append(T0[2])
			T.pop(0)
			passoSkyline(R,T)
		else:
			print("OK")
			y = R[-2]
			z = R[-1]

			print(z, T0[1], y, T0[2], T)
			if y == 0 and z == 0:
				print("Cond 0")
				R.pop()
				R.pop()
				R.append(T0[0])
				R.append(T0[1])
				R.append(T0[2])
				T.pop(0)
				passoSkyline(R,T)
			# T0 comeca antes do termino de z
			# T0 eh maior que o y, entao add
			#a porra da linha encontrou uma linha maior que ela, adiciona a nova linha
			elif z > T0[1] and y < T0[2]:
				print("Cond 1")
				R.pop()
				R.append(T0[0])
				R.append(T0[1])
				R.append(T0[2])
				T.pop(0)
				passoSkyline(R,T)
			elif(z < T0[0]):
				print("Cond 2")
				R.pop()
				R.append(T0[0])
				R.append(T0[1])
				R.append(T0[2])
				T.pop(0)
				passoSkyline(R,T)
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

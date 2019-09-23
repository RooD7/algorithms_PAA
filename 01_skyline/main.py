
def passoSkyline(R, T):
 	novoR = ()
 	print('T: ',T)
 	if len(R) == 0:
 		novoR = T + (0,)
 	else:
	 	for i in range(0, len(R)-2, 2):
	 		# xe->0, xd->2, e->8, d->23
	 		xe, xd, e, d = R[i], R[i+2], T[0], T[2]
	 		# avalia segmento xe --- xd com e --- d
	 		if xe > e:
	 			return R
	 		else:
		 		if xd > e:
		 			if R[i+1] < T[1]:
			 			# remove xd, usar e and T[1]
			 			novoR = R[:len(R)-2] + (e, T[1], d, 0)
		 			if R[i+1] > T[1]:
			 			#usar xd and R[i+1]
			 			novoR = R[:len(R)-2] + (xd, R[i+1], d, 0)
	 		# acrescenta coordenada x e altura em novoR
 	# return novoR atualizado e finalizado
 	return novoR

# S = [(0,8,5), (2, 10, 9), (1, 4, 7), (11, 5, 15), \
# 	(17, 11, 20), (19, 17, 22), (14, 3, 28), \
# 	(25, 13, 30), (8, 6, 23)]

inputs = []

# TEST
f = open("1.in","r")
line = f.readline()
while True:
	if line == '':
		break
	inputs.append(eval(line))
	line = f.readline()

# Production
# line = input()
# while True:
# 	if line == None:
# 		break
# 	inputs.append(eval(line))
# 	line = input()

print(inputs)


# R = ()
# for T in S:
# 	R = passoSkyline(R, T)
#
# Rodrigo Sousa - 0011264
#
def passoSkyline(R, T):
	if T != []:
		new = T[0]
		newX, newY, newZ = new[0], new[1], new[2]
		if newY == 0:
			T.pop(0)
			passoSkyline(R,T)
		elif R == []:
			R.append(newX)
			R.append(newY)
			R.append(newZ)
			# T.pop(0)
			passoSkyline(R,T)
		else:
			oldX, oldY, oldZ = R[-3], R[-2], R[-1]
			
			# encontra a intersecao de maior altura
			maior = (0,0,0)
			for a in T:
				if oldX < a[0] < oldZ and oldY < a[1]:
					maior = a
					break
				elif a[0] <= oldZ and a[2] > oldZ:
					if a[1] > maior[1]:
						maior = a
					if oldZ > a[2]:
						T.remove(a)
			if maior != (0,0,0):
				R.pop()
				# se eh maior usa maior[0], se eh menor usa oldZ 
				if oldY == maior[1]:
					R.append(maior[2])
				elif oldY < maior[1]:
					R.append(maior[0])
					R.append(maior[1])
					R.append(maior[2])
				else:
					R.append(oldZ)
					R.append(maior[1])
					R.append(maior[2])
				# T.remove(maior)
				passoSkyline(R,T)
			else:
				for a in T:
					if a[0] > oldZ:
						R.append(0)
						R.append(a[0])
						R.append(a[1])
						R.append(a[2])
						# T.remove(a)
						passoSkyline(R,T)
						break
	return R

inputs = []

# TEST
# f = open("4.in", "r")
# line = f.readline()
# while True:
# 	if line == '':
# 		break
# 	inputs.append(eval(line))
# 	line = f.readline()

# PRODUCTION
while True:
	try:
		line = str(input())
		if line != "":
			inputs.append(eval(line))
	except(EOFError):
		break

inputs.sort(key=lambda x: x[0])

RT = passoSkyline([],inputs)
RT.append(0)
result = str(RT)
result = result.replace("[","(")
result = result.replace("]",")")
result = result.replace(" ","")
print(result)
# print("(0,8,1,11,3,13,9,8,10,4,11,5,12,7,17,11,19,18,22,3,23,13,30,2,34,15,43,7,58,2,109,0)")

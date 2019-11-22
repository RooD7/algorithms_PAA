
def merge(v, left, right):
	tp = v.copy()
	mid = (left + right) // 2
	i, j, k, inv = left, mid+1, left, 0
	while i <= mid and j <= right:
		if v[i] <= v[j]:
			tp[k] = v[i]
			k += 1
			i += 1
		else:
			tp[k] = v[j]
			inv += mid - i + 1
			k += 1
			j += 1

	while i <= mid:
		tp[k] = v[i]
		k += 1
		i += 1
	while j <= right:
		tp[k] = v[j]
		k += 1
		j += 1
	# for i in range(left, right+1):
	# 		v[i] = tp[i]
	i = left
	while(i <= right):
		v[i] = tp[i]
		i += 1
	return inv
	

def bubblesBuckets(v, left, right):
	mid,inv = 0, 0
	if right > left:
		mid = (left+right) // 2
		inv =  bubblesBuckets(v, left, mid)
		inv += bubblesBuckets(v, mid+1, right)
		inv += merge(v, left, right)
	return inv

# TEST
# f = open("1.in", "r")
# sequencia = []
# line = f.readline().rstrip()
# while line != '0':
# 	sequencia = line.split(' ')
# 	result = bubblesBuckets(list(map(int,sequencia)),1,len(sequencia)-1)
# 	if result % 2 == 1:
# 		print(str(result)+" - Marcelo")
# 	else:
# 		print(str(result)+" - Carlos")
# 	line = f.readline().rstrip()
# f.close()

# PRODUCTION
sequencia = []
while True:
	try:
		line = input().rstrip()
		if line != '0':
			sequencia = line.split(' ')
			result = bubblesBuckets(list(map(int,sequencia)),1,len(sequencia)-1)
			if result % 2 == 1:
				print("Marcelo")
			else:
				print("Carlos")
	except(EOFError):
		break

import random
l = [ random.randint(1,100) for i in range(20)]
print(l)
l.sort(reverse = True)
print(l)
def Distribution(l):
	l1 = []
	for k in range(11):
		l1.append(0)
	for i in l:
		for j in range(11):
			sum1 = 0
			if j * 10 <= i < (j + 1) * 10:
				sum1 = 1
			else:
				sum1 = 0
			l1[j] += sum1
	for i in range(10,-1,-1):
		if i == 10:
			print('%5s:'%(i * 10),end='')
			print('*' * l1[i])
			
		else:
			print('%2s~%2s:'%(i * 10,(i + 1) * 10 -1),end='')
			print('*' * l1[i])
Distribution(l)

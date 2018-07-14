#str a b min max
a = input('please input str data:')
b = input('please input str data:')
if len(a)<=len(b):
	x = 0
	for i in range(len(a)):
		if a[i] > b[i]:
			print('a > b')
		elif a[i] < b[i]:
			print('a < b')
		else:
			x += 1
			continue
	if x == len(a):
		print('a = b')
else:
	x = 0
	for i in range(len(b)):
		if a[i] > b[i]:
			print('a > b')
		elif a[i] < b[i]:
			print('a < b')
		else:
			x += 1
			continue
	if x == len(b):
		print('a = b')

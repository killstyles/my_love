# 9 * 9
for i in range(1,10):
	for j in range(1,i + 1):
		print('{} * {} = {:2.0f}'.format(i,j,i * j),end = ' ')
	print()

# 111 11 1 121 1221
n = input('please input a interger:')
m = (1 + len(n)) // 2
flag = 1
for i in range(m):
	if n[i] == n[len(n)-i-1]:
		pass
	else:
		flag = 0
if flag:
	print('Yes')
else:
	print('No')

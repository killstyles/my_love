m = input('please input your name:')
flag = 1
for i in m:
	if i.isdigit() or i == '_' or i.isupper() or i.islower():
		pass
	else:
		flag = 0
		break
if flag:
	print('Yes')
else:
	print('No')

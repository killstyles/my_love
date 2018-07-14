#count str a A 1
myuser = input('please input something:')
nu1 = 0
nu2 = 0
nu3 = 0
for i in myuser:
	if i.isupper():
		nu1 += 1
	elif i.islower():
		nu2 += 1
	elif i.isdigit():
		nu3 += 1
print('upper:{} lower:{} digit:{}'.format(nu1,nu2,nu3))

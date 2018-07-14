# a-->A A-->a
others = ''
user = input('please input somethings:')
for i in user:
	if ord('a') <= ord(i) <= ord('z'):
		others += chr(ord(i)-32)
	elif ord('A') <= ord(i) <= ord('Z'):
		others += chr(ord(i)+32)
	else:
		others += i
print(others)
#print(user.swapcase())

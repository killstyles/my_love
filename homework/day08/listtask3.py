import random
l = []
for i in range(ord('A'),ord('Z') + 1):
	l.append(chr(i))
	l.append(chr(i + 32))
for i in range(10):
	l.append(str(i))
print(l)
l1 = []
for i in range(10):
	s = ''
	for i in range(8):
		s += random.choice(l)
	l1.append(s)
print(l1)

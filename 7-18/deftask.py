def intsquare(n):
	return n ** 2
def FindStrMax(n):
	m = n[0]
	for i in n:
		if i >= m:
			m = i
	return m
def FindDivMax(m,n):
	for i in range(1,m):
		if m % i == 0 and n % i == 0:
			y = i
	return y
def mysum(*m):
	s = 0
	for i in m:
		s += i
	return s
def mydef(a,b = 0,*c):
	print('a=',a,'b=',b,c)
def Rec

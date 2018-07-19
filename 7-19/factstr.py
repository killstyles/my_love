def FactStr(n):
	if n == '':
		return n
	return FactStr(n[1:]) + n[0]
print(FactStr('abc'))

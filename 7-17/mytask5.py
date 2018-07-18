def fact(n):
	if n == 1:
		return 1
	return (fact(n - 1) + 1) * 2
print(fact(11))

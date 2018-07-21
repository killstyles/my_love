def StuScore(l):
	print('max:{} min:{} avg:{}'.format(max(l),min(l),sum(l)/len(l)))
	return max(l),min(l),sum(l)/len(l)
l = [ eval(input('student{}:'.format(i))) for i in range(1,11)]
i = 0
while i < 10:
	if l[i] < 0 or l[i] > 100:
		l[i] = eval(input('student{} is error! try again:'.format(i + 1)))
		continue	
	i += 1
StuScore(l)

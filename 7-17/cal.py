def isleap(y):
	return (i % 4 == 0 and i % 100 != 0) or i % 400 == 0
def monthday(j,y):
	if j == 1 or j == 3 or j == 5 or  j == 7 or j == 8 or j == 10 or j == 12:
		return 31
	elif j == 2:
		return 28
	elif isleap(y):
		return 29
	else:
		return 30
mymonth,myyear = eval(input('please input a month and a year(after 1990):'))
mysum = 0
for i in range(1990,myyear):
	mysum +=365
	mysum += isleap(myyear)
for j in range(1,mymonth):
		mysum += monthday(j,myyear)
week = (mysum + 1) % 7 
print('{}月 {}'.format(mymonth,myyear).center(20,' '))
print('日 一 二 三 四 五 六')
flag = monthday(mymonth,myyear)
flag1 = 1
for i in range(1,flag+1):
	if flag1:
		print(' ' * 3 * (week % 7) + '{:2.0f}'.format(i),end=' ')
		if (i + week % 7) % 7== 0:
			print()
		flag1 = 0
		continue
	print('{:2.0f}'.format(i),end=' ')
	if (i + week % 7) % 7== 0:
		print()
print()

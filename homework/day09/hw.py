'''
1.
	cost > 10 and cost < 50
'''

'''
2.
	True
	True
'''

'''
3.
def int(n)
	if n % 1 >= 0.5:
		return n + 1
	else:
		return n - 1
'''

'''
4.
	4
'''

'''
5.
'''
x = 1
while True:
	if x % 2 == 1 and x % 3 == 2 and x % 5 == 4 and x % 6 == 5:
		print('at least:%s',x)
		break
	else:
		x += 7

'''
6.
x,y,z = 1,2,3
x,y,z = y,z,x or x,y,z = ...
'''

'''
7.
	None
'''

'''
8.
	False
'''

'''
9.
	list1[1][2][0] = '小坏蛋'
'''

'''
10.
	list.sort()
'''

'''
11.
	list.sort(reverse = True)
'''

'''
12.
	保存数据 不做更改
	??? 看心情把
'''

'''
13.
	True
'''

'''
14.
'''
import math
def tohex(m,n = 2):
	'''
	m = 十进制数 n默认参数为2 n为 2 or 4 or 8 or 16
	'''
	x = bin(m)
	y = len(x)
	z = int(math.log(n,2))
	mysum = ''
	for i in range(-1,-y + 1,-z):
		mysum1 = 0
		for j in range(z):
			if i - j == -y + 1:
				break
			else:
				mysum1 += (int(x[i - j]) * (2 ** j))
		for i in range(6):
			if mysum1 == 10 + i:
				mysum1 = chr(ord('A') + i)
		mysum += str(mysum1)
	return mysum[::-1]
print(tohex(113,16))		

'''
15.
	序列类型:(Sequence Types)
	有序 可迭代
'''

'''
16.
	Myfun is error
'''

'''
17.
'''

def MyBaseSum(*n,base=3):
	'''
	计算打印所有参数的和乘以基数（base=3）的结果
	'''
	bs = 0
	for i in n:
		bs += i
	return bs * base
print(MyBaseSum(1,2,3,4))

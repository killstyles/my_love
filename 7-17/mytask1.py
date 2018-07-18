# guess 1~10 
import random
num = random.randint(1,10)
print(num)
mynum = eval(input('please input a interger 1~10 data:'))
cnt = 1
while True:
	if mynum > num:
		print('too big')
		mynum = eval(input('please try again:'))
		cnt += 1
	elif mynum < num:
		print('too small')
		mynum = eval(input('please try again:'))
		cnt += 1
	else:
		print('right!!!')
		break
	if cnt == 3:
		print('only three times')
		break


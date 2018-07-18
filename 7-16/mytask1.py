#input hight weight BMI
height = eval(input('please input your height(kg):'))
weight = eval(input('please input your weight(m):'))
BMI = weight / (height ** 2)
if BMI < 18.5:
	print('underweight')
elif BMI < 23.9:
	print('normal')
elif BMI < 27:
	print('overweight')
elif BMI < 32:
	print('fat')
else:
	print('very fat')


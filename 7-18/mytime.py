import turtle
import datetime
td = datetime
strtime = td.datetime.now().strftime('%y %m %d %H %M %S').split()
print(strtime)
def isnt(n,i):
	if n == '0':
		if i == 0:
			turtle.penup()
		else:
			turtle.pendown()
	elif n == '1':
		if i == 1 or i == 6:
			turtle.pendown()
		else:
			turtle.penup()
	elif n == '2':
		if i == 1 or i == 4:
			turtle.penup()
		else:
			turtle.pendown()
	elif n == '3':
		if i == 3 or i == 4:
			turtle.penup()
		else:
			turtle.pendown()
	elif n == '4':
		if i == 2 or i == 3 or i == 5:
			turtle.penup()
		else:
			turtle.pendown()
	elif n == '5':
		if i == 3 or i == 6:
			turtle.penup()
		else:
			turtle.pendown()
	elif n == '6':	
		if i == 6:
			turtle.penup()
		else:
			turtle.pendown()
	elif n == '7':
		if i == 1 or i == 5 or i == 6:
			turtle.pendown()
		else:
			turtle.penup()
	elif n == '8':
		pass
	elif n == '9':
		if i == 3:
			turtle.penup()
		else:
			turtle.pendown()
t = turtle
t.pensize(5)
t.speed(0)
t.ht()
t.penup()
t.setx(-450)
t.pendown()
for i in range(6):
	for k in range(2):
		for j in range(7):
			isnt(strtime[i][k],j)
			if j != 3:
				t.fd(40)
				t.rt(90)
			else:
				t.fd(40)
		t.penup()
		t.fd(-25)
		t.lt(180)
		t.pendown()
	t.penup()	
	t.fd(20)
	t.pendown()
t.end_fill()
t.done()


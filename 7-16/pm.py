#pm2.5
mypm = eval(input('please input your city air quality:'))
#print('bad') if mypm > 75 else (print('good')if mypm > 35 else print('very good'))
a = mypm > 75 and 1 or (mypm > 35 and 2 or 3)
print(a)

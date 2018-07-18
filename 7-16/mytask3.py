# input your price show your discount
myprice = eval(input('please input your price:'))
mydiscount = 0
if myprice < 50:
	print('you will get {}% discount and the final price is {}'.format(mydiscount * 100,myprice * (1-mydiscount)))
elif myprice <= 100:
	mydiscount = 0.1
	print('you will get {}% discount and the final price is {}'.format(mydiscount * 100,myprice * (1-mydiscount)))
else:
	mydiscount = 0.2
	print('you will get {}% discount and the final price is {}'.format(mydiscount * 100,myprice * (1-mydiscount)))
	

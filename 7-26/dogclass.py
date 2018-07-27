class MyDog:
	name = 'lucky'
	def __init__(self,master):
		self.master = master
	def speak(self):
		print('wang wang!!!')
	def owner(self):
		print('my owner is {}'.format(self.master))
	def getname(self):
		print('my name is {}'.format(MyDog.name))

dog1 = MyDog('Carrey')
dog1.speak()
dog1.getname()
dog1.owner()

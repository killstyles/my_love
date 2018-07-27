# class

class Person:
	#属性 特征
	role = 'person'#类属性
	def __init__(self,name,age = 20):#构造方法
		self.name = name #self.name 实例属性 self 当前对象
		self.__age = age #私有属性
	def __del__(self):#析构方法 当对象销毁时，自动调用
		print('please forget me')
	#方法（函数）技能
	def sayHello(self):
		print('hello!!!')
		print('i m {}'.format(Person.role))
	def getName(self):
		print('my name is {}'.format(self.name))
	def getInfo(self):
		print('my name is {},i m {} yearsold.'.format(self.name,self.__age))

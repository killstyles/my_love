import myclass

class Student(myclass.Person):
	def __init__(self,no,time):
		super().__init__(name,age)
		self.no = no
		self.time = time
	def getInfo(self)
		super().getInfo()
		print('no:{} time:{}'.format(self.no,self.time))

if __name__ == '__main__':
	s1 = Student('xiaowang',21,'201501','7:15')
	s1.getInfo()
	

class Car:
	'''car class'''
	role = 'car'
	def __init__(self,logo,color):
		self,logo = logo
		self.__color = color
		self.wheel = 4
	def run(self):
		print('logo:{} color:{}'.format(self.logo,self.__color))
	def __getColor(self):
		return self.__color	

if __name__ == '__main__':
	QQcar = Car('QQ','Green')
	QQcar.run()

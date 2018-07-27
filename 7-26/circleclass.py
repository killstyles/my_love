# circle
import math
class Circle:
	def __init__(self,r):
		self.r = r
	def Perimeter(self):
		return 2 * math.pi * self.r
	def Area(self):
		return math.pi * (self.r ** 2)

class Ring:
	def __init__(self,r1,r2):
		self.c1 = Circle(r1)
		self.c2 = Circle(r2)
	def RingPerimeter(self):
		return abs(self.c1.Perimeter() + self.c2.Perimeter())
	def RingArea(self):
		return abs(self.c1.Area() - self.c2.Area())
if __name__ == '__main__':
	R1 = Ring(5,10)
	print(R1.RingPerimeter())
	print(R1.RingArea())

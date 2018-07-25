import sys

if __name__ == '__main__':
	s = 0
	for i in sys.argv:	
		if i == sys.argv[0]:
			 continue
		else:
			s += int(i)
	print(s)

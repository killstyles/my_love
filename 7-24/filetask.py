with open('filetest','w+') as fd:
	print(fd.tell())
	fd.write('Who\nAre\nYou')	
	print(fd.read())
	print(fd.tell())
	fd.seek(0,0)
	print(fd.read())
	fd.seek(int(fd.tell()-5),0)
	print(fd.read())
	

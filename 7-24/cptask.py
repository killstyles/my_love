#cp 
cp = input('Please enter the file path that you want to copy:')
cp1 = input('Please enter the paste to the file path:')
fd1 = open(cp);fd2 = open(cp1,'w+')
while True:
	ff = fd1.readline(100)
	if ff  == '':
		break
	else:
		fd2.write(ff)
fd1.close()
fd2.close()

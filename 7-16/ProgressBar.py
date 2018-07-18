# 进度条
import time
import sys
for i in range(11):
#	print('\r{}% '.format(i * 10) + '##' * i + '--' *(10 - i))
	sys.stdout.write('{:3.0f}% '.format(i * 10) + '##' * i + '--' *(10 - i) + '\r')
	time.sleep(1)
	sys.stdout.flush()
print('\n')

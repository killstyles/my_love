import os

op = os.path
ld = os.listdir('../7-23')
print(ld)
os.chdir('../7-23')
for i in ld:
	if op.isfile(i):
		print(i)


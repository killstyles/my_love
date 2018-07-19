import random
l = [random.randint(1,10) for i in range(10)]
print(l)
a = max(l)
l.append(a)
print(l)

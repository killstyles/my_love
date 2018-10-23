import random
import string

def Type1():
    l = []
    s = string.digits
    for i in s:
        l.append(i)
    str1 = random.choice(l)
    return str1
def Type2():
    l = ['0','1','2','3','4','5','6','7','8','9']
    str1 = ''
    for i in range(1000):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        l[a],l[b] = l[b],l[a]
    for j in l:
        str1 += j
    return str1
def Type3():
    l = ['A','B','C','D','E','F']
    str1 = ''
    for i in range(1000):
        a = random.randint(0,5)
        b = random.randint(0,5)
        l[a], l[b] = l[b], l[a]
    for j in l:
        str1 += j
    return str1
def Type4():
    l = []
    s = string.ascii_lowercase
    for i in s:
        l.append(i)
    str1 = random.choice(l)
    return str1

def Type(tnum=0):
    if tnum == 1:
        return Type1()
    elif tnum == 2:
        return Type2()
    elif tnum == 3:
        return Type3()
    elif tnum == 4:
        return Type4()
    else:
        if random.randint(0,1):
            return Type2()
        else:
            return Type3()
def TypeTotal(**postion):
    str1 = ''
    for i in range(1,65):
        if postion[str(i)] != 0:
            str1 += Type(postion[str(i)])
        else:
            str1 += Type()
    return str1
def IntputTxt(con,l):
    for i in range(1, con + 1):
        file = open('./00{}.txt'.format(i), 'w')
        filelist = []
        for j in range(1000000):
            filelist.append(TypeTotal(**l) + '\n')
        newfilelist = list(set(filelist))
        file.writelines(newfilelist)
        file.close()
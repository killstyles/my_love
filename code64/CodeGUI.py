import tkinter as tk
import itertools
l1 = [str(x) for x in range(1,65)]
l2 = [0]
l3 = dict(itertools.product(l1,l2))

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
        for j in range(10):
            filelist.append(TypeTotal(**l) + '\n')
        newfilelist = list(set(filelist))
        file.writelines(newfilelist)
        file.close()

class Application(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.pack()

        self.create_widgets()
    def create_widgets(self):
        self.label1 = tk.Label(root, text='根据数字选择生成串码方式（没有设置方式默认为方式0）').pack()
        self.label2 = tk.Label(root, text='单个数字(0-9):1').pack()
        self.label3 = tk.Label(root, text='数字组合(0~9):2').pack()
        self.label4 = tk.Label(root, text='字母组合(A~F):3').pack()
        self.label5 = tk.Label(root, text='单个字母(a-z):4').pack()
        self.label6 = tk.Label(root, text='数字组合(0~9)或字母组合(A~F):0').pack()
        self.label7 = tk.Label(root, text='位置(1-64)：(ps:若想选择多个位置以英文逗号分隔)').pack()


        self.text1 = tk.Entry()
        self.contents1 = tk.StringVar()
        self.text1['textvariable'] = self.contents1
        self.text1.pack()
        self.label8 = tk.Label(root, text='方式(0-4):(位置与其选择方式一一对应)').pack()
        self.text2 = tk.Entry()

        self.contents2 = tk.StringVar()
        self.text2['textvariable'] = self.contents2
        self.text2.pack()
        self.label9 = tk.Label(root, text='当前文件夹生成文件个数:(100W/文件)').pack()

        self.text3 = tk.Entry()

        self.contents3 = tk.StringVar()
        self.text3['textvariable'] = self.contents3
        self.text3.pack()

        self.button1 = tk.Button()
        self.button1['text'] = '生成'
        self.button1['command'] = self.print_txt
        self.button1.pack()

    def print_txt(self):
        try:
            con1 = self.contents1.get().split(',')
            con2 = self.contents2.get().split(',')
            le = len(con1)
            con3 = int(self.contents3.get())
            cnt = 0
            while cnt < le:
                l3[con1[cnt]] = int(con2[cnt])
                cnt += 1
            IntputTxt(con3,l3)
        except:
            IntputTxt(con3, l3)
root = tk.Tk()
root.geometry('400x400')
app = Application(master=root)
app.mainloop()
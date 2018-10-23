import itertools
import os
import tkinter as tk
from tkinter import messagebox
import random
import string
l1 = [str(x) for x in range(1,65)]
l2 = [0]
l3 = dict(itertools.product(l1,l2))
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

def ShowBox():
    tk.messagebox.showinfo('提示', '成功在Code文件夹中生成文件')

def ShowBox1():
    tk.messagebox.showinfo('提示', '请输入需要生成的串码个数')
def ClickSet(m,n):
    createVar['var'+str(m)].set( createVar['newbutton'+str(m)+str(n)]['text'])
def SetButton(i,j):
     newlist[i].append(j)
     createVar['newbutton'+str(i)+str(j) ]= tk.Button(fm,text= j,command =lambda:ClickSet(newlist[i][0],newlist[i][j+1]))
     createVar['newbutton'+str(i)+str(j) ].pack(side = 'left')
def SetText(i):
    label1 = tk.Label(fm, text='窗格{:2}:'.format(i + 1))
    label1.pack(side='left')
    createVar['var' + str(i)] = tk.StringVar()
    createVar['text' + str(i)] = tk.Entry(fm, width=4, textvariable=createVar['var' + str(i)])
    createVar['text' + str(i)].pack(side='left')
    label1 = tk.Label(fm, text='方式:')
    label1.pack(side='left')


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
def Type4():
    l = ['A','B','C','D','E','F']
    str1 = ''
    for i in range(1000):
        a = random.randint(0,5)
        b = random.randint(0,5)
        l[a], l[b] = l[b], l[a]
    for j in l:
        str1 += j
    return str1
def Type3():
    l = ['a','b','c','d','e','f']
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
            return Type4()
def TypeTotal(**postion):
    str1 = ''
    for i in range(1,65):
        if postion[str(i)] != 0:
            str1 += Type(postion[str(i)])
        else:
            str1 += Type()
    return str1 + '\n'
def IntputTxt(con,l):
    dirpath = os.getcwd() + '\\Code\\'
    mkdir(dirpath)
    codesum = con
    for i in range(1, con//1000001 + 2):
        file = open(dirpath + '\\{}.txt'.format(i), 'w')
        filelist = []
        if codesum <= 1000000:
            for j in range(codesum):
                filelist.append(TypeTotal(**l))
            newfilelist = set(filelist)
            file.writelines(newfilelist)
            file.close()
        else:
            codesum -= 1000000
            for j in range(1000000):
                filelist.append(TypeTotal(**l))
            newfilelist = set(filelist)
            file.writelines(newfilelist)
            file.close()

def print_txt():
    try:
        cnt = 0
        while cnt < 64:
            con1 = str(cnt+1)
            con2 = createVar['var'+str(cnt)].get()
            if con2 == '':
                cnt += 1
                continue
            l3[con1] = int(con2)
            cnt += 1
        con3 = var.get()
        if con3 == '':
            ShowBox1()
        IntputTxt(int(con3),l3)
        ShowBox()
    except:
        IntputTxt(int(con3),l3)
        ShowBox()
root = tk.Tk()
root.geometry('400x400')
root.title('串码生成器')
root.resizable(0,0)
canvas = tk.Canvas(root,width=370,height=400)
canvas.pack(side=tk.LEFT)

f1 = tk.Frame(canvas,width = 350, height=400)
canvas.create_window(0,0,window = f1,anchor = 'nw')
label1 = tk.Label(f1, text='根据数字选择生成串码方式（没有设置方式默认为方式:0）').pack()
label6 = tk.Label(f1, text='数字组合(0~9)或字母组合(A~F):0').pack()
label2 = tk.Label(f1, text='单个数字(0-9):1').pack()
label3 = tk.Label(f1, text='数字组合(0~9):2').pack()
label5 = tk.Label(f1, text='单个字母(a-f):3').pack()
label4 = tk.Label(f1, text='字母组合(A~F):4').pack()

label7 = tk.Label(f1, text='在程序运行目录中创建Code文件夹并生成txt文件:(100W串码/文件)').pack()
label8 = tk.Label(f1, text='ps:再次生成时会从1.txt开始覆盖原重名文件，请注意及时保存').pack()
label9 = tk.Label(f1, text='ps2:请不要在360安全桌面等软件运行的桌面上运行').pack()
label10 = tk.Label(f1, text='请在下面方框中输入你想生成的串码数量').pack()
var  = tk.StringVar()
text = tk.Entry(f1,textvariable =var).pack()
button1 =tk.Button(f1,text='生成',command = print_txt).pack()

createVar = locals()
newlist = []
for i in range(64):
    newlist.append([])
    newlist[i].append(i)
    fm = tk.Frame(f1)
    fm.pack(side='top')

    SetText(i)

    for j in range(5):
        SetButton(i,j)
s = tk.Scrollbar(root,width=20,command = canvas.yview)
canvas['yscrollcommand']=s.set
s.pack(side = 'right',expand = 1,fill = 'y')
root.update()
canvas.config(scrollregion=canvas.bbox("all"))
root.mainloop()


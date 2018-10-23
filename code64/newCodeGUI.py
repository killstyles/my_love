import tkinter as tk
def ClickSet(m,n):
    createVar['var'+str(m)].set( createVar['newbutton'+str(m)+str(n)]['text'])
def SetText(i,j):
     newlist[i].append(j)
     createVar['newbutton'+str(i)+str(j) ]= tk.Button(fm,text= j,command =lambda:ClickSet(newlist[i][0],newlist[i][j+1]))
     createVar['newbutton'+str(i)+str(j) ].pack(side = 'left')
root = tk.Tk()
root.geometry('400x400')
root.title('串码生成器')
canvas = tk.Canvas(root,width=370,height=400)
canvas.pack(side=tk.LEFT)

f1 = tk.Frame(canvas,width = 350, height=400,bg = 'blue')
canvas.create_window(0,0,window = f1,anchor = 'nw')
label1 = tk.Label(f1, text='根据数字选择生成串码方式（没有设置方式默认为方式:0）').pack()
label6 = tk.Label(f1, text='数字组合(0~9)或字母组合(A~F):0').pack()
label2 = tk.Label(f1, text='单个数字(0-9):1').pack()
label3 = tk.Label(f1, text='数字组合(0~9):2').pack()
label4 = tk.Label(f1, text='字母组合(A~F):3').pack()
label5 = tk.Label(f1, text='单个字母(a-z):4').pack()
label7 = tk.Label(f1, text='在当前文件夹生成文件个数:(100W/文件)').pack()
var  = tk.StringVar()
text = tk.Entry(f1,textvariable =var).pack()
button1 =tk.Button(f1,text='生成文件').pack()

createVar = locals()
newlist = []
for i in range(64):
    newlist.append([])
    newlist[i].append(i)
    fm = tk.Frame(f1)
    fm.pack(side='top')
    label1 = tk.Label(fm,text = '窗格{:2}:'.format(i+1))
    label1.pack(side = 'left')
    createVar['var'+str(i)]  = tk.StringVar()
    createVar['text'+str(i)] = tk.Entry(fm,width = 4,textvariable = createVar['var'+str(i)])
    createVar['text'+str(i)].pack(side = 'left')
    label1 = tk.Label(fm, text='方式:')
    label1.pack(side='left')
    for j in range(5):
        SetText(i,j)
s = tk.Scrollbar(root,width=20,command = canvas.yview)
canvas['yscrollcommand']=s.set
s.pack(side = 'right',expand = 1,fill = 'y')
root.update()
canvas.config(scrollregion=canvas.bbox("all"))
root.mainloop()


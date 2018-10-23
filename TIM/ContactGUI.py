from tkinter import *
import TIMDAO
import threading
import  TalkGUI
def ContactSet(userid):
    def closeWindow():
        TIMDAO.Updateuser_state(userid,state=0)
        root.destroy()

    def fun_timer():
        l2.delete(0, END)
        var = TIMDAO.Lookuser()
        for i in var:
            if i[-1] == 1:
                l2.insert(END, i[0] + '：在线')
            else:
                l2.insert(END, i[0] + '：失踪')
        global timer
        timer = threading.Timer(5.5, fun_timer)
        timer.start()
    def AddListBox():
        TalkGUI.TalkSet(userid)

    root = Tk()
    root.geometry('300x600')
    root.title('用户：{}'.format(userid))
    root.resizable(0,0)
    f2 = Frame(root)
    lable1 = Label(f2,text = '在线用户').pack(side = 'top')
    l2 =Listbox(f2,width = 290,height = 30)
    timer = threading.Timer(1, fun_timer)
    timer.start()
    l2.pack(side = TOP)
    button2 = Button(f2,command = AddListBox)
    button2['text'] = '对话'
    button2.pack(side = TOP)

    f2.pack(side =LEFT)
    root.protocol('WM_DELETE_WINDOW', closeWindow)
    root.mainloop()
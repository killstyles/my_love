import tkinter as tk
from tkinter import messagebox
import socket
import TalkGUI
import RegisterGUI
import TIMDAO
import os
import ContactGUI

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('TIM')
        self.root.geometry('420x290')
        self.root.resizable(0, 0)

        f1 = tk.Frame(self.root, width=420, height=290)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        f11 = tk.Frame(f1)
        l1 = tk.Label(f11, text='用户名').pack(side='left')
        logintext = tk.Entry(f11, textvariable=self.username).pack(side='left')
        login_button = tk.Button(f11, text='注册账号', width=10, command=self.openreg).pack(side='left')

        f11.pack()

        f12 = tk.Frame(f1)

        l2 = tk.Label(f12, text='密   码').pack(side='left')
        passwordtext = tk.Entry(f12, textvariable=self.password, show='*').pack(side='left')
        login_button = tk.Button(f12, text='找回密码', width=10, command=self.openfind).pack(side='left')

        f12.pack()

        login_button = tk.Button(f1, text='登录', width=25, command=self.LoginFuc).pack()
        f1.pack()
        self.root.mainloop()
    def openfind(self):
        os.system('python FindpwdGUI.py')
    def openreg(self):
        os.system('python RegisterGUI.py')
    def LoginFuc(self):
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        s.connect(('{}'.format(TIMDAO.get_host_ip()), 9999))
        up =self.username.get()+' '+self.password.get()
        s.send(up.encode('utf-8'))
        re = str(s.recv(1024).decode('utf-8'))
        if  re== '1':
            if TIMDAO.Onlylogin(self.username.get()) == 1:
                tk.messagebox.showinfo('提示', '该用户已经登录，请勿重复登录')
            else:
                tk.messagebox.showinfo('提示','登录成功')
                TIMDAO.Updateuser_state(self.username.get())
                ContactGUI.ContactSet(self.username.get())
                # TalkGUI.TalkSet(self.username.get())
        elif re == '2':
            tk.messagebox.showinfo('提示','用户名不存在')
        else:
            tk.messagebox.showinfo('提示','密码错误')
        s.close()
if __name__ == '__main__':
    lo1 = Login()
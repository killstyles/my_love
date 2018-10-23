import tkinter as tk
import sqlite3
import TIMDAO
class register:
    def __init__(self):
        root = tk.Tk()
        root.geometry('400x300')
        root.title('注册账号')
        f1 = tk.Frame(root, width=420, height=290)

        self.userid = tk.StringVar()
        self.password = tk.StringVar()
        self.name = tk.StringVar()
        self.email = tk.StringVar()

        f11 = tk.Frame(f1)
        l1 = tk.Label(f11, text='用户名').pack(side='left')
        logintext = tk.Entry(f11, textvariable=self.userid).pack(side='left')

        f11.pack()

        f12 = tk.Frame(f1)

        l2 = tk.Label(f12, text='密   码').pack(side='left')
        passwordtext = tk.Entry(f12, textvariable=self.password).pack(side='left')

        f12.pack()
        f13 = tk.Frame(f1)

        l3 = tk.Label(f13, text='姓   名').pack(side='left')
        nametext = tk.Entry(f13, textvariable=self.name).pack(side='left')

        f13.pack()
        f14 = tk.Frame(f1)

        l4 = tk.Label(f14, text='邮   箱').pack(side='left')
        emailtext = tk.Entry(f14, textvariable=self.email).pack(side='left')

        f14.pack()

        reg_button = tk.Button(f1, text='注册', width=25, command=self.Reg).pack()
        f1.pack()
        root.mainloop()
    def Reg(self):
        TIMDAO.Insertuser(self.userid.get(), self.password.get(), self.name.get(), self.email.get())
if __name__ == '__main__':
    reg1 =register()
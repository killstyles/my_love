import tkinter as tk
import TIMDAO
class findpwd:
    def __init__(self):
        root = tk.Tk()
        root.geometry('400x300')
        root.title('找回密码')
        f1 = tk.Frame(root, width=420, height=290)

        self.userid = tk.StringVar()

        self.email = tk.StringVar()

        f11 = tk.Frame(f1)
        l1 = tk.Label(f11, text='用户名').pack(side='left')
        logintext = tk.Entry(f11, textvariable=self.userid).pack(side='left')

        f11.pack()
        f14 = tk.Frame(f1)

        l4 = tk.Label(f14, text='邮   箱').pack(side='left')
        emailtext = tk.Entry(f14, textvariable=self.email).pack(side='left')

        f14.pack()

        find_button = tk.Button(f1, text='找回', width=25, command=self.FindFuc).pack()
        f1.pack()
        root.mainloop()
    def FindFuc(self):
        TIMDAO.Findpassword(self.userid.get(), self.email.get())
if __name__ == '__main__':
    fpwd1 = findpwd()
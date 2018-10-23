import tkinter as tk
import time
import socket
import TIMDAO
import pymysql

def TalkSet(userid):
    # def TalkFuc():
    #     s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    #     s.connect(('192.168.100.40', 5555))
    #     up = send_text.get(0.0,tk.END)
    #     s.send(up.encode('utf-8'))
    #     re = str(s.recv(1024).decode('utf-8'))
    #     s.close()
    #     return re

    def send():
        recv_text.config(state = 'normal')
        str1 =time.ctime()+'\n'+('用户{}:'.format(userid)).center(22,'*')+'\n'+send_text.get(0.0,tk.END)+'\n'
        recv_text.insert(tk.END,'{}'.format(str1))
        recv_text.config(state='disable')
        send_text.delete(1.0,tk.END)
        # TalkFuc()
    root = tk.Tk()
    root.title('修真聊天群')
    root.geometry('600x500')

    recv_text = tk.Text(root,stat = 'disable')
    recv_text.pack()

    send_text = tk.Text(root,height = 10)
    send_text.pack()
    send_button = tk.Button(root,command = send ,text = '发送',width = 10).pack()

    root.mainloop()


if __name__ == '__main__':
    TalkSet()
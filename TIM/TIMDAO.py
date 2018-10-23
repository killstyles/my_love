import sqlite3
from tkinter import messagebox
import  socket
conn = sqlite3.connect('./tim.db')
cursor = conn.cursor()
def Insertuser(userid,password,username='',email='',state = 0):
    try:
        cursor.execute('INSERT INTO user (userid,password,username,email,state) VALUES (?,?,?,?,?)',(userid,password,username,email,state))
        conn.commit()
        messagebox.showinfo('提示', '申请成功')
    except:
        messagebox.showinfo('提示','用户名已经存在')
def Updateuser_state(userid,state = 1):
    try:
        cursor.execute('UPDATE user SET state=? WHERE userid=?', (state,userid))
        conn.commit()
        if state == 1:
            print('上线！')
        else:
            print('下线！')
    except:
        print('登录状态更新失败！')
def Findpassword(userid,email):
    try:
        cursor.execute('SELECT password FROM user WHERE userid = ? and email = ?',(userid,email))
        values = cursor.fetchall()
        messagebox.showinfo('提示', '你的密码：{}'.format(values[0][0]))
    except:
        messagebox.showinfo('提示', '找回失败，请核对你输入的信息')
def Lookuser():
    conn1 = sqlite3.connect('./tim.db')
    cursor1 = conn1.cursor()
    cursor1.execute('SELECT * FROM user')
    values = cursor1.fetchall()
    conn1.commit()
    conn1.close()
    return values
def Insertmessage(recvid,msg,userid):

    cursor.execute('INSERT INTO message (recvid,msg,userid) VALUES (?,?,?)',(recvid,msg,userid))
    conn.commit()
def Onlylogin(myuserid):
    cursor.execute('SELECT state FROM user WHERE userid = ?',[myuserid])
    va = cursor.fetchall()
    conn.commit()
    return va[0][0]
def Lookmessage():
    cursor.execute('SELECT * FROM message')
    values = cursor.fetchall()
    conn.commit()
    return values
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
if __name__ == '__main__':
    print(Lookuser())
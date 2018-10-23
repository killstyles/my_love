import socket
from multiprocessing import Pool
import TIMDAO



def handler(newsd):
    user = {}
    values = TIMDAO.Lookuser()
    for i in values:
        user[i[0]] = i[1]
    data = newsd.recv(1024)
    datas = str(data.decode('utf-8')).split()
    if datas[0] not in user :
        newsd.send('2'.encode('utf-8'))
    elif user[datas[0]] == datas[1]:
        newsd.send('1'.encode('utf-8'))
    else:
        newsd.send('0'.encode('utf-8'))
    newsd.close()
if __name__ == '__main__':
    s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    s.bind(('0.0.0.0',9999))
    s.listen(5)
    p = Pool()
    while True:
        conn,addr = s.accept()
        print(addr)
        p.apply_async(handler,(conn,))

import sqlite3
conn = sqlite3.connect('./tim.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS message ')
cursor.execute('CREATE TABLE message (id integer PRIMARY KEY AUTOINCREMENT NOT NULL,recvid varchar(20) NOT NULL,msg text,userid varchar(20) NOT NULL);')
cursor.execute('''
INSERT INTO message VALUES (1,'787503811','hello 11','787503810');
''')
cursor.execute('''
INSERT INTO message VALUES (2,'787503810','hello 10','787503811');
''')

cursor.execute('DROP TABLE IF EXISTS user ')
cursor.execute('CREATE TABLE user (userid varchar(20) PRIMARY KEY NOT NULL,password varchar(40) NOT NULL,username varchar(20) DEFAULT NULL,email varchar(20) DEFAULT NULL,state int(11) NOT NULL DEFAULT 0)')

cursor.execute('''
INSERT INTO user VALUES ('787503810','123','fwx','787503810@qq.com',0);
''')
cursor.execute('''
INSERT INTO user VALUES ('787503811','123','fff','787503811@qq.com',0);
''')

cursor.close()
conn.commit()
conn.close()
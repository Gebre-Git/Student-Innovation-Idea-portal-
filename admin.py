import sqlite3
conn = sqlite3.connect('admin.db')
c = conn.cursor()
c.execute('''CREATE TABLE admin
        (adminID VARCHAR(20) PRIMARY KEY NOT NULL,
         adminName TEXT NOT NULL,
         Gmail TEXT NOT NULL,
         password TEXT NOT NULL)''')

conn.commit()
conn.close()
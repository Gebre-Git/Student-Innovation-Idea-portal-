import sqlite3
conn = sqlite3.connect('helper.db')
c = conn.cursor()
c.execute('''CREATE TABLE helper
        (helperID VARCHAR(20) PRIMARY KEY NOT NULL,
        Name TEXT NOT NULL,
        Gmail TEXT NOT NULL,
        Occupation TEXT NOT NULL,
        categoryID FOREIGN KEY REFERENCES category(categoryID))''')

conn.commit()
conn.close()
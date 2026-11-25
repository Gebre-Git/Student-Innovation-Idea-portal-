import sqlite3

conn = sqlite3.connect('categories.db')
c = conn.cursor()

c.execute('''CREATE TABLE categories
        (categoryID VARCHAR(20) PRIMARY KEY NOT NULL,
                categoryName TEXT NOT NULL)''')

conn.commit()
conn.close()

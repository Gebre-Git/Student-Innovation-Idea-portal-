import sqlite3

conn = sqlite3.connect('TeamMembers.db')
c = conn.cursor()
c.execute('''CREATE TABLE TeamMembers
        (teamMemberID VARCHAR(20) PRIMARY KEY NOT NULL,
         teamMemberName TEXT NOT NULL,
         ideasID FOREIGN KEY REFERENCES ideas(ideaID))''')

conn.commit()
conn.close()
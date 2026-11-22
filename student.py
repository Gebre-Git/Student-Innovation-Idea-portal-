import sqlite3

conn = sqlite3.connect('Lstudents.db')
#Lstudents table states the information about leader studenStudentName TEXT NOT NULLts
c = conn.cursor()

c.execute('''CREATE TABLE Lstudents 
        (studentID VARCHAR(20) PRIMARY KEY NOT NULL,
              StudentName TEXT NOT NULL,
              Gmail TEXT NOT NULL,
              ideaID FOREIGN KEY REFERENCES ideas(ideaID))''')

conn.commit()
conn.close()
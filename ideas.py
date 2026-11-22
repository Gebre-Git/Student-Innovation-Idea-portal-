import sqlite3

conn = sqlite3.connect('ideas.db')

c = conn.cursor()

c.execute('''CREATE TABLE ideas
        (ideaID VARCHAR(20) PRIMARY KEY NOT NULL,
                ideaTitle TEXT NOT NULL
                IdeaDescription TEXT NOT NULL,
                IdeaDescription TEXT NOT NULL,
                categoryID FOREIGN KEY REFERENCES categories(categoryID)
                Status VARCHAR(20) NOT NULL IN ('Pending', 'Approved', 'Rejected'))''')

conn.commit()
conn.close()
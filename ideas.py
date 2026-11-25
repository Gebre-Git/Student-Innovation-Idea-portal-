import sqlite3

conn = sqlite3.connect('ideas.db')

c = conn.cursor()

c.execute('''CREATE TABLE ideas
        (idea_id VARCHAR(20) PRIMARY KEY NOT NULL,
                idea_title TEXT NOT NULL,
                idea_description TEXT NOT NULL,
                category_id FOREIGN KEY REFERENCES categories(category_id),
                submitted_by FOREIGN KEY REFERENCES users(user_id),
                status VARCHAR(20) NOT NULL IN ('Pending', 'Approved', 'Rejected')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP),
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect('comments.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE comments (
                comment_id INTEGER PRIMARY KEY, 
                idea_id FOREIGN KEY REFERENCES ideas(idea_id),
                admin_id FOREIGN KEY REFERENCES users(user_id) WHERE role=="admin",
                comment_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP''')

conn.commit()
conn.close()

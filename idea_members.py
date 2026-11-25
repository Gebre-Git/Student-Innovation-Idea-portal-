import sqlite3
conn = sqlite3.connect('idea_members.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE idea_members
        (idea_id FOREIGN KEY REFERENCES ideas(idea_id) PRIMARY KEY NOT NULL),
        user_id FOREIGN KEY REFERENCES users(user_id) PRIMARY KEY NOT NULL,
        team_role VARCHAR(20) NOT NULL,
        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP''')
conn.commit()
conn.close()

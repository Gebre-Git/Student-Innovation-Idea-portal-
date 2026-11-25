import sqlite3
conn = sqlite3.connect('status_history.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE status_history
        (history_id INTEGER PRIMARY KEY NOT NULL,
        idea_id REFERENCES idea_members(idea_id),
        old_status REFERENCES ideas(status) NOT NULL,
        new_status REFERENCES ideas(status) NOT NULL,
        Admin_id REFERENCES users(user_id) WHERE role = 'admin' NOT NULL,
        changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()
conn.close()

import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE users
        (user_id VARCHAR(20) PRIMARY KEY NOT NULL,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role VARCHAR(20) NOT NULL IN ('admin', 'user','helper'),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()
conn.close()

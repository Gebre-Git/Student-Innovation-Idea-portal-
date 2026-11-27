import sqlite3

conn = sqlite3.connect('categories.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name VARCHAR(50) UNIQUE NOT NULL
);
""")
conn.commit()
conn.close()

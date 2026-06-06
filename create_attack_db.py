import sqlite3

conn = sqlite3.connect('database/attack_logs.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS attacks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
attack_type TEXT,
payload TEXT
)
''')

conn.commit()
conn.close()

print("Attack Database Created")
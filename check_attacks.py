import sqlite3

conn = sqlite3.connect('database/attack_logs.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM attacks")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
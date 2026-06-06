import sqlite3

conn = sqlite3.connect('database/attack_logs.db')

cursor = conn.cursor()

try:
    cursor.execute(
        "ALTER TABLE attacks ADD COLUMN severity TEXT"
    )
except:
    pass

conn.commit()
conn.close()

print("Database Upgraded")
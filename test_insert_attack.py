import sqlite3
from attack_detector import detect_attack

payload = "<script>alert('Hacked')</script>"

attack_type = detect_attack(payload)

if attack_type:

    conn = sqlite3.connect('database/attack_logs.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attacks (attack_type, payload) VALUES (?, ?)",
        (attack_type, payload)
    )

    conn.commit()
    conn.close()

    print("Attack Inserted")

else:
    print("No Attack Found")
    
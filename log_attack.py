import sqlite3

def log_attack(attack_type, payload):

    severity = "LOW"

    if attack_type == "SQL Injection":
        severity = "HIGH"

    elif attack_type == "XSS Attack":
        severity = "MEDIUM"

    elif attack_type == "Brute Force":
        severity = "HIGH"

    conn = sqlite3.connect('database/attack_logs.db')

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO attacks
        (attack_type,payload,severity)
        VALUES(?,?,?)
        """,
        (attack_type,payload,severity)
    )

    conn.commit()
    conn.close()
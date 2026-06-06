# attack_detector.py

def detect_sql_injection(payload):

    sql_patterns = [
        "' OR",
        '" OR',
        "1=1",
        "UNION SELECT",
        "DROP TABLE",
        "--",
        ";",
        "INSERT INTO",
        "DELETE FROM",
        "UPDATE "
    ]

    payload_upper = payload.upper()

    for pattern in sql_patterns:
        if pattern.upper() in payload_upper:
            return True

    return False


def detect_xss(payload):

    xss_patterns = [
        "<script>",
        "</script>",
        "alert(",
        "onerror=",
        "onload=",
        "javascript:",
        "<img",
        "<iframe",
        "<svg"
    ]

    payload_lower = payload.lower()

    for pattern in xss_patterns:
        if pattern in payload_lower:
            return True

    return False


def detect_attack(payload):

    if detect_sql_injection(payload):
        return "SQL Injection"

    if detect_xss(payload):
        return "XSS Attack"

    return None

def detect_bruteforce(username):

    suspicious_users = [
        "admin",
        "root",
        "administrator"
    ]

    if username.lower() in suspicious_users:
        return True

    return False
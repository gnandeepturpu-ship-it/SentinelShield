# test_insert_attack.py

from log_attack import log_attack

log_attack(
    "SQL Injection",
    "' OR '1'='1"
)

print("Attack Logged")
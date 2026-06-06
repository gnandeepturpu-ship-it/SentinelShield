from attack_detector import detect_attack

payload = "<script>alert('Hacked')</script>"

result = detect_attack(payload)

if result:
    print("Attack Detected:", result)
else:
    print("No Attack Detected")
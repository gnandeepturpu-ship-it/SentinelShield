from flask import Flask, render_template, request, redirect, session
import sqlite3
import random
from log_attack import log_attack

app = Flask(__name__)
app.secret_key = "sentinelshield_secret_key"

# Track failed login attempts
failed_attempts = {}

# ==========================
# LOGIN PAGE
# ==========================
@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database/sentinel.db')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        if username not in failed_attempts:
            failed_attempts[username] = 0

        if not user:

            failed_attempts[username] += 1

            if failed_attempts[username] >= 3:

                log_attack(
                    "Brute Force",
                    f"{username} exceeded login attempts"
                )

                return """
                <h1>Account Locked</h1>
                <h3>Brute Force Attack Detected</h3>
                """

            return f"""
            <h2>Invalid Username or Password</h2>
            <h3>Attempt {failed_attempts[username]} of 3</h3>
            """

        # Reset failed attempts
        failed_attempts[username] = 0

        # Generate OTP
        otp = random.randint(100000, 999999)

        session['otp'] = str(otp)
        session['username'] = username

        print("\n========================")
        print("MFA OTP:", otp)
        print("========================\n")

        return redirect('/otp')

    return render_template('login.html')


# ==========================
# OTP VERIFICATION
# ==========================
@app.route('/otp', methods=['GET', 'POST'])
def otp():

    if request.method == 'POST':

        entered_otp = request.form['otp']

        if entered_otp == session.get('otp'):
            return redirect('/dashboard')

        return "<h2>Invalid OTP</h2>"

    return render_template('otp.html')


# ==========================
# DASHBOARD
# ==========================
@app.route('/dashboard')
def dashboard():

    conn = sqlite3.connect('database/attack_logs.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM attacks")
    total_attacks = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM attacks
        WHERE attack_type='SQL Injection'
    """)
    sql_count = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM attacks
        WHERE attack_type='XSS Attack'
    """)
    xss_count = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM attacks
        WHERE attack_type='Brute Force'
    """)
    brute_force_count = cursor.fetchone()[0]

    conn.close()

    return render_template(
        'dashboard.html',
        total_attacks=total_attacks,
        sql_count=sql_count,
        xss_count=xss_count,
        brute_force_count=brute_force_count
    )


# ==========================
# ATTACK LOGS
# ==========================
@app.route('/attack_logs')
def attack_logs():

    conn = sqlite3.connect('database/attack_logs.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attacks")

    attacks = cursor.fetchall()

    conn.close()

    return render_template(
        'attack_logs.html',
        attacks=attacks
    )


# ==========================
# GENERATE REPORT
# ==========================
@app.route('/generate_report')
def generate_report():

    conn = sqlite3.connect('database/attack_logs.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attacks")
    attacks = cursor.fetchall()

    conn.close()

    with open("security_report.txt", "w") as report:

        report.write("SentinelShield Security Report\n")
        report.write("=============================\n\n")

        report.write(f"Total Attacks: {len(attacks)}\n\n")

        for attack in attacks:
            report.write(str(attack) + "\n")

    return """
    <h1>Security Report Generated</h1>
    <h3>Check security_report.txt in project folder</h3>
    """


# ==========================
# LOGOUT
# ==========================
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')


# ==========================
# RUN APP
# ==========================
if __name__ == '__main__':
    app.run(debug=True)
# 🛡️ SentinelShield

> **Advanced Intrusion Detection and Web Application Protection System**


SentinelShield is a cybersecurity-focused web application that acts as a **lightweight Intrusion Detection System (IDS)** and **Web Application Protection platform**. It monitors user activities, detects suspicious behavior, and prevents unauthorized access in real time — helping protect web applications from common cyber threats.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Attack Detection Capabilities](#attack-detection-capabilities)
- [Dashboard & Reporting](#dashboard--reporting)
- [Contributing](#contributing)

---

## Overview

SentinelShield addresses the need for accessible, lightweight web security tooling — particularly for small projects and teams that need real-time threat detection without the complexity of enterprise security infrastructure.

The system continuously monitors incoming requests and login activity, identifies malicious payloads and patterns, logs all incidents with severity levels, and presents actionable insights through a centralized dashboard.

---

## Features

- 🔐 **Secure Authentication** — Credential-based login with optional Multi-Factor Authentication (MFA) via OTP verification
- 🕵️ **SQL Injection Detection** — Pattern matching against known SQL injection signatures to block malicious database queries
- 🚫 **XSS Detection** — Real-time Cross-Site Scripting payload identification and request blocking
- 🔁 **Brute Force Detection** — Monitors repeated failed login attempts and temporarily restricts access from suspicious sources
- 📊 **Centralized Dashboard** — Live statistics for total attacks, SQL injection attempts, XSS attacks, and brute force incidents
- 🗂️ **Attack Logging** — All detected threats stored in SQLite with attack type, payload, severity level, and timestamp
- 📈 **Severity Classification** — Threats categorized as High, Medium, or Low to help prioritize incident response
- 📄 **Security Reports** — Generate exportable summaries of attack history for auditing and analysis

---



## Architecture

```
SentinelShield
├── Authentication Layer      
├── Request Inspection Engine 
│   ├── SQL Injection Detector
│   ├── XSS Detector
│   └── Brute Force Monitor
├── Attack Log Database       
├── Dashboard                 
└── Report Generator          
```

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gnandeepturpu-ship-it/SentinelShield.git
   cd SentinelShield
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Initialize the database**
   ```bash
   python init_db.py
   ```

### Running the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000` by default.

> ⚠️ For development use only. Do not expose directly to the public internet without additional hardening.

---

## Usage

1. Open `http://127.0.0.1:5000` in your browser.
2. Log in with your credentials. If MFA is enabled, complete OTP verification.
3. Navigate to the **Dashboard** to view live attack statistics.
4. Review the **Attack Logs** for detailed records of all detected threats.
5. Generate a **Security Report** from the Reports section for audit/analysis.

---

## Attack Detection Capabilities

### SQL Injection
SentinelShield analyzes user-submitted inputs and compares them against a database of known SQL injection patterns (e.g., `' OR 1=1`, `UNION SELECT`, `--` comments). Detected payloads are blocked and logged immediately.

### Cross-Site Scripting (XSS)
Incoming inputs are scanned for common XSS vectors such as `<script>`, `onerror=`, `javascript:`, and other known attack strings. Matching requests are rejected before any processing occurs.

### Brute Force Detection
The system tracks failed login attempts per user/IP. When a configurable threshold is exceeded within a time window, access is temporarily blocked to prevent credential stuffing and brute force attacks.

---

## Dashboard & Reporting

The SentinelShield dashboard provides an at-a-glance view of:

- **Total attacks detected** (all time and recent)
- **Breakdown by type** — SQL Injection, XSS, Brute Force
- **Severity distribution** — High / Medium / Low
- **Recent attack log** with timestamps and payloads

Security reports can be generated from the Reports section, covering configurable time ranges with full attack summaries suitable for security audits.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add: your feature description'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

Please ensure your code follows existing conventions and includes relevant comments.

---

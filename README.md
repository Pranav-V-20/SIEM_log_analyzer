# 🛡️ SIEM Log Analyzer

A lightweight Python-based **Security Information and Event Management (SIEM)** tool designed to **ingest**, **analyze**, and **detect anomalies** in logs from multiple sources — including **Apache logs**, **Syslog**, and **Windows Event Logs**. Alerts are automatically sent via email when suspicious activity is detected using regex-based or ML-based methods.

---

## ✅ Features

* 📥 **Log Ingestion**
  Parse and normalize logs from:

  * Apache access logs
  * Linux Syslog
  * Windows Event Logs (mock text)

* 🔍 **Anomaly Detection**

  * Regex-based pattern matching for known suspicious activity
  * Optional machine learning anomaly detection using `IsolationForest`

* 📧 **Email Alerts**

  * Automatically send alerts via SMTP (Gmail supported via App Passwords)

---

## 📁 Project Structure

```
siem_log_analyzer/
├── main.py                  # Entry point
├── log_parsers.py           # Apache, syslog, and Windows log parsers
├── anomaly_detector.py      # Regex + ML anomaly detection
├── email_alert.py           # Email notification module
└── logs/
    ├── apache.log
    ├── syslog.log
    └── windows_events.log
```

---

## ⚙️ Requirements

* Python 3.7+
* Libraries:

  ```bash
  pip install scikit-learn
  ```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/siem-log-analyzer.git
cd siem-log-analyzer
```

### 2. Configure Email Alerts

Edit `email_alert.py` and replace:

```python
EMAIL_SENDER = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'  # Use Gmail App Password
EMAIL_RECEIVER = 'receiver_email@example.com'
```

> 🔐 **Important**: Gmail blocks basic auth. Use an **App Password** by enabling 2-Step Verification and generating one [here](https://myaccount.google.com/apppasswords).

### 3. Add Your Logs

Place your `.log` files inside the `/logs` folder.

Example file names:

* `apache.log`
* `syslog.log`
* `windows_events.log`

---

### 4. Run the Analyzer

```bash
python main.py
```

---

## 📡 Sample Log Formats

**Apache:**

```
192.168.1.1 - - [10/Oct/2024:13:55:36] "GET /admin HTTP/1.1" 401
```

**Syslog:**

```
Feb 14 10:23:45 server sshd[1234]: Failed password for invalid user root
```

**Windows Events (text):**

```
Access denied on file cmd.exe
```

---

## 🧠 Anomaly Detection

### Regex-based:

Detects known patterns such as:

* Failed login
* `cmd.exe`, `powershell`, `/etc/passwd`
* "unauthorized", "denied", "malware"

### ML-based (optional):

Uses `IsolationForest` to detect outliers based on frequency (e.g., IP frequency anomalies).

---

## 📬 Email Alert Sample

Subject: `SIEM ALERT: Anomaly Detected in Logs`

```
Suspicious activity detected in logs:

{'source': 'syslog', 'line': 'Failed password for invalid user root'}
{'source': 'apache', 'ip': '192.168.1.1', 'request': 'GET /admin HTTP/1.1', ...}
...
```

---

## 🔒 Security Note

Do **NOT** hardcode real passwords or sensitive keys in production.
Use `.env` files or secret managers to protect your credentials.

---

## 🛠️ To Do

* [ ] Real-time log streaming
* [ ] Web dashboard (Flask/Django)
* [ ] Integration with Slack or Discord
* [ ] JSON log format support

---

## 🤝 Contributing

PRs and issues are welcome! For major changes, please open an issue first to discuss what you would like to change.

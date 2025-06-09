import smtplib
from email.mime.text import MIMEText

# CONFIGURE THIS FIRST
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_SENDER = 'pranavvijayakumar20@gmail.com'
EMAIL_PASSWORD = 'app_password'
EMAIL_RECEIVER = 'pranavofficialskill@gmail.com'

def send_email_alert(anomalies):
    message = "Suspicious activity detected in logs:\n\n"
    for a in anomalies:
        message += str(a) + "\n"

    msg = MIMEText(message)
    msg['Subject'] = '[SIEM ALERT] Anomaly Detected in Logs'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("[+] Alert email sent.")
    except Exception as e:
        print("[-] Failed to send email:", e)

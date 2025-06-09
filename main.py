from log_parsers import parse_apache_logs, parse_syslog, parse_windows_event_logs
from anomaly_detector import detect_anomalies
from email_alert import send_email_alert

def main():
    print("[*] Starting SIEM Log Analyzer...")

    apache_logs = parse_apache_logs("logs/apache.log")
    sys_logs = parse_syslog("logs/syslog.log")
    windows_logs = parse_windows_event_logs("logs/windows_events.log")

    all_logs = apache_logs + sys_logs + windows_logs
    print(f"[*] Parsed {len(all_logs)} total log entries")

    anomalies = detect_anomalies(all_logs)

    if anomalies:
        print(f"[!] Detected {len(anomalies)} anomalies.")
        send_email_alert(anomalies)
    else:
        print("[✓] No anomalies detected.")

if __name__ == "__main__":
    main()

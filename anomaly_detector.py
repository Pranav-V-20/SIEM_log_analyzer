import re
from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(logs):
    anomalies = []

    suspicious_patterns = [
        r"Failed password",
        r"unauthorized",
        r"denied",
        r"malware",
        r"/etc/passwd",
        r"cmd.exe",
        r"powershell"
    ]

    # Regex-based detection
    for log in logs:
        text = log.get('line', log.get('request', ''))
        for pattern in suspicious_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                anomalies.append(log)
                break

    # ML-based detection (basic feature: IP frequency anomaly)
    ip_addresses = [log.get('ip', '0.0.0.0') for log in logs if 'ip' in log]
    if ip_addresses:
        ip_counts = {ip: ip_addresses.count(ip) for ip in set(ip_addresses)}
        features = np.array([[ip_counts[ip]] for ip in ip_addresses])

        clf = IsolationForest(contamination=0.1, random_state=42)
        preds = clf.fit_predict(features)

        for i, pred in enumerate(preds):
            if pred == -1:
                anomalies.append(logs[i])

    return anomalies

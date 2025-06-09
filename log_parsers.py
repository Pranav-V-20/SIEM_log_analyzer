import re

def parse_apache_logs(filepath):
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d{3})')
    logs = []
    with open(filepath, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                logs.append({
                    'source': 'apache',
                    'ip': match.group(1),
                    'timestamp': match.group(2),
                    'request': match.group(3),
                    'status': match.group(4)
                })
    return logs

def parse_syslog(filepath):
    logs = []
    with open(filepath, 'r') as f:
        for line in f:
            logs.append({'source': 'syslog', 'line': line.nstrip()})
    return logs

def parse_windows_event_logs(filepath):
    logs = []
    with open(filepath, 'r') as f:
        for line in f:
            logs.append({'source': 'windows', 'line': line.strip()})
    return logs

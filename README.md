# Failed Login Analyzer

A simple SOC tool to parse Windows Security logs (`.evtx`) and detect failed login attempts.  
Generates a CSV report with account names and timestamps.

## Features
- Detect failed login events (Event ID 4625)
- Generate a CSV report
- Easy to extend for other log analysis

## Folder Structure

failed_login_analyzer/
├── sample_logs/
├── parse_failed_logins.py
├── failed_logins_report.csv
└── README.md


## Setup & Usage

```bash
git clone <your-repo-url>
cd SOC-Toolkit/failed_login_analyzer
source ~/SOC-Toolkit/venv/bin/activate
pip install pandas requests scapy Evtx
python3 parse_failed_logins.py
cat failed_logins_report.csv

 Place your .evtx file in sample_logs/ before running.

## Sample Output
```

time,account
2025-11-23T08:42:15.0000000Z,John
2025-11-23T09:01:22.0000000Z,Admin

```



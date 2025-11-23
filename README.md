Failed Login Analyzer

A lightweight SOC tool that parses Windows Security Logs (.evtx) to detect failed login attempts (Event ID 4625).
It extracts usernames, timestamps, and generates a clean CSV report for fast analysis.
Features

✔ Detect failed login events (Event ID 4625)
✔ Extract account name + timestamp
✔ Export results into failed_logins_report.csv
✔ Easy to modify for more detection logic (4624, 4720, brute-force patterns, etc.)
Folder Structure
failed_login_analyzer/
│
├── sample_logs/
│   └── Security.evtx        # place your log file here
│
├── parse_failed_logins.py   # main script
├── failed_logins_report.csv # generated output
└── README.md
Setup & Usage
1. Clone the repository
   git clone https://github.com/TahsinAhmedRifat/failed_login_analyzer.git
cd failed_login_analyzer
2. (Optional) Activate your virtual environment
   source ~/SOC-Toolkit/venv/bin/activate
3. Install dependencies
   pip install pandas Evtx
4. Place your log file
   sample_logs/
5. Run the analyzer
   python3 parse_failed_logins.py
6. View the generated report
   cat failed_logins_report.csv
Sample Output
time,account
2025-11-23T08:42:15.0000000Z,John
2025-11-23T09:01:22.0000000Z,Admin

Put your .evtx file inside:

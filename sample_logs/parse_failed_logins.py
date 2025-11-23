import Evtx.Evtx as evtx
import xml.etree.ElementTree as ET
import csv
import os

# Paths
log_file = "sample_logs/Security.evtx"
output_file = "failed_logins_report.csv"

failed_logins = []

# Open the EVTX file
with evtx.Evtx(log_file) as log:
    for record in log.records():
        xml_str = record.xml()
        root = ET.fromstring(xml_str)
        # Look for EventID 4625 (Failed login)
        event_id = root.find(".//EventID")
        if event_id is not None and event_id.text == "4625":
            account = root.find(".//Data[@Name='TargetUserName']")
            time_created = root.find(".//TimeCreated")
            failed_logins.append({
                "account": account.text if account is not None else "Unknown",
                "time": time_created.attrib.get("SystemTime") if time_created is not None else "Unknown"
            })

# Save results to CSV
if failed_logins:
    with open(output_file, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["time", "account"])
        writer.writeheader()
        for f in failed_logins:
            writer.writerow(f)
    print(f"Saved {len(failed_logins)} failed logins to {output_file}")
else:
    print("No failed logins found.")


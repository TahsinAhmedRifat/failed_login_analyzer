import xml.etree.ElementTree as ET
import csv

# Path to fake XML file
log_file = "sample_logs/Security.evtx"
output_file = "failed_logins_report.csv"

# Read the XML file as plain text
with open(log_file, "r") as f:
    xml_data = f.read()

root = ET.fromstring(xml_data)
failed_logins = []

for event in root.findall("Event"):
    event_id = event.find(".//EventID")
    if event_id is not None and event_id.text == "4625":
        account = event.find(".//Data[@Name='TargetUserName']")
        time_created = event.find(".//TimeCreated")
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


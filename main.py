import json
import pprint

# Sample raw railway system logs (simulating corrupted lines and sensor failures)
raw_telemetry_logs = [
    "2026-11-03T08:00:01;HVAC_01;200;22.4",
    "2026-11-03T08:00:02;TRACTION_02;503;88.7",
    "2026-11-03T08:00:03;BRAKE_01;200;N/A",      # Sensor failure (non-numeric value)
    "2026-11-03T08:00:04;DOOR_04;ERROR;19.1",    # Invalid status code
    "2026-11-03T08:00:05;TRACTION_02;200;92.1",
    "CORRUPTED_LINE_WITHOUT_DELIMITERS",         # Malformed packet
]

def parse_railway_telemetry(logs):
    """
    Parses raw telemetry logs, guards against invalid data types,
    and returns a list of validated records.
    """
    valid_records = []

    for line in logs:
        try:
            # Step 1: Split the log line by delimiter
            parts = line.split(";")
            
            # Verify structure (must contain exactly 4 columns)
            if len(parts) != 4:
                continue 

            timestamp, subsystem_id, raw_status, raw_temp = parts
            
            # Step 2: Safe type casting
            status_code = int(raw_status)
            temperature = float(raw_temp)
            
            # Step 3: Append the valid structured record
            valid_records.append({
                "timestamp": timestamp,
                "subsystem": subsystem_id,
                "status_code": status_code,
                "temperature": temperature
            })

        except ValueError:
            # Silently skip lines containing corrupt or non-numeric data (e.g., "N/A" or "ERROR")
            continue

    return valid_records

if __name__ == "__main__":
    print("--- Starting telemetry log analysis ---")
    results = parse_railway_telemetry(raw_telemetry_logs)
    
    pprint.pprint(results)
    
    # Save the structured report to a JSON file
    with open("telemetry_report.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print("\n[SUCCESS]: Report successfully generated and saved to telemetry_report.json")

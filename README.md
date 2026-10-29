# Rail Log Parser & Telemetry Analyzer

A robust Python utility designed for parsing, cleaning, and analyzing industrial and railway telemetry logs. It handles corrupted packets, implements defensive programming via `try/except` blocks, and generates structured JSON reports.

## Key Features
- **Defensive Parsing:** Safely processes raw log streams, ignoring corrupted or malformed entries without crashing.
- **Exception Handling:** Catches `ValueError` and `IndexError` when dealing with invalid sensor data (e.g., `"N/A"` or missing parameters).
- **Data Export:** Compiles clean telemetry data into structured JSON format for downstream monitoring or AI ingestion.

## Tech Stack
- Python 3.x
- Built-in modules: `json`, `pprint`

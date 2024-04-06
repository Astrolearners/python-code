import os

capture_path = f"{os.getcwd()}/data/captures"
csv_path = f"{os.getcwd()}/data/csv-files"
log_path = f"{os.getcwd()}/data/logs"

if not os.path.exists(csv_path):
    os.mkdir(csv_path)

if not os.path.exists(log_path):
    os.mkdir(log_path)

if not os.path.exists(capture_path):
    os.mkdir(capture_path)
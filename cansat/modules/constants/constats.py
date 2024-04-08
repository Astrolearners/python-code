import os
from datetime import datetime

base_name = datetime.now().strftime("%d_%m_%y")

data_path = f"{os.getcwd()}/data"

capture_path = f"{data_path}/captures"
csv_path = f"{data_path}/csv-files"
log_path = f"{data_path}/logs"

log_file = f"{log_path}/{base_name}.log"
csv_file = f"{csv_path}/{base_name}.csv"

if not os.path.exists(data_path):
    os.mkdir(data_path)

if not os.path.exists(csv_path):
    os.mkdir(csv_path)

if not os.path.exists(log_path):
    os.mkdir(log_path)

if not os.path.exists(capture_path):
    os.mkdir(capture_path)
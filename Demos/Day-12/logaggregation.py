# Log Aggregation with Python Pandas 

# when processing GB of log files, parsing it line by line in python can cause performance bottleneck for CPU. 
# Using Pandas library can help to vectorize operations and aggregate. 

# Use pandas for scalable analysis 

# for deep data processing, first convert the raw data structure into a pandas dataframe. This allows you to 
# aggregate the occurances, filter out anomalies and query the specific parameters across the thousands of lines simultaneously. 

import pandas as pd 

# Mock the data extracted from logs 

raw_logs = [
    {"timestamp": "2026-07-21 09:10:00", "level": "INFO", "message": "User login success"},
    {"timestamp": "2026-07-21 09:12:00", "level": "WARNING", "message": "High bandwidth utilization" },
    {"timestamp": "2026-07-21 09:15:00", "level": "ERROR", "message": "Router Connection is failed" },
    {"timestamp": "2026-07-21 09:16:00", "level": "ERROR", "message": "Gateway Timeout Error" },
    {"timestamp": "2026-07-21 09:17:00", "level": "ERROR", "message": "SSH Connection Failed" },
]

# Load these logs into data frame and convert the data types 

df = pd.DataFrame(raw_logs)
df['timestamp'] = pd.to_datetime(df['timestamp'])


# 1. Count the logs by severity level 
level_counts = df['level'].value_counts()
print("Log counts by Level:\n", level_counts)

# 2. Filter out specific problem states 
errors_only = df[df['level'] == 'ERROR']
print("\nIsolated System Errors:\n", errors_only)
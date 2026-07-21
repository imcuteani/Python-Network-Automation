# Log parsing in Python converts the unstructured plain log data into structured actionable data. 
# 
# if your logs use a fixed seperators, use standard string manipulation. 
# 
# Basic text splitting 
# 
log_line = "2026-06-08 09:42:00 INFO User logged in" 

# split by whitespaces, limiting the splits to isolate the message 
parts = log_line.split(" ", 3)

if len(parts) >= 4:
    timestamp = f"{parts[0]} {parts[1]}"
    log_level = parts[2]
    message = parts[3]

    print(f"level: {log_level} | Msg: {message}")   

# using regular expression -> use the standard server logs, use the python re module to provide named capture groups to pull out variables cleanly. 
# 
import re 

# standard Apache/ Nginx log format example 

log_pattern = r'(\S+) (\S+) (\S+) \[([w:/]+\s[+\-]\d{4})\] "(\S+)\s*(S*)" (\d{3}) (\d+)'

sample_log = '192.168.1.1 -- [25/May/2026:09:51:00 +0000] "GET /index.html HTTP 1.1" 200 54321'

#parse the log entry using regex
match = re.match(log_pattern, sample_log)
if match:
    ip_address = match.group(1)
    date_time = match.group(4)
    method = match.group(5)
    requested_url = match.group(6)
    http_status = match.group(8)
    bytes_transferred = match.group(9)
   
    print("IP address:", ip_address)
    print("date/time:", date_time)
    print("Method:", method)
    print("Requested URL", requested_url)
    print("HTTP status", http_status)
else:
   print("Log entry does not match with the expected format")


# Python handles the end to end log parsing in Production Automation environment using built-in modules like 
# logging and re for generation and extraction for logs. It also uses the 3rd-party libraries like 
# pandas and loguru for high throughput based scaling, using these two libraries, it can be performed - 

# 1. collection/structuring of logs at the emission time 
# 2. Parsing / extracting data from existing data streams. 

# Basic logging string splitting (Fastest format)

# sample: TimeStamp | Level | Message 

line = "2026-07-21 08:50:00 | WARNING | Network Utilization at 80%"

parts = line.split(" | ")
if len(parts) >= 3:
    log_data = {
        "time": parts[0],
        "level": parts[1],
        "message": parts[2].strip()
    }
    print(log_data)

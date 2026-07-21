# The server log file ('server.log') is opened and read line by line. Each line is split into parts 
# based on spaces, and the timestamp with severity are extracted from the first two parts. 
# the remaining parts are joined together to form the message. 
# finally the extracted information is printed onto the console for finalized processing. 

log_file = 'server.log'

with open(log_file, 'r') as file: 
    for line in file: 
        parts = line.split(' ')
        timestamp = parts[0]
        severity = parts[1]
        message = ' '.join(parts[2:]) # process extracted information as needed
        print(
            f"Timestamp: {timestamp}, Severity: {severity}, Message: {message}"
        )
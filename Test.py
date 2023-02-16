import re

# Open the log file and read the contents into a string
with open('TE.log', 'r') as f:
    log = f.read()

# Split the log file into individual lines
lines = log.split('\n')

# Initialize a list to store the extracted information
log_entries = []

# Iterate over each line in the log file
for line in lines:
    # Initialize a dictionary to store the log entry
    log_entry = {}

    # Extract the time using a regular expression
    time_match = re.search(r'\d{2}:\d{2}:\d{2}', line)
    if time_match:
        log_entry['time'] = time_match.group(0)

    # Extract the IP using a regular expression
    ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
    if ip_match:
        log_entry['ip'] = ip_match.group(0)

    # Extract the connection type using string manipulation
    log_entry['conn_type'] = line.split()[6]

    # Extract the services using string manipulation
    log_entry['services'] = line.split()[7]

    # Extract the URL using string manipulation
    log_entry['url'] = line.split()[8]

    # Extract the bytes using string manipulation
    log_entry['bytes'] = line.split()[9]

    # Extract the packets using string manipulation
    log_entry['packets'] = line.split()[10]

    # Add the log entry to the list
    log_entries.append(log_entry)

# Print the extracted information
print(log_entries)

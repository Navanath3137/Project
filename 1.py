import re
import pandas as pd

# Open the log file and read the contents into a string
with open('connectio.log', 'r') as f:
    log = f.read()

# Split the log file into individual lines
lines = log.split('\n')

# Initialize lists to store the extracted information
time = []
ip = []
conn_type = []
services = []
url = []
bytes = []
packets = []

# Iterate over each line in the log file
for line in lines:
    # Extract the time using a regular expression
    time_match = re.search(r'\d{2}:\d{2}:\d{2}', line)
    if time_match:
        time.append(time_match.group(0))

    # Extract the IP using a regular expression
    ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
    if ip_match:
        ip.append(ip_match.group(0))

    # Extract the connection type using string manipulation
    conn_type.append(line.split()[6])

    # Extract the services using string manipulation
    services.append(line.split()[7])

    # Extract the URL using string manipulation
    url.append(line.split()[8])

    # Extract the bytes using string manipulation
    bytes.append(line.split()[9])

    # Extract the packets using string manipulation
    packets.append(line.split()[10])

# Create a DataFrame from the extracted information
df = pd.DataFrame({
    'time': time,
    'ip': ip,
    'conn_type': conn_type,
    'services': services,
    'url': url,
    'bytes': bytes,
    'packets': packets
})

# Print the DataFrame
print(df)

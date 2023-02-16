import pandas as pd
from datetime import datetime
import re

# Open the log file
with open("connectio.log", "r") as file:
    logs = file.readlines()

# Initialize an empty dictionary to store the data
data = {'Date_Time': [], 'Source_IP': [], 'Destination_URL': [], 'Destination_IP': [],'Duration':[], 'Bytes':[], 'Packets':[], 'Iface':[]}

# Iterate over each log
for log in logs:
    try:
        date_time = datetime.strptime(log.strip()[1:20], '%d/%b/%Y %H:%M:%S')
        data['Date_Time'].append(date_time)
        source_ip = log.strip().split(" ")[6].split(":")[0]
        data['Source_IP'].append(source_ip)
        destination_url = log.strip().split(" ")[8]
        data['Destination_URL'].append(destination_url)
        destination_ip = log.strip().split(" ")[9][1:-1]
        data['Destination_IP'].append(destination_ip)
        match = re.search(r'\[(.*?)\] \[ID\] (.*?) \[Rule\] (.*?) \[Service\] (.*?) \[Connection\] (.*?) (.*?) -> (.*?) \((.*?)\):(.*?) \[Iface\] (.*?) \[Duration\] (.*?) sec \[Bytes\] (.*?)\/(.*?)\/(.*?) \[Packets\] (.*?)\/(.*?)\/(.*?)', log)
        if match:
            duration = match.group(12)
            bytes = match.group(13)
            packets = match.group(15)
            iface = match.group(11)
            data['Duration'].append(duration)
            data['Bytes'].append(bytes)
            data['Packets'].append(packets)
            data['Iface'].append(iface)
    except Exception as e:
        print(f'Error processing log: {log}')
        print(e)

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv("logs.csv",index=False)

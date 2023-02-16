import re
import pandas as pd

# Open the log file
with open("TE.log", "r") as file:
    logs = file.readlines()

# Initialize an empty dictionary to store the data
data = {'Date_Time': [], 'Source_IP': [], 'Destination_URL': [], 'Destination_IP': []}

# Iterate over each log
for log in logs:
    match = re.search(r'\[(.*?)\] \[ID\] (.*?) \[Rule\] (.*?) \[Service\] (.*?) \[Connection\] (.*?) (.*?) -> (.*?) \((.*?)\):(.*?) \[Iface\] (.*?) \[Duration\] (.*?) sec \[Bytes\] (.*?)\/(.*?)\/(.*?) \[Packets\] (.*?)\/(.*?)\/(.*?)', log)
    if match:
        date_time = match.group(1)
        source_ip = match.group(6)
        destination_url = match.group(7)
        destination_ip = match.group(8)
        data['Date_Time'].append(date_time)
        data['Source_IP'].append(source_ip)
        data['Destination_URL'].append(destination_url)
        data['Destination_IP'].append(destination_ip)
    else:
        print(f'No match found for log: {log}')

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv("logs.csv",index=False)

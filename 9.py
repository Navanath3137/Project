"""
from datetime import datetime

# Open the log file
with open("TE.log", "r") as file:
    logs = file.readlines()

# Initialize an empty dictionary to store the data
data = {'Date_Time': [], 'Source_IP': [], 'Destination_URL': [], 'Destination_IP': []}

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
    except Exception as e:
        print(f'Error processing log: {log}')
        print(e)

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv("logs.csv",index=False)"""

import pandas as pd
from datetime import datetime

# Open the log file
with open("TE.log", "r") as file:
    logs = file.readlines()

# Initialize an empty dictionary to store the data
data = {'Date_Time': [], 'Source_IP': [], 'Destination_URL': [], 'Destination_IP': []}

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
    except Exception as e:
        print(f'Error processing log: {log}')
        print(e)

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv("logs.csv",index=False)

import re
import csv

# Open the log file for reading
with open('connectio.log', 'r') as log_file:

    # Define the regular expression to extract data from each line of the log file
    log_pattern = re.compile(r'\[(.*)\]\s\[ID\] (\d+)\s\[Rule\] (.+?)\s?\[(?:Service|Connection)\] (.+?)\s(TCP|UDP) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+) -> (.+?) \((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\):(\d+)\s?\[(?:Iface|Zone)\] (\w+)\s?\[(?:Duration|Elapsed)\] (\d+) sec\s?\[(?:Bytes|Sent|Received)\] (\d+)/(\d+)/(\d+)\s?\[(?:Packets|Frames)\] (\d+)/(\d+)/(\d+)')

    # Initialize a list to store the extracted data
    log_data = []

    # Loop over each line in the log file and extract the relevant data
    for line in log_file:
        match = log_pattern.search(line)
        if match:
            log_data.append(match.groups())

# Open a CSV file for writing
with open('output.csv', 'w', newline='') as csv_file:

    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the header row to the CSV file
    csv_writer.writerow(['Timestamp', 'ID', 'Rule', 'Connection', 'Protocol', 'Source IP', 'Source Port', 'Destination IP', 'Destination Port', 'Zone', 'Duration', 'Bytes Sent', 'Bytes Received', 'Bytes Total', 'Packets Sent', 'Packets Received', 'Packets Total'])

    # Write the log data to the CSV file
    for row in log_data:
        csv_writer.writerow(row)

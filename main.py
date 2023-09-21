import re
import csv

def extract_data_from_log(log_file_path):
    log_data = []

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = re.search(r'\[ID\] (\d+) \[Rule\] ([^[]+) \[Service\] (\S+) \[Connection\] TCP [^\s]+ -> (\S+)', line)
            if match:
                connection_id = match.group(1)
                rule = match.group(2)
                internet_access = match.group(3)
                url = match.group(4)
                log_data.append((connection_id, rule, internet_access, url))

    return log_data

def write_to_csv(output_file_path, data):
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Rule', 'Internet Access', 'URL'])

        for item in data:
            writer.writerow(item)

if __name__ == "__main__":
    log_file_path = "irctc.log"
    extracted_data = extract_data_from_log(log_file_path)

    output_csv_path = "output.csv"
    write_to_csv(output_csv_path, extracted_data)

    # Print the extracted data separately
    for item in extracted_data:
        connection_id, rule, internet_access, url = item
        print(f"ID: {connection_id}, Rule: {rule}, Internet Access: {internet_access}, URL: {url}")

import re

# Open the log file in read mode
with open('connectio.log', 'r') as f:
  # Iterate over each line in the file
  for line in f:
    # Use regular expressions to extract the relevant information
    date_regex = r'\d{2}/\d{2}/\d{4}'
    time_regex = r'\d{2}:\d{2}:\d{2}'
    ip_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    url_regex = r'[^\s]+\.com'
    connection_regex = r'[A-Z]+'
    bytes_regex = r'\d+'
    packets_regex = r'\d+'
    duration_regex = r'\d+'  # regular expression to extract duration from log lines

    date_match = re.search(date_regex, line)
    time_match = re.search(time_regex, line)
    ip_match = re.search(ip_regex, line)
    url_match = re.search(url_regex, line)
    connection_match = re.search(connection_regex, line)
    bytes_match = re.search(bytes_regex, line)
    packets_match = re.search(packets_regex, line)
    duration_match = re.search(duration_regex, line)  # extract duration from log line

    if date_match:
      date = date_match.group()
    else:
      date = 'N/A'

    if time_match:
      time = time_match.group()
    else:
      time = 'N/A'

    if ip_match:
      ip = ip_match.group()
    else:
      ip = 'N/A'

    if url_match:
      url = url_match.group()
    else:
      url = 'N/A'

    if connection_match:
      connection = connection_match.group()
    else:
      connection = 'N/A'

    if bytes_match:
      bytes = bytes_match.group()
    else:
      bytes = 'N/A'

    if packets_match:
      packets = packets_match.group()
    else:
      packets = 'N/A'

    if duration_match:
      duration = duration_match.group()  # assign duration value to variable
    else:
      duration = 'N/A'  # set duration to "N/A" if no match is found

    # Print the extracted information to the console
    print("Date:", date)
    print("Time:", time)
    print("IP:", ip)
    print("URL:", url)
    print("Connection:", connection)
    print("Bytes:", bytes)
    print("Packets:", packets)
    print("Duration:", duration)

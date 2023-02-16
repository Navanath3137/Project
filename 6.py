"""import re
from collections import Counter

# Open and read the log file
logfile = open("connectio.log", "r")
logfile_lines = logfile.readlines()

# Create a list to store the IP addresses
newip = []

# Create a Counter() object to count the number of occurrences of each IP address
c = Counter()

# Loop through the log file lines
for line in logfile_lines:

    # Extract all IP addresses from the log file lines
    ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)

    # Update the Counter() object with the IP addresses
    c.update(ips)

# Print the IP addresses and their count
print('Source IP addresses:', c)
"""
"""
import re
from collections import Counter

# Open and read the log file
logfile = open("TE.log", "r")
logfile_lines = logfile.readlines()

# Create a Counter() object to count the number of occurrences of each IP address
c = Counter()
d = Counter()
# Loop through the log file lines
for line in logfile_lines:
    
    # Extract all source and destination IP addresses from the log file lines
    source_ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
    dest_ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
    
    # Update the Counter() object with the source and destination IP addresses
    c.update(source_ips)
    d.update(dest_ips)

# Print the IP addresses and their count
print('Source IP addresses:', c)
print('Destination IP address:', d)
"""
"""
import logging

# Define logging format 
formatter = logging.Formatter('Source IP: %(message)s Destination IP: %(asctime)s')

# Create logger object
logger = logging.getLogger('logger') 
logger.setLevel(logging.INFO)

# Configure the logger with the formatter
logging.basicConfig(format=formatter)

# Log the source and destination IPs
logger.info('172.68.0.1')
logger.info('172.68.0.2')

# Read the log file
with open('TE.log', 'r') as f: 
  log_records = f.readlines()

# Extract the source and destination IPs in tabular format
print('Source IP\tDestination IP')
for log_record in log_records: 
  log_record_obj = logging.LogRecord(log_record)
  print(log_record_obj.getMessage(),'\t', log_record_obj.asctime)
  """
"""
import logging

# Define logging format
formatter = logging.Formatter('Source IP: %(message)s Destination IP: %(asctime)s')

# Create logger object
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

# Configure the logger with the formatter
logging.basicConfig(format='Source IP: %(message)s Destination IP: %(asctime)s')

# Log the source and destination IPs
logger.info('172.68.0.1')
logger.info('172.68.0.2')

# Read the log file
with open('TE.log', 'r') as f:
  log_records = f.readlines()

# Extract the source and destination IPs in tabular format
print('Source IP\tDestination IP')
for log_records in log_records:
  log_record_obj = logging.LogRecord(log_records)
  print(log_record_obj.getMessage(),'\t', log_record_obj.asctime)
  """
"""
import logging

# Define logging format
formatter = logging.Formatter('Source IP: %(message)s Destination IP: %(asctime)s')

# Create logger object
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

# Configure the logger with the formatter
logging.basicConfig(format='Source IP: %(message)s Destination IP: %(asctime)s')

# Log the source and destination IPs
logger.info('172.68.0.1')
logger.info('172.68.0.2')

# Read the log file
with open('TE.log', 'r') as f:
  log_records = f.readlines()

# Extract the source and destination IPs in tabular format
print('Source IP\tDestination IP')
for log_record in log_records:
  log_record_obj = logging.LogRecord(
    name = logger.name,
    level = logging.INFO,
    pathname = 'log_file.log',
    lineno = 0,
    msg = log_record,
    args = None,
    exc_info = None
    )
  print(log_record_obj.getMessage(),'\t', log_record_obj.asctime)
  """
"""
import logging

# Define logging format
formatter = logging.Formatter('Source IP: %(message)s Destination IP: %(created)s')

# Create logger object
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

# Configure the logger with the formatter
logging.basicConfig(format='Source IP: %(message)s Destination IP: %(created)s')

# Log the source and destination IPs
logger.info('172.68.0.1')
logger.info('172.68.0.2')

# Read the log file
with open('TE.log', 'r') as f:
  log_records = f.readlines()

# Extract the source and destination IPs in tabular format
print('Source IP\tDestination IP')
for log_record in log_records:
  log_record_obj = logging.LogRecord(
    name = logger.name,
    level = logging.INFO,
    pathname = 'log_file.log',
    lineno = 0,
    msg = log_record,
    args = None,
    exc_info = None
    )
  print(log_record_obj.getMessage(),'\t', log_record_obj.created)
  """
"""
# Define empty lists
src_ip_list = []
dest_ip_list = []

# Read the log file
with open('TE.log', 'r') as f:
  log_records = f.readlines()

# Extract the source and destination IPs
for log_record in log_records:
  src_ip, dest_ip = log_record.split(',')
  src_ip_list.append(src_ip)
  dest_ip_list.append(dest_ip)

# Print the source and destination IPs in tabular format
print('Source IP\tDestination IP')
for i in range(len(src_ip_list)):
  print(src_ip_list[i], '\t', dest_ip_list[i])"""
"""
# Define empty lists
src_ip_list = []
dest_ip_list = []

# Read the log file
with open('connectio.log', 'r') as f:
  log_records = f.readlines()

# Extract the source and destination IPs
for log_record in log_records:
  # Split the log record into two parts
  timestamp, ip_addresses = log_record.split(';')
  # Split the IP addresses into two parts
  src_ip, dest_ip = ip_addresses.split(',')
  src_ip_list.append(src_ip)
  dest_ip_list.append(dest_ip)

# Print the source and destination IPs in tabular format
print('Source IP\tDestination IP')
for i in range(len(src_ip_list)):
  print(src_ip_list[i], '\t', dest_ip_list[i])
  """
"""
# Define empty lists
src_ip_list = []
dest_ip_list = []

# Read the log file
with open('TE.log', 'r') as f:
  log_records = f.readlines()

# Extract the source and destination IPs
for log_record in log_records:
  # Split the log record into three parts
  timestamp, src_ip, dest_ip = log_record.split('')
  src_ip_list.append(src_ip)
  dest_ip_list.append(dest_ip)

# Print the source and destination IPs in tabular format
print('Source IP\tDestination IP')
for i in range(len(src_ip_list)):
  print(src_ip_list[i], '\t', dest_ip_list[i])
"""
"""
# Define empty lists
src_ip_list = []
dest_ip_list = []

# Read the log file
with open('TE.log', 'r') as f:
  log_records = f.readlines()

# Extract the source and destination IPs
for log_record in log_records:
  # Split the log record into three parts
  timestamp, src_ip, dest_ip = log_record.split(';')
  src_ip_list.append(src_ip)
  dest_ip_list.append(dest_ip)

# Print the source and destination IPs in tabular format
print('Source IP\tDestination IP')
for i in range(len(src_ip_list)):
  print(src_ip_list[i], '\t', dest_ip_list[i])
  """
"""
# Define empty lists
src_ip_list = []
dest_ip_list = []

# Read the log file
with open('TE.log', 'r') as f:
  log_records = f.readlines()

# Extract the source and destination IPs
for log_record in log_records:
  # Split the log record into three parts
  timestamp, src_ip, dest_ip = log_record.split(';')
  src_ip_list.append(src_ip)
  dest_ip_list.append(dest_ip)

# Print the source and destination IPs in tabular format
print('Source IP\tDestination IP')
for i in range(len(src_ip_list)):
  print(src_ip_list[i], '\t', dest_ip_list[i])
"""

"""
srciplist = []
destiplist = []

#Read the log file

with open('TE.log', 'r') as f:
  logrecords = f.readlines()

#Extract the source and destination IPs

for logrecord in logrecords:
  # Split the log record into three parts
  timestamp, srcip, destip = logrecord.split(';')
  srciplist.append(srcip)
  destiplist.append(dest_ip)
#Print the source and destination IPs in tabular format
print('Source IP\tDestination IP')
for i in range(len(srciplist)):
  print(srciplist[i], '\t', destiplist[i])"""
"""
#Define empty lists

srciplist = [] 
destiplist = []

#Read the log file

with open('logfile.log', 'r') as f: 
  logrecords = f.readlines()

#Extract the source and destination IPs

for logrecord in logrecords: 
  # Split the log record into three parts
  timestamp, srcip, destip = logrecord.split(';')
  srciplist.append(srcip)
  destiplist.append(dest_ip)
#Print the source and destination IPs in tabular format

print('Source IP\tDestination IP')
for i in range(len(srciplist)):
  print(srciplist[i], '\t', destiplist[i])"""
"""
srciplist = []
destiplist = []
datetimelist = []


#Read the log file

with open('TE.log', 'r') as f:
  logrecords = f.readlines()


#Extract the source and destination IPs, as well as the date and time

for logrecord in logrecords:
  # Split the log record into parts
  time, id, rule, service, connection, iface, duration, bytes, packets = logrecord.split(' ')


# Extract the date and time
  datetime = time[1:-1]
  datetimelist.append(datetime)


# Extract the source and destination IPs
  srcip, destip = connection.split('->')[0].split(':')[0], connection.split('->')[1].split(':')[0]
  srciplist.append(srcip)
  destiplist.append(destip)


#Sort the lists

srciplist.sort()
destiplist.sort()
datetimelist.sort()


#Print the sorted lists

print('Source IP\tDestination IP\tDate Time')
for i in range(len(srciplist)):
  print(datetimelist[i], '\t',srciplist[i], '\t', destiplist[i] )"""
"""
srciplist = []
destiplist = []
datetimelist = []


#Read the log file

with open('TE.log', 'r') as f:
  logrecords = f.readlines()


#Extract the source and destination IPs, as well as the date and time

for logrecord in logrecords:
  # Split the log record into parts
  time, id, rule, service, connection, iface, duration, bytes, packets = logrecord.split(' ', 8)


# Extract the date and time
  datetime = time[1:-1]
  datetimelist.append(datetime)


# Extract the source and destination IPs
  srcip, destip = connection.split('->')[0].split(':')[0], connection.split('->')[1].split(':')[0]
  srciplist.append(srcip)
  destiplist.append(destip)

#Sort the lists

srciplist.sort()
destiplist.sort()
datetimelist.sort()

#Print the sorted lists

print('Source IP\tDestination IP\tDate Time')
for i in range(len(srciplist)):
  print(srciplist[i], '\t', destiplist[i], '\t', datetimelist[i])"""

"""
srciplist = []
destiplist = []
datetimelist = []


#Read the log file

with open('TE.log', 'r') as f:
  logrecords = f.readlines()


#Extract the source and destination IPs, as well as the date and time

for logrecord in logrecords:
  # Split the log record into parts
  time, id, rule, service, connection, iface, duration, bytes, packets = logrecord.split(' ', 8)


# Extract the date and time
  datetime = time[1:-1]
  datetimelist.append(datetime)


# Extract the source and destination IPs
  srcip, destip = connection.split('->')[0].split(':')[0], connection.split('->')[0].split(':')[0]
  srciplist.append(srcip)
  destiplist.append(destip)


#Sort the lists

srciplist.sort()
destiplist.sort()
datetimelist.sort()


#Get the length of the list

listlength = len(srciplist)


#Print the sorted lists

print('Source IP\tDestination IP\tDate Time')
for index in range(listlength):
  # Set the index if the length of the list is greater than the index
  if listlength > index:
    index = listlength - 1
  print(srciplist[index], '\t', destiplist[index], '\t', datetimelist[index])
"""
"""
srciplist = []
destiplist = []
datetimelist = []


#Read the log file

with open('TE.log', 'r') as f:
  logrecords = f.readlines()


#Extract the source and destination IPs, as well as the date and time

for logrecord in logrecords:
  # Split the log record into parts
  time, id, rule, service, connection, iface, duration, bytes, packets = logrecord.split(' ', 8)


# Extract the date and time
  datetime = time[1:-1]
  datetimelist.append(datetime)


# Extract the source and destination IPs
  srcip, destip = connection.split('->')[0].split(':')[0], connection.split('->')[1].split(':')[0]
  srciplist.append(srcip)
  destiplist.append(destip)


#Sort the lists

srciplist.sort()
destiplist.sort()
datetimelist.sort()


#Print the sorted lists

print('Source IP\tDestination IP\tDate Time')
for i in range(len(srciplist)):
  print(srciplist[i], '\t', destiplist[i], '\t', datetimelist[i])
  """
"""
srciplist = []
destiplist = []
datetimelist = []


#Read the log file

with open('TE.log', 'r') as f:
  logrecords = f.readlines()


#Extract the source and destination IPs, as well as the date and time

for logrecord in logrecords:
  # Split the log record into parts
  time, id, rule, service, connection, iface, duration, bytes, packets = logrecord.split(' ', 8)


# Extract the date and time
  datetime = time[1:-1]
  datetimelist.append(datetime)


# Extract the source and destination IPs
  srcip, destip = connection.split('->')[0].split(':')[0], connection.split('->')[1].split(':')[0]
  srciplist.append(srcip)
  destiplist.append(destip)


#Sort the lists

srciplist.sort()
destiplist.sort()
datetimelist.sort()


#Print the sorted lists

print('Source IP\tDestination IP\tDate Time')
for i in range(len(srciplist)):
  print(srciplist[i], '\t', destiplist[i], '\t', datetimelist[i])
"""
"""
srciplist = []
destiplist = []
datetimelist = []


#Read the log file

with open('TE.log', 'r') as f:
  logrecords = f.readlines()


#Extract the source and destination IPs, as well as the date and time

for logrecord in logrecords:
  # Split the log record into parts
  time, id, rule, service, connection, iface, duration, bytes, packets = logrecord.split(' ', 8)


# Extract the date and time
  datetime = time[1:-1]
  datetimelist.append(datetime)


# Extract the source and destination IPs
  connparts = connection.split('->')
  if len(connparts) == 2:
    srcip, destip = connection.split('->')[0].split(':')[0], connection.split('->')[1].split(':')[0]
    srciplist.append(srcip)
    destiplist.append(destip)


#Sort the lists

srciplist.sort()
destiplist.sort()
datetimelist.sort()


#Print the sorted lists

print('Source IP\tDestination IP\tDate Time')
for i in range(len(srciplist)):
  print(srciplist[i], '\t', destiplist[i], '\t', datetimelist[i])
  """
"""
srciplist = []
destiplist = []
datetimelist = []


#Read the log file

with open('TE.log', 'r') as f:
  logrecords = f.readlines()


#Extract the source and destination IPs, as well as the date and time

for logrecord in logrecords:
  # Split the log record into parts
  time, id, rule, service, connection, iface, duration, bytes, packets = logrecord.split(' ', 8)


# Extract the date and time
  datetime = time[1:-1]
  datetimelist.append(datetime)


# Extract the source and destination IPs
  connparts = connection.split('->')
  if len(connparts) == 2:
    srcip, destip = connection.split('->')[0].split(':')[0], connection.split('->')[1].split(':')[0]
    srciplist.append(srcip)
    destiplist.append(destip)


#Sort the lists

srciplist.sort()
destiplist.sort()
datetimelist.sort()


#Print the sorted lists

print('Source IP\tDestination IP\tDate Time')
for i in range(len(srciplist)):
  print(srciplist[i], '\t', destiplist[i], '\t', datetimelist[i])
  """


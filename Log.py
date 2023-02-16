import re
from datetime import datetime

logfile = open("connectio.log", "r")
pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))"
regex = r'\/.+?\sHTTP\/1\..\"\s.{3}\s(.+?)\s'

ip_addrs_lst = []
bytes = []
packages = []
for log in logfile:
    #print(log)
    ip_add = re.search(pattern, log)
    bytesCount = re.search(regex, log)[1]
    #print(ip_add)
    #print(ip_add.group())
    ip_addrs_lst.append(ip_add.group())

    lst = log.split(" ")
    #bytes = lst[-3]
    #packets = lst[-1]







print(ip_addrs_lst, bytesCount)
import re
import pandas as pd

logs = ["[25/Oct/2022 16:47:08] [ID] 1024673 [Rule] Internet access (NAT) [Service] HTTPS [Connection] TCP 192.16.47.26:39378 -> youtubei.googleapis.com (216.58.196.170):443 [Iface] NKN [Duration] 38 sec [Bytes] 1171/5990/7161 [Packets] 11/6/17",
        "[25/Oct/2022 16:47:08] [ID] 1024672 [Rule] Internet access (NAT) [Service] HTTPS [Connection] TCP 192.16.47.26:37988 -> i.ytimg.com (142.250.196.86):443 [Iface] NKN [Duration] 38 sec [Bytes] 1171/6023/7194 [Packets] 11/6/17"]

data = {'Date_Time': [], 'Source_IP': [], 'Destination_URL': [], 'Destination_IP': []}

for log in logs:
    match = re.search(r'\[(.*?)\] \[ID\] (.*?) \[Rule\] (.*?) \[Service\] (.*?) \[Connection\] (.*?) (.*?) -> (.*?) \((.*?)\):(.*?) \[Iface\] (.*?) \[Duration\] (.*?) sec \[Bytes\] (.*?)\/(.*?)\/(.*?) \[Packets\] (.*?)\/(.*?)\/(.*?)', log)
    date_time = match.group(1)
    source_ip = match.group(6)
    destination_url = match.group(7)
    destination_ip = match.group(8)
    data['Date_Time'].append(date_time)
    data['Source_IP'].append(source_ip)
    data['Destination_URL'].append(destination_url)
    data['Destination_IP'].append(destination_ip)

df = pd.DataFrame(data)

print(df)

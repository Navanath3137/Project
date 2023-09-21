import re
import csv

x = 1

with open("C:\\Users\\Navanath\\Desktop\\PROGRAM\\Project\\Samples\\SyslogCatchAll-2023-03-11.txt", 'r', encoding='Latin-1') as log_file:
    regex_str1 = ('\d{4}-\d{2}-\d{2}')
    regex_str2 = ('\d{2}:\d{2}:\d{2}')
    regex_str3 = ('(Local(\d+)\.(Info|Debug))')
    regex_str4 = ('(\d{3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
    regex_str5 = ('(\d{1,4})-(\d{1,2})-(\d{1,2})[T](\d{2}):(\d{2}):(\d{2})\+(\d{2}):(\d{2})')
    regex_str7 = ('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,4}:\d+) -> (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,4}:\d+)')
    regex_str8 = ('(ALLOW|Drop|DROP|DENY|DENY|Allow|Deny)')
    regex_str9 = ('packet dropped|"DNS Drop"|DNS')

    log_data = []

    file2 = open('a.txt', 'w')
    for line in log_file:
        generic_re = re.search(regex_str1, line)
        generic_re1 = re.search(regex_str2, line)
        generic_re2 = re.search(regex_str3, line)
        generic_re3 = re.search(regex_str4, line)
        generic_re4 = re.search(regex_str5, line)
        generic_re6 = re.search(regex_str7, line)
        generic_re7 = re.search(regex_str8, line)
        generic_re8 = re.search(regex_str9, line)

        if generic_re and generic_re1 and generic_re2 and generic_re3 and generic_re4 and generic_re6 and generic_re7 and generic_re8:
            date = generic_re.group(0)
            time = generic_re1.group(0)
            local = generic_re2.group(0)
            ip = generic_re3.group(0)
            gmt = generic_re4.group(0)
            source_ip = generic_re6.group(0)
            d_ip = generic_re6.group(2)
            rule = generic_re7.group(0)
            pd = generic_re8.group(0)

            log_data.append([date, time, local, ip, gmt, source_ip, d_ip, rule, pd])

with open('output3.csv', 'w', newline='', encoding='Latin-1') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['date', 'time', 'local', 'ip', 'gmt', 'source_ip', 'd_ip', 'rule', 'pd'])

                for row in log_data:
                    csv_writer.writerow(row)

print("complete")

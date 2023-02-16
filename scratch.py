'''First of all I have the log details, which I have Converted them in text file and I have keep the extension as
he .log and then I havewriten this Program This will make for only the log file that is in the static not the Dynamic'''


f = open("connectio.log","r")

for line in f:
    linestrip = line.strip().split(" ")
    #print(linestrip.split(" "))
    date = linestrip[0]
    time = linestrip[1]
   # id = linestrip[3]
   # connection = linestrip[11]
    ip = linestrip[12]
    url = linestrip[14]
   # bytes = linestrip[-3]
    #packets = linestrip[-1]


    print(date, time, ip, url,)

f.close()
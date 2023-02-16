
f = open("connectio.log",'r')
for log in f:
    newlist = line.split(" ")
    print(newlist[0] + " " + newlist[9])
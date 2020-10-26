import os
import socket
import subprocess
import json
from time import gmtime,strftime,sleep

def ping_add(address):

    ping = subprocess.Popen(["ping","-t","1", address], stdout=subprocess.PIPE)
    output = ping.communicate()
    
    output = str(output)
    output = output.split(",")
    row = output[0]
    row = row.split(" ")

    times = row[11].split("=")
    ms = times[1]

    date = strftime("%Y-%m-%d,%H:%M:%S".format(gmtime()))
    
    print(date)

    time = date.split(',')
    time = time[1]
    
    file = open("PINGINFO.txt", "a")
    file.write(str(time)+","+str(ms)+"\n")

        
while True:
    sleep(2)
    pinginfo = ping_add("google.com")


    

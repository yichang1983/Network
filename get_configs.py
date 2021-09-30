# Cisco switch python 3

import getpass
import sys
import telnetlib
import time
# Ask for username and password
user = input("Enter User name: ")
password = getpass.getpass()

# Open a file called my_switches
data = []       # create a list
with open('my_switches.txt', 'r') as f:
    for line in f:
        data.append(line.strip())       #line.strip() means get rid of spaces.

#Telnet to switches and get the running config
for line in data:
    print("Getting running config from Swich:" + line )
    Host = line
    tn = telnetlib.Telnet(Host)        #telnet to the switch
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")              #write the username to the switch

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")      #write the password to the switch

    #use tn.write(b "command"  \n") to do the configuration.
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    readoutput = tn.read_all().decode('ascii')      #read all config
    saveoutput = open("switch" + Host, "w")         #name the file which is going to be saved.
    saveoutput.write(readoutput)                    #save the file.
    saveoutput.close                                #close the file.

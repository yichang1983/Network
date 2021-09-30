# Cisco switch python 3

import getpass
import sys
import telnetlib
import time

Host="192.168.122.145"

user=input("Enter User name: ")
password=getpass.getpass()

tn = telnetlib.Telnet(Host)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

#use tn.write(b "command"  \n") to do the configuration.
tn.write(b"config t\n")

for n in range(2,11):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")             #tn.write(b"vlan " + str(n).encode('ascii') + b"\n") not working because "The (b"... means that you want to work with bytes. You need to convert the str(n) to bytes too. Try - tn.write(b"vlan " + str(n).encode('ascii') + b"\n") instead. That will convert each string into byte and then concat them. "
    tn.write(b"name Python_vlan " + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
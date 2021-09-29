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
tn.write(b"vlan 2\n")
tn.write(b"exit\n")
tn.write(b"vlan 3\n")
tn.write(b"exit\n")
tn.write(b"vlan 4\n")
tn.write(b"exit\n")
tn.write(b"vlan 5\n")
tn.write(b"exit\n")
tn.write(b"vlan 6\n")
tn.write(b"exit\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
# Cisco router python 3

import getpass
import sys
import telnetlib
import time

Host="192.168.122.146"

user=input("Enter User name: ")
password=getpass.getpass()

tn = telnetlib.Telnet(Host)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

#use tn.write(b "command"  \n") to do the configuration.
tn.write(b"enable\n")
tn.write(b"install\n")
tn.write(b"config t\n")
tn.write(b"int loop 1\n")
tn.write(b"ip address 1.1.1.1 255.255.255.0\n")
tn.write(b"int loop 2\n")
tn.write(b"ip address 2.2.2.2 255.255.255.0\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
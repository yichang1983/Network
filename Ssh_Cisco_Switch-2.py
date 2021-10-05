#!/usr/bin/env python

from netmiko import ConnectHandler

#setup multiple devices
iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'install',
    'password': 'install',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'install',
    'password': 'install',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.74',
    'username': 'install',
    'password': 'install',
}

#Open a file which has configuration(vlan 2, access and trunk ports etc)
with open('iosv_l2_config1') as f:
    lines = f.read().splitlines()
print(lines)

#Star configuring the s3 device followed by s2 then s1
all_devices = [iosv_l2_s3, iosv_l2_s2, iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
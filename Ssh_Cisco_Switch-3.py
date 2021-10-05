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

#Open a file which has configuration(vtp, snmp etc)
with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print(lines)

#implement the iosv_l2_cisco_design command file on the access switches
all_devices = [iosv_l2_s3, iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)

#Open a file which has configuration(vtp, snmp etc)
with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print(lines)

#Open a file which has configuration(default-gateway, dhcp etc)
all_devices = [iosv_l2_s1]

#implement the iosv_l2_cisco_design command file on the core switche
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
vlan 2
int range g2/0 - 3
switchport mode access
switchport access vlan 2
int range g0/0 - 3
switchport trunk encapsulation dot1q
switchport mode trunk
switchport nonegotiate
switchport trunk allowed vlan 1,2
int range g1/0 - 1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport nonegotiate
switchport trunk allowed vlan 1,2
#!/usr/bin/env python
from click._compat import raw_input
from netmiko import ConnectHandler
from getpass import getpass

ip_addr = raw_input("Enter IP Address: ")

device = {
    'device_type': 'cisco_ios',
    'ip': ip_addr,
    'username': 'admin',
    'password': getpass(),
    'port': 22,
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command_expect("show version")

print()
print('#' * 50)
print(output)
print('#' * 50)
print()
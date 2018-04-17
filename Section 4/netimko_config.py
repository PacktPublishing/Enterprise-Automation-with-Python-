#!/usr/bin/env python
from getpass import getpass
from tempfile import NamedTemporaryFile

from click._compat import raw_input
from netmiko import ConnectHandler

ip_addr = raw_input("Enter IP Address: ")

device_data = {
    'device_type': 'cisco_ios',
    'ip': ip_addr,
    'username': "admin",
    'password': getpass(),
}

f = NamedTemporaryFile(delete=False)
print('Stored temporary config at {}'.format(f.name))
f.write(b'some specific config')
f.flush()

net_connect = ConnectHandler(**device_data)
output = net_connect.send_config_from_file(f.name)
print(output)
print('Config uploaded!')

f.close()

print('Done.')

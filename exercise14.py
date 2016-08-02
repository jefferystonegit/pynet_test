#!/usr/bin/env python
import os

#net_devices = {}
#net_devices['vendor'] = 'arista'
#net_devices['model'] = 'fattwin'
#net_devices['password'] = 'my_password'
#net_devices['username'] = 'me'

net_devices = {
    'ip_addr': '192.168.5.1',
    'username': 'my_username',
    'password': 'my_password',
    'vendor': 'arista',
    'model': 'fattwin',
}

print "*" * 50
print "{:12} -> {:12}".format("KEY","VALUE")
for k, v in net_devices.items():
   print "{:12} -> {:12}".format(k,v)
print "*" * 50
print

net_devices['password'] = 'my_new_password'
net_devices['secret'] = 'my_secret'

get_device_type = net_devices.get('device_type','cisco_ios')
print "Response when device_type not set: {}".format(get_device_type)

print
print "*" * 50
print "{:12} -> {:12}".format("KEY","VALUE")
for k, v in net_devices.items():
   print "{:12} -> {:12}".format(k,v)
print "*" * 50

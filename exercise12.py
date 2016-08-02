#!/usr/bin/env python
import os

network = raw_input("Please enter a Class C (/24) network: ")
octets = network.split(".")

for last_octet in range (1,11):
    octets[-1] = str(last_octet)
    ping_ip = ".".join(octets)
    #print ping_ip
    ping_cmd = "ping -c 1 -W 1 {} > /dev/null".format(ping_ip)
    #print ping_cmd
    status = os.system(ping_cmd)
    print status
    if status == 0:
        print "Ping of {} successful.".format(ping_ip)


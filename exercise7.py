#!/usr/bin/env python

ip_address = raw_input("Please enter an IPv4 IP Address: ")
octets = [ip_address.split(".")]
octets[-1] = 0

#ip_binary = []
#ip_binary.append(bin(int(octets[0])))
#ip_binary.append(bin(int(octets[1])))
#ip_binary.append(bin(int(octets[2])))
#ip_binary.append(bin(int(octets[3])))

ip_binary = []
ip_binary.append(bin(int(octets[0])))
ip_binary.append(bin(int(octets[1])))
ip_binary.append(bin(int(octets[2])))
ip_binary.append(bin(int(octets[3])))

print "#" * 50
print "{:12} {:12} {:12} {:12}".format('Octet1','Octet2','Octet3','Octet4')
print "{:<12} {:<12} {:<12} {:<12}".format(*octets)
print "{:<12} {:<12} {:<12} {:<12}".format(*ip_binary)

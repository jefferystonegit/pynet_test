#!/usr/bin/env python

ip_address = raw_input("Please enter an IPv4 IP Address: ")

octets = ip_address.split(".")

print "#" * 50
print "printing using the individual octets from a split"
print "{:12} {:12} {:12} {:12}".format(octets[0], octets[1], octets[2], octets[3])

print "\n"
print "#" * 50
print "Printing by wildcard expansion of the list"
print "{:12} {:12} {:12} {:12}".format(*octets)

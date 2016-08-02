#!/usr/bin/env python
import os

input_file = raw_input("Please enter the router output file location: ")

with open(input_file) as f:
    show_ver = f.read().splitlines()

for line in show_ver:
    if 'Processor board ID' in line:
        #_, serial_number = line.split("Processor board ID")
        serial_number = line.split()[3]

print "The serial number is: {}".format(serial_number)

#!/usr/bin/env python

input_file = raw_input("Please enter the router output file location (show_version): ")

with open(input_file) as f:
    show_ver = f.read().splitlines()


def return_version(show_ver):
    for line in show_ver:
        if 'Processor board ID' in line:
            serial_number = line.split()[3]
            print "*" * 100
            print "The serial number is: {}".format(serial_number)
            print "*" * 100
            print

def return_file(show_ver):
   for line in show_ver:
       print line

print_version = return_version(show_ver)
print_file = return_file(show_ver)     

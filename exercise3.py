#!/usr/bin/env python

first_name = "Matsumi"
second_name = "Hanako"
third_name = "Jeffery"

print "The three names are:"
print "{:>30} {:>30} {:>30}".format(first_name, second_name, third_name)

print "#" * 50
fourth_name = raw_input("Please enter a fourth name: ")
print "#" * 50
print "The entered fourth name is {}".format(fourth_name)

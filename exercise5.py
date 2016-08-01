#!/usr/bin/env python

#### READ ####
f = open("exercise5_input")
for line in f:
    print line.strip()

### WRITE TO NEW FILE ###
f = open("exercise5_output", "w")
f.write("This is my first line of output\n")
f.close()

### APPEND TO A FILE ###
f = open("exercise5_output", "a")
f.write("This is my appended line of output\n")
f.close()


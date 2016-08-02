#!/usr/bin/env python

def sum_func(x, y, z=20):
    sum = x + y + z
    return sum

sum_pos = sum_func(5, 10, 80)
sum_named = sum_func(x=10, y=20, z=30)
sum_combo = sum_func(33, y=25, z=50)
sum_string = sum_func("Hello", " There", " Y'all")

my_list = [1, 3, 11]
sum_lists = sum_func(*my_list)

print "POSITIONAL: {}".format(sum_pos)
print "NAMED: {}".format(sum_named)
print "COMBO: {}".format(sum_combo)
print "STRING: {}".format(sum_string)
print "LIST: {}".format(sum_lists)


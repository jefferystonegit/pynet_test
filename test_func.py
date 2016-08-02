#!/usr/bin/env python

def my_func():
   print "Hello world"
   return 0

ret_val = my_func()
print ret_val


def my_func2(x,y):
   print x + y

ret_val2 = my_func2(7, 12)

## Example passing in defined values
def my_func3(x,y):
   print x + y

ret_val3 = my_func3(y=13, x=11)



def my_func4(x,y, z=19):
   print x + y + z

ret_val4 = my_func4(y=13, x=11)




def my_func4(x,y, z=19):
   print x + y + z

ret_val4 = my_func4(13, z=11, y=12)





# To pass a list into 1 variable (x)
#def my_func5(x,y, z=19):
#   print x + y + z

#my_list = [1, 3, 11]
#ret_val5 = my_func5(my_list)





# To expand a list and pass each value into multiple variables 
def my_func5(x, y, z=19):
   print x + y + z

my_list = [1, 3, 11]
ret_val5 = my_func5(*my_list)





# To expand a list and pass each value into multiple variables 
def my_func6(x,y, z=19):
   print x + y + z

my_list = [1, 3, 11]

my_dict = {
    'x': 22,
    'y': 7,
    'z': 12
}

ret_val6 = my_func6(*my_list)




# To expand a list and pass each value into multiple variables 
def my_func7(x,y,*args, ):
   print x + y + z

my_list = [1, 3, 11]

my_dict = {
    'x': 22,
    'y': 7,
    'z': 12
}

ret_val7 = my_func7(*my_list)

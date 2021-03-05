# modules
# a module is like a code library
# a file containing a set of functions to include
import mymodule as mx
mx.greeting("Jonathan")

a = mx.person1["age"]
print(a)

b = mx.person1["name"]
print(b)


# built in modules
import platform
x = platform.system()
print(x)


# dir() function
# built-in function to list all function names in a module
x = dir(platform)
print(x)


# from keyword - import only some parts of a module
from mymodule import person1
print(person1["age"])
# do not use module name in this case
# i.e. not mymodule.person1["age"]


# dates
# date is not a data type in python
# instead you can import the module datetime to work with date objects
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))


# create a datetime object
# use the datetime() class constructor
# it requires 3 parameters:year, month, day
# can also take parameters for time (default value 0) and timezone (default value None)
x = datetime.datetime(2020, 5, 17)
print(x)


# strftime() method - for formatting date objects into readable strings.

print(x.strftime("%B"))
# strftime.net is a good resource for format codes.


# Python Math
# Python has built in math functions and a math module
# built in math functions
x = min(5, 10, 25)
y = max(5, 10, 25)
z = abs(-15)
a = pow(4, 3)

print(x, y, z, a)

# math module
import math
    x = math.sqrt(64)
print(x)
print(math.ceil(5.5))
print(math.floor(5.5))
print(math.pi)



























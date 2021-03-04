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



















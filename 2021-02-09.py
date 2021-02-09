# casting to specify the data type
x = str(3)
y = int(3)
z = float(3)


# use type() to get the data type of a variable
print(x)
print(type(x))

print(y)
print(type(y))

print(z)
print(type(z))

# you can use single or double quotes

# variables
# variable names are case-sensitive.
# must start with a letter or the underscore character
# cannot start with a number
# can containe alpha-numeric characters and underscores

# camel case
myVariableName = "camel case"

# Pascal Case
MyVariableName = "Pascal case"

# snake case
my_variable_name = "snake case"

# assigning multiple variables in a line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# assigning the same value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# output variables with print: variable plus text
x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)

# for numbers, + inside print works as addition
x = 5
y = 10
print(x + y)


# variable with global scope
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()


# variable with local scope
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)


# global keyword
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)


# data types
# assignment of a value, constructor function

# text
str
x = str("Hello World")
x = "Hello World"


# numeric
int
x = int(20)
x = 20

float
x = float(20.5)
x = 20.5

complex
x = complex(1j)
x = 1j


# sequence
list
x = list(("apple", "banana", "cherry"))
x = ["apple", "banana", "cherry"]

tuple
x = tuple(("apple", "banana", "cherry"))
x = ("apple", "banana", "cherry")

range
x = range(6)
x = range(6)


# mapping
dict
x = dict(name="John", age=36)
x = {"name": "John", "age": 36}


# set
set
x = set(("apple", "banana", "cherry"))
x = {"apple", "banana", "cherry"}

frozenset
x = frozenset(("apple", "banana", "cherry"))
x = frozenset({"apple", "banana", "cherry"})


# boolean
bool
x = bool(5)
x = True


# binary
bytes
x = bytes(5)
x = b"Hello"


bytearray
x = bytearray(5)
x = bytearray(5)

memoryview
x = memoryview(bytes(5))
x = memoryview(bytes(5))





























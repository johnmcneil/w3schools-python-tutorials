# functions
# in python, using the def keyword
def my_function():
    print("Hello from a function")


my_function()


# function with an argument
def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")

# arguments often shortened to args in python documentation
# a parameter is the variable listed inside the parentheses
# in the function definition
# an arguemnt is the value that is sent to the function when called.


# functions must be called with the correct number of arguments
# otherwise you get an error
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


# arbitrary arguments
# add a * before the parameter name if you don't know how many arguments
# this way the function will receive a tuple of arguments
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")
# arbitrary arguments often shortened to *args in python docs


# keyword arguments
# you can send arguments with the key = value syntax
# then the order of the arguments doesn't matter
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# keyword arguments is often shortened as kwargs in python documentation


# arbitrary keyword arguments
# **kwargs in python docs
# use ** before the parameter if you don't know how many keyword args
# the function recieves a dictionary of arguments
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# default parameter value
# if you call a function without an argument, it uses the default value
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# passing a list as an argument
# you can pass any data type to a function, e.g. a list
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# to let a function return a value, use the return statement
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))


# pass statement
# functions can't be empty. if you have a function with no content,
# use pass statement to avoid an error.
def my_function():
    pass


# recursion
# python accepts function recursion
# meaning a defined function can call itself
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\nRecursion Example Results")
tri_recursion(6)









































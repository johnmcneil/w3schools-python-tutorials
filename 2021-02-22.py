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














































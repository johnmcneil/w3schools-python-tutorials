# lambda
# a lambda function is a small anonymous function
# can take any number of arguments
# but has only one expression
x = lambda a: a + 10
print(x(5))


x = lambda a, b: a * b
print(x(5, 6))


# use as anonymous functions inside functions
def myfunc(n):
    return lambda a: a * n


# use the function definition to make a function
# that doubles whatever number goes in.
mydoubler = myfunc(2)
print(mydoubler(11))


mytripler = myfunc(3)
print(mytripler(8))


# use lambda functions when an anonymous function
# is required for a short period of time.





























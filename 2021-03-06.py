# try... except
# try block lets you test code
# except block lets you handle the error
# finally block executes code regardless of the result of the other two

# when an error/exception occurs python stops and generates an error message
# this is handled using a try statement
try:
    print(x)
except:
    print("An exception occurred")


try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong.")


# you can use else to say what to do if no errors were raised
try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")


# finally block is executed regardless of whether the try block raised an error
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished")

# useful when closing objects
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("something went wrong when writing to the file")
# finally:
#     f.close()

# raise keyword - used to raise an error
# x = -1
# if x < 0:
#    raise Exception("Sorry, no numbers below zero")


# you can define what kind of error to raise
x = "hello"
if not type(x) is int:
    raise TypeError("only integers allowed")























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
# x = "hello"
# if not type(x) is int:
#    raise TypeError("only integers allowed")


# user input
# username = input("Enter username:")
# print("Username is: " + username)
# python stops executing when it comes to input() function, continues when the user has given some input


# format() method - allows you to format selected parts of a string
# using placeholders  {} in the text
price = 49
txt = "The price is {} dollars"
print(txt.format(price))


# format price to be displayed as a number with two decimals
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# string format reference
# https://www.w3schools.com/python/ref_string_format.asp

# multiple placeholder values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


# you can use index numbers to make sure values are in correct order
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# index number allows you to use the same value more than once
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(name, age))


# you can name indexes in the {} and use them within the format method
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))







































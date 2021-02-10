# Strings
# Assign a multiline string by using three quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.\n\n"""
print(a)


# or three single quotes
b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.\n\n'''
print(b)


# line breaks in the result are in the same position as in the code.
stringsAreBytes = """strings in Python are arrays of bytes representing
unicode characters. However, Python does not have a character data type,
a single character is simply a string wtih length of 1.\n\n"""
print(stringsAreBytes)

stringsAreArrays = '''In Python, strings are arrays.
Square brackets can be used to access elements of the string.\n\n'''
print(stringsAreArrays)


# looping through a string
for x in "banana":
    print(x)


# len()
# to get the length of a string, use the len() function
a = "Hello, World!"
print(len(a))


# keyword in
# check if a certain phrase or character is present in a string
txt = "The best things in life are free!"
print("free" in txt)
print("zzzz" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")
if "zzzz" in txt:
    print("Yes, 'zzzz' is present.")


# keyword not in
# check is a certain phrase or character is NOT present in a string
print("expensive" not in txt)

if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")


# slicing
print(a[2:5])

# slice from the start by leaving out first index
print(a[:5])

# slice to the end by leaving out second index
print(a[2:])

# use negative indexes to start the slice from the end of the string
print(a[-5:-2])


# modify strings
# all characters to upper or lower case
print(a.upper())
print(a.lower())

# remove whitespace
c = " Hello, World! "
print(c.strip())

# replace a string with another string
print(a.replace("H", "J"))

# split
# creates a list out of a string, spliting by a separator
print(a.split(","))


# concatenate
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# concatenating a string with a number
# you can't do this in  python (but I believe you can in JavaScript):
age = 36
# txt = "My name is John, I am " + age

# use the format method instead
txt = "My name is John, I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# index numbers make sure the arguments are placed in the correct placeholders
myorder = "I want to pay {2} dolars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# escape character
# is a backslash \ followed by the character you want to insert
# e.g. double quotes inside a string that is surrounded by double quotes
txt = "We are the so-called \"Vikings\" from the north."

# other escape characters
# \"
# \' single quote
# \\ backslash
# \n new line
# \r carriage return
# \t tab
# \b backspace
# \f form feed
# \ooo octal value
# \xhh hex value


# string methods
# all string methods return new values.
# they don't change the original string.
a = "hello, world!"
print(a.capitalize())   # converts the first character to upper case
print(a.casefold())     # converts the whole string to lower case
print(a.center(50))     # center align the string using a fill character
print(a.count("h"))     # return number of time a value occurs in the string
print(a.encode())       # the encoded version of the string
print(a.endswith("!"))  # true if the string ends with the specified value
print(a.find(" "))      # searches for a value, returns its position
print(a.format())       # formats specified values in a string.


print(a.index("o"))     # searches for a value, returns its position
print(a.isalnum())      # true if all characters in string are alphanumeric
print(a.isalpha())      # true if all characters in the string are letters
print(a.isdecimal())    # true if all characters in the string are digits
print(a.isnumeric())    # true if all characters in string are numeric
print(a.isprintable())  # true if all characters in string are printable
print(a.isspace())      # true if all characters in string are whitespaces
print(a.istitle())      # true if string follows the rules of a title
print(a.isupper())      # true if all characters are upper case


myTuple = ("John", "Peter", "Vicky")
print("#".join(myTuple))        # join elements of an iterable to end of string

print(a.ljust(50))              # return left justified version of the string
print(a.lower())                # converts string to lower case
print(a.lstrip())               # return left trim version of string

print(a.partition("w"))         # return tuple where string is parted in 3
print(a.replace("h", "i"))      # replace a specified value with another value
print(a.rfind("o"))             # return last position of specified value
print(a.rjust(50))              # return right justified version of the string


print(a.rpartition("w"))        # return a tuple where string is parted in 3
# how is this different from partition()?

print(a.rsplit("w"))            # split string at separator. return list.
# how is this different from split()?

txt2 = "Hello World!     "
print(txt2.rstrip())               # return a right trim version of the string

print(a.split("w"))             # split string at the separator, return a list.

# splitlines()                  split the string at line breaks
print(a.startswith("h"))        # true if string starts with specified value

txt3 = "      Hello World!    "
print(a.strip())                # returns a trimmed version of string

print(a.swapcase())             # swaps case, lower becomes upper, upper lower

print(a.title())                # first character of each word to upper case

print(a.zfill(25))              # adds specified number of 0s at beggining

mytable = a.maketrans("h", "j")
print(a.translate(mytable))







































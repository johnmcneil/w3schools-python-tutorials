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
























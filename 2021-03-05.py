# regexp
# for regular expressions, python has the built-in package re
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# regex functions
# findall() - returns a list of all matches
x = re.findall("ai", txt)
print(x)

x = re.findall("sdkj", txt)
print(x)

# search() - returns a match object if there is a match anywhere in the string
x = re.search("ai", txt)
print(x)

x = re.search("Portugal", txt)
print(x)


# split() - returns a list where the string has been split at each match
x = re.split("i", txt)
print(x)
x = re.split("\s", txt)
print(x)
x = re.split("q", txt)
print(x)

# maxsplit parameter
# e.g. split string only at first occurence
x = re.split("\s", txt, 1)
print(x)

# sub() - replaces one or many matches with a string
x = re.sub("\s", "9", txt)
print(x)

# count parameter controls the number of replacements
x = re.sub("\s", "9", txt, 2)
print(x)


# Match Object
# contains information about the search and its result
# if there is no match, None will be returned
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

# Match object properties and methods
# span() - returns a tuple containing the start and end positions of the match
print(x.span())


# string - print the string passed into the function
print(x.string)


# print the part of the string where there was a match
print(x.group())


# pip
import camelcase
c = camelcase.CamelCase()
txt = "hello world!"

print(c.hump(txt))

















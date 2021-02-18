# dictionaries
# store data in key: value pairs
# ordered, changeable, does not allow duplicates
# duplicate values overwrite existing ones
# ordered as of Python 3.7. Unordered in Python 3.6 and earlier.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))


# values can be any data type
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))


# accessing - brackets
x = thisdict["brand"]
print(x)


# get() method
y = thisdict.get("brand")
print(y)


# keys() method - returns a list of all keys in the dictionary
z = thisdict.keys()
print(z)
# the keys list is a view of the dictionary.
# changes to the dictionary will be reflected in the keys list.

thisdict["model"] = "Mustang"

print(z)


# values() method - returns a list of all values in the dictionary.
a = thisdict.values()
print(a)
# the values list is a view of the dictionary.
# changes to the dictionary will be reflected in the values list


# items() method - return each item in a dictionary as tuples in a list
b = thisdict.items()
print(b)
# the items list is a view of the items in the dictionary
# changes done to the dictionary will be reflected in the items list


# in keyword - check if a specified key is present
if "model" in thisdict:
    print("Yes, 'model' is one of the keys.")


# update() method - argument must have key:value pairs.
thisdict.update({"year": 2020})
print(thisdict)


# add items
# use a new index key and assign a value to it
# or use update()


# remove items
# pop() method - remove item with specified key name
thisdict.pop("model")
print(thisdict)


# popitem() method - remove last inserted item
# in versions before 3.7, remove a random item
print(thisdict)
thisdict.popitem()
print(thisdict)


# del keyword
# remove item with specified key name
del thisdict["electric"]
print(thisdict)


# clear() method - empties the dictionary
thisdict.clear()
print(thisdict)

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "color": "white"
}

# loop dictionaries
# for loop - return values are keys
for x in thisdict:
    print(x)

# for loop - returns values one by one
for x in thisdict:
    print(thisdict[x])


# for loop - return keys with the keys() method
for x in thisdict.keys():
    print(x)


# for loop - return values with the values() method
for x in thisdict.values():
    print(x)


# for loop with items() method - both keys and values
for x, y in thisdict.items():
    print(x, y)


# copy a dictionary

# wrong way: dict2 = dict1
# dict2 is only a reference to dict1.
# changes to dict1 will automatically also be made in dict2


# copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# built-in function dict()
newdict = dict(thisdict)
print(newdict)


# nested dictionaries
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
print(myfamily)
myfamily.clear()


# create three dictionaries, then another to contain them.
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
print(myfamily)


# dictionary methods

# clear()

# copy()

# fromkeys() # returns a dictionary with specified keys and value
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

# get  # returns value of specified key
print(thisdict.get("key1"))

# items()

# keys()

# pop()

# popitem()

# setdefault() returns value of specified key.
# If the key does not exist, insert the key with the specified value.

# update()

# values()











































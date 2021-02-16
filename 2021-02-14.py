# Lists
# are store multiple items in a single variable
# are one of four built-in data types in Python used to store collections
# of information.


# list: ordered, changeable, duplicates allowed
# tuple: ordered, unchangeable, duplicates allowed
# set: unordered, unindexed, no duplicates.
# dictionary: unordered, changeable, no duplicates.


# are created using square brackets
thisList = ["apple", "banana", "cherry"]
print(thisList)


# list items are ordered, changeable, and allow duplicate values.
# firt item has index [0], second has index [1], etc.
# if you add new items they will be placed at the end of the list.


# changeable means we can change, add, remove items
# after the list has been created.


# since lists are indexed, they can have duplicates.
thisList = ["apple", "banana", "cherry", "apple", "cherry"]
print(thisList)


# len()
# determines length of list
print(len(thisList))


# list items can be of any data type.
# a list can contain different data types
list1 = ["abc", 34, True, 40.5, "male"]
print(list1)
print(type(list1))


# list() - the list constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)


# access list items
print(thislist[1])
# -1 is last item, -2 is second to last, etc.
print(thislist[-1])

# range
# second cut-off value not included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

# check if an item exists
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


# change list items using ranges
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# replace a value with two values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrent", "watermelon"]
print(thislist)


# replace with fewer values
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# append() - add items to end of list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# extend() - append elements from another list to end of current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# extend() can also append tuples, sets, dictoinaries, etc.


# remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# pop() - remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# pop() removes last item if no index is specified.


# del keyword removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# del can delete the list entirely
thislist = ["apple", "banana", "cherry"]
del thislist


# clear() - empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


# loop by index number
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])


# while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


# list comprehension - shortest syntex for looping through lists
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# create a new list with items containing letter a
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


# list comprehension can do this in one line of code
newlist = []
newlist = [x for x in fruits if "a" in x]
print(newlist)


# syntax for list comprehension
# newlist = [expression for item in iterable if condition == True]


# the condition is a filter tha t only accepts items that valuate True
# the conditional can be omitted
newlist = []
newlist = [x for x in fruits]
print(newlist)


# the iterable can be any iterable object, e.g. list, tuple, set, etc.
newlist = []
newlist = [x for x in range(10)]
print(newlist)


newlist = []
newlist = [x for x in range(10) if x > 5]
print(newlist)


# the expression is the current item in the iteration, but also the
# "outcome" (?) which you can maniuplate before it becomes an item in the
# new list
newlist = []
newlist = [x.upper() for x in fruits]
print(newlist)


newlist = []
newlist = ['hello' for x in fruits]
print(newlist)


# the expression can also contain conditionals
newlist = []
newlist = [x if x != "banana" else "orange" for x in fruits]
print(fruits)
print(newlist)


















































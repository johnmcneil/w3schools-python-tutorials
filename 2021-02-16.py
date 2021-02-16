# tuples
# tuples store multiple items in a singe variable.
# tuples are ordered and unchangeable
# tuples are written with round brackets
thistuple = ("apple", "banana", "cherry")
print(thistuple)


# ordered: items have a defined order, which will not change.
# unchangeable: cannot change, add or remove items after created.
# can have duplicated, because indexed.


# tuple length
print(len(thistuple))


# tuple with one item
# comma after the item so python knows it's a tuple.
thistuple = ("apple",)
print(type(thistuple))


# tuples can be any data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


# tuples can have items of different data types
tuple4 = ("abc", 34, True, 40, "male")


# tuples are defined as objects with the data type tuple
print(type(tuple4))


# tuple() - the tuple constructor  can be used to make a tuple
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


# accessing - same as for lists. indexes, etc.


# updating tuples
# you can convert to a list, change, then convert back to tuple
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# similar for adding, removing items.


# del keyword
del thistuple


# unpack a tuple
# assigning values to a tuple is "packing"
# in python you can extract the values back into variables. unpacking.
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green, yellow, red)
# number of varibales must match number of values in tuple
# or use * to collect remaining values as a list.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, tropic, *red) = fruits
print(green)
print(tropic)
print(red)


# if * added to another varibale name than last, python assigns values
# to the variable until the number of values left matches the number
# of varibables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


# loops - similar to lists


# join
# +
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# *
mytuple = fruits * 2
print(mytuple)


# two built-in methods for tuples
count()  # returns number of times a specified value occurs in a tuple
index()  # searches tuple for a specified value, returns its position.






































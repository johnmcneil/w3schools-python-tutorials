# sets
# unordered, unindexed
myset = {"apple", "banana", "cherry"}
print(myset)
# can't be sure in what order they will apppear
# cannot be refered to by index or key
# once a set is created, you can add new items but can't change its items
# cannot have duplicate values. they'll be ignored.


# get length of set
print(len(myset))


# sets can be of any data type, can have multiple data types


# type()
print(type(myset))


# set constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)


# access items using a loop
for x in thisset:
    print(x)


# ask if a certain item is present in the set
print("banana" in thisset)


# add new items
thisset.add("orange")
print(thisset)


# add sets - use update() method
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)


# the object in update() can be any iterable
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)


# remove() method
print(myset)
myset.remove("banana")
print(myset)
# if item does not exist, raises an error


# discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# if item does not exist, does NOT raise an error


# pop() removes last item
# you won't know which one that will be, because sets are unordered
# returns the removed item
thisset = {"apple", "banana", "cherry"}
print(thisset)
x = thisset.pop()
print(x)
print(thisset)


# clear() empties the set
thisset.clear()
print(thisset)


# del keyword deletes the set completely
thisset = {"apple", "banana", "cherry"}
del thisset


# loops
# for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)


# join sets
# union() method - returns a new set containing all items from both
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


# update() method - inserts all items from one set into another
set1.update(set2)
print(set1)


# both union() and update() exclude duplicate items.


# intersection_update() - keep only items present in both
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


# intersection() - return a new set that only contains items present in both
z = x.intersection(y)
print(z)


# symmetric_difference_update() - keep all except duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)


# set methods
add()           # adds an element to the set
clear()         # remove all elements from set
copy()          # returns a copy of the set
difference()    # returns set containing difference between two or more sets
difference_update()  # removes items also included in another specified set
discard()       # remove specified item
intersection()  # returns a set that is the intersection of two other sets
isdisjoint()    # returns whether two sets have an intersection or not
issubset()      # returns whether another set contains this set or not
issuperset()    # returns whether this set contains another set or not
pop()           # removes an element from the set
remove()        # removes the specified element
symmetric_difference()          # above
symmetric_difference_update()   # above
union()         # return a set containing the union of sets
update()        # update the set with the union of this set and others.



































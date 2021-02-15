# lists continued.
# sort()  - sort lists alphanumerically, ascending by default
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# customize sort function using key = function
def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)


# case insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist.sort(key=str.lower)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# copy lists
# in list2 = list1, list2 is only a reference to list1
# changes made to list1 will automatically be made to list2
# instead use list.copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# or ths built in method list()
mylist = list(thislist)
print(mylist)


# join, i.e. concatenate, lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


# or append items one by one
list4 = ["a", "b", "c"]
list5 = [1, 2, 3]
for x in list5:
    list4.append(x)
print(list5, list4)


# extend()
list6 = ["a", "b", "c"]
list7 = [1, 2, 3]
list6.extend(list7)
print(list6)


# list methods
append()   # adds an element at the end of the list
clear()    # removes all elements from the list
copy()     # returns a copy of the list
count()    # returns the number of elements with specified value
extend()   # add elements of an iterable to end of current list
index()    # returns index of first element with specified value
insert()   # adds an element at specified position
pop()      # removes element at the specified position
remove()   # removes item with specified value
reverse()  # reverses the order of the list
sort()     # sort the list





























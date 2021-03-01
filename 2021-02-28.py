# python iterators
# an iterator is ano object that contains a countable number of values
# i.e. can be iterated upon, i.e. you can traverse through all values.
# it implements the iterator protocol: methods __iter__() and __next__()


# iterator verus iterable.
# lists, tuples, dictionaries and sets are iterable objects
# they are containers you can get an iterator from.
# return an iterator from a tuple, print each value
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# strings are iterable objects too.
mystr = "banana"
myit = iter(mystr)


print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# for loop to iterate through an iterable object
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)


# iterate the characters of string
mystr = "banana"

for x in mystr:
    print(x)
# the for loop creates an iterator object and executes next()
# for each loop


# create an object/class as an iterator
# you have to implement the methods __iter__() and __next__()


# create an iterator that returns numbers
# starting with 1, and each sequence will increase by one.
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# StopIteration statement
# prevent iteration from going on forever
# use a terminating condition in the __next()__ method
# e.g. stop after 20 iterations
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


























































# Booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)


# conditional
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# bool() function
print(bool("Hello"))
print(bool(15))

# "Almost any value is evaluated as True if it has some sort of content."
# "Any string is True, except empty strings."
# "Any number is True, except 0."
# "Any list, tuple, set, and dictionary are True, except empty ones."

empty = ""
print(bool(empty))

print("\nbool(abc)")
print(bool("abc"))


# values that are false
#
print("\n\nSome values are false.")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# another thing that evaluates false
class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


# functions can return Boolean values
def myFunction():
    return True


print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")

# isinstance() function
# check if an object is of a certain data type

# check whether an object is an instance
x = 200
print(isinstance(x, int))












































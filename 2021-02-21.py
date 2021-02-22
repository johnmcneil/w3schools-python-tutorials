# while loops

# python has two primative loop commands: while and for

# while executes a set of statements as long as
# a condition holds true.


# print i as long as i is less than six
i = 1
while i < 6:
    print(i)
    i += 1
# if you don't incremen i, it will loop forever.


# break statement - can stop the loop even while the condition is true.
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


# continue statement - stop the current iteration, continue with the next.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# else statement - run a block of code when the condition is no longer true.
print("\n")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


# for loops
# used for iterating over a sequence
# works like an iterator method
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# does not require an indexing variable


for x in "banana":
    print(x)


# continue and break work the same as in while loops


# range() function - loop through a specific number of times.
# starts at zero by default
for x in range(6):
    print(x)

# specify values for the range
for x in range(2, 6):
    print(x)

# third parameter specifies the increment value. default is 1.
for x in range(2, 30, 3):
    print(x)

# else works the same as in while loops
# if there's a break, else will not be executed.


# nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

print("\n")
for x in adj:
    for y in fruits:
        print(x, y)


# pass statement
# for loops can't be empty, use pass instead
for x in [0, 1, 2]:
    pass




















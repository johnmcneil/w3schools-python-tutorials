# operators

# arithmetic operators
x = 5
y = 3

print(x + y)    # addition
print(x - y)    # subtraction
print(x * y)    # multiplication
print(x / y)    # division
print(x % y)    # modulus
print(x ** y)   # exponentiation
print(x // y)   # floor division


# assignment operators
x = 5       #
x += 3      # x = x + 3
print(x)

x -= 3      # x = x - 3
print(x)

# *=, /=, %=, //=, **=,

# &=, |=, ^=, >>=, <<=


# comparison operators
print(x == y)     # equal
print(x != y)     # not equal
print(x > y)      # greater than
print(x < y)      # less than
print(x >= y)     # greater than or equal to
print(x <= y)     # less than or equal to


# logical operators
print(x)
print(x < 5 and x < 10)         # returns true if both true
print(x > 5 or x > 4)           # returns true if at least one is true
print(not(x < 5 and x < 10))    # reverse the result


# identity operators
# compare objects: "not if they are equal, but if they are
# actually the same object, with the same memory location."
print("\n")
print(x is y)
print(x is x)

print("\n")
print(x is not y)
print(x is not x)


# membership operators
# test if a sequence is presented in an object
print("\n")
txt1 = "Hello"
txt2 = "Hello, World"
print(txt1 in txt2)
# true if a  sequence within the specified value is present in the object.

print(txt1 not in txt2)


# bitwise operators
print("\n")
# used to compare binary numbers

# &     AND     Set each bit to 1 if both bits are 1
w = 0
x = 1
y = 1
z = 0
print(x & y)
print(x & z)

# |     OR      Set each bit to 1 if one of two is 1
print("\n")
print(x | z)
print(w | z)

# ^     XOR     Set each bit to 1 if only one of two is 1
print("\n")
print(x ^ z)


# ~     NOT     Invert all the bits


# <<    Zero fill left shift
# Shift left by pushing zeros in from the right
# and let the leftmost bits fall off
# >>    Signed right shift
# Shift right by pushing copies of the leftmost bit in from the left,
# and let the rightmost bits fall off



























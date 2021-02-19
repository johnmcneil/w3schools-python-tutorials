# if... else


# conditionals - most commonly used in if statements
# equals: a == b
# not equals: a != b
# less than: a < b
# less than or equal to : a <= b
# greater than: a > b
# greater than or equal to: a >= b

a = 33
b = 200
if b > a:
    print("b is greater than a")


# python uses indentation instead of curly brakets to define the scope of code


# elif keyword: like else if.
# if the previous conditions were not true, then try this condition.
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


# else keyword: catches anything not caught by previous conditions
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# shorthand if
if a > b: print("a is greater than b")
# can use if you have only one statement to execute


# shorthand if... else
print("A") if a > b else print("B")
# this is called ternary operators, or conditional expressions.
# can do this with multiple else statements
print("A") if a > b else print("=") if a == b else print("B")


# and keyword - logical operator to combine conditional statements
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true")


# or keyword
if a > b or a > c:
    print("At least one of the conditions is True")


# nested if statements
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


# pass statement
# if statements can't be empty
# if you have no content for some reason, pass avoids an error
a = 33
b = 200
if b > a:
    pass













































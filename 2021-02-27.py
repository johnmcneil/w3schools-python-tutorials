# class
# a class is a blueprint for creating objects
class MyClass:
    x = 5


# use myclass to create objects
p1 = MyClass()
print(p1.x)


# __init()__ function
# all classes have it.
# executed when a class is being initiated
# assigns values to object properties,
# or other operations necessary when object created
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)


print(p1.name)
print(p1.age)


# object methods
# methods are functions that belong to objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


# the self parameter is
# a reference to the current instance of the class
# used to access variables that belong to the class
# it does not have to be called self
# it does have to be the first parameter of any function in the class


# modify properties in objects
p1.age = 40


# delete properties in objects
del p1.age


# delete objects
del p1


# class definitions can't be empty
# if for some reason you have an empty class
# use the pass statement
class Person:
    pass


# Python inheritance
# inheritance allows us to define a class that
# inherits all methods and properties from another class
# parent class, aka base class: class being inherited from
# child class, aka derived class: class that inherits from another
# any class can be a parent class. syntax is the same.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()


# create a class Student which will inherit props and methods from Person
class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()


# add __init__() function to the child class
# the child's __init__() function overrides the parent's
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


# super() function
# makes the child class inherit all methods and props from its parent
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


# add properties
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)
x.welcome()


# if you add a method to the child class with the same name
# as a method in the parent class, the inheritance of the
# parent method will be overriden

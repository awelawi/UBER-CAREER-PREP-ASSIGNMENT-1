 # Object Oriented Programming in Python

 # a string is an object of the class string
 # an int is an object of the class int
 # all things in pythhon that u work with is an object of a certain class
 #they are built in types. 
 # a method is something that acts on an object

from os import stat
from unicodedata import name


class Dog:

    #This is a method that defines what the class should Dog should do when initialized
    def __init__(self, name, age) -> None:
        #This declares an attribute of the class, and u can access attributes that 
        #are specific to each 
        self.name = name
        self.age = age
        # print(name)
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def bark(self):
        print("bark")

    def addOne(self, x):
        return x + 1

#This is instatiating a new object, d that is of type, class Dog
#And what are the operations of Dog, that is methods, well it can print "bark
#" when the .bark() method is called.
# d = Dog("Tim", 40)
# print(d.get_name())
# print(d.get_age())
# d2 = Dog("Bill", 90)
# print(d2.get_name())
# d.bark()
# d.addOne(2)
# print(type(d))

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
s1 = Student("Ella", 18, 100)
s2 = Student("Bill", 18, 92)
s3 = Student("Mark", 18, 80)

course = Course("Science", 2) 
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.get_average_grade())


#Pet is called generalization class while Cat and Dog are Specific Classes
# Parent class
class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age  = age

    def show(self):
        print(f"I am {self.name}. I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

# Inheritancxe in OOP
# u notice that both classes have the same init method so create something generally
#that both classes can inherit and define their specific aqttributes within the
# classes trhemselves

# You inherit the properties of the genreal class by putting it in a parentheses like 
# an invocationm call
#child class
class Cat(Pet):
    def __init__(self, name, age, color) -> None:
        # super stands for, reference the super class which is Pet, so u don't
        # need to initialize name and age again.
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("meow")
    
    def show(self):
        print(f"I am {self.name}. I am {self.age} years old and I am {self.color} color")

class Dog(Pet):
    def speak(self):
        print("bark")

# If a method isn't defined in the child class but defined in the parent class
# The child object asssumes the method. But if it's also defined in the child class, 
# the child class overrides the general parent method
p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34, "Brown")
c.show()

# Class atributes, and they attributes specific to a class and not the object of the class.

class Person:
    number_of_people = 0

    def __init__(self, name) -> None:
        self.name = name

p1 = Person("tim")
p2 = Person("jill")
# This is an attribute number_of_people = 0 that's specific to the class and not 
# the object of the class like "tim"
print(p1.number_of_people)

# class methods act on the class themselves and have no access to any instance
class Person:
    number_of_people = 0

    def __init__(self, name) -> None:
        self.name = name
        Person.add_person()
    
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
print(Person.number_of_people_())

# Static methods, creating classes that organizes functions together

class Math:
    # they dont change anythiong but just do something
    @staticmethod
    def adds(x):
        return x + 5

print(Math.adds(5))
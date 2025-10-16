# # OOPS- Object oriented programming system
# # Encapsulation, Inheritance, Polymorphism, Abstraction

# #oops - implementation of class and objects

# # create a class 
# # class Employee:
# # objects - instance of a class 
# # what is instance - an object of a class is called instance

# class Customer:
#     # class attributes(variables)
#     bank_name = "SBI"
    
#     def greet(self): # self is a reference variable
#         print("Welcome to the bank")

# # create an object of a class
# c1 = Customer() # c1 is an object of class Customer
# print(c1.bank_name)
# c1.greet()

# c2 = Customer()
# print(c2.bank_name)
# c2.greet()

# class Customer:
#     def __init__(self, name, age,initial_amount): # __init__ - constructor, it initializes the object, it is called automatically when an object is created
#         self.name = name # instance variable
#         self.age = age 
#         self.balance = initial_amount

# c1 = Customer("Chinnu",21,1000)
# print(c1.name)
# print(c1.age)
# print(c1.balance)

# c2 = Customer("Praveen",20,2000)
# print(c2.name)
# print(c2.age)
# print(c2.balance)


# class Customer:
#     bank_name = "SBI" # class attributes(variables)
    
#     def __init__(self, name, age,initial_amount): 
#         self.name = name # instance variable
#         self.age = age 
#         self.balance = initial_amount
    
#     def deposit(self, amount):
#         self.balance = amount + self.balance
#         print(f'{amount} deposited successfully. New balance is {self.balance}')

# c1 = Customer("Chinnu",21,1000)
# c2 = Customer("Praveen",20,2000)

# c1.deposit(500)
# print(c1.balance)

# constructor - a special type of method which is called automatically when an object is created
# self - to store the reference of the current object

# class student:
#     school_name = "ABC School" # class variable
    
#     def __init__(self, name, age):
#         self.name = name # instance variable
#         self.age = age
    
#     def display(self):
#         print(f'Student name is {self.name} and age is {self.age}')
    
#     @classmethod # class method - it takes class as first argument
#     def get_school_name(cls): # cls - class reference variable
#         return cls.school_name
    
#     @staticmethod - static method - it doesn't take any argument
#     def is_adult(age):
#         return age>18

# x = student("Chinnu",21)
# x.display()

# print(student.get_school_name())
# print(student.is_adult(20))
# print(x.is_adult(17))


# class Engine:
#     def __init__(self):
#         self.power = 1000
#     def start(self):
#         print("Engine started")

# class Car:
#     def __init__(self):
#         self.engine = Engine() # composition - Car has an Engine
    
#     def move(self):
#         self.engine.start()
#         print("Car is moving")

# c = Car()
# c.move()


# Encapsulation - wrapping data and methods into a single unit
# Public, Private, Protected

# class Car:
#     __price = 10000 # private variable
#     _model = "BMW" # protected variable
#     color = "Black" # public variable

# c1 = Car()
# print(c1._model) # protected variable can be accessed outside the class 
# print(c1.__price) # name mangling - _ClassName__variableName
# print(c1.color) # public variable can be accessed outside the class
# c1.price = 0
# print(c1.price) # 0

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name          # public attribute
#         self.__salary = salary    # private attribute

# emp = Employee("Chinnu", 50000)
# print(emp.name)       
# print(emp.__salary)

# self.name = name: Public attribute, can be accessed directly.
# self.__salary = salary: Private attribute, cannot be accessed directly.
# print(emp.name): Prints "Chinnu" because name is public.
# print(emp.__salary): Raises an error because __salary is private and hidden.



# Inheritance - acquiring properties and behaviors from a parent class
# parent class - base class, super class
# child class - derived class, sub class

# types of inheritance - single, multiple, multilevel, hierarchical, hybrid

# single level inheritance - one parent and one child

# class A:
#     def a(self):
#         print("I am class A")
# class B(A): # B is inheriting A
#     def b(self):
#         print("I am class B")
# obj = B()
# # obj.b()
# # obj.a()

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Employee(Person):  # Employee inherits from Person
#     def show_role(self):
#         print(self.name, "is an employee")

# emp = Employee("Chinnu")
# print("Name:", emp.name)
# emp.show_role()


# Multiple inheritance - one child and multiple parents

# class A:
#     def a(self):
#         print("I am class A")
# class B: 
#     def b(self):
#         print("I am class B")
# class C(A,B): # C is inheriting A and B
#     def c(self):
#         print("I am class C")

# obj = C()
# obj.a()
# obj.b()
# obj.c()


# class Person:
#     def __init__(self, name):
#         self.name = name

# class Job:
#     def __init__(self, salary):
#         self.salary = salary

# class Employee(Person, Job):  # Inherits from both Person and Job
#     def __init__(self, name, salary): 
#         Person.__init__(self, name) # Initialize Person part
#         Job.__init__(self, salary) # Initialize Job part

#     def details(self):
#         print(self.name, "earns", self.salary)

# emp = Employee("Praveen", 50000)
# emp.details()


# Multilevel inheritance - grandparent, parent, child


# class A:
#     def a(self):
#         print("I am class A")
# class B(A): # B is inheriting A
#     def b(self):
#         print("I am class B")

# class C(B): # C is inheriting B
#     def c(self):
#         print("I am class C")

# # obj = A()
# # obj.a()

# obj = B()
# obj.a()
# obj.b()
# obj.c() # AttributeError: 'B' object has no attribute 'c'

# obj = C()
# obj.a()
# obj.b()
# obj.c()

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Employee(Person):  # Employee inherits from Person
#     def show_role(self):
#         print(self.name, "is an employee")

# class Manager(Employee):  # Manager inherits from Employee
#     def department(self, dept):
#         print(self.name, "manages", dept, "department")

# mgr = Manager("Joy")
# mgr.show_role()
# mgr.department("HR")

# Hierarchical inheritance - one parent and multiple children

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Employee(Person):  # Employee inherits from Person
#     def role(self):
#         print(self.name, "works as an employee")

# class Intern(Person):  # Intern inherits from Person
#     def role(self):
#         print(self.name, "is an intern")

# emp = Employee("Yaash")
# emp.role()

# intern = Intern("Chinnu")
# intern.role()

# Hybrid inheritance - combination of two or more types of inheritance

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Employee(Person):  
#     def role(self):
#         print(self.name, "is an employee")

# class Project:
#     def __init__(self, project_name):
#         self.project_name = project_name

# class TeamLead(Employee, Project):  # Hybrid Inheritance - inherits from Employee and Project
#     def __init__(self, name, project_name):
#         Employee.__init__(self, name)
#         Project.__init__(self, project_name)

#     def details(self):
#         print(self.name, "leads project:", self.project_name)

# lead = TeamLead("Yuvan", "AI Development")
# lead.role()
# lead.details()


# class Parent:
#     def __init__(self,name,age,house):
#         self.name = name
#         self.age = age
#         self.house = house

# class Child(Parent):
#         def __init__(self,name,age,house,school):
#             Parent.__init__(self,name,age,house) # parent is a super class , is a reference variable for parent class
#             self.school = school
            
# obj = Child("Chinnu",21,"ABC School","hosur")
# print(obj.name)
# print(obj.age)
# print(obj.school)
# print(obj.house)


# Polymorphism - ability to take many forms

# overloading - same method name with different parameters

# def f1():
#     print("one")
# def f1():
#     print("two")
# def f1():
#     print("three")

# f1()

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

# Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))
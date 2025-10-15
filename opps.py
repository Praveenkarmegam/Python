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


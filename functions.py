# # Functions - a bock od codes that can bse reused multiple times whenever we call the function

# # def - keyword to define a function

# def greeting():
#     print("Hello, Everyone")
#     print("Welcome to Python Programming")

# greeting()

# # DRY - Don't Repeat Yourself

# def add_numbers(num1, num2): # parameters - holds the values
#     return num1 + num2

# print(add_numbers(5,10)) # arguments - actual values passed to the function

# # formal vs actual parameters

# def f1(x,y): # formal parameters
#     return x * y 

# print(f1(4,5))


# # how to access the parameter inside the function.
# # we can access the parameter like a normal variable

# def function(my_list):
#     my_list.append(1) # add the value 1 to the list
    
# l1 = [2,3,4]
# print("Before function call:", l1)

# function(l1) # passing the list l1 to the function

# print("After function call:", l1)

# # we are sharing only the reference of the variable to the function, not a variable to the function 



# def my_work(text):
#     text += " World"

# text = "Hello"
# print("Before function call:", text)

# my_work(text)
# print(text)


# def welcome(name):
#     print("Welcome", name)
    
# welcome("Chinnu")
# welcome("Yaash")
# welcome("Muthu")

# # key = value arguments

# def my_function( y = 2, x = 3):
#     return x * y

# print(my_function())


# def my_function2(name="Guest",surename="User",age=25,height=5.5):
#     print("Name:", name)
#     print("Surename:", surename)
#     print("Age:", age)
#     print("Height:", height)
#     print()
    
# my_function2()


# # a user can have multiple details for example: name, age, height, weight, address, email, phone number etc
# # arbitary keyword arguments - **kwargs

# def my_function3(**details):
#     for key,value in details.items(): # items() - method to get the key value pairs from the dictionary
#         print(key, ":", value)
        

# my_function3(name="Chinnu", age=23, height=5.7, weight=70, address="Chennai", email="chinnu@gmail.com", phone=1234567890)


# #1. Default Arguments - if the user does not provide any value to the parameter, the default value will be used

# def myFun(x=23,y=45):
#     print("x: ", x)
#     print("y: ", y)

# myFun(10)

# # 2. Keyword Arguments = we can pass the arguments to the function by using the parameter name

# def student(fname, lname):
#     print(fname, lname)

# student(fname='muthu', lname='kumar')

# # 3. Positional Arguments - we can pass the arguments to the function by using the position of the parameter

# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)

# print("Case-1:")
# nameAge("Chinnu", 27)

# print("Case-2:")
# nameAge(27, "Chinnu") # wrong way of passing the arguments


# # functions inside functions

# def f1():
#     s = 'I love Python'
#     print("Inside f1")
#     def f2():
#         print(s)
        
#     f2()
#     print("End of f1")
# f1()


# function scope - local and global

# x = 10 # global variable
# print(x)

# def f1():
#     print(x) # accessing the global variable inside the function

# f1()


# def f2():
#     y = 20 # local variable
#     print(y)
#     print(x) 

# f2()

# print(y) # trying to access the local variable outside the function - will give an error


# Recursion - a function that calls itself
# factorial of a number - n! = n * (n-1) * (n-2) * ... * 1

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5)) # 5 * 4 * 3 * 2 * 1 = 120

# # fibanacci series - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2) # sum of the previous two numbers, n-1 is the previous number, n-2 is the number before the previous number
    
# print(fibonacci(13)) # 233 -position 13 in the series



# lambda functions - anonymous functions - a function without a name


# def f1(x): 
#     return x + 10

# print(f1(5))

# a = lambda x : x + 10 # lambda function
# print(a(10))


# a = lambda x, y, z : x + y + z
# print(a(10, 20, 30))

# def square(x):
#     return x** 2
# print(square(5))

# def cube(x):
#     return x**3
# print(cube(2))

# def power(n):
#     return lambda x : x ** n

# sqaure = power(2)
# cube = power(3)
# fourth_power = power(4)

# print(sqaure(5))
# print(cube(3))
# print(fourth_power(2))


# decorators - a function that takes another function as an argument and extends its behavior without modifying it


# def my_decorator(func): # say_hello() function is passed as an argument to the my_decorator function
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello, World!")

# say_hello()



# def decorator(new_function):
    
#     def combine(*args, **kwargs):
#         print("Before execution")
#         result = new_function(*args, **kwargs)
#         print("After execution")
#         return result
#     return combine

# @decorator
# def add(a, b):
#     return a + b

# print(add(5, 3))

# generator functions - a function that returns an iterator that produces a sequence of values using the yield statement


# def my_generator():
#     yield 1 # passing the value 1 to the caller
#     yield 2 # passing the value 2 to the caller
#     yield 3 # passing the value 3 to the caller
#     yield "Hello" # passing the value "Hello" to the caller
    
# for value in my_generator():
#     print(value)
#     print(value ,"is a generator value")
#     print(value, "is yielded from the generator function")
#     print(value, "will move to the next yield statement")
#     print("-----")

# def genre():
#     yield "Action"
#     yield "Comedy"
#     yield "Drama"
#     yield "Horror"
#     yield "Romance"
#     yield "Sci-Fi"
#     yield "Thriller"
#     yield "Fantasy"
#     yield "Mystery"
#     yield "Documentary"

# x = genre() 
# # for i in x:
# #     print(i)
# print(next(x)) # next() - to get the next value from the generator
# print(next(x))


# def fibonacci(limit):
#      a,b = 0,1
#      while a <= limit:
#             yield a # yield - to pass the value to the caller 
#             a,b = b, a + b 

# for num in fibonacci(10):
#     print(num) # 0,1,1,2,3,5,8
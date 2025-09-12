# Python Basics

print("Hello, World!")


#Data Types

# 1. Numbers
 # Integer, Float, Complex
 
# integer - whole numbers without decimal points
 
x = 10

# Float - numbers with decimal points

y = 10.5

# Complex - numbers with real and imaginary parts
z = 3 + 4j

print(type(x))
print(type(y))
print(type(z))

# 2. String
print("This is a string")
print(type("This is a string"))
print(type('This is also a string'))

#3. Boolean - True or False

print(True)
print(False)
print(type(True))
print(type(False))


# 4. List - ordered, mutable collection of items
l1 = [1, 2, 3, 4, 5, "Hello" , 10.5, True]
print(l1)
print(type(l1))

# 5. Tuple - ordered, immutable collection of items

l2 = (1, 2, 3, 4, 5, "Hello" , 10.5, True)
print(l2)
print(type(l2))

# 6. Sets - unordered, mutable collection of unique items

s1 = {1, 2, 3, 4, 5,1,1,1, "Hello" , 10.5} # duplicates will be removed , only unique items will be stored
print(s1)
print(type(s1))


# 7. Dictionary - unordered, mutable collection of key-value pairs
# key value pairs are separated by colon (:) and items are separated by comma (,) and enclosed in curly braces {}

d1 = {
    "name": "John", 
    "age": 30, 
    "city": "New York",
    "name": "Doe" # key must be unique and the recent value will overwrite the previous value if the key is duplicated
    }
print(d1)
print(type(d1))

# variables

fruit = "Banana"
x = 5 # integer

# casting
y = float(x) # cast integer to float
print(y)

z = str(x) # cast integer to string
print(z)
print(type(z))

# Rules for variable names
#1. Variable names must start with a letter or underscore (_) e.g. my_variable, _myvariable
#2. Variable names cannot start with a number e.g. 1variable (invalid)
#3. Variable names can only contain alphanumeric characters and underscores (A-z, 0-9, and _) eg. my_variable1 (valid) , my-variable (invalid)
#4. Variable names are case-sensitive (myVariable and myvariable are different variables) eg. myVariable, myvariable
#5. Variable names cannot be a reserved keyword in Python e.g. if, else, while, for, def, class, etc. (invalid)


# Assingning multiple values to multiple variables

x,y,z = 'apple', 'banana', 'cherry'

print(x,y,z,sep='\n') # this  \ is called as escape character and n is new line


# Assigning same value to multiple variables

a = b = c = "Orange"

print(a,b,c,sep='\n')


# variable name which as a meaning or a purpose is called as a good variable name

# what is the total payment if the time is 10 hours and payment per hour is 100

time = 10 # hours
payment = 100 # payment per hour

total = time * payment 
print(total)

# normal
a = 10
b = 100
c = a * b
print(c)

totalpayment = time * payment # game , movie , bank 

# camel case eg totalPayment - second word starts with a capital letter
# pascal case eg TotalPayment - every word starts with a capital letter
# snake case eg total_payment - every word is in lowercase and words are separated by underscore (_)


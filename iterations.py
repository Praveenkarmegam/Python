# while and for loops 
# While Loop - excutes a set of statements as long as a condition is true until the condition becomes false

# i = 0

# while i < 5: # True 
#     print(i) # prints the value infinite times
#     i += 1 # incrementing the value of i by 1
    
# if the condition became false it exits the loop.

# break keyword - used to exit the loop when a certain condition is met


# i = 0 
# while i < 10:
#     print(i)
#     if i ==3:
#         break # exits the loop when i is equal to 4
#     i += 1

# continue keyword - used to skip the current iteration and move to the next iteration of the loop

# i = 0 
# while i < 10:
#     i += 1 # incrementing the value of i by 1 to avoid infinite loop
#     if i == 4:
#         continue 
#     print(i)

# i = 0
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")

# where to use while loop?
# when the number of iterations is not known in advance
# when you want to repeat a block of code until a certain condition is met
# when you want to create an infinite loop that runs until a specific event occurs

# For Loop - used to iterate over a sequence or range  (like a list, tuple, dictionary, set, or string) or other iterable objects

l1 = [10,20,30,40,50]

for each_item in l1:
    print(each_item )
    

text = "Hello, World!"

for each_char in text:
    print(each_char)
    
for each_num in l1:
    print(each_num)
    if each_num == 30:
        break

for each_num in l1:
    if each_num == 30:
        continue
    print(each_num)

else:
    print("Loop is completed")
    

# range() function - generates a sequence of numbers within a specified range

for i in range(5): # starts with 0 and ends at n-1 or last number is exclusive (5-1=4)
    print(i)
    
# range(start, end)

for i in range(1, 6): 
    print(i)

# range(start, end, step)

for i in range(1, 10, 2):
    print(i)


# nested for loop - a for loop inside another for loop

# inner loop and outer loop
# the inner loop will be executed for each iteration of the outer loop

colors = ["yellow","red","blue"]

transport = ["bike","car","bus"]


for color in colors:
    for vehicle in transport:
        print(color, vehicle)
        

# where to use for loop?
# when the number of iterations is known in advance
# when you want to iterate over a sequence or collection of items
# when you want to perform a specific action for each item in a list, tuple, or string


# assert keyword - used to test if a condition is true, if the condition is false it raises an AssertionError

x = "hello"

assert x == "hello" # no error

assert x == "world" # raises an AssertionError

print(x) # x is hello but not world

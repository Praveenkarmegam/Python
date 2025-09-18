# # a = "Chinnu is data analyst" # main string
# # b = 'Python is fun.'
# # c = """This is a multi-line
# # string. It can span multiple lines.
# # You can include 'single' and "double" quotes without escaping them."""

# # # print(a)
# # # print(b)
# # # print(c)

# # # print(type(a))
# # # print(type(b))
# # # print(type(c))

# # print(len(a))
# # # print(dir(a)) # list of all methods available for string objects directory

# # print(a.split(" ")) # from the main string the substrings are separated by space.


# # multipy a string

# print("a"*3)

# b = "thilipan "

# c = b * 5
# print(c)

# # sitring are immutable once created cannot be modified the original string.

# word = "this coding to boring "
# print(word)
# print('this' in word)
# print('python' not in word )


# string are indexed 

# a = "HELLO WORLD" # 0,1,2,3,.... (or) ....,-3,-2,-1
# print(a)

# print(a[6])

# print(a[-1])


# #slicing- start:end

# print(a[2:5]) # index value 2 to 5 
# print(a[:5]) # index value 0 to 5
# print(a[6:]) # index value 6 to n-1
# print(a[:]) # print all string
# print(a[::2]) # print the step value or skips the value based step value in the string [start,end,step-up]
# print(a[::-1]) # reverse the string

# # palindrom
# # mom => reverse = mom  or  dad => reverse = dad

# word = input("enter the word:")
# print(word == word[::-1])

# s = "mom" # string
# rev = ''.join(reversed(s))

# if s == rev:
#     print("Yes")
# else:
#     print("No")
    

place = 'munnar'
food = 'ICE-CREAM'

print(place.upper())

print(place.title())

print(food.lower())

print(food.title())

print(place.isalnum()) # may be an alphabets or numeric 

print(place.isdigit()) # takes only numbers 
print(place.isalpha()) # takes only alphabets

print(place.islower()) # checks the value is lower
print(food.isupper()) # checks the value is upper

# removing and replace 

transport = "    car and bike   "

print(transport.replace("bike","train"))
print(transport.strip()) # remove the space in front and backside of the string 
print(transport.lstrip(" ")) # remove the left side space
print(transport.rstrip(" ")) # remove the right side space


a = 'A B C D E F'
print(a.split(" "))

a = ['A', 'B', 'C', 'D', 'E', 'F']
print(''.join(a))


a = "Hello thilipan in few minites the session will be ended"

print(a.find("thilipan"))

# concatenation (combining of the strings)
a = "I am Hungry and "
b = "I need to at My Dinner"

c = a + b
print(c)

# format : takes an argument , places it where there are placeholders {}

age = 21
text  = "I am {} years old"

print(text.format(age))

age = 21 
college = "PMC"

text1 = 'I am {} years old. I study in {}'
print(text1.format(age,college))

text2 = 'I am {} years old. I study in {}'.format(age,college)
print(text2)


text3 = f'I am {age} years old. I study in {college}'
print(text3)
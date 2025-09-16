# 1. Arthimetic Operators - Add, Subtract, Multiply, Divide, Modulus, Exponent, Floor Division

a = 10
b = 3

print("Addition:",a + b)
print("Subtraction:",a - b)
print("Multiplication:",a * b)
print("Division:",a / b)
print("Modulus:",a % b) #  Remainder - value after division is called as modulus
print("Exponent:",a ** b) # power value 
print("Floor Division:",a // b) # Quotient - value before decimal point is called as quotient

# 2. Assignment Operators - =, +=, *=, /=, %=, **=, //=

x  = 10 # assigin a value 10 to variable x  (equal to)

print("Initial Value of x:",x)

x += 5 # x = x + 5 (add and equal to)
print(x)

x-= 2 # x = x - 2  ( subtract and equal to)
print(x)

x *= 3 # x = x * 3  (multiply and equal to)
print(x)

x /= 4 # x = x / 4 (divide and equal to)
print(x)

x %= 3 # x = x % 3 (modulus and equal to)
print(x)

x **= 2 # x = x ** 2 (exponent and equal to)
print(x)

x //= 2 # x = x // 2 (floor division and equal to)
print(x)


# 3. Comparison Operators - ==, !=, >, <, >=, <=

# = - assign the value to variable
# == - compare the value of variable

x = 10 # equal to
y = 10
print(x == y) 

x = 5
y = 10
print(x != y) # not equal to

x = 15
y = 10
print(x > y) # greater than

x = 5
y = 10
print(x < y) # less than

x = 15
y = 10
print(x >= y) # greater than or equal to

x = 20
y = 10
print(x <= y) # less than or equal to


#4. Logical Operators - and, or, not

# and - all conditions should be true

x = 10 
print(x > 5 and x < 15)

# or - any one condition should be true

y = 20
print(y > 25 or y < 30)


# not - reverse the result, returns false if the result is true or returns true if the result is false

z = 30
print(not(z==30))

#5. Identity Operators - is, is not

x = ["apple", "banana"] # list object
y = ["apple", "banana"] # list object

# x and y are not same objects, they are different objects with same values

print(x is y) 

print(x is not y) # x and y are not same objects 

x = ["apple", "strawberry"]
y = ["apple", "strawberry"]
z = x  # z is assigned to x, so they are same objects 

print(x is y)
print(x is z)

# 6. Membership Operators - in, not in

x = ["apple", "banana", "cherry"]
y = "banana"
z = "orange"

print(y in x)
print(z not in x)


#7. Bitwise Operators - &, |, ^, ~, <<, >>

x = 9
y = 5

result_and = x & y # AND
print("AND:",result_and) # Output: 1 (Binary: 1001 & 0101 = 0001)

result_or = x | y # OR
print("OR:",result_or)  # Output: 13 (Binary: 1001 | 0101 = 1101)

result_xor = x ^ y # XOR
print("XOR:",result_xor) # Output: 12 (Binary: 1001 ^ 0101 = 1100)

result_not = ~x # NOT
print("NOT:",result_not) # Output: -10 (Binary: ~0000...1001 = 1111...0110 which is -10 in two's complement)

result_left = x << 2 # Left Shift
print("Left Shift:",result_left) # Output: 36 (Binary: 1001 << 2 = 100100 which is 36 in decimal)

result_right = x >> 2 # Right Shift
print("Right Shift:",result_right) # Output: 2 (Binary: 1001 >> 2 = 0010 which is 2 in decimal)

# binary value of 9 is 1001 is converted to not 0110  if we coverted to decimal it becomes 6 how ?
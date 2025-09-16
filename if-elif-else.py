# one way selection  (if statement)

order = 560
minimum_order = 500 
delivery = 50

totalprice = order + delivery
print("Total price is:", totalprice)

if order > minimum_order:  # condition true means indented block will run
    print("You qualify for free delivery")
    delivery = 0
    
print("Total price is:", order + delivery)


# two way selection (if-else statement)


mark = int(input("Enter your marks: "))
passing_marks = 45

if mark >= passing_marks:
    print("You have passed the exam")
else:
    print("You have failed the exam")
    

# multiple way selection (if-elif-else statement)

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("You got an O grade")

elif marks >= 80:
    print("You got an A+ grade")

elif marks >= 70:
    print("You got an A grade")
    
elif marks >= 60:
    print("You got a B+ grade")

elif marks >= 50:
    print("You got a B grade")

elif marks >= 45:
    print("You got a C grade")

else:
    print("You have failed the exam")
    

# short hand if-else (ternary operator)

# if i has only one statement to execute, we can write it in a single line
a = 10

print("a is even") if a % 2 == 0 else print("a is odd") 

# nested if statement

age = int(input("Enter your age: "))

choice = input("Enter your Gender:")

if choice =="male":
    if age >= 25:
        print("Male are eligible for marriage")
    else:
        print("Male are not eligible for marriage")

elif choice =="female":
    if age >= 21:
        print("Female are eligible for marriage")
    elif age < 21 and age >= 18:
        print("Female are eligible for marriage with guardian consent")
    else:
        print("Female are not eligible for marriage")
else:
    print("You are child")
    
    
age = int(input("Enter your age: "))
member = True

if age > 18:
    if member == True and age < 60:
        print("Ticket price is $12.")
    else:
        print("Ticket price is $20.")
else:
    if member == True and age < 12:
        print("Ticket price is $8.")
    else:
        print("Ticket price is $10.")



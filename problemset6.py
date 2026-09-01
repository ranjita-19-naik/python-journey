#conditinal expressions
#if else
"""a = int(input("Enter your age: "))

if a >= 18:
    print("You are eligible")
else:
    print("You are not eligible")
# if elif else ladder
a = int(input("Enter your age: "))

if a >= 18:
    print("You are eligible")
elif a >= 16:
    print("You are almost eligible")
elif a >= 14:
    print("You are somewhat eligible")
else:
    print("You are not eligible")
#relational or comparison operators
x = 5
print(x > 3)
print(x < 3)
print(x == 3)
print(x != 3)
print(x >= 3)
print(x <= 3)
#logical operators
print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))
print(not(x > 3 or x < 4))
print(x > 3 and x < 10)"""
#multiple if statements
"""a = int(input("Enter your age: "))
if a%2 == 0:
    print("You are eligible")
if a >= 18:
    print("You are eligible")
elif a >= 16:
    print("You are almost eligible")
else:
    print("You are not eligible")"""
#practise set #1
"""a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if(a1 > a2 and a1 > a3 and a1 > a4):
    print("The greatest number is a1:", a1)
elif(a2 > a1 and a2 > a3 and a2 > a4):
    print("The greatest number is a2:", a2)
elif(a3 > a1 and a3 > a2 and a3 > a4):
    print("The greatest number is a3:", a3)
else:
    print("The greatest number is a4:", a4)
#2 
marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

#check total percentage
total_percentage = (100 * (marks1 + marks2 + marks3)) / 300

if (total_percentage >= 40 ):
    print("You have passed the exam")
else:
    print("You have failed the exam")"""
#3 
p1 = "make a sandwich"
p2 = "make a cup of tea"
p3 = "do your homework"
p4 = "go to the gym"
message = input("Enter your message: ")
if(p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("I have to do this task")
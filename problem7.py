#1
username =input("Enter your username: ")
if(len(username)<10):
    print("Username must be at least 10 characters long")
else:
    print("Username is valid")
#2
l = ["harry", "hermione", "ron"]
name = input("Enter your name: ")
if name in l:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")
#3
marks = int(input("Enter your marks: "))
if marks <=100 and marks >=90:
    grade = "EX"
elif marks <90 and marks >=80:
    grade = "A"
elif marks <80 and marks >=70:
    grade = "B"
elif marks <70 and marks >=60:
    grade = "C"
elif marks <60 and marks >=50:
    grade = "D"
elif marks <50:
    grade = "E"
    print("Your grade is:", grade)
#4
post = "hey ranjita is girl she is so lazy:"
post = input("Enter your post: ")
if "ranjita".lower() in post.lower():
    print("This post is allowed")
else:
    print("This post is  notallowed")
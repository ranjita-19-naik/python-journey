#problem set 1
n = input ("Enter a number: ")

for i in range(1, 11):
    print(f"{n} x {i} = {int(n) * i}")
#2
l = ["harry ", "rohan", "skillf", "carry"]
for name in l:
    if name.startswith("s"):
        print(f"Hello {name}")
#3
n = input ("Enter a number: ")
i = 1
while i <= 10:
    print(f"{n} x {i} = {int(n) * i}")
    i += 1
#4prime number check
n = input ("Enter a number: ")
for i in range(2, int(n)):
    if(int(n)%i)==0:
        print("number is not prime")
        break 
    else:
        print("number is prime")
        break
#5
n = int(input("Enter a number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i+= 1
    print(sum)
#6factorial of a number
n = int(input("Enter a number: "))
product = 1
for i in range(1, n+1):
    product *= i
print(product)
#7star pattern
n = int(input("Enter a number: "))
for i in range(n):
    print("*" * (i + 1))
#8
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
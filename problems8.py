#loops in python
for i in range(5):
    print(i)
for i in range (1,12,):
    print(i)
#while loop
i = 7
while i < 12:
    print(i)
    i += 1
#to print 1 to 50 using while loop
i = 1
while i <= 50:
    print(i)
    i += 1
# 1 to 50 using for loop
for i in range(1, 51):
    print(i)
#list u sing while loop
l = [1, 2, 3, 4, "ranjita","sussu"]
i = 0
while i < len(l):
    print(l[i])
    i += 1
#using for loop
for i in l:
    print(i)
#tables of 2 using while loop
i = 0
while i <= 10:
    print(2 * i)
    i += 1
#tables of 2 using for loop
for i in range(0, 20, 2):
    print(i)
#string with for loop
s = "ranjita"
for i in s:
    print(i)
#while loop with string
s = "ranjita"
i = 0
while i < len(s):
    print(s[i])
    i += 1
#for loop with else
l = [1, 2, 3, 4, 5]
for item in l:
    print(item)
else:
    print("No items left")
#break and continue 
for i in range(100):
    if i == 50:
        break
    print(i)

for i in range(100):
    if i == 50:
        continue
    print(i)
#pass statement
for i in range(645):
  pass

i = 0
while i < 45:
    print(i)
    i += 1

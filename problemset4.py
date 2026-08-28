#Tuple
a = (1, 2, 3, 4, 5)
print(type(a))
a=()
print(type(a))

#tuple methods
b = (1, 2, 3,4, 45,"ranju" ,"suss", "sammu", 45)
no = a.count(4)
print(no)
print(b.count("ranju"))
print(b.index("suss"))
print(len(b))
print(b[0:5])
print(b.index(45))
concatination = a + b
print(concatination)
print(2 in a and 2 in b)
print(2 in a)
print(min(a))
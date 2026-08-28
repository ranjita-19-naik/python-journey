#list 
friends=["John", "Mary", 5 ,345.6 ,True]
friends[0] = "mike"
print(friends[0])
print(friends[1:3])

#list methods
friends.append("ranjita")
print(friends)
friends.insert(2,"ranjit")
print(friends)
friends.remove("ranjit")
print(friends)
friends.pop()
print(friends)
print(friends.index("Mary"))
print(friends.count("Mary"))
l1=[1,142,13,54,35]
l1.sort()
print(l1)
value =l1.pop(2)
print(value)
print(l1)
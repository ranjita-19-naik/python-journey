#sets
s = {1, 2, 3, 4, 5, "ranju", "suss", "sammu", 45}
r = {1, 2, 3, 4, 5, "nanu","adu","ava",}
print(type(s))
#methods of sets

s.add(6)
print(s)
print(s,type(s))
s.remove(3)
print(s)
s.discard(4)
print(s)
#print(s.clear())
print(s.copy())
print(s.union(r))
print(s.intersection(r))
print(s.isdisjoint(r))
#practice set #1
words ={
    "apple": " fruit",
    "car": "a vehicle",
    "book": "a written work"
}
word =input("Enter the word" \
" you want meaning of:")
print(words[word])
#2
s = set()
n = int(input("Enter the number :"))
s.add(int(n))
n = int(input("Enter the number :"))
s.add(int(n))
n = int(input("Enter the number :"))
s.add(int(n))
n = int(input("Enter the number :"))
s.add(int(n))
n = int(input("Enter the number :"))
s.add(int(n))
n = int(input("Enter the number :"))
s.add(int(n))
n = int(input("Enter the number :"))
s.add(int(n))
n = int(input("Enter the number :"))
s.add(int(n))

print(s)
#3
s = set()
s.add(20)
s.add(30)
s.add('18')
print(len(s))
#4
s = {}
print(type(s))
#5
d = {}
name = input("Enter the name:")
lang = input("Enter the language:")
d.update({name: lang})
print(d)
#6
s ={8, 9, 10,"harry",(1,2,3)}
print(s)
#string
name = "Hello, World!"
b ='Hello, World!'
c= """Hello, World!"""
nameshort = name[2:5]
print(nameshort)
character = name[0]
print(character)
print(len(name))
print(name.endswith("rld!"))
print(name.startswith("Hello"))
print(name.capitalize())
print(name.title())
print(name.strip())

#negative slicing 
print(name[-5:-2])
print(name[2:5])

#Advanced slicing
print (name[:4])
print(name[2:])

#replace the word
print(name.replace("Hello", "Hi"))
print(name.removeprefix("Hello,"))

#escape sequence
a ="ranjita is good girl\nbut not a bad girl"
print (a)
a ="ranjita is good girl but not a \"bad girl\""
print(a)
a ="ranjita is \t good girl\tbut not a bad girl"
print(a)
a ="ranjita \\is good girl\\but not a bad girl"
print("hell\bo")
print("ran\bjii\btta")

#practise problems
a= input("Enter your name: ")
print("Good afternoon" , a)
#2
letter = '''Dear <|name|>,
You are selected!
<|date|>'''
print(letter.replace("<|name|>", "ranjita").replace("<|date|>", "20/06/2024"))
#3
name ="ranjit   is good   boy"
print(name.find("  "))
#4
name ="ranjit   is good   boy"
print(name.replace("  "," "))
print(name)
#5
name ="dear ranjita \nyou are\t nice"
print(name)
name ="dear ranjita \nyou are\t nice"
print(name.lower())
print(name.upper())
name ="dear ranjit\byou are\t nice"
print(name)

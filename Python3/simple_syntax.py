
a , b = 2, 3

print(a + b)
print(a + 5)
print(a + int("5"))
print(str(a))

# Hey, our first comment! Lists are easy to operate
names = ["ben", "steve", "bob"]

for name in names:
	print(name)

# A dictionary, just like key value pairs
names_dict = {"name": "Ben", "age": "25", "company": "Accenture"}

# Note the indentation here...
for key, value in names_dict.items():
	print(key + "," + value)


#A backslash means that we should also read the next line
total = 1 + \
2 + \
3
print(total)



# Handy Paragraph
paragraph = """This is a long paragraph and it can span across multiple lines
This is the second line """
print(paragraph)

''' Well that's some basic syntax 
this is a multi line comment ...
'''

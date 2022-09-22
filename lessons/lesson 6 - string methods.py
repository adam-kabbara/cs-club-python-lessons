# escape characters
quote = "she said, \"Hello World of Python\""
print(quote)

# new line (\n) character
multi_line_text = "what\nis\nhappening!?"
print(multi_line_text)

# multiline string!
# we reassigned the variable multi_line_string to a new string
multi_line_text = """Wow!  
this is actually really cool

python rocks!
python > java
🤭🤪"""
print(multi_line_text)

# fun fact; the code below is from my own notes when i started learning python!
a = "run"
b = " wolfs are coming"
c = a + b # remember string concatination from lesson 1?
print(c)

c = a+' watch out'+b
print(c)
print(len(a))
print(len(c))

a = 'flamingo'
# this prints out the letter in the 3 position in the string a
# (python starts counting from zero!)
print(a[3])
print(a[4:7])
print(a[:3])
print(a[3:])

# this prints out the position of i in string a
print(a.index('i'))
print(a.index('o'))

string = "Hello World"
#this counts how many (l) there are in string and prints them
print(string.count('l'))
#This prints the characters of string from 3 to 7 skipping one character
#This is extended slice syntax. The general form is [start:stop:step]
print(string[3:10:2])
#to reverse string
print(string[::-1])
#prints all string in lower case
print(string.lower())
#prints all string in upper case
print(string.upper())
#checks if the string starts with H
print(string.startswith('H'))
#checks if string ends with j
print(string.endswith('j'))

# returns True if a string contains ONLY alphanumeric character
print('hello123'.isalnum())
print('hello123!'.isalnum())

# returns True if a string contains ONLY letter character
print('hello'.isalpha())
print('hello123'.isalpha())

# returns True if a string contains ONLY letter character
print('1 dog'.isdigit())
print('123'.isdigit())
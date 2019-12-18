import re

txt = '''Python is an interpreted, high-level, general-purpose programming language. 
Created by Guido van Rossum and first released of Python in 1991, 
Python's design philosophy emphasizes code readability with its notable use of significant whitespace.'''

print(txt)

if re.search('high-level', txt):
    print("The keyword is exists into the text.")
else:
    print("Not exists.")

if re.search('abc', txt):
    print("The keyword is exists into the text.")
else:
    print("Not exists.")

if re.search('Guido', txt):
    print("The keyword is exists into the text.")
else:
    print("Not exists.")

txt = 'here is \\drogba'
print(txt)
print(re.search(r'\\drogba', txt))

# \w = [a-zA-Z0-9_]
# \W = [^a-zA-Z0-9_]
# phone number validation
phone = '412-123-1212'
if re.search(r"\d{3}-\d{3}-\d{4}", phone):
    print("It is a phone number.")

# name validation
# \s = space
if re.search(r'\w{2,10}\s\w{2,10}', 'Jayanta Biswas'):
    print("Name is valid.")


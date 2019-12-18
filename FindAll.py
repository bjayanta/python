import re

text = '''Jayanta is 75 and Shibbir is 25
Maruf is 26 and Amor is 27
Sir is 105 and Araf is 7 years old.'''

ages = re.findall(r'\d+', text) # ['75', '25', '26', '27', '105', '7']
# ages = re.findall(r'\d{2}', text) # ['75', '25', '26', '27', '10']
# ages = re.findall(r'\d{2,3}', text) # ['75', '25', '26', '27', '105']
print(ages)

names = re.findall(r'[A-Z][a-z]*', text)
print(names)

data = {}
x = 0

for name in names:
    data[name] = ages[x]
    x += 1

print(data)

txt = '''Python is an interpreted, high-level, general-purpose programming language. 
Created by Guido van Rossum and first released of Python in 1991, 
Python's design philosophy emphasizes code readability with its notable use of significant whitespace.'''

# findall
data = re.findall('Python', txt)
for i in data:
    print(i)

txt = 'Sat, hat, pat, mat, rat'
data = re.findall('[Smhpr]at', txt) # ['Sat', 'hat', 'pat', 'mat', 'rat']
data = re.findall('[smhpr]at', txt) # ['hat', 'pat', 'mat', 'rat']
data = re.findall('[smhp]at', txt) # ['hat', 'pat', 'mat']
data = re.findall('[^mh]at', txt) # ['Sat', 'pat', 'rat']
print(data)

num = '123455'
print('Matches:', len(re.findall(r'\D', num)))
print('Matches:', len(re.findall(r'\d{5}', num)))

num = '123 1234 12345 123456 1234567 12345678'
print('Matches:', len(re.findall(r'\d{5,7}', num)))

# email validation
email = "bjayanta.neo@gmail.com     b@.com  @.com   emarufhasan@gmail.com"
print("Email matches:", re.findall(r'[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-Z]{2,3}', email))

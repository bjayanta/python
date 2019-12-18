import re

txt = 'Sat, hat, pat, mat, rat'

regex = re.compile('[r]at')
data = regex.sub('food', txt)
print(data)

txt = '''
i
am
jayanta
'''
print(txt)
regex = re.compile('\n')
data = regex.sub(' ', txt)
print(data)
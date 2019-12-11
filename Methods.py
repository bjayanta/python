my_tuple = ('a', 'p', 'p', 'l', 'e')
print(type(my_tuple))

print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3


my_tuple = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in my_tuple) # Output: True
print('b' in my_tuple) # Output: False

# Not in operation
print('g' not in my_tuple) # Output: True
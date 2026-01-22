# The Syntax
# newlist = [expression for item in iterable if condition == True]

# Traditional way:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

# print("a" in "jayanta") # True
print(newlist)

# With list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Condition
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# Without condition
newlist = [x for x in fruits]
print(newlist)

# Iterable
# newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression
newlist = [x.upper() for x in fruits]
print(newlist)

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits] # return x if x not equal "banana" else "orange"
print(newlist)



num = {1, 2, 3, 4, 5}
print(num)

num1 = {1, 2, 3, 4, 5, 5, 4}
print(num1)

# list to set
num2 = set([4, 5, 6, 5])
print(num2)

# add
num.add(7)
print(num)

# remove
num.remove(7)
print(num)

# el exists or not
print(4 in num)
print(7 in num)
print(7 not in num)

# ex:
a = {1, 2, 3, 4, 5}
b = set([4, 5, 6, 7])

# union
print(a | b)

# intersection
print(a & b)

# difference
print(a - b)
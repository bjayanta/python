
# Operators

# Arithmetic operators
a = 18
b = 4

print("Arithmetic operators operations: ")
print("a + b = ", a+b)
print("a - b = ", a-b)
print("a * b = ", a*b)
print("a / b = ", a/b)
print("a % b = ", a%b) # Modulus
print("a // b = ", a//b) # Floor division
print("a ** b = ", b**2) # exponential

# Assignment operators
print("Assignment operators operations: ")
x = 10
print("x = ", 10)

x = 10
x += 2
print("x += 2:", x)

x = 10
x -= 2
print("x -= 2:", x)

x = 10
x *= 2
print("x *= 2:", x)

x = 10
x /= 2
print("x /= 2:", x)

x = 10
x %= 2
print("x %= 2:", x)

x = 10
x //= 2
print("x //= 2:", x)

x = 10
x **= 2
print("x **= 2:", x)

x = 10
x &= 2
print("x &= 2:", x)

x = 10
x |= 2
print("x |= 2:", x)

x = 10
x ^= 2
print("x ^= 2:", x)

x = 10
x >>= 2
print("x >>= 2:", x)

x = 10
x <<= 2
print("x <<= 2:", x)

# Comparison/relational operators
print("Comparison/relational operators: ")
print("30 > 20", 30 > 20) # True
print("30 < 20", 30 < 20) # False
print("30 >= 20", 30 >= 20) # True
print("30 => 20", 30 <= 20) # False
print("30 == 20", 30 == 20) # False
print("30 != 20", 30 != 20) # True
print("Jayanta == Jayanta", "Jayanta" == "Jayanta") # True

# Logical operators
print("Logical operators: ")
x = 5
print("x = 5; x > 3 and x < 10: ", x > 3 and x < 10)
print("x = 5; x > 3 or x < 4: ", x > 3 or x < 4)
print("x = 5; not(x > 3 and x < 10): ", not(x > 3 and x < 10))

# Identity operators
print("Identity operators: ")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# Membership operators
print("Membership operators: ")
x = ["apple", "banana"]
print("banana" in x) # returns True because a sequence with the value "banana" is in the list
print("pineapple" not in x) # returns True because a sequence with the value "pineapple" is not in the list

# Bitwise operators
print("Bitwise operators: ")
a = 10
b = 4
print(a & b) # Print bitwise AND operation
print(a | b) # Print bitwise OR operation
print(~a) # Print bitwise NOT operation
print(a ^ b) # print bitwise XOR operation
print(a >> 2) # print bitwise right shift operation
print(a << 2) # print bitwise left shift operation




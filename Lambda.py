
# lambda parameter : expression
a = (lambda a, b : a * a + 2 * a * b + b * b) (3, 3)
print(a)

print((lambda a, b : a * a + 2 * a * b + b * b) (2, 3))

# cube
c = (lambda x : x * x * x) (2)
print(c)
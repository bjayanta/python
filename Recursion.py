
# n! = n * (n-1)!

def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

# call
result = fact(4)
print(result)

# call
print(fact(5))
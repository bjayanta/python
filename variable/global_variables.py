"""
Create a variable outside of a function, and use it inside the function.
Example:
"""
# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

"""
Create a variable inside a function, with the same name as the global variable.
Example:
"""
# x = "awesome"

# def myfunc():
#   x = "fantastic" # Update value
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

"""
The global Keyword:
If you use the global keyword, the variable belongs to the global scope.
Example:
"""
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

"""
The global Keyword:
To change the value of a global variable inside a function, refer to the variable by using the global keyword.
Example:
"""
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
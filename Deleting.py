# delete
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
# print("After deleting tup : ")
# print(tup) # error

my_tuple = ('p','r','o','g','r','a','m','i','z')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
del my_tuple

# NameError: name 'my_tuple' is not defined
print(my_tuple)
# Copy Lists

"""
NB. You cannot copy a list simply by typing list2 = list1, 
because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also be made in list2.
"""

# Use the copy() method
thislist = ["apple", "banana", "cherry"]
myList = thislist.copy()
print(myList)

# Use the list() method
thislist = ["apple", "banana", "cherry"]
myList = list(thislist)
print(myList)

# Use the slice Operator
thislist = ["apple", "banana", "cherry"]
myList = thislist[:]
print(myList)
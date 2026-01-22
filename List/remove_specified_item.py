# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.pop(1)
print(thislist)

# Remove Last Item
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.pop()
print(thislist)

# Remove the first item: using del
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
del thislist[0]
print(thislist)

# Remove the entire list: using del
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
del thislist
# print(thislist) # This will raise a NameError because the list has been deleted

# Remove the entire list: using clear()
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.clear()
print(thislist) # not deleted but empty


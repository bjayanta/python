# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend List
thislist = ["apple", "banana", "cherry"]
thislist.extend(["orange", "kiwi", "mango"])
print(thislist)

# Add Any Iterable: Tuple
thislist = ["apple", "banana", "cherry"]
thistuple = ("orange", "kiwi", "mango")
thislist.extend(thistuple)
print(thislist)

# Add Any Iterable: Set
thislist = ["apple", "banana", "cherry"]
thisset = {"orange", "kiwi", "mango"}
thislist.extend(thisset)
print(thislist)

# Add Any Iterable: Dictionary
thislist = ["apple", "banana", "cherry"]
thisdict = {"orange": 1, "kiwi": 2, "mango": 3}
thislist.extend(thisdict)
print(thislist)

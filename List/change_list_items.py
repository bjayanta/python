thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

# Change Item Value
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
print(thislist[1:3])
thislist[1:3] = ["watermelon", "blackcurrant"]
print(thislist)

# Insert Items
thislist.insert(2, "watermelon")
print(thislist)

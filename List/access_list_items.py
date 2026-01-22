thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "grapes"]
print(thislist[1])

# Negative Indexing
print(thislist[-1])

# Range of Indexes
print('Range of Indexes: ', thislist[1:3])
print('Range of Indexes: ', thislist[2:5])
print('Range of Indexes: ', thislist[:4])
print('Range of Indexes: ', thislist[4:])

# Range of Negative Indexes
print('Range of Negative Indexes: ', thislist[-4:-1])
print('Range of Negative Indexes: ', thislist[-2:5])

# Check if Item Exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
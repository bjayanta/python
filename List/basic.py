mylist = ["apple", "banana", "cherry", 'orange', 'kiwi', 'melon', 'grapes']
print('List items are: ', mylist)
print('Length of list is: ', len(mylist))
print('Type of list is: ', type(mylist))

# List Items
print('First item is: ', mylist[0])
print('Second item is: ', mylist[1])
print('Third item is: ', mylist[2])
print('Fourth item is: ', mylist[3])
print('Fifth item is: ', mylist[4])
print('Sixth item is: ', mylist[5])
print('Seventh item is: ', mylist[6])
print('Last item is: ', mylist[-1])
print('Second last item is: ', mylist[-2])
print('Third last item is: ', mylist[-3])
print('Fourth last item is: ', mylist[-4])
print('Fifth last item is: ', mylist[-5])
print('Sixth last item is: ', mylist[-6])
print('Seventh last item is: ', mylist[-7])

# Allow Duplicates
mylist = ["apple", "banana", "cherry", 'apple', 'grapes']
print('List items are: ', mylist)

# Mixed Data Types
mylist = ["apple", "banana", "cherry", 1, 2, 3, True, False, 3.14, 2.71]
print('List items are: ', mylist)

# The list() Constructor
mylist = list(("apple", "banana", "cherry")) # note the double round-brackets
print('List items are: ', mylist)

subject = ["C", "C++", "Java", "Python", "Android"]

# get length
print(len(subject))

# append
subject.append("HTML")
print(subject)

# insert
subject.insert(2, "OS")
print(subject)

# remove
subject.remove("Java")
print(subject)

# copy all items
subject2 = subject.copy()
print(subject2)

subject3 = list(subject)
print(subject3)

# get index by value
index = subject.index("Python")
print(index)

# clear all items
subject.clear()
print(subject)

# count
num = [10, 20, 4, 5, 4, 18, 4]
count = num.count(4)
print(count)

# delete an item
del num[1]
print(num)

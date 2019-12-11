
subject = ["C", "C++", "Java", "Python", "Android", "OS", "TOC"]

print(subject)
print(subject[0])
print(subject[2:])
print(subject[-1])
print(subject[-4:-1])

print(subject + ["Swift", 20])
print(subject * 3)

# join
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# another way
list1.extend(list2)
print(list1)

# create a new list using list constructor
list4 = list(("a", "ab", "abc", "abcd"))
print(list4)



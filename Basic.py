
students = (
    "Jayanta Biswas",
    "Joy",
    "Shibbir",
    "Maruf Hasan"
)

print(students)
print(students[1])

# students[1] = "Baky" # error
# print(students)

students = (
    "Jayanta Biswas",
    (10, 15, 20, 25),
    "Joy",
    "Shibbir",
    "Maruf Hasan"
)

print(students)
print(students[1])

print(students[2:])
print(students[-1])

# join
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

tup3 = tup1 + tup2
print(tup3)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# assignment
my_tuple = (3, 4.6, "dog")
print(my_tuple)

a, b, c = my_tuple
print(a)      # 3
print(b)      # 4.6
print(c)      # dog

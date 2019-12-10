
# for loop
names = ["Jayanta", "Shibbir", "Joy", "Sagor", "Rony", "Sadik", "Baky"]
for name in names:
    print(name)
print("Program end.")

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    print(x)
print("Program end.")

# Prints out 3,4,5
for x in range(3, 6):
    print(x)
print("Program end.")

# Prints out 3,5,7
for x in range(1, 10, 2):
    print(x)

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

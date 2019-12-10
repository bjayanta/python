
# nested for loop

# square
for row in range(5):
    for column in range(5):
        print("* ", end="")

    print("\r")

print("Program end.")

# triangle
for i in range(5):
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")

print("Program end.")



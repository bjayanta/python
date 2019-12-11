
# prob 1
print("Prob 1")
n = input("Enter a text of numbers: ")
# 10 20 30 40 ...

list = n.split()
sum = 0

for num in list:
    sum += int(num)

print("Sum of the given data is ", sum)


# prob 2
print("Prob 2")

numOfWords = 0
numOfLetters = 0
numOfDigits = 0

txt = input("Enter your text: ")

for x in txt:
    # convert to lower
    x = x.lower()

    if x >= 'a' and x <= 'z':
        numOfLetters += 1

    elif x >= '0' and x <= '9':
        numOfDigits += 1

    elif x == ' ':
        numOfWords += 1

print("Number of letters ", numOfLetters)
print("Number of digits ", numOfDigits)
print("Number of words ", numOfWords + 1)
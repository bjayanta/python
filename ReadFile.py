# open a file
data = open("data.txt", "r")

# is readable or writable
# print(data.readable())

# read
# txt = data.read()
# print(txt)

# size of char
# print(len(txt))

# read all text
# txt = data.readlines()
# txt = data.readlines()[1]
# print(txt)

for line in data:
    print(line)

# close a file
data.close()


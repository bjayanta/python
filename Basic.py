# type error
# num = input("Enter your number: ")
# result = 20 / num
# print(result)
# print("Done")

# zero(0) division error
# result = 20 / 0
# print(result)
# print("Done")

# index error
# txt = "Jayanta"
# print(txt[10])
# print("Done")

try:
    list = [20, 0, 30]
    result = list[0] / list[5]
    print(result)
    print("End")
except ZeroDivisionError:
    print("Dividing by zero is not possible!")
# except IndexError:
#     print("Index Error!")
finally:
    print("Successful!")


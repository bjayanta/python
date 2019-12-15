try:
    a = int(input("First number: "))
    b = int(input("Second number: "))

    result = a / b

    print(result)

except (ValueError, ZeroDivisionError):
    print("You have to insert incorrect input!")

finally:
    print("Thanks!")
# xargs
def student(*details):
    print(details[0])
    print(details)


student(101, "Jayanta", 3.75)  # tuple


# ex:
def add(*numbers):
    sum = 0

    for num in numbers:
        sum += num

    print(sum)


add(1, 5, 2, 3)


# xxargs
def human(**details):
    print(details["name"])
    print(details)


human(id=101, name="Jayanta")

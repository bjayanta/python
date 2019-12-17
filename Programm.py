class Triangle:
    base = ""
    height = ""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(f"Area of the triangle is: {0.5 * self.base * self.height}")


# create an object
t1 = Triangle(10, 20)
t1.area()

t2 = Triangle(20, 30)
t2.area()
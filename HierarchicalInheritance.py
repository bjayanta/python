class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am area method of shape class.")


class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of triangle is: ", area)


class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of rectangle is: ", area)


# object
triangle = Triangle(20, 30)
triangle.area()

rectangle = Rectangle(20, 30)
rectangle.area()
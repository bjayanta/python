class A:
    def display1(self):
        print("I am inside A class.")


class B(A):
    # display1()

    def display2(self):
        print("I am inside B class.")


class C(B):
    # display1()
    # display2()

    def display3(self):
        super().display1()
        super().display2()

        print("I am inside C class.")


# object
obj1 = C()
# obj1.display1()
# obj1.display2()
obj1.display3()

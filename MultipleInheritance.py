class A:
    def display(self):
        print("I am inside A class.")


class B():
    def display(self):
        print("I am inside B class.")


class C(B, A):
    # A -> display()
    # B -> display()

    pass

    # def display(self):
    #     print("I am inside C class.")


# object
obj = C()
obj.display()

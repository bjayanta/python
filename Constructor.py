class Student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


# create an object
robin = Student(101, 3.70)
robin.display()

# create an object
jb = Student(102, 3.70)
jb.display()
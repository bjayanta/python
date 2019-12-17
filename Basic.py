class Student:
    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


# create an object
robin = Student()
print(isinstance(robin, Student))

# robin.roll = 101 # variable
# robin.gpa = 3.70 # variable
robin.set_value(101, 3.70)

# print(f"Roll: {robin.roll}, GPA: {robin.gpa}")
robin.display()

# create an object
jb = Student()
print(isinstance(jb, Student))

# jb.roll = 102
# jb.gpa = 3.75
robin.set_value(101, 3.70)

# print(f"Roll: {jb.roll}, GPA: {jb.gpa}")
jb.display()
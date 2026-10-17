class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, "ke marks:", self.marks)

s1 = Student("Abhi", 85)
s1.show()   
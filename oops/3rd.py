class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name, "| Marks:", self.marks)

    def is_pass(self):
        return self.marks >= 33

s1 = Student("Rahul", 85)
s1.show()
print(s1.is_pass())
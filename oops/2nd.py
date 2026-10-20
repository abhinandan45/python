class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Rahul", 85)
s2 = Student("Priya", 92)

print(s1.name, s1.marks)
print(s2.name, s2.marks)
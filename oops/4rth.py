class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi,", self.name)

class Student(Person):
    def study(self):
        print(self.name, "is studying")

s = Student("Abhi")
s.greet()    # Person se mila
s.study()    # apna method
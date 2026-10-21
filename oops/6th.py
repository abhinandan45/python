class Animal:
    def sound(self):
        print("Koi awaaz")

class Dog(Animal):
    def sound(self):
        print("Bhau bhau")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.sound()
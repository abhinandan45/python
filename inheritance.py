class Animal:
    def sound(self):
        print("Koi awaaz")

class Dog(Animal):
    def sound(self):   # method overriding
        print("Bhow bhow")

d = Dog()
d.sound() 
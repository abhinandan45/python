'''1st'''

# class animal():
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species

# class dog(animal):
#     def __init__(self,name,species,breed):
#         super().__init__(name,species)
#         self.breed = breed

# Dog = dog('tommy','Canine', 'Golden Retriever')
# print(Dog.name,Dog.species,Dog.breed)

# =====================================================================================================================================
'''2nd'''

# class animal():
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species

# class dog(animal):
#     def __init__(self,name,species,breed):
#         super().__init__(name,species)
#         self.breed = breed

#     def __str__(self):
#         return f"name : {self.name}, species : {self.species}, breed : {self.breed}"

# Dog = dog("tommy","canien","golden retriver")
# print(Dog)

# =====================================================================================================================================
'''3rd'''

# class animal():
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species

# class dog(animal):
#     def __init__(self,name,species,breed):
#         super().__init__(name,species)
#         self.breed = breed
    
#     def bark(self):
#         print("woof woof!")

# Dog = dog("tommy","canien","golden retriver")
# Dog.bark()

# =====================================================================================================================================
'''4th'''

# class walker():
#     def walk(self):
#         print("walking......")

# class runner():
#     def run(self):
#         print("runnning......")

# class athlete(walker,runner):
#     pass

# Athlete = athlete()
# Athlete.run()
# Athlete.walk()

# =====================================================================================================================================
'''5th'''
 
# class father():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class child(father):
#     def __init__(self,name,age,surname,place):
#        super().__init__(name,age)
#        self.surname = surname
#        self.place = place

# son = child("abhi",17,"thakur","indore")
# print(son.name,son.age,son.surname,son.place)

# =====================================================================================================================================
'''6th'''

# class engine():
#     def __init__(self,fuel,power):
#         self.fuel = fuel
#         self.power = power

# class body():
#     def __init__(self,colour,seat,bodytype):
#         self.colour = colour
#         self.seat = seat
#         self.bodytype = bodytype

# class Car(engine,body):
#     def __init__(self,fuel,power,colour,seat,bodytype,brand):
#         engine.__init__(self,fuel,power)
#         body.__init__(self,colour,seat,bodytype)
#         self.brand = brand

# car = Car("petrol",120,"skyblue",5,"steel","tesla")
# print(f"fuel type of car : {car.fuel}")
# print(f"car horse power : {car.power}")
# print(f"colour of car : {car.colour}")
# print(f"seater : {car.seat}")
# print(f"car brand : {car.brand}")
# print(f"type of body : {car.bodytype}")

# =====================================================================================================================================
'''7th'''

# class grandfather:
#     def __init__(self, property):
#         self.property = property

# class father(grandfather):
#     def __init__(self, property, name):
#         super().__init__(property) 
#         self.name = name

# class son(father):
#     def __init__(self, property, name, surname):
#         super().__init__(property, name)
#         self.surname = surname

# beta = son(100, "Ankit", "Thakur")
# print(beta.name)

# =====================================================================================================================================
'''8th'''

# class A():
#     def show(self):
#         print("a sow method.")

# class B(A):
#     def show(self):
#         print("b show method")
        
# class C(A):
#     def show(self):
#         print("c show method")
    
# class D(B,C):
#         pass

# d = D()
# d.show()

# =====================================================================================================================================
'''9th'''

# class person():
#     def __init__(self,name):
#         self.name = name

# class Employee():
#     def __init__(self,em_id):
#         self.em_id = em_id

# class manager(person,Employee):
#     def __init__(self,name,em_id):
#         super().__init__(name)
#         Employee.__init__(self,em_id)

# m = manager("abhi","E123")
# print(m.name,m.em_id)

# =====================================================================================================================================
'''10th'''

# class vehicle:
#     def start(self):
#         print("vehicle starting.....")

# class car(vehicle):
#     def start(self):
#         print("car starting.....")
#         super().start()
    
# c = car()
# c.start()

# =====================================================================================================================================
'''11th'''

# class flyer():
#     def fly(self):
#         print("flying")

# class swimmer():
#     def swim(self):
#         print("swimming")

# class superhero(flyer,swimmer):
#     pass

# s = superhero()
# s.fly()
# s.swim()

# =====================================================================================================================================
'''12th'''

# class base1():
#     def __init__(self,a):
#         self.a = a

# class base2():
#     def __init__(self,b):
#         self.b = b

# class derived(base1,base2):
#     def __init__(self,a,b,c):
#         super().__init__(a)
#         base2.__init__(self,b)
#         self.c = c

# d = derived(1,2,3)
# print(d.a,d.b,d.c)


# =====================================================================================================================================
'''13th'''

# class animal:
#     pass

# class cat(animal):
#     pass

# a = animal()
# c = cat()

# print(isinstance(a,animal))
# print(isinstance(a,cat))
# print(isinstance(c,cat))
# print(isinstance(c,animal))

# =====================================================================================================================================
'''14th'''

# class bird:
#     def speak(self):
#         pass

# class parrot(bird):
#     def speak(self):
#         print("Parrot says : Squawk!")

# class Penguin(bird):
#     def speak(self):
#         print("Penguin says : honk!")

# class crow(bird):
#     def speak(self):
#         print("crow says : caw caw!")

# class eagle(bird):
#     def speak(self):
#         print("eagle says : viuuuu")

# b = [parrot(),Penguin(),crow(),eagle()]
# for bird in b:
#     bird.speak()

# =====================================================================================================================================
'''15th'''

# class device:
#     def __init__(self,brand):
#         self.brand = brand

# class phone(device):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model = model

# class Camera:
#     def __init__(self,resolution):
#         self.resolution = resolution

# class Smartphone(phone,Camera):
#     def __init__(self,brand,model,resolution):
#         super().__init__(brand,model)
#         Camera.__init__(self,resolution)

# s = Smartphone("Apple","iphone14","12 mp")
# print(f"brand name : {s.brand}")
# print(f"model name : {s.model}")
# print(f"resolution : {s.resolution}")

# =====================================================================================================================================


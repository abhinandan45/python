# account details

# class Account():
#     bank = "bank of baroda"

#     def __init__(self,account_holder,balance=0):
#         self.account_holder = account_holder
#         self.balance = balance

#     def withdraw(self,amount):
#         if amount > 0:
#             self.balance -= amount
#             print(f"deposited : {amount:.2f}")
#             print(f"account balance : {self.balance:.2f}")
#         else:
#             print("Invalid deposit amount. Please enter a positive value.")

#     def deposit(self,amount):
#         if 0 < amount <= self.balance:
#             self.balance += amount
#             print(f"withdraw : {amount:.2f}")
#             print(f"account balance : {self.balance:.2f}")

#     def get_balance(self):
#         return self.balance

# account = Account("abhinandan",10000)
# print(f"bank name : {account.bank}")
# print(f"account holder name : {account.account_holder}")
# print(f"account balance : {account.balance}")
# account.deposit(1000)
# account.withdraw(10000)
# print(f"final balance : {account.get_balance()}")


# ------------------------------------------------------------------------------------------------------------------------------------------

# class car():

#     def __init__(self,modelname,year,price):
#         self.modelname = modelname
#         self.year = year
#         self.price = price

#     def price_increse(self,amount):
#         self.price += amount
#         return self.price
        
# kia = car("ford",2012,100000)
# print(kia.price)
# print(kia.modelname)
# print(kia.year)
# total = kia.price_increse(1000)
# print(total)

#``===================================================================================================================================``
'''abstract_method'''

# from abc import ABC,abstractmethod
# class car(ABC):
#     def __init__(self,brand,yearm,hp,price):
#         self.brand = brand
#         self.yearm = yearm
#         self.hp = hp
#         self.price = price

#     @abstractmethod
#     def price_inc(self):
#         pass

# class supercar(car):
#     def price_inc(self):
#         self.price = int(self.price*1.4)

# honda = supercar("tata",2024,240,1000000)
# honda.price_inc()
# print(honda.price)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# from abc import ABC,abstractmethod

# class bike(ABC):
#     def __init__(self,model,brand,price):
#         self.model = model
#         self.brand = brand
#         self.price = price

#     @abstractmethod
#     def price_inc(self):
#         pass

#     @abstractmethod
#     def brand_name(self):
#         pass

# class superbike(bike):
#     def price_inc(self):
#         self.price = int(self.price + 200000)
    
#     def brand_name(self):
#         self.brand = "TATA"

# b = superbike(2009,"HONDA",20000)
# b.price_inc()
# b.brand_name()
# print(b.price)
# print(b.brand)

# ``===================================================================================================================================``

# from abc import ABC,abstractmethod

# class student(ABC):
#     def __init__(self,name,age,cource,rollno):
#         self.name = name
#         self.age = age
#         self.cource = cource
#         self.rollno = rollno

#     @abstractmethod
#     def your_name(self):
#         pass

#     @abstractmethod
#     def your_age(self):
#         pass

# class std(student):
#     def __init__(self,name,age,cource,rollno):
#         super().__init__(name,age,cource,rollno)

#     def your_name(self):
#         self.name = "rohit sharma"

#     def your_age(self):
#         self.age = 17

# s = std("Hitman",37,"ds",121212)
# s.your_age()
# # s.your_name()
# print(f"name : {s.name}")
# print(f"age : {s.age}")

# print(f"name : {s.name}")
# print(f"age : {s.age}")




# class person:
#     def __init__(self):
#         self.name = "abhi"
#         self.age = 17
#         self.place = "indore"

#     def info(self):
#         return f"name : {self.name}, age : {self.age}, place : {self.place}"

# k = person()
# print(k.info())
# print(k.name)




# class car:
#     def __init__(self,_brand_,_model_):
#         self._brand_ = _brand_
#         self._model_ = _model_

# class electric_car(car):
#     def __init__(self,_brand_,_model_,_battery_capacity_):
#         super().__init__(_brand_,_model_)
#         self._battery_capacity_ = _battery_capacity_

# e = electric_car("TATA",2019,"70")
# print(e._brand_,e._model_,e._battery_capacity_)
        

# class Car:
#     def __init__(self, modelname, yearm, price):
#         self.modelname = modelname
#         self._yearm_ = yearm
#         self._price_ = price

#     def get_price(self):  
#         return self._price_

# class supercar(Car):
#     def __init__(self, modelname, yearm, price, brand):
#         super().__init__(modelname, yearm, price)
#         self.brand = brand

# s = supercar("harrier", 2000, 200000, "TATA")
# print(s.modelname)  
# print(s.brand)     
# print(s.get_price())  



# class Car:
#     def __init__(self, modelname, yearm, price):
#         self.modelname = modelname
#         self._yearm_ = yearm
#         self._price_ = price

#     def get_price(self):  
#         return self._price_

# class supercar(Car):
#     def __init__(self, modelname, yearm, price, brand):
#         super().__init__(modelname, yearm, price)
#         self.brand = brand

# s = supercar("harrier", 2000, 200000, "TATA")
# print(s.modelname)  
# print(s.brand)     
# print(s.get_price())  


# class std():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name
    
#     def set_name(self,name):
#         self.name = name

# s = std("abhi",17)
# print(s.get_name())
# # s.set_name("ram")
# # print(s.get_name())
# print(s.age)





# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     # def __str__(self):
#     #     return f"{self.name},{self.age} years old"

#     def __repr__(self):
#         return f"Person(name={self.name},age={self.age})"

# person=Person("Shiv",27)
# print(person)
# print(repr(person))
# print(person)


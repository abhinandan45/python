'''1st'''

# class car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year

# my_car = car("bmw","camry",2006)
# print(f"company : {my_car.make}")
# print(f"model name : {my_car.model}")
# print(f"year of manufacturing : {my_car.year}")

# ====================================================================================================================================
'''2nd'''

# class car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def start_engine(self):
#         print("the engine has started.")

# my_car = car("bmw","camry",2006)
# print(f"company : {my_car.make}")
# print(f"model name : {my_car.model}")
# print(f"year of manufacturing : {my_car.year}")
# my_car.start_engine()

# ====================================================================================================================================
'''3rd'''

# class student():

#     def __init__(self,name,age,subject):
#         self.name = name
#         self.age = age
#         self.subject = subject
    
# s1 = student("abhi",17,"ds")
# print(f"student name : {s1.name}")

# ====================================================================================================================================
'''4rth'''

# class Account():
#     bank = "bank of baroda"

#     def __init__(self,account_holder,balance=0):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"deposit : {amount:.2f}")
#             print(f"total balance : {self.balance:.2f}")
    
#     def withdraw(self,amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"withdraw : {amount:.2f}")
#             print(f"total balance : {self.balance:.2f}")
        
#         else:
#             print("Insufficient balance!")


#     def acc_info(self):
#         print(f"account holder name : {self.account_holder}")
#         print(f"account balance : {self.balance:.2f}")

# account = Account("abhinandan",10000)
# print(f"bank name : {account.bank}")
# account.acc_info()
# account.deposit(10000)
# account.withdraw(20000)

# ====================================================================================================================================
'''5th'''

# class person():
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age

# class Employee(person):
#     def __init__(self,name,age,employee_id):
#         super().__init__(name,age)
#         self.employee_id = employee_id

# employee = Employee("abhi",17,"E17")
# print(employee.name,employee.age,employee.employee_id)

# ====================================================================================================================================
'''6th'''

# class person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Employee(person):
#     def __init__(self,name,age,employee_id):
#         super().__init__(name,age)
#         self.employee_id = employee_id

#     def __str__(self):
#         return f"Employee (name : {self.name}, age : {self.age}, employee id : {self.employee_id})"

# employee = Employee("abhi",17,"E123")
# print(employee)

# ====================================================================================================================================
'''7th'''

# class Address():
#     def __init__(self,street,city,zipcode):
#         self.street = street
#         self.city = city
#         self.zipcode = zipcode

# class Person():
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address

# address = Address("123 Main St","indore",1001)
# person = Person("abhi","17",address)
# print(person.address.street,person.address.city,person.address.zipcode)

# ====================================================================================================================================
'''8th'''

# class counter():
#     count =  0

#     def __init__(self):
#         counter.count += 1

#     @classmethod
#     def get_count(cls):
#         return cls.count

# c1 = counter()
# c2 = counter()
# c3 = counter()
# c4 = counter()
# print(counter.get_count())

# ====================================================================================================================================
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
'''1th'''                            '''''''senario based solution'''''''''

# class library:
#     def __init__(self):
#         self.books = []

#     def add_book(self,bookname):
#         if bookname not in self.books:
#             self.books.append(bookname)
#             print(f"{bookname} book add in the library")

#     def remove_book(self,bookname):
#         if bookname in self.books:
#             self.books.remove(bookname)
#             print(f"{bookname} book remove")

#     def dis_book(self):
#         print(f"all books : {self.books}")

# b = library()

# b.add_book("hindi")
# b.add_book("english")
# b.add_book("science")
# b.remove_book("hindi")
# b.dis_book()

# =====================================================================================================================================
'''2nd'''

# class Employee:
#     def __init__(self, name, age, salary, percent):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.percent = percent

#     def bonus(self):
#         return self.salary * (self.percent / 100)

#     def total_salary(self):
#         return self.salary + self.bonus()

# e = Employee("Abhi", 24, 150000, 20)

# print(f"Name: {e.name}")
# print(f"Age: {e.age}")
# print(f"Salary: {e.salary}")
# print(f"Bonus: {e.bonus()}")
# print(f"Total Salary: {e.total_salary()}")

# =====================================================================================================================================
'''3rd'''

# class vehicle():
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price

# class car(vehicle):
#     def car_info(self):
#         return f"brand : {self.brand} , price : {self.price}"
    
# class bike(vehicle):
#     def bike_info(self):
#         return f"brand : {self.brand} , price : {self.price}"
    
# c = car("TATA",2000000)
# b = bike("HONDA",120000)

# print(f"car : {c.car_info()}")
# print(f"bike : {b.bike_info()}")

# =====================================================================================================================================
'''4rth'''

# class counter:
#     count = 0

#     def __init__(self):
#         counter.count += 1

# a = counter()
# b = counter()
# c = counter()
# d = counter()
# print(counter.count)

# =====================================================================================================================================
'''5th'''

# class Team:
#     def __init__(self):
#         self.employees = [] 

#     def add_employee(self, name, age):
#         self.employees.append((name, age))
#         print(f"{name} added to the team.")

#     def remove_employee(self, name):
#         for employee in self.employees:
#             if employee[0] == name:
#                 self.employees.remove(employee)
#                 print(f"{name} removed from the team.")
#                 return
#         print(f"{name} not found.")

#     def calculate_average_age(self):
#         if not self.employees:
#             return 0
#         total_age = sum(age for _, age in self.employees)
#         return total_age / len(self.employees)

#     def display_team(self):
#         if not self.employees:
#             print("No employees in the team.")
#         else:
#             for name, age in self.employees:
#                 print(f"name : {name}, Age: {age}")


# team = Team()
# team.add_employee("Alice", 30)
# team.add_employee("Bob", 25)
# team.add_employee("Charlie", 35)
# team.add_employee("annu", 23)
# team.add_employee("vishu", 24)

# print("\nTeam Members:")
# team.display_team()

# average_age = team.calculate_average_age()
# print(f"\nAverage Age: {average_age:.2f}")

# team.remove_employee("Bob")
# print("\nTeam Members After Removal:")
# team.display_team()

# average_age = team.calculate_average_age()
# print(f"\nAverage Age After Removal: {average_age:.2f}")

# =====================================================================================================================================
'''6th'''

# class calculator:
#     def add(self,a,b):
#         return a + b
    
#     def subtract(self,a,b):
#         return a - b
    
#     def multiply(self,a,b):
#         return a * b
    
#     def divide(self,a,b):
#         try:
#           return a / b
#         except Exception as e:
#             print(e,"zero division not allowed")

# a = calculator()
# print(a.divide(2,1))
# print(a.subtract(100,30))
# print(a.multiply(10,2))
# print(a.add(10,29))

# =====================================================================================================================================
'''7th'''

# class onlineshopping:
#     def __init__(self, TAX_rate=0.1):
#         self.order = []
#         self.TAX_rate = TAX_rate

#     def add_orders(self, item, price, quantity):
#         self.order.append({"item": item, "price": price, "quantity": quantity})

#     def cal_total_price(self):
#         subtotal = sum(order["price"] * order["quantity"] for order in self.order)
#         tax = subtotal * self.TAX_rate
#         return subtotal + tax

#     def display_orders(self):
#         return self.order

# o = onlineshopping(TAX_rate=0.28)
# o.add_orders("laptop", 100000, 5)

# print("Orders:", o.display_orders())
# print("Total Price:", o.cal_total_price())

# =====================================================================================================================================

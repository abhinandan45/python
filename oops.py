# class student:
#     name = "abhi"
#     age = 17
#     place = "indore"
#     height = 5.6

# s1 = student()
# print(s1.name)

# s2 = student()
# print(s2.age)

# s1 = student()
# print(s1.place)

# s1 = student()
# print(s1.height)


# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

# s1 = student("abhinandan",17,97)
# print(s1.name,s1.marks)
        
# s2 = student("shivraj",17,95)
# print(s2.name,s2.marks)



# class coaching():
#     coaching_name = "placement adda"
#     def __init__(self,name,cource):
#         self.name = name
#         self.cource = cource
        
# s1 = coaching("abhinandan","data science")
# print(s1.name,s1.cource)
# print(s1.coaching_name)

# s2 = coaching("karan","data science")
# print(s1.name,s1.cource)
# print(s2.coaching_name)


# class student():

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome,",self.name,self.marks)
    
#     def get_marks(self):
#         return self.marks

# s1 = student("abhinandan",97)
# s1.welcome()
# print(s1.get_marks())

# class student():
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name,"your avg score is : ",sum/3)

# s1 = student("abhinandan",[95,96,97])
# s1.get_avg()

# s1.name = "shivraj"
# s1.get_avg()






# class  student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
# s1 = student("abhi",17)
# print(s1.name,":",s1.age)

# s2 = student("shiv",17)
# print(s2.name,":",s2.age)


# class school():
#     school_name = "s.v.m dewas"

#     def __init__(self,name,age,cource):
#         self.name = name
#         self.age = age
#         self.cource = cource

# s1 = school("abhi",17,"pcm")
# print(s1.school_name)
# print(s1.name,s1.age,s1.cource)

# s2 = school("shiv",17,"pcb")
# print(s2.school_name)
# print(s2.name,s2.age,s2.cource






# class Account():
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ₹ {amount:.2f}.")
#             print(f"Account Balance: ₹ {self.balance:.2f}")
#         else:
#             print("Invalid deposit amount. Please enter a positive value.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew ₹ {amount:.2f}.")
#             print(f"Account Balance: ₹ {self.balance:.2f}")
#         else:
#             print("Invalid withdrawal amount or insufficient balance.")

#     def get_balance(self):
#         return self.balance

# account = Account("Rohit Sharma", 5000)  
# print(f"Account Holder: {account.account_holder}")        
# print(f"Account Balance: ₹ {account.get_balance():.2f}")   
# account.deposit(1500)                                       
# account.withdraw(2000)                                                                    
# print(f"Final Balance: ₹ {account.get_balance():.2f}")      







# class bike():
#     company = "honda"
#     def __init__(self,name,model,price):
#         self.name = name
#         self.model = model
#         self.price = price

# Bike = bike("splendor",2009,20000)
# print(Bike.company)
# print(Bike.name)
# print(Bike.model)
# print(Bike.price)



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



# class person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def my_function(self):
#         print(f"hello my name is {self.name}")
#         print(f"and my age is {self.age}")

# s1 = person("abhi",17)
# s1.my_function()




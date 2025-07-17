'''1st'''

# num = int(input("enter number : "))

# if num > 10:
#     print(num,"is greater than 10")

# else:
#     print(num,"is less than 10")

# ----------------------------------------------------------------------------------------------------
'''2nd'''

# num = int(input("enter a number : "))

# if num % 2 == 0:
#     print(num,"is even number")

# else:
#     print(num,"is odd number")

# ----------------------------------------------------------------------------------------------------
'''3rd'''

# num = int(input("enter a number : "))

# if num > 0:
#     print(num,"is positive number")

# elif num < 0:
#     print(num,"is negative number")

# else:
#     print(num,"is zero")

# ----------------------------------------------------------------------------------------------------
'''4rth'''

# num = int(input("enter your percentage(%) = "))

# if num >= 90:
#     print ("A grade")

# elif 80<= num < 90:
#     print("B grade")

# else:
#     print("you failed")

# ----------------------------------------------------------------------------------------------------
'''5th'''

# year = int(input("enter year : "))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(year,"is a leap year")

# else:
#     print(year,"is not leap year")

# ----------------------------------------------------------------------------------------------------
'''6th'''

# num = int(input("enter number : "))
# num1 = int(input("enter number : "))
# num2 = int(input("enter number : "))

# if num1>num2 and num1>num:
#     print(num1,"is largest number")

# elif num>num1 and num>num2:
#     print(num,"is largest number")

# else:
#     print(num2,"is largest number")

# ----------------------------------------------------------------------------------------------------
'''7th'''

# num = int(input("enter number : "))

# if num % 3 == 0 and num % 5 ==0:
#     print(num,"is divisible by 3 and 5")

# else:
#     print(num,"is not devisible by 3 and 5")

# ----------------------------------------------------------------------------------------------------
'''8th'''

# str = input("enter a sting : ")

# if "python" in str:
#     print("found")

# else:
#     print("not found")

# ----------------------------------------------------------------------------------------------------
'''9th'''

# num = int(input("enter a number : "))

# if num < 10:
#     print(num,"is small.")

# elif 10 <= num <100:
#     print(num,"is medium.")

# else:
#     print(num,"is large.")

# ----------------------------------------------------------------------------------------------------
'''10th'''

# a, b, c = 5, 7,6

# if a == b == c:
#     print("Equilateral Triangle")

# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")

# else:
#     print("Scalene Triangle")

# ----------------------------------------------------------------------------------------------------
'''11th'''

# password = input("enter your password : ")

# if len(password) <= 8:
#     print("at least 8 characters long.")

# else:
#     print("valid password.")

# ----------------------------------------------------------------------------------------------------
'''12th'''

# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
# c = float(input("Enter the third number: "))
# d = float(input("Enter the fourth number: "))

# smallest = a

# if b < smallest:
#     smallest = b

# if c < smallest:
#     smallest = c

# if d < smallest:
#     smallest = d

# print("The smallest number is:", smallest)

# ----------------------------------------------------------------------------------------------------
'''13th'''

# num = int(input("enter a number : "))

# if num > 1:
#     for i in range(2,num):
#         if num % i ==0:
#             print(num,"is not a prime number.")
#             break
#     else:
#         print(num,"is a prime")

# ----------------------------------------------------------------------------------------------------
'''14th'''

# num = int(input("enter a number : "))
# num1 = int(input("enter a number : "))

# if num == num1:
#     print("equal")

# elif num > num1:
#     print(num,"is big")

# else:
#     print(num1,"is big")

# ----------------------------------------------------------------------------------------------------
'''15th'''

# num = (input("enter a number : "))

# if num == num[::-1]:
#     print(num,"is palindrom")

# else:
#     print(num,"is not palindrom")

# ----------------------------------------------------------------------------------------------------
'''16th'''

# num =  (input("enter a number : "))

# if len(num) < 6:
#     print("weak password")

# elif 6<= len(num) <= 8:
#     print("medium password")

# else:
#     print("strong password")

# ----------------------------------------------------------------------------------------------------
'''17th'''

# msg = input("ente text : ")

# vowels = "aeiouAEIOU"

# if msg.lower() in "aeiouAEIOU":
#     print(msg,"vowels")

# else:
#     print(msg,"its comsonants")

# ----------------------------------------------------------------------------------------------------
'''18th'''

# def is_fibonacci(n):
#         a, b = 0, 1
#         while b < n:
#             a, b = b, a + b
#         return b == n or n == 0

# num = 3
# if is_fibonacci(num):
#     print("Fibonacci number")
# else:
#     print("Not a Fibonacci number")

# ----------------------------------------------------------------------------------------------------
'''19th'''

# marks = int(input("enter your marks : "))

# if marks >= 90:
#     print("A grade")

# elif 75<= marks <=89:
#     print("first class")

# elif 60<= marks <=74:
#     print("second class")

# else:
#     print("fail")

# ----------------------------------------------------------------------------------------------------
'''20th'''

# age = int(input("enter age = "))

# if age < 12:
#     print("child")

# elif 12<= age <=19:
#     print("teen")

# elif 19< age <=64:
#     print("adult")

# else:
#     print("senior")

# ----------------------------------------------------------------------------------------------------

'''1st'''

# for i in range(1,100):
#     print(i)

# ---------------------------------------------------------------------
'''2nd'''

# num = int(input("enter number : "))
# sum = 0

# for i in range(1,num+1):
#     sum += i

# print(sum)

# ---------------------------------------------------------------------
'''3rd'''

# num = int(input("enter number : "))
# fac = 1

# for i in range(1,num+1):
#     fac *= i

# print(fac)

# ---------------------------------------------------------------------
'''4rth'''

# num = 2

# while num < 51:
#     print(num)
#     num += 2

# ---------------------------------------------------------------------
'''5th'''

# str = input("enter msg = ")

# count = 0
# vowels = "aeiouAEIOU"

# for char in str:
#     if char in vowels:
#         count += 1

# print(count)

# ---------------------------------------------------------------------
'''6th'''

# str = input("enter message = ")

# char = " "

# for i in str:
#     char = i + char
# print(char)

# ---------------------------------------------------------------------
'''7th'''

# num = int(input("enter number = "))

# for i in range(1,num+1):
#     print(num,"*",i,"=",num*i)

# ------------------------------------------------------------

'''8th'''

# num = int(input("enter number : "))

# for i in range(num,0,-1):
#     print(i)

''''''''''''
# num = int(input("enter number : "))

# while num > 0:
#     print(num)
#     num -= 1

# ------------------------------------------------------------------
'''9th'''

# num = int(input("enter number : "))
# sum = 0

# for i in range(num,0,-2):
#     sum = sum + i
# print(sum)

# ------------------------------------------------------------------
'''10th'''

# num = int(input("enter number : "))

# count = 0

# while num != 0:
#     num //= 10
#     count += 1

# print(count) 

# ------------------------------------------------------------------
'''11th'''

# num = int(input("enter number: "))

# sum_of_digits = 0

# while num > 0:
#     digit = num % 10
#     sum_of_digits += digit
#     num = num //10

# print("sum of digits = ",sum_of_digits)


# ------------------------------------------------------------------
'''12th'''

# def is_prime(number):
#     if number <=0:
#         return False
#     for i in range(2,number):
#         if number % i == 0:
#             return False
#     return True

# number = int(input("enter number = "))
# if is_prime(number):
#     print(number,"is a prime number.")

# else:
#     print(number,"is not a prime number")

# ------------------------------------------------------------------
'''13th'''

# n = int(input("enter a number: "))


# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def print_primes(n):
#     for num in range(2, n + 1):
#         if is_prime(num):
#             print(num, end=", ")

# print_primes(n)

# ------------------------------------------------------------------
'''14th'''

# def power(x, y):
#     result = 1
#     for _ in range(y):
#         result *= x
#     return result

# x = int(input("Enter the value of x: "))
# y = int(input("Enter the value of y: "))


# print(f"{x} raised to the power of {y} is:, {power(x,y)}")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# x = int(input("Enter the base (x): "))
# y = int(input("Enter the exponent (y): "))

# result = 1

# for _ in range(abs(y)):
#     result *= x

# if y < 0:
#     result = 1 / result

# print(f"{x} raised to the power of {y} is: {result}")

# ------------------------------------------------------------------
'''15th'''

# n = int(input("Enter the number of terms: "))

# a,b = 0,1
# if n <= 0:
#     print("Number of terms must be a positive integer.")

# else:
#     print("fibonacci sequence :")
#     for _ in range(n):
#         print(a, end=" ")
#         a,b = b,a+b

# ------------------------------------------------------------------
'''16th'''

# string = input("enter a string : ")

# for _ in string:
#     if string == string[::-1]:
#         print("this is a palindrome.")
#     break
# else:
#     print("this is not a palindrome")

''''''''''''

# def is_palindrome(str):
#     if str == str[::-1]:
#         print("this is a palindrome")
#     else:
#         print("this is not a palindrome")

# str = input("enter str : ")
# is_palindrome(str)


# ------------------------------------------------------------------
'''17th'''

# number = [1,3,2,6,4,9,6,3,5,7,8,99]

# max_number = number[0]
# min_number = number[0]

# for num in number:
#     if num > max_number:
#        max_number = num

#     if num < min_number:
#         min_number = num

# print("maximum number: ",max_number)
# print("minimum number:",min_number)

# ------------------------------------------------------------------
'''18th'''

# n = int(input("enter number = "))

# sum_of_odds = 0

# for i in range(1,n+1):
#     if i % 2 != 0:
#         sum_of_odds += i
    
# print("sum of all odd numbers up to",n,"is",sum_of_odds)

# ------------------------------------------------------------------
'''19th'''

# n = int(input("enter the number of rows : "))

# for i in range(1,n+1):

#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# -------------------------------------------------------------------
'''20th'''

# input_string = input("Enter a string: ")


# char_frequency = {}

# for char in input_string:
#     if char in char_frequency:
#         char_frequency[char] += 1  
#     else:
#         char_frequency[char] = 1  


# print("Character frequencies:")
# for char, frequency in char_frequency.items():
#     print(f"'{char}': {frequency}")

''''''''''''''''''''''''''''''''

# def count_character_frequency(string):
#     frequency = {}  
    
#     for char in string:  
#         if char in frequency: 
#             frequency[char] += 1
#         else:
#             frequency[char] = 1 
    
#     for char, freq in frequency.items():  
#         print(f"'{char}' occurs {freq} times.")

# 
# string = input("Enter a string: ")
# count_character_frequency(string)

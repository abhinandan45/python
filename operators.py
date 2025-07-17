'''arithmetic'''

# a = 10
# b = 5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# print(a//b) 

# ------------------------------------------------------------------------------------------------------------------------------
'''assignment'''

# a = 20
# a += 10
# print(a)

# a = 20
# a -= 10
# print(a)

# a = 20
# a *= 10
# print(a)

# a = 20
# a /= 10
# print(a)

# a = 20
# a %= 10
# print(a)

a = 20
a /= 10
print(a)

# a = 20
# a **= 2
# print(a)

# ------------------------------------------------------------------------------------------------------------------------------
'''logical'''

# a = 10
# b = 12
# print(a<b and b==a)

# a = 10
# b = 12
# print(a<b or b!=a)

# a = 10
# b = 12
# print(not(a<b and b!=a))


# ------------------------------------------------------------------------------------------------------------------------------
'''bitwise'''

# a = 110
# b = 1050
# print(a & b)

# a = 110
# b = 1050
# print(a | b)

# a = 110
# b = 1050
# print(a ^ b)

# ------------------------------------------------------------------------------------------------------------------------------



'''''''''''''''''''''question solution'''''''''''''''''''''''''''

'''1st'''

# num1 = int(input("enter number : "))
# num2 = int(input("enter number : "))

# def add_number(num1,num2):
#     return num1 + num2

# print(add_number(num1,num2))

# -----------------------------------------
'''2nd'''

# num1 = int(input("enter number : "))
# num2 = int(input("enter number : "))

# def subtract_number(num1,num2):
#      return num1 - num2

# print(subtract_number(num1,num2))

# -----------------------------------------
'''3rd'''

# def multiply(a,b):
#     negative = False

#     if a < 0 and b > 0 or a > 0 and b < 0:
#         negative = True

#     a = abs(a)
#     b = abs(b)

#     result = 0

#     for _ in range(b):
#         result += a

#     return -result if negative else result

# print(multiply(3,5))

# -----------------------------------------
'''4rth'''




# def divide(a, b):
#     if b == 0:
#         return "Division by zero is not allowed."

#     quotient = a // b  
#     remainder = a % b  

#     return quotient, remainder

# a = 10
# b = 3
# quotient, remainder = divide(a, b)
# print(f"Quotient: {quotient}, Remainder: {remainder}")

# -----------------------------------------
'''5th'''

# def square(a,b):
#     return a**2

# a = 5
# b = 2
# result = square(a,b)
# print(f"the square of {a} = {result}")

# -----------------------------------------
'''6th'''

# def square(a,b):
#     return a**3

# a = 5
# b = 2
# result = square(a,b)
# print(f"the cube of {a} = {result}")

# -----------------------------------------
'''7th'''

# def area_of_rectangle(length,width):
#     a = length * width
#     return a

# length = 12
# width = 15
# result = area_of_rectangle(length,width)
# print("area of rectangle is : ",result)

# -----------------------------------------
'''8th'''

# def minuts_hours(minuts):
#     hours = minuts // 60
#     minut = minuts % 60

#     print("total minuts" ,minuts, " = ", hours,":", minut)

# minuts_hours(100)

# -----------------------------------------
'''9th'''

# def interest(principle,rate,time):

#     simple_interest = (principle*rate*time)/100
#     print("simple interest = ",simple_interest)
#     print("total amount = ",simple_interest+principle)


# principle = float(input("enter principal : "))
# rate = float(input("enter rate : "))
# time = float(input("enter time : "))

# interest(principle,rate,time) 

# -----------------------------------------
'''10th'''

# fehrenheit = float(input("enter the value in fehrenheit = "))

# def convert_to_celsius(fehrenheit):
#     celsius = (fehrenheit-32)*5/9
#     print(f"f = {fehrenheit} in c = {celsius:.2f}")

# convert_to_celsius(fehrenheit)

# -----------------------------------------
'''11th'''

# import math

# def cal_distance(x1,y1,x2,y2):
#     return math.sqrt(x2-x1)**2 + (y2-y1)**2

# x1 = float(input("enter the value of (x1) = "))
# y1 = float(input("enter the value of (y1) = "))
# x2 = float(input("enter the value of (x2) = "))
# y2 = float(input("enter the value of (y2) = "))

# distance = cal_distance(x1,y1,x2,y2)
# print("distance between two point on a plane is = ",distance)

# -----------------------------------------
'''12th'''

# import math

# def cal_cylinder_volume(radius,height):
#     return math.pi* radius**2*height

# radius = float(input("Enter the radius of the cylinder: "))
# height = float(input("Enter the height of the cylinder: "))

# volume = cal_cylinder_volume(radius,height)
# print(f"the volume of cylinder is : {volume:.2f} ")

# -----------------------------------------
'''13th'''

# import math

# def cal_area_of_triangle(base,height):
#     return 0.5*base*height

# base = float(input("enter base of triangle = "))
# height = float(input("enter the height of triangle = "))

# area = cal_area_of_triangle(base,height)

# print("area of triangle is : ",area)

# ------------------------------------------
'''14th'''

# import math

# def speed(distance,time):
#     if time == 0:
#         return "time can not be zero"
#     return distance/time

# distance = float(input("enter the distance in km : "))
# time = float(input("enter the time in hours :"))

# total = speed(distance,time)
# print("speed = ",total)

# ------------------------------------------
'''15th'''

# import math

# def circle(radius):
#     return math.pi * 2 * radius

# radius = float(input("enter the radius of circle : "))
# result = circle(radius)
# print(f"the perimeter of a circle is : {result:.2f}")

# ------------------------------------------
'''16th'''

# def product(number):
#     total = 1
#     for num in number:
#         total *= num
#     return total

# number = [1,2,3,4,5]
# result = product(number)
# print(result)

# ------------------------------------------
'''17th'''

# def sum_of_squares(n):
#     return n * (n + 1) * (2 * n + 1) // 6

# n = 5  
# result = sum_of_squares(n)
# print(f"The sum of squares of numbers from 1 to {n} is {result}")

# ------------------------------------------
'''18th'''

# import math

# def radians(degree):
#     return degree*math.pi/180

# degree = float(input("enter degrees = "))
# cal = radians(degree)
# print(f"{degree} is = {cal:.2f} radians")

# ------------------------------------------
'''19th'''

# def avg(number):
#     return sum(number)/len(number)

# number = [1,2,3,4]
# total = avg(number)
# print(total)

# ------------------------------------------
'''20th'''

# days = int(input("enter days : "))

# def convert_days(days):

#     years = days // 365
#     day = days % 365
#     weeks = day // 7
#     dayss = day % 7

#     print(f"total days {days} , years {years} , weeks {weeks} , days {dayss}")

# convert_days(days)

# ------------------------------------------
'''21th'''

# def is_equal(num,num1):
#     if num == num1:
#         print(num,"and",num1,"are equal")
#     else:
#         print(num,"and",num1,"are not equal")

# is_equal(10,10)
# is_equal(20,19)

# ------------------------------------------
'''22th'''

# def is_larger(a,b):
#     if a > b:
#         print(a,"is large")
#     else:
#         print(b,"is large")

# is_larger(10,20)
# is_larger(20,21)

# ------------------------------------------
'''23th'''

# def is_larger(a,b):
#     if a > b:
#         print(a,"is larger than ",b)
#     elif a < b :
#         print(b,"is larger than ",a)
#     else:
#         print(a, "and", b ,"are equal")

# is_larger(10,20)
# is_larger(20,21)
# is_larger(10,10)

# ------------------------------------------
'''24th'''

# def is_between(a,b,c):
#     if a > b and a < c or a < b and a > c:
#         print(a,"is between")

#     elif b > a and b < c or b < a and b > c:
#         print(b,"is between")

#     else:
#         print(c,"is between")
    
# is_between(10,20,30)
# is_between(20,40,30)
# is_between(10,5,15)

# ------------------------------------------
'''25th'''

# def is_greater_than(str):
#     if len(str) >= 5:
#         print(f"length of {str} is greater than 5")
    
#     else:
#         print(f"length of {str} is less than 5")

# is_greater_than("abhinandan")
# is_greater_than("ctal")
# is_greater_than("shivraj")
# is_greater_than("shiv")
# is_greater_than("abhii")

# ------------------------------------------
'''26th'''

# def is_uppercase(char):
#     if char == char.upper():
#         print("char is uppercase")

#     else:
#         print("char in not uppercase")

# is_uppercase("ABHINANDAN")
# is_uppercase("ABHi")

# ------------------------------------------
'''27th'''

# def longe_len_str(str1,str2):
#     a = len(str1)
#     b = len(str2)

#     if a > b:
#         print(str1,"is longer")
    
#     elif a == b:
#         print(a, " and ",b,"are equal")

#     else:
#         print(str2,"is longer")
    
# longe_len_str("abhinandan","shivraj")

# ------------------------------------------
'''28th'''

# def is_multiple(num1,num2):
#     if num1 % num2 == 0:
#         print(num1,"is multiple of ",num2)

#     else:
#         print(num1,"is not multiple of ",num2)
    
# is_multiple(10,2)
# is_multiple(10,3)
# is_multiple(10,5)

# ------------------------------------------
'''29th'''

# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(year,"is a leap year")
    
#     else:
#         print(year,"is not a leap year")

# is_leap_year(2023)
# is_leap_year(2024)

# ------------------------------------------
'''30th'''

# def is_even_divisible(num):
#     if num % 4 == 0 and num % 2 == 0:
#         print(num,"is even and divisible by 4")

#     else:
#         print(num," not divisible by 4")
    
# is_even_divisible(4)
# is_even_divisible(6)
# is_even_divisible(10)
# is_even_divisible(12)

# ------------------------------------------
'''31th'''

# def has_both_upper_and_lower(s):

#     has_upper = any(char.isupper() for char in s)
#     has_lower = any(char.islower() for char in s)

#     if has_upper and has_lower:
#         print("The string contains both uppercase and lowercase letters.")
#     else:
#         print("The string does not contain both uppercase and lowercase letters.")

# has_both_upper_and_lower("HelloWorld")  
# has_both_upper_and_lower("HELLO")       
# has_both_upper_and_lower("hello")       
# has_both_upper_and_lower("1234!")       

# ---------------------------------------------
'''32th'''

# def is_in_ranges(a,num,b):
#     if a < num < b or b < num < a:
#         print(f"number in ranges")
#     else:
#         print("number not in ranges")


# is_in_ranges(10,15,20)
# is_in_ranges(10,20,30)
# is_in_ranges(20,10,30)

# ---------------------------------------------
'''33th'''

# def  is_eligible(age):
#     if age > 18:
#         print("you can vote.")

#     elif age == 18:
#         print("submit your form")

#     else:
#         print("you can'nt vote.")

# is_eligible(10)
# is_eligible(20)
# is_eligible(18)

# ---------------------------------------------
'''34th'''

# num = "abhi"
# print(num.isalpha())

# ---------------------------------------------
'''35th'''

# num1 = 8
# num2 = 1

# if num1 % 2 == 0 and num2 % 2 == 0:
#     print(f"Both numbers ({num1} and {num2}) are even.")
# else:
#     print(f"Both numbers ({num1} and {num2}) are not even.")

# ---------------------------------------------
'''36th'''

# def dividible_check(num):
#     if num % 2 == 0 and num % 7 == 0:
#         print(num,"is divisible by 2 and 7")

#     else:
#         print(num,"is not divisible by 2 and 7")

# dividible_check(14)
# dividible_check(35)
# dividible_check(28)

# ---------------------------------------------
'''37th'''

# a = 10
# a += 10
# print(a)

# ---------------------------------------------
'''38th'''

# a = 10
# a *= 3
# print(a)

# ---------------------------------------------
'''39th'''

# number = 13
# result = round(number/5)
# print(result)

# ---------------------------------------------
'''40th'''

# number = 77
# number *= 0.5
# print(number)

# ---------------------------------------------
'''41th'''

# num = 3
# num **= 3
# print(num)

# ---------------------------------------------
'''42th'''

# a = 10
# b =  20

# a,b = b,a

# print("a = ",a)
# print("b = ",b)

# ---------------------------------------------
'''43th'''

# num = 17
# num //= 4
# print(num)

# ---------------------------------------------
'''44th'''

# num = 18
# num *= 2
# print(num)

# ---------------------------------------------
'''45th'''


# def set_bit(number, bit_position):
#     return number | (1 << bit_position)

# number = 5  
# bit_position = 3
# result = set_bit(number, bit_position)

# print("Original number:", number)
# print("Number after setting the bit:", result)

# ----------------------------------------------
'''46th'''

# def clear_bit(num, bit_position):
#     mask = ~(1 << bit_position)  
#     return num & mask  

# num = 29
# bit_position = 3
# result = clear_bit(num, bit_position)
# print(f"Original number: {num}, After clearing bit {bit_position}: {result}")

# ----------------------------------------------
'''47th'''

# def toggle_bit(number, position):
#     bitmask = 1 << position

#     return number ^ bitmask

# number = 29  
# position = 2  

# new_number = toggle_bit(number, position)
# print(bin(new_number))  

# ----------------------------------------------
'''48th'''

# def is_even(num):
#     if num & 1 == 0:
#         print(num,"is even")
#     else:
#         print(num,"is odd")

# is_even(10)
# is_even(11)

# ----------------------------------------------
'''49th'''

# def AND(num1,num2):
#     return num1 & num2

# result = AND(10,39)
# print(result)

# ----------------------------------------------
'''50th'''

# def AND(num1,num2):
#     return num1 | num2

# result = AND(10,39)
# print(result)

# ----------------------------------------------
'''51th'''

# def swap(a,b):
#     a = a^b
#     b = a^b
#     a = a^b
#     return a,b

# print(swap(11,10))

# ----------------------------------------------
'''52th'''

# def ones_complement(binary):
#     return ''.join('1' if bit == '0' else '0' for bit in binary)

# def twos_complement(binary):
#     ones_comp = ones_complement(binary)
#     return bin(int(ones_comp, 2) + 1)[2:]

# binary_number = "1101"
# ones_comp = ones_complement(binary_number)
# twos_comp = twos_complement(binary_number)

# print(ones_comp)
# print(twos_comp)

# ----------------------------------------------
'''53th'''

# num = 23<<2
# print(num)

# ----------------------------------------------
'''54th'''

# num = 23>>2
# print(num)

# ----------------------------------------------
'''55th'''

# string = "my name is abhi"

# if "ram" in string:
#     print("yes")

# else:
#     print("no")

# ----------------------------------------------
'''56th'''

# list1 = [1,3,6,7,9,4]

# if 5 in list1:
#     print("yes")

# else:
#     print("no")

# ----------------------------------------------
'''57th'''

# dict1 = {
#     "name":"abhi",
#     "age":17,
#     "place":"dewas"

# }
# key = "name"

# if key in dict1:
#     print("yes")

# ----------------------------------------------
'''58th'''

# str = "abhinandan"
# str1 = "abhi"

# if str1 in str:
#     print("yes")
# else:
#     print("no")

# ----------------------------------------------
'''59th'''

# range1 = 100
# range2 = 200
# num = 150

# def is_in_range(range1,range2,num):
#     if min(range1, range2) < num < max(range1, range2):
#         print(f"{num} in range of {range1} and {range2}")
#     else:
#         print(num,"not in range.")

# is_in_range(range1,range2,num)

# ----------------------------------------------
'''60th'''

# fruits = ["apple","mango","banana","grapes","pinaple","orange"]

# def find_in_list(fruit):
#     if fruit in fruits:
#         print(fruit,"in this list")

#     else:
#         print("not found")

# find_in_list("abhi")

# ----------------------------------------------
'''61th'''

# myset = {12,13,16,16,33,44,55,66,77,88,34,566,88,40}

# def check_elements(num):
#     if num not in myset:
#         print(num,"not in myset.")
    
#     else:
#         print(num,"in myset.")

# check_elements(10)
# check_elements(12)

# ----------------------------------------------
'''62th'''

# list1 = [10,20,30,40]

# def is_same_list(list2):
#     if all(item in list2 for item in list1):
#         print(f"all element of {list1} are in {list2}")
    
#     else:
#         print(f"all elements of  {list1} not in {list2} list.")

# is_same_list([10,20,30,40])
# is_same_list([10,20,30,40,50])

# ----------------------------------------------
'''63th'''

# def check(email):
#     if "@" in email:
#         print("valid email.")

#     else:
#         print("invalid email.")
    
# check("abhi45@gmail")
# check("abhi45gamiil")

# ----------------------------------------------
'''64th'''

# def check_username(name,letter):
#     if letter in name:
#         print(f"The letter '{letter}' is in the username.")

#     else:
#         print(f"The letter '{letter}' is not in the username.")

# check_username("abhi","a")
# check_username("abhi","k")

# ----------------------------------------------
'''65th'''

# a = [1,2,3]
# b = a
# c = [1,2,3]

# print(a is b)
# print(a is c)
# print(b is a)

# ----------------------------------------------
'''66th'''

# list1 = [1,2,3,4]
# list2 = [1,2,3,4]

# print(list1 == list2)

# ----------------------------------------------
'''67th'''

# a = "abhi"
# b = "abhi"
# print(a is b)

# ----------------------------------------------
'''68th'''

# dict1 = {"a":1,"b":2}
# dict2 = {"a":1,"b":2}
# dict3 = {"a":1,"b":2}
# dict4 = {"a":11,"b":2}

# print(dict1 == dict2)
# print(dict3 == dict4)

# ----------------------------------------------
'''69th'''

# tuple1 = (1,2,3,4)
# tuple2 = (1,2,3,4)

# print(tuple1 == tuple2)

# ----------------------------------------------
'''70th'''

# list1 = [1,2,3,4]
# list2 = [1,2,3,4]

# print(list1 is not list2)

# ----------------------------------------------
'''71th'''

# num1 = -5
# num = abs(-5)

# num2 = 5
# print(num is num2)

# ----------------------------------------------
'''72th'''

# set1 = {1,2,3,4}
# set2 = {1,2,3,4}

# print(set1 is set2)

# ----------------------------------------------
'''73th'''

# var1 = [1, 2, 3]
# var2 = [1, 2, 3]


# if var1 is var2:
#     print("var1 and var2 refer to the same object.")
# else:
#     print("var1 and var2 do not refer to the same object.")

# var3 = var1

# if var1 is var3:
#     print("var1 and var3 refer to the same object.")
# else:
#     print("var1 and var3 do not refer to the same object.")

# ----------------------------------------------
'''74th'''

# num1 = 100
# num2 = 100

# if id(num1) == id(num2):
#     print("num1 and num2 have the same memory address.")
# else:
#     print("num1 and num2 have different memory addresses.")

# num3 = 1000
# num4 = 1000

# if id(num3) == id(num4):
#     print("num3 and num4 have the same memory address.")
# else:
#     print("num3 and num4 have different memory addresses.")

# ----------------------------------------------
'''75th'''

# que = 12+10-5*2/2
# print(que)

# ----------------------------------------------
'''76th'''

# a = 10**2*10
# print(a)

# ----------------------------------------------
'''77th'''

# a = 10*20/(2+4)
# print(a)

# a = 10*20/2+4
# print(a)

# ----------------------------------------------
'''78th'''

# a = 100 + 200 % 7 // 2
# print(a)

# ----------------------------------------------
'''79th'''

# def toggle_bits(num):
#     mask = 0xFFFFFFFF
#     return num ^ mask

# num = 92
# print(f"Toggled bits of {num}: {toggle_bits(num)}")

# ----------------------------------------------
'''80th'''

# def rotate_digits(num, rotations):
#     num_str = str(num)
#     rotations = rotations % len(num_str)
#     rotated_num = num_str[-rotations:] + num_str[:-rotations]
#     return int(rotated_num)

# num = 12345
# rotations = 1
# print(f"Rotated number: {rotate_digits(num, rotations)}")

# ----------------------------------------------
'''81th'''

# def sum_of_odds(n):
#     sum = 0
#     for i in range(1,n+1,2):
#         sum += i
    
#     return sum

# n = 10
# print(f"sum of odd numbers up to {n} : {sum_of_odds(n)}")

# ----------------------------------------------
'''82th'''

# def is_power_2(n):
#     return n > 0 and (n & (n - 1))==0

# n = 128
# print(f"{n} is power of 2: {is_power_2(n)}")

# ----------------------------------------------
'''83th'''

# def is_middle(a,b,c):
#     return sorted([a,b,c])[1]

# result = is_middle([10],[11],[15])
# print(result,"is middle number")

# ----------------------------------------------
'''84th'''

# from math import gcd

# def are_coprime(a, b):
#     return gcd(a, b) == 1

# a = 3
# b = 4
# print(f"{a} and {b} are co-prime: {are_coprime(a, b)}")

# ----------------------------------------------
'''85th'''

# def count_ones(num):
#     count = 0
#     while num:
#         count += num & 1  
#         num >>= 1  
#     return count

# num = 15 
# print(f"Number of 1's in binary representation: {count_ones(num)}")

# ----------------------------------------------
'''86th'''

# def reverse_bits(num, bit_length=32):
#     result = 0
#     for _ in range(bit_length):
#         result = (result << 1) | (num & 1)  
#         num >>= 1  
#     return result


# num = 5  
# bit_length = 32
# print(f"Reversed bits: {bin(reverse_bits(num, bit_length))}")
# # 


# for i in range(10,0,-1):
#     print(i,"hello")

# num = int(input("enter number = "))

# is_prime = True

# if num <= 1:
#     is_prime = False

# else:
#     for i in range(2,int(num**0.5)+1):
#         if num % i == 0:
#             is_prime = False
#         break
# if is_prime:
#     print(num,"is a prime number.")

# else:
#     print(num,"is not  aprime number")

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2,number):
#         if number % i == 0:
#             return False
#     return True

# num = int(input("enter number = "))

# if is_prime(num):
#     print(num,"is a prime number.")

# else:
#     print(num,"is not a prime number")


# n = int(input("enter number = "))

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2,int(number**0.5)+1):
#         if number % i == 0:
#             return False
#     return True

# def print_primes(n):
#     for number in range(1,n+1):
#        if is_prime(number):
#            print(number,end=",")

# print_primes(n)


# def power(x,y):
#     result = 1
#     for _ in range(y):
#         result *= x
#     return result

# x = int(input("enter the value of (x) : "))
# y = int(input("enter the value of (y) : "))

    
# print(power(x,y))

# n = 5


# def fibonacci(n):
#     a,b = 0,1
#     for _ in range(n):
#         print(a,end=" ")
#         a,b = b , a+b
        
    
# fibonacci(n)


# str = input("enter string = ")

# for _ in str:
#     if str == str[::-1]:
#         print("this is a palindrome.")
#     break
# else:
#     print("this is not a palindrome")


# def is_palindrome(str):
#     if str == str[::-1]:
#         print("this is a palindrome")
#     else:
#         print("this is not a palindrome")

# str = input("enter str : ")
# is_palindrome(str)

# m = [1,2,3,4,5,6,7,8,9]

# max_num = m[0]
# min_num = m[0]

# for n in m:
#     if n > max_num:
#         max_num = n
#     if n < min_num:
#         min_num = n

# print(max_num)
# print(min_num)


# def min_max_num(list):
#     m = max(list)
#     n = min(list)
#     print(m)
#     print(n)

# list = [1,2,3,4,5,6,7,8,9]

# print(min_max_num(list))


# num = int(input("enter number = "))
# sum_of_odds = 0

# for i in range(1,num+1):
#     if i % 2 != 0:
#         sum_of_odds += i
    
# print(sum_of_odds)

# num = int(input("enter the number of rows = "))

# for i in range(1,num+1):

#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# def count_character_frequency(string):
#     frequency = {}  
    
#     for char in string:  
#         if char in frequency:  
#             frequency[char] += 1
#         else:
#             frequency[char] = 1 
    
#     for char, freq in frequency.items():  
#         print(f"'{char}' occurs {freq} times.")


# string = input("Enter a string: ")
# count_character_frequency(string)


# def char_freq(string):
#     frequency = {}

#     for char in string:
#         if char in frequency:
#             frequency[char] += 1

#         else:
#             frequency[char] = 1
#     for char,freq in frequency.items():
#         print(f"'{char}' occurs {freq} times.") 


# string = input("enter a string : ")
# char_freq(string)
# 





# indian union terretury ka table







# def minion_game(string):
#     vowels = "AEIOU"
#     stuart_score = 0
#     kevin_score = 0
#     n = len(string)
    
#     for i in range(n):
#         if string[i] in vowels:
#             kevin_score += (n - i)
#         else:
#             stuart_score += (n - i)
    
#     if stuart_score > kevin_score:
#         print("Stuart", stuart_score)
#     elif kevin_score > stuart_score:
#         print("Kevin", kevin_score)
#     else:
#         print("Draw")

# string = "APPLE"
# minion_game(string)



# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# result = [[i,j,k] for i in range(x+1) for j in range(y+1) for  k in range(z+1) if i + j + k != n]
# print(result)




# n = int(input())
# students = []

# for _ in range(n):
#     name = input()
#     grade = float(input())
#     students.append([name, grade])

# grades = sorted(set([student[1] for student in students]))
# second_lowest_grade = grades[1]

# second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

# for name in sorted(second_lowest_students):
#     print(name)




# n = int(input())
# student_marks = {}

# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores

# query_name = input()

# if query_name in student_marks:
#     scores = student_marks[query_name]
#     average = sum(scores) / len(scores)
#     print(f"{average:.2f}")


# A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52}

# # Operation 1: intersection_update
# B = {2, 3, 5, 6, 8, 9, 1, 4, 7, 11}
# A.intersection_update(B)

# # Operation 2: update
# C = {55, 66}
# A.update(C)

# # Operation 3: symmetric_difference_update
# D = {22, 7, 35, 62, 58}
# A.symmetric_difference_update(D)

# # Operation 4: difference_update
# E = {11, 22, 35, 55, 58, 62, 66}
# A.difference_update(E)

# # Print the final set
# print(sum(A))









# list1 = [1,2,3,4,5,6,77,33]
# m = max(list1)

# if m != list1:
#     s = max(list1)
#     print(s)



# rows = 10
# for i in range(1,rows+1):
#     for j in range(i):
#         rows + 1
#         print(j,end="")

#     print()


# word = 'abhinandan'

# x = " "
# for i in word:
#     x += i
#     print(x)




# a = 'abcdef'
# b = "cdef"

# count = 0
# for i in range(len(a)):
#     if a[i] == b[0]:
#         break
#     count += 1
    
# print(count)


# def print_formatted(n):
#     width = len(bin(n)[2:]) 
    
#     for i in range(1, n + 1):
#         decimal_val = str(i).rjust(width)
#         octal_val = oct(i)[2:].rjust(width)
#         hex_val = hex(i)[2:].upper().rjust(width)
#         binary_val = bin(i)[2:].rjust(width)

#         print(f"{decimal_val} {octal_val} {hex_val} {binary_val}")

# n = int(input("Enter a number: "))
# print_formatted(n)


# def formate(n):
#     width = len(bin(n)[2:]) 

#     for i in range(1,n+1):
#         dec = str(i).rjust(width)
#         oc = oct(i)[2:].rjust(width)

#         hex1 = hex(i)[2:].upper().rjust(width)
#         bi = bin(i)[2:].rjust(width)

#         print(f"{dec} {oc} {hex1} {bi}")

# n = int(input("enter number : "))
# formate(n)



# i = 1


# for i in range(1,10):
#     for j in range(1, i ):
#         print(j , end="")
#     print()   




# N = int(input())
# l = [1,5,9,4]
    
# k = l.insert(0,5)
# a = l.insert(2,4)
# print(l)
# m = l.remove(1)
# n = l.append(1)
# s = l.sort(key=None,reverse=False)
# print(l)
# p = l.pop()
# r = l.reverse()

# print(l)





# from itertools import permutations

# S, k = input().split()
# k = int(k)

# perm = sorted([''.join(p) for p in permutations(S, k)])
# print(perm)

# for p in perm:
#     print(p)




# list1 = [int(input(k)) for k in range()]

# print(list(list1))








#=============================================================================================================================================





# def fac(num):
#     fact = 1
#     for i in range(1, num + 1):  
#         fact *= i
#     return fact

# def strong_num(n):
#     temp = n
#     sum_of_fact = 0  

#     while temp != 0:
#         digit = temp % 10  
#         sum_of_fact += fac(digit)
#         temp //= 10  
#     return sum_of_fact == n  

# n = 14
# print(strong_num(n))




# def reverse_num(num):
#     re = 0
#     while num != 0:
#         digit = num % 10
#         re = re*10 + digit
#         num //= 10
#     print(re)

# num = 128
# reverse_num(num)



# num = 5
# power = 7

# output = 1
# for i in range(power):
#     output *= num

# print(output)




# num = 100
# count = 0

# while num != 0:
#     num = num // 10
#     count += 1
    
# print(count)





# num = input("Enter number: ")
# power = len(num)  

# result = 0

# for i in num:
#     result += int(i) ** power 

# if int(num) == result:
#     print("This is an Armstrong number")
# else:
#     print("This is not an Armstrong number")




for i in range(1,11):
    print(i)
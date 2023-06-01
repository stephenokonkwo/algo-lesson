# Lesson prac 1: User Inputs two numbers, One number is  assigned to a variable, the other number is assigned to another variable.
#The task is to invert the variable,so that the first variable contains the second number, while the first number
#is in the second variable.


#code here
#O(1)
# a = 5
# b = 10
#
# print(f"a = {a}")
# print(f"b = {b}")
#
# temp = a
# a = b
# b = temp
#
# print(f"a = {a}")
# print(f"b = {b}")


# Lesson prac 2: A leap year is exactly divisible by 4. except for century years (years ending with 00)
# The century tear is a leap year only if it is perfectly divisible by 400. for example,
#
# 2017 is not a leap year
# 1999 is not a leap year
# 2012 is a leap year
# 2000 is a leap year

# #code here
# # O(1)
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print(f'{year} is a leap year')
#             else:
#                 print(f'{year} is NOT a leap year')
#         else:
#             print(f'{year} is a leap year')
#     else:
#         print(f'{year} is a NOT leap year')
#
#
# print(is_leap_year(2100))   # true
# print(is_leap_year(2000))   # true
# print(is_leap_year(1900))   # false
# print(is_leap_year(1975))   # false
# print(is_leap_year(2016))   # true

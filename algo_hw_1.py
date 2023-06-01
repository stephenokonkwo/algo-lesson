# 1) Compute the sum of digits in all numbers from 1 to n. When a function gets a number n,
# find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# code O(n)
def sum_of_digits(n):
    total_sum = 0

    for i in range(1, n + 1):
        for digit in str(i):
            total_sum += int(digit)

    return total_sum

n = 5
result = sum_of_digits(n)
print("Sum of digits from 1 to", n, ":", result)








# 2) Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

# code: O(1)
num1 = 124
num2 = 21
num3 = 32

max_num = num1

if num2 > max_num:
    max_num = num2

if num3 > max_num:
    max_num = num3

print("The maximum number is:", max_num)







# 3) Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

# code: O(n)
def count_odd_even_numbers_digits(number):
    even_numbers_count = 0
    odd_numbers_count = 0
    even_digits_count = 0
    odd_digits_count = 0

    temp_number = abs(number)

    if temp_number == 0:
        even_digits_count += 1
        return even_numbers_count, odd_numbers_count, even_digits_count, odd_digits_count

    while temp_number > 0:
        digit = temp_number % 10
        temp_number = temp_number // 10

        if digit % 2 == 0:
            even_digits_count += 1
        else:
            odd_digits_count += 1

        if temp_number == 0:
            break

    if number % 10 == 0 or number % 2 == 0:
        even_numbers_count += 1
    else:
        odd_numbers_count += 1

    return even_numbers_count, odd_numbers_count, even_digits_count, odd_digits_count

number = 34560
even_numbers, odd_numbers, even_digits, odd_digits = count_odd_even_numbers_digits(number)
print("Even numbers count:", even_numbers)
print("Odd numbers count:", odd_numbers)
print("Even digits count:", even_digits)
print("Odd digits count:", odd_digits)





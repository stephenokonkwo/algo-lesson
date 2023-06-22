# Even First Your input is a list of integers, and you have to reorder its entries so that the even entries appear
# first. You are required to solve it without allocating additional storage (operate with the input list). Example: [
# 7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

# O(n)
def reorder_even_first(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums


nums = [7, 3, 5, 6, 4, 10, 3, 2]
reordered_nums = reorder_even_first(nums)
print(reordered_nums)


# Increment a Number Write a program that takes as input a list of digits encoding a nonnegative decimal integer D
# and updates the list to represent the integer D + 1. For example, if the input is [1, 2, 9] then you should update
# the array to [1, 3, 0].

# O(n)
def increment_number(digits):
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        digit_sum = digits[i] + carry
        digits[i] = digit_sum % 10

        carry = digit_sum // 10

        if carry == 0:
            break

    if carry == 1:
        digits.insert(0, carry)

    return digits


digits = [1, 2, 9]
result = increment_number(digits)
print(result)

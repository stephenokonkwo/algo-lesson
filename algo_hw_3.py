# Homework 3

# 1) Below The Arithmetical Mean When given a list, the program should return a list of all the elements below the
# original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of
# elements. Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

# Big O notation of;  O(n)
def elements_below_mean(lst):
    mean = sum(lst) / len(lst)  # Calculate the arithmetic mean
    below_mean = [num for num in lst if num < mean]  # Create a list of elements below the mean
    return below_mean


lst = [1, 3, 5, 6, 4, 10, 2, 3]
result = elements_below_mean(lst)
print(result)  # Output: [1, 3, 4, 2, 3]


# 2)Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def find_two_lowest_elements(lst):
    lowest1 = float('inf')
    lowest2 = float('inf')

    for num in lst:
        if num < lowest1:
            lowest2 = lowest1
            lowest1 = num
        elif num < lowest2 and num != lowest1:
            lowest2 = num

    return lowest1, lowest2


lst = [198, 3, 4, 9, 10, 9, 2]
result = find_two_lowest_elements(lst)
print(result)  # Output: (2, 3)

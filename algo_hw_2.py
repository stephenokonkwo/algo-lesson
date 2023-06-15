# Homework 2


# 1) Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.


# O(n)
def split_and_swap(string):
    length = len(string)
    midpoint = length // 2 + length % 2  # calculate the midpoint

    part1 = string[:midpoint]  # extract the first part
    part2 = string[midpoint:]  # extract the second part

    swapped_string = part2 + part1  # swap the positions of the parts

    return swapped_string


string = 'bbbbbcaaaaa'
result = split_and_swap(string)
print(result)

# 2)Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.


# O(1)


def unique_char_str(s):
    lenstr = len(s)
    lenset = len(set(s))
    return lenset == lenstr


test_data_pos = "abcde"  # true
test_data_neg = "abcdee"  # false
print(unique_char_str(test_data_pos))
print(unique_char_str(test_data_neg))






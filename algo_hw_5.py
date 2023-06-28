# 1. Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.

# O(n^2)
def selection_sort_descending(arr):
    n = len(arr)

    for i in range(n - 1):
        max_index = i

        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


arr = [4, 2, 7, 1, 9, 5]
sorted_arr = selection_sort_descending(arr)
print(sorted_arr)

arr = [4, 2, 7, 1, 9, 5]
sorted_arr = selection_sort_descending(arr.copy())
print(sorted_arr)
print(arr)  # Original array remains unchanged




# 2. Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

# O(n^2)
def bubble_sort_descending(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [4, 2, 7, 1, 9, 5]
sorted_arr = bubble_sort_descending(arr)
print(sorted_arr)

arr = [4, 2, 7, 1, 9, 5]
sorted_arr = bubble_sort_descending(arr.copy())
print(sorted_arr)
print(arr)  # Original array remains unchanged




# 3. Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.

# O(n^2)
def insertion_sort_descending(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

arr = [4, 2, 7, 1, 9, 5]
sorted_arr = insertion_sort_descending(arr)
print(sorted_arr)

arr = [4, 2, 7, 1, 9, 5]
sorted_arr = insertion_sort_descending(arr.copy())
print(sorted_arr)
print(arr)  # Original array remains unchanged





# 4. Merge Sort
# Implement the merge sort algorithm that is sorting in descending order.

# O(n
def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_descending(arr[:mid])
    right = merge_sort_descending(arr[mid:])

    return merge_descending(left, right)


def merge_descending(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

arr = [4, 2, 7, 1, 9, 5]
sorted_arr = merge_sort_descending(arr)
print(sorted_arr)




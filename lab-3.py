# 3a - Selection Sort
'''
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

# Selection Sort
for i in range(n - 1):

    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array:", arr)

# 3b - Insertion Sort

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

# Insertion Sort
for i in range(1, n):

    key = arr[i]
    j = i - 1

    # Shift elements greater than key
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    # Insert key at correct position
    arr[j + 1] = key

print("Sorted array:", arr)

# 3c - Bubble Sort

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

# Bubble Sort
for i in range(n - 1):

    for j in range(n - 1 - i):

        if arr[j] > arr[j + 1]:

            # Swap adjacent elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)  

# 3d - Merge Sort

def merge_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    # Find middle
    mid = len(arr) // 2

    # Divide into two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    # Compare elements from both halves
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Input
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

# Sort
arr = merge_sort(arr)

print("Sorted array:", arr) '''

# 3e - Quick Sort

def partition(arr, low, high):

    # Choose last element as pivot
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:

            i += 1

            # Swap
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):

    if low < high:

        # Find pivot position
        pivot_index = partition(arr, low, high)

        # Sort left part
        quick_sort(arr, low, pivot_index - 1)

        # Sort right part
        quick_sort(arr, pivot_index + 1, high)


# Input
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

# Quick Sort
quick_sort(arr, 0, n - 1)

print("Sorted array:", arr)

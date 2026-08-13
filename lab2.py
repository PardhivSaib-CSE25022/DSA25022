'''
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

# Get user input
size = int(input("Enter number of elements: "))
print(f"Enter {size} elements (separated by spaces):")
elements = [int(x) for x in input().split()[:size]]

key = int(input("Enter the element to search for: "))

# Execution
result = linear_search(elements, key)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found.")
'''

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1  
            
    return -1  

size = int(input("Enter number of elements: "))
print(f"Enter {size} elements in SORTED order (separated by spaces):")
elements = [int(x) for x in input().split()[:size]]

elements.sort() 

key = int(input("Enter the element to search for: "))

result = binary_search(elements, key)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found.")

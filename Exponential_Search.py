def binary_search(arr, l, r, x):                                       # Define a function to perform binary search
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def exponential_search(arr, x):                                        # Define a function to perform exponential search
    n = len(arr)
    if arr[0] == x:                                                    # Check if the first element is the search element
        return 0
    i = 1
    while i < n and arr[i] <= x:                                       # Find the range for binary search
        i *= 2
    return binary_search(arr, i // 2, min(i, n - 1), x)                # Perform binary search on the range

arr = [1, 2, 5, 5, 6, 9]                                               # Create an array and element to search
x = 5

result = exponential_search(arr, x)                                    # Call the exponential search function and store the result

if result == -1:                                                       # If the element is not found, print a message
    print("Element not found")
else:                                                                  # If the element is found, print its index
    print(f"Element found at index {result}")

'''
OUTPUT:
Element found at index 2
'''
